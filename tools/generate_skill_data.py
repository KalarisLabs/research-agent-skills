"""Generate review-ready skill data with Claude: trigger-rich descriptions and eval suites.

Outputs are data files that the import pipeline and benchmarks consume. They are generated
from each skill's own SKILL.md, validated mechanically here, and labeled as generated so a
human can review them (see `provenance`).

    descriptions -> third_party/description-overrides.yaml (adapted skills whose description lacks
                    "Use when" triggers, is short, or contains marketing words)
    evals        -> evals/<skill>/evals.json (3 realistic prompts + 1-2 near misses per skill)

Usage (uses the Claude Code CLI login or ANTHROPIC_API_KEY):
    uv run tools/generate_skill_data.py descriptions --model claude-sonnet-5-5 --workers 6
    uv run tools/generate_skill_data.py evals --model claude-sonnet-5-5 --workers 6 [--skills a b]
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import ROOT, THIRD_PARTY, load_skills  # noqa: E402
from skill_quality import MARKETING, TRIGGER, tfidf_overlap  # noqa: E402

OVERRIDES = THIRD_PARTY / "description-overrides.yaml"
LOCK = threading.Lock()

DESC_PROMPT = """You are improving the frontmatter description of an Agent Skill. Agents decide whether to load a skill
from its name and description alone, so the description must say precisely what the skill does and when to use it.

Skill name: {name}
Current description: {desc}

SKILL.md (excerpt):
<skill>
{body}
</skill>

Write a new description that:
- is 250-900 characters, third person, plain technical English
- first says what the skill does, naming the concrete library/tool/database/file formats/commands it covers
- then gives 3-6 triggers phrased as "Use when ..." clauses describing what a researcher is trying to do
- if a closely related tool exists, says when NOT to use this skill (one short clause)
- contains no marketing words (comprehensive, powerful, advanced, cutting-edge, state-of-the-art, seamless,
  robust, battle-tested, revolutionary), no star counts, no angle brackets, no claims absent from the excerpt
Reply with JSON only: {{"description": "..."}}"""

EVAL_PROMPT = """You are writing an evaluation suite for an Agent Skill used by researchers.

Skill name: {name}
Description: {desc}

SKILL.md (excerpt):
<skill>
{body}
</skill>

Similar skills in the same library (for near misses):
{siblings}

Write:
- 3 prompts a real researcher would type that SHOULD make an agent use this skill. Vary them: one short,
  one with concrete context (file names, dataset, organism, model, journal, error message), one describing a goal
  without naming the tool. Do not copy phrases from the description.
- 1 or 2 near-miss prompts that look related but should NOT use this skill (they belong to a listed similar
  skill, or to no skill). For each, name the better skill or "none".
