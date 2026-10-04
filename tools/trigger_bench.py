"""Trigger-routing benchmark: does the right skill get picked for a request?

Agents choose skills from their name + description alone, so a skill that is never
selected is worthless however good its body is. This benchmark replays the prompts in
evals/<skill>/evals.json against every skill description in the library.

Routers:
  bm25    (default) deterministic lexical router over name+description. Free, runs in CI.
          Measures description distinctiveness; a lower bound on real routing.
  claude  asks `claude -p` to choose skills from the full catalog, as a harness would.
          Costs API tokens; run manually or in the scheduled benchmark workflow.

Metrics: hit@1 and hit@3 for prompts that should trigger their skill; false-trigger
rate for near-miss prompts (should_trigger: false) where the skill still ranks first.

Usage:
    uv run tools/trigger_bench.py                          # bm25, reviewed evals
    uv run tools/trigger_bench.py --include-pending        # include generated evals pending review
    uv run tools/trigger_bench.py --min-hit3 0.8           # CI gate
    uv run tools/trigger_bench.py --router claude --model claude-sonnet-5-5 --limit 20
"""

from __future__ import annotations

import argparse
import json
import math
import random
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import ROOT, load_skills  # noqa: E402

TOKEN = re.compile(r"[a-z0-9][a-z0-9+#.-]*")
STOP = set("a an the and or of to in on for with by is are be this that it as at from use using when you your my our "
           "i we me us can how what which do does into about".split())


def tokens(text: str) -> list[str]:
    """Tokens for *text* and return list[str]."""
    out = []
    for t in TOKEN.findall(text.lower()):
        t = t.strip(".-")
        if t and t not in STOP:
            out.append(t)
            if len(t) > 5 and t.endswith("s"):
                out.append(t[:-1])  # crude plural folding
    return out


class BM25:
    """Bm25."""
    def __init__(self, docs: dict[str, list[str]], k1: float = 1.4, b: float = 0.75):
        self.docs, self.k1, self.b = docs, k1, b
        self.avg = sum(len(d) for d in docs.values()) / max(len(docs), 1)
        df = Counter(t for d in docs.values() for t in set(d))
        n = len(docs)
        self.idf = {t: math.log(1 + (n - c + 0.5) / (c + 0.5)) for t, c in df.items()}
        self.tf = {k: Counter(v) for k, v in docs.items()}

    def rank(self, query: list[str]) -> list[tuple[str, float]]:
        """Rank for *query* and return list[tuple[str, float]]."""
        scores = {}
        for name, tf in self.tf.items():
            dl = len(self.docs[name])
            s = 0.0
            for t in query:
                if t in tf:
                    f = tf[t]
                    s += self.idf[t] * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * dl / self.avg))
            scores[name] = s
        return sorted(scores.items(), key=lambda x: -x[1])


def claude_rank(prompt: str, catalog: str, model: str | None) -> list[str]:
    """Claude rank and return list[str]."""
    exe = shutil.which("claude")
    if not exe:
        sys.exit("claude CLI not found on PATH")
    ask = (f"{catalog}\n\nA user sends this request to an AI agent that has the skills above installed:\n"
           f"<request>{prompt}</request>\nWhich skills (if any) should the agent load? Reply with JSON only: "
           '{"skills": ["name1", "name2", "name3"]} ordered by relevance, at most 3, or {"skills": []} if none apply.')
    # The catalog is large: send it on stdin (Windows caps command lines at ~32k chars).
    cmd = [exe, "-p", "--output-format", "json", "--disable-slash-commands", "--tools", "",
           "--no-session-persistence"] + (["--model", model] if model else [])
    res = subprocess.run(cmd, input=ask, capture_output=True, text=True, encoding="utf-8", timeout=300)
    try:
        text = json.loads(res.stdout)["result"]
        return json.loads(re.search(r"\{.*\}", text, re.S).group(0))["skills"]
    except (json.JSONDecodeError, KeyError, AttributeError, TypeError):
        print(f"warn: unparseable router output for: {prompt[:60]}", file=sys.stderr)
        return []


def main(argv: list[str] | None = None) -> int:
    """Main for *argv* and return int."""
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--router", choices=["bm25", "claude"], default="bm25")
    ap.add_argument("--model")
    ap.add_argument("--limit", type=int, help="max prompts (for the paid router)")
    ap.add_argument("--sample", type=int, help="random subsample of N prompts (reproducible with --seed)")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--include-pending", action="store_true", help="include generated evals marked pending review")
    ap.add_argument("--min-hit3", type=float, help="exit 1 if aggregate hit@3 falls below this")
    ap.add_argument("--max-false", type=float, help="exit 1 if the false-trigger rate exceeds this")
    ap.add_argument("--json", type=Path)
    args = ap.parse_args(argv)

    skills = {s.name: s for s in load_skills()}
    cases = []
    for f in sorted((ROOT / "evals").glob("*/evals.json")):
        data = json.loads(f.read_text(encoding="utf-8"))
        if not args.include_pending and "pending review" in str(data.get("provenance", "")).lower():
            continue
        for ev in data["evals"]:
            cases.append((data["skill_name"], ev["prompt"], ev.get("should_trigger", True)))
    if args.sample and args.sample < len(cases):
        cases = random.Random(args.seed).sample(cases, args.sample)  # noqa: S311 - reproducible subsample
    if args.limit:
        cases = cases[: args.limit]
    if not cases:
        sys.exit("no evals found under evals/*/evals.json")

    if args.router == "bm25":
        index = BM25({n: tokens(n.replace("-", " ")) * 2 + tokens(str(s.meta.get("description", "")))
                      for n, s in skills.items()})
        route = lambda p: [n for n, sc in index.rank(tokens(p))[:5] if sc > 0]  # noqa: E731
    else:
        catalog = "Available skills:\n" + "\n".join(f"- {n}: {' '.join(str(s.meta.get('description', '')).split())}"
                                                   for n, s in sorted(skills.items()))
        route = lambda p: claude_rank(p, catalog, args.model)  # noqa: E731

    rows = []
    for skill, prompt, should in cases:
        ranked = route(prompt)
        pos = ranked.index(skill) + 1 if skill in ranked else None
        rows.append({"skill": skill, "prompt": prompt, "should_trigger": should, "rank": pos, "top": ranked[:3]})
    pos_rows = [r for r in rows if r["should_trigger"]]
    neg_rows = [r for r in rows if not r["should_trigger"]]
    hit1 = sum(r["rank"] == 1 for r in pos_rows) / max(len(pos_rows), 1)
    hit3 = sum(r["rank"] is not None and r["rank"] <= 3 for r in pos_rows) / max(len(pos_rows), 1)
    false = sum(r["rank"] == 1 for r in neg_rows) / max(len(neg_rows), 1)

    for r in rows:
        ok = (r["rank"] is not None and r["rank"] <= 3) if r["should_trigger"] else r["rank"] != 1
        if not ok:
            kind = "MISS " if r["should_trigger"] else "FALSE"
            print(f"{kind} {r['skill']:<36} rank={r['rank']} top={r['top']}  | {r['prompt'][:70]}")
    print(f"\nrouter={args.router} prompts={len(rows)}  hit@1={hit1:.2f}  hit@3={hit3:.2f}  "
          f"false-trigger={false:.2f} ({len(neg_rows)} near-miss prompts)")
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps({"router": args.router, "hit@1": hit1, "hit@3": hit3,
                                         "false_trigger": false, "cases": rows}, indent=2) + "\n", encoding="utf-8")
    fail = ((args.min_hit3 is not None and hit3 < args.min_hit3)
            or (args.max_false is not None and false > args.max_false))
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
