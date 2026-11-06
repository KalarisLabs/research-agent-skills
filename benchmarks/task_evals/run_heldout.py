"""Held-out task benchmark: several answer models, a judge that never grades its own model,
order-swapped blind judging, and deterministic checks.

For every task in heldout.json and every answer model, generate an answer without skills
(baseline) and one with the skill's SKILL.md appended to the system prompt. Then:

1. Deterministic checks (checks.py) run on both answers. No LLM involved.
2. The judge compares the two answers twice, once in each order. A winner counts only if
   both orders agree; otherwise the pair is a tie. This removes position bias.

Calls run in a scratch directory so no project instructions leak into either condition.
Every model call is cached in --cache (JSONL), so an interrupted run resumes without paying twice.

Usage (paid; uses your Claude Code login or ANTHROPIC_API_KEY):
    uv run benchmarks/task_evals/run_heldout.py --workers 8 \
        --answer-models claude-haiku-4-5-20251001 claude-sonnet-5-5 claude-opus-5-5 \
        --judge claude-opus-5-5 --alt-judge claude-sonnet-5-5 \
        --json benchmarks/results/task-evals-heldout.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import re
import shutil
import subprocess
import sys
import tempfile
import threading
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from checks import run_checks  # noqa: E402

for _stream in (sys.stdout, sys.stderr):  # Windows consoles default to cp1252
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[2]
TASKS = Path(__file__).with_name("heldout.json")
JUDGE = """You are grading two answers to the same research-assistant request. Be strict and specific.

<request>{prompt}</request>
<rubric>A strong answer: {rubric}</rubric>

<answer_A>
{a}
</answer_A>

<answer_B>
{b}
</answer_B>