- For each prompt, an expected_output rubric: what a correct, careful answer must contain (one or two sentences).
Reply with JSON only:
{{"evals": [{{"prompt": "...", "expected_output": "...", "should_trigger": true}},
            {{"prompt": "...", "expected_output": "...", "should_trigger": false, "better_skill": "name-or-none"}}]}}"""


def claude(prompt: str, model: str) -> str:
    exe = shutil.which("claude")
    if not exe:
        sys.exit("claude CLI not found on PATH")
    cmd = [exe, "-p", "--output-format", "json", "--disable-slash-commands", "--tools", "",
           "--no-session-persistence", "--model", model]
    res = subprocess.run(cmd, input=prompt, capture_output=True, text=True, encoding="utf-8", timeout=600)
    return json.loads(res.stdout)["result"]


def parse_json(text: str) -> dict:
    return json.loads(re.search(r"\{.*\}", text, re.S).group(0))


def excerpt(body: str, limit: int = 14000) -> str:
    body = re.sub(r"```.*?```", "[code block omitted]", body, flags=re.S)
    return body[:limit]


def valid_description(d: str) -> list[str]:
    problems = []
    if not 200 <= len(d) <= 1024:
        problems.append(f"length {len(d)}")
    if not TRIGGER.search(d):
        problems.append("no 'Use when' trigger")
    if MARKETING.search(d):
        problems.append("marketing word")
    if re.search(r"[<>]", d):
        problems.append("angle bracket")
    return problems


def needs_description(s) -> bool:
    d = " ".join(str(s.meta.get("description", "")).split())
    return bool(valid_description(d))


def adapted_names() -> set[str]:
    m = json.loads((THIRD_PARTY / "upstream-manifest.json").read_text(encoding="utf-8"))
    return {s["name"] for s in m["skills"] if s["rewrite_status"] == "imported"}


def cmd_descriptions(args: argparse.Namespace) -> int:
    existing = yaml.safe_load(OVERRIDES.read_text(encoding="utf-8")) if OVERRIDES.exists() else {}
    overrides: dict = (existing or {}).get("descriptions", {})
    adapted = adapted_names()
    todo = [s for s in load_skills() if s.name in adapted and s.name not in overrides
            and (args.skills and s.name in args.skills or not args.skills and needs_description(s))]
    print(f"{len(todo)} descriptions to generate")

    def work(s):
        for _ in range(3):
            try:
                prompt = DESC_PROMPT.format(name=s.name, desc=s.meta.get("description", ""), body=excerpt(s.body))
                d = " ".join(parse_json(claude(prompt, args.model))["description"].split())
            except (json.JSONDecodeError, AttributeError, KeyError, subprocess.TimeoutExpired):
                continue
            if not valid_description(d):
                return s.name, d
        return s.name, None

    with ThreadPoolExecutor(args.workers) as pool:
        for fut in as_completed([pool.submit(work, s) for s in todo]):
            name, d = fut.result()
            if d is None:
                print(f"FAILED {name}")
                continue
            with LOCK:
                overrides[name] = d
                OVERRIDES.write_text(yaml.safe_dump({
                    "_comment": "Generated by tools/generate_skill_data.py from each skill's SKILL.md and "
                                "validated (length, triggers, no marketing). Applied by tools/rebrand.py at import. "
                                "Review welcome.",
                    "model": args.model, "descriptions": dict(sorted(overrides.items()))},
                    sort_keys=False, allow_unicode=True, width=10_000), encoding="utf-8")
            print(f"ok {name}")
    return 0


def cmd_evals(args: argparse.Namespace) -> int:
    skills = {s.name: s for s in load_skills()}
    pairs = tfidf_overlap(list(skills.values()), 0.12)
    neighbours: dict[str, list[tuple[float, str]]] = {}
    for a, b, sim in pairs:
        neighbours.setdefault(a, []).append((sim, b))
        neighbours.setdefault(b, []).append((sim, a))
    todo = [n for n in sorted(skills) if (not args.skills or n in args.skills)
            and (args.force or not (ROOT / "evals" / n / "evals.json").exists())]
    print(f"{len(todo)} eval suites to generate")

    def work(name: str):
        s = skills[name]
        sib = sorted(neighbours.get(name, []), reverse=True)[:6]
        siblings = "\n".join(f"- {b}: {' '.join(str(skills[b].meta.get('description', '')).split())[:300]}"
                             for _, b in sib) or "- (none)"
        for _ in range(3):
            try:
                prompt = EVAL_PROMPT.format(name=name, desc=s.meta.get("description", ""),
                                            body=excerpt(s.body, 10000), siblings=siblings)
                data = parse_json(claude(prompt, args.model))
                evs = data["evals"]
            except (json.JSONDecodeError, AttributeError, KeyError, subprocess.TimeoutExpired):
                continue
            pos = [e for e in evs if e.get("should_trigger", True)]
            neg = [e for e in evs if not e.get("should_trigger", True)]
            if len(pos) >= 3 and neg and all(e.get("prompt") and e.get("expected_output") for e in evs):
                return name, evs
        return name, None

    with ThreadPoolExecutor(args.workers) as pool:
        for fut in as_completed([pool.submit(work, n) for n in todo]):
            name, evs = fut.result()
            if evs is None:
                print(f"FAILED {name}")
                continue
            out = []
            for i, e in enumerate(evs, 1):
                item = {"id": i, "prompt": e["prompt"].strip(), "expected_output": e["expected_output"].strip(),
                        "files": []}
                if not e.get("should_trigger", True):
                    item["should_trigger"] = False
                    if e.get("better_skill") and e["better_skill"] in skills:
                        item["better_skill"] = e["better_skill"]
                out.append(item)
            path = ROOT / "evals" / name / "evals.json"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps({"skill_name": name, "provenance": f"generated ({args.model}), pending review",
                                        "evals": out}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            print(f"ok {name}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("descriptions", "evals"):
        p = sub.add_parser(name)
        p.add_argument("--model", default="claude-sonnet-5-5")
        p.add_argument("--workers", type=int, default=6)
        p.add_argument("--skills", nargs="*")
        p.add_argument("--force", action="store_true")
    args = ap.parse_args()
    return {"descriptions": cmd_descriptions, "evals": cmd_evals}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