Score each answer 1-10 on: correctness and rigor (no fabricated facts, identifiers or citations), following
the request's constraints and the rubric, specificity and usefulness for a working researcher. Length is not a
virtue. Then pick a winner.
Reply with JSON only: {{"score_A": n, "score_B": n, "winner": "A" | "B" | "tie", "reason": "one sentence"}}"""


class Cache:
    """Append-only JSONL cache of model calls keyed by a hash of (model, system file, prompt)."""

    def __init__(self, path: Path):
        """Initialise the instance."""
        self.path, self.lock, self.data = path, threading.Lock(), {}
        if path.exists():
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    rec = json.loads(line)
                    self.data[rec["key"]] = rec
        path.parent.mkdir(parents=True, exist_ok=True)

    def get(self, key: str) -> dict | None:
        """Get."""
        return self.data.get(key)

    def put(self, key: str, rec: dict) -> None:
        """Handle put."""
        rec = {"key": key, **rec}
        with self.lock:
            self.data[key] = rec
            with self.path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def call(cache: Cache, model: str, prompt: str, system_file: Path | None, workdir: str) -> dict:
    """One `claude -p` call with tools and slash commands disabled; cached."""
    sys_text = system_file.read_text(encoding="utf-8") if system_file else ""
    key = hashlib.sha256(f"{model}\0{sys_text}\0{prompt}".encode()).hexdigest()
    hit = cache.get(key)
    if hit and not hit.get("error"):
        return hit
    exe = shutil.which("claude")
    if not exe:
        sys.exit("claude CLI not found on PATH")
    cmd = [exe, "-p", "--model", model, "--output-format", "json", "--disable-slash-commands", "--tools", "",
           "--no-session-persistence"]
    if system_file:
        cmd += ["--append-system-prompt-file", str(system_file)]
    try:
        res = subprocess.run(cmd, input=prompt, capture_output=True, text=True, encoding="utf-8", timeout=900,
                             cwd=workdir)
        out = json.loads(res.stdout)
        rec = {"model": model, "text": out.get("result", ""), "cost": out.get("total_cost_usd", 0.0),
               "error": bool(out.get("is_error"))}
    except (json.JSONDecodeError, subprocess.TimeoutExpired) as exc:
        rec = {"model": model, "text": "", "cost": 0.0, "error": True, "detail": str(exc)[:300]}
    cache.put(key, rec)
    return rec


def parse_verdict(text: str) -> dict | None:
    """Parse verdict."""
    m = re.search(r"\{.*\}", text, re.S)
    try:
        v = json.loads(m.group(0)) if m else None
    except json.JSONDecodeError:
        return None
    return v if isinstance(v, dict) and v.get("winner") in {"A", "B", "tie"} else None


def _mean_or_none(xs: list) -> float | None:
    """Mean of `xs` when every item is numeric, otherwise None."""
    return sum(xs) / len(xs) if all(isinstance(x, (int, float)) for x in xs) else None


def judge_pair(cache: Cache, judge: str, task: dict, skill_ans: str, base_ans: str, workdir: str) -> dict:
    """Judge in both orders. Returns winner (skill/baseline/tie/error) and mean scores."""
    orders = []
    for skill_first in (True, False):
        a, b = (skill_ans, base_ans) if skill_first else (base_ans, skill_ans)
        r = call(cache, judge, JUDGE.format(prompt=task["prompt"], rubric=task["rubric"], a=a, b=b), None, workdir)
        v = parse_verdict(r["text"]) if not r["error"] else None
        if v is None:
            return {"winner": "error", "skill_score": None, "baseline_score": None}
        win = {"A": "skill" if skill_first else "baseline", "B": "baseline" if skill_first else "skill"}.get(
            v["winner"], "tie")
        s, bsc = (v["score_A"], v["score_B"]) if skill_first else (v["score_B"], v["score_A"])
        orders.append((win, s, bsc, v.get("reason", "")))
    winner = orders[0][0] if orders[0][0] == orders[1][0] else "tie"
    return {"winner": winner, "skill_score": _mean_or_none([o[1] for o in orders]),
            "baseline_score": _mean_or_none([o[2] for o in orders]), "order_agree": orders[0][0] == orders[1][0],
            "reason": orders[0][3]}


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """Handle wilson."""
    if not n:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - h) / d, (c + h) / d)


def sign_test_p(wins: int, losses: int) -> float:
    """Two-sided exact sign test, ties dropped."""
    n = wins + losses
    if not n:
        return 1.0
    k = min(wins, losses)
    tail = sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n
    return min(1.0, 2 * tail)


def summarize(rows: list[dict]) -> dict:
    """Summarize."""
    valid = [r for r in rows if r["winner"] != "error"]
    wins = sum(r["winner"] == "skill" for r in valid)
    losses = sum(r["winner"] == "baseline" for r in valid)
    scored = [r for r in valid if r["skill_score"] is not None and r["baseline_score"] is not None]
    delta = sum(r["skill_score"] - r["baseline_score"] for r in scored) / max(len(scored), 1)
    chk = [r for r in rows if r["checks_total"]]
    return {
        "tasks": len(rows), "graded": len(valid), "errors": len(rows) - len(valid),
        "skill_wins": wins, "baseline_wins": losses, "ties": len(valid) - wins - losses,
        "win_rate": wins / max(len(valid), 1), "win_rate_ci95": wilson(wins, len(valid)),
        "sign_test_p": sign_test_p(wins, losses), "mean_score_delta": delta,
        "checks_pass_skill": sum(r["checks_pass_skill"] for r in chk) / max(len(chk), 1),
        "checks_pass_baseline": sum(r["checks_pass_baseline"] for r in chk) / max(len(chk), 1),
        "tasks_with_checks": len(chk),
    }


def _parse_args() -> argparse.Namespace:
    """Parse the command line for the held-out suite."""
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--answer-models", nargs="+", required=True)
    ap.add_argument("--judge", required=True, help="primary judge model")
    ap.add_argument("--alt-judge", help="judge used when the answer model equals --judge; also used for "
                    "judge-agreement on the first answer model")
    ap.add_argument("--skills", nargs="*", help="limit to these skills")
    ap.add_argument("--limit", type=int, help="first N tasks (smoke test)")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--cache", type=Path, default=ROOT / ".cache" / "task-evals-heldout.jsonl")
    ap.add_argument("--json", type=Path)
    return ap.parse_args()


def _judges_for(args: argparse.Namespace, model: str) -> list[tuple[str, str]]:
    """Return the (role, judge model) pairs used to grade answers from `model`."""
    primary = args.alt_judge if model == args.judge else args.judge
    if not primary or primary == model:
        sys.exit(f"no judge distinct from answer model {model}; pass --alt-judge")
    js = [("primary", primary)]
    if args.alt_judge and model == args.answer_models[0] and args.alt_judge not in (primary, model):
        js.append(("agreement", args.alt_judge))
    return js


def _run_one(args: argparse.Namespace, cache: Cache, workdir: str, model: str, t: dict) -> dict:
    """Generate baseline and skill answers for one task, run checks and judge them."""
    skill_md = ROOT / "skills" / t["skill"] / "SKILL.md"
    base = call(cache, model, t["prompt"], None, workdir)
    with_skill = call(cache, model, t["prompt"], skill_md, workdir)
    if base["error"] or with_skill["error"]:
        return {"model": model, "skill": t["skill"], "id": t["id"], "winner": "error", "skill_score": None,
                "baseline_score": None, "checks_total": 0, "checks_pass_skill": 0, "checks_pass_baseline": 0}
    cs, cb = run_checks(with_skill["text"], t["checks"]), run_checks(base["text"], t["checks"])
    row = {"model": model, "skill": t["skill"], "id": t["id"],
           "checks_total": int(bool(t["checks"])), "checks_skill": cs, "checks_baseline": cb,
           "checks_pass_skill": int(bool(cs) and all(cs.values())),
           "checks_pass_baseline": int(bool(cb) and all(cb.values())),
           "answer_cost_usd": base["cost"] + with_skill["cost"]}
    for role, jm in _judges_for(args, model):
        v = judge_pair(cache, jm, t, with_skill["text"], base["text"], workdir)
        if role == "primary":
            row.update(v, judge=jm)
        else:
            row["agreement_judge"], row["agreement_winner"] = jm, v["winner"]
    return row


def _run_jobs(args: argparse.Namespace, cache: Cache, workdir: str, tasks: list[dict]) -> list[dict]:
    """Run every (model, task) job on a thread pool, printing progress, and return the result rows."""
    rows: list[dict] = []
    jobs = [(m, t) for m in args.answer_models for t in tasks]
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = {pool.submit(_run_one, args, cache, workdir, m, t): (m, t["id"]) for m, t in jobs}
        for i, fut in enumerate(as_completed(futs), 1):
            r = fut.result()
            rows.append(r)
            print(f"[{i}/{len(jobs)}] {r['winner']:<8} {r['model']:<28} {r['id']:<8} "
                  f"checks skill={r['checks_pass_skill']} base={r['checks_pass_baseline']}", flush=True)
    return rows


def _summarize_by_skill(rows: list[dict], tasks: list[dict], models: list[str]) -> dict[str, dict]:
    """Summarize results per skill and answer model."""
    by_skill_model: dict[str, dict] = defaultdict(dict)
    for m in models:
        for s in sorted({t["skill"] for t in tasks}):
            sub = [r for r in rows if r["model"] == m and r["skill"] == s]
            by_skill_model[s][m] = {k: summarize(sub)[k] for k in ("skill_wins", "baseline_wins", "ties",
                                                                   "mean_score_delta", "checks_pass_skill",
                                                                   "checks_pass_baseline")}
    return by_skill_model


def _build_report(args: argparse.Namespace, data: dict, tasks: list[dict], rows: list[dict],
                  by_model: dict[str, dict]) -> tuple[dict, dict]:
    """Assemble the JSON report and the judge-agreement summary."""
    by_skill_model = _summarize_by_skill(rows, tasks, args.answer_models)
    agree = [r for r in rows if r.get("agreement_winner") not in (None, "error") and r["winner"] != "error"]
    agreement = {"pairs": len(agree), "same_winner": sum(r["winner"] == r["agreement_winner"] for r in agree)}
    order_agree = [r for r in rows if "order_agree" in r]
    report = {
        "suite": str(TASKS.relative_to(ROOT)).replace("\\", "/"), "provenance": data["provenance"],
        "answer_models": args.answer_models, "judge": args.judge, "alt_judge": args.alt_judge,
        "judging": "blind, both answer orders; a winner counts only if both orders agree",
        "by_model": by_model, "by_skill": by_skill_model, "judge_agreement": agreement,
        "order_consistency": sum(r["order_agree"] for r in order_agree) / max(len(order_agree), 1),
        "answer_cost_usd": round(sum(r.get("answer_cost_usd", 0) for r in rows), 2),
        "results": sorted(rows, key=lambda r: (r["model"], r["id"])),
    }
    return report, agreement


def _print_summary(by_model: dict[str, dict], agreement: dict) -> None:
    """Print the per-model summary lines and the judge agreement."""
    for m, s in by_model.items():
        lo, hi = s["win_rate_ci95"]
        print(f"\n{m}: skill {s['skill_wins']} / baseline {s['baseline_wins']} / tie {s['ties']} "
              f"(win rate {s['win_rate']:.2f}, 95% CI {lo:.2f}-{hi:.2f}, sign test p={s['sign_test_p']:.3g}); "
              f"delta {s['mean_score_delta']:+.2f}; checks pass {s['checks_pass_skill']:.2f} vs "
              f"{s['checks_pass_baseline']:.2f}; errors {s['errors']}")
    if agreement["pairs"]:
        print(f"judge agreement: {agreement['same_winner']}/{agreement['pairs']}")


def main() -> int:
    """Run the held-out suite for each answer model and write per-model, per-skill and per-task results."""
    args = _parse_args()
    data = json.loads(TASKS.read_text(encoding="utf-8"))
    tasks = [t for t in data["tasks"] if not args.skills or t["skill"] in args.skills][: args.limit]
    random.Random(args.seed).shuffle(tasks)  # spread skills across workers  # noqa: S311
    cache = Cache(args.cache)
    workdir = tempfile.mkdtemp(prefix="heldout-")
    rows = _run_jobs(args, cache, workdir, tasks)
    by_model = {m: summarize([r for r in rows if r["model"] == m]) for m in args.answer_models}
    report, agreement = _build_report(args, data, tasks, rows, by_model)
    _print_summary(by_model, agreement)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
