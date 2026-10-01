"""Task-outcome benchmark: do answers get better with the skill in context?

For each prompt in evals/<skill>/evals.json that should trigger the skill, generate two
answers with `claude -p`: one with no skills (baseline) and one with the skill's SKILL.md
appended to the system prompt. A separate judge call compares them blind (A/B order
randomized) against the eval's expected_output rubric.

This isolates the value of the skill's *instructions*. Scripts are not executed
(tools are disabled), so it understates skills whose value is in their code. Deterministic
script behavior is covered by the unit tests and domain benchmarks instead.

Usage (paid; uses your Claude Code login or ANTHROPIC_API_KEY):
    uv run benchmarks/task_evals/run.py --skills unslop-academic-writing citation-verification \
        --model claude-sonnet-5-5 --judge-model claude-opus-5-5 --json benchmarks/results/task-evals.json
    uv run benchmarks/task_evals/run.py --all-original --max-budget-usd 20
"""

from __future__ import annotations

import argparse
import json
import random
import re
import shutil
import subprocess
import sys
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):  # Windows consoles default to cp1252
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[2]
JUDGE = """You are grading two answers to the same research-assistant request. Be strict and specific.

<request>{prompt}</request>
<rubric>A strong answer: {expected}</rubric>

<answer_A>
{a}
</answer_A>

<answer_B>
{b}
</answer_B>

Score each answer 1-10 on: correctness and rigor (no fabricated facts or citations), following
the rubric, specificity and usefulness for a working researcher. Then pick a winner.
Reply with JSON only: {{"score_A": n, "score_B": n, "winner": "A" | "B" | "tie", "reason": "one sentence"}}"""


def claude(prompt: str, model: str | None, system_file: Path | None, budget: float | None) -> str:
    exe = shutil.which("claude")
    if not exe:
        sys.exit("claude CLI not found on PATH (install Claude Code and log in, or set ANTHROPIC_API_KEY)")
    cmd = [exe, "-p", "--output-format", "json", "--disable-slash-commands", "--tools", "", "--no-session-persistence"]
    if model:
        cmd += ["--model", model]
    if system_file:
        cmd += ["--append-system-prompt-file", str(system_file)]
    if budget:
        cmd += ["--max-budget-usd", str(budget)]
    res = subprocess.run(cmd, input=prompt, capture_output=True, text=True, encoding="utf-8", timeout=900)
    try:
        return json.loads(res.stdout)["result"]
    except (json.JSONDecodeError, KeyError):
        raise RuntimeError(f"claude failed: {res.stderr[:300] or res.stdout[:300]}") from None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--skills", nargs="*", default=[])
    ap.add_argument("--all-original", action="store_true", help="every skill that has evals/<skill>/evals.json")
    ap.add_argument("--model", help="model answering the task")
    ap.add_argument("--judge-model", help="model grading (default: same as --model)")
    ap.add_argument("--max-budget-usd", type=float, help="per-call budget cap passed to claude")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--merge", action="store_true", help="merge into an existing --json report, replacing re-run tasks")
    ap.add_argument("--json", type=Path)
    args = ap.parse_args()
    rng = random.Random(args.seed)  # noqa: S311 - A/B order shuffling, not cryptography

    eval_files = sorted((ROOT / "evals").glob("*/evals.json"))
    wanted = {f.parent.name for f in eval_files} if args.all_original else set(args.skills)
    if not wanted:
        ap.error("pass --skills NAME ... or --all-original")
    results = []
    for f in eval_files:
        data = json.loads(f.read_text(encoding="utf-8"))
        skill = data["skill_name"]
        if skill not in wanted:
            continue
        skill_md = ROOT / "skills" / skill / "SKILL.md"
        for ev in data["evals"]:
            if not ev.get("should_trigger", True):
                continue
            skill_is_a = rng.random() < 0.5
            try:
                base = claude(ev["prompt"], args.model, None, args.max_budget_usd)
                with_skill = claude(ev["prompt"], args.model, skill_md, args.max_budget_usd)
                a, b = (with_skill, base) if skill_is_a else (base, with_skill)
                verdict_raw = claude(JUDGE.format(prompt=ev["prompt"], expected=ev["expected_output"], a=a, b=b),
                                     args.judge_model or args.model, None, args.max_budget_usd)
                v = json.loads(re.search(r"\{.*\}", verdict_raw, re.S).group(0))
            except (RuntimeError, AttributeError, json.JSONDecodeError, subprocess.TimeoutExpired) as exc:
                # A failed call (rate limit, budget, malformed output) is an error, never a tie.
                v = {"score_A": None, "score_B": None, "winner": "error", "reason": f"run failed: {exc}"[:300]}
            skill_score = v["score_A"] if skill_is_a else v["score_B"]
            base_score = v["score_B"] if skill_is_a else v["score_A"]
            winner = {"A": "skill" if skill_is_a else "baseline", "B": "baseline" if skill_is_a else "skill",
                      "error": "error"}.get(v.get("winner"), "tie")
            results.append({"skill": skill, "prompt": ev["prompt"], "winner": winner, "skill_score": skill_score,
                            "baseline_score": base_score, "reason": v.get("reason", "")})
            print(f"{winner:<8} {skill:<36} skill={skill_score} base={base_score}  {ev['prompt'][:60]}")

    if args.merge and args.json and args.json.exists():  # replace re-run tasks, keep the rest
        old = json.loads(args.json.read_text(encoding="utf-8"))["results"]
        rerun = {(r["skill"], r["prompt"]) for r in results}
        results = [r for r in old if (r["skill"], r["prompt"]) not in rerun] + results
    valid = [r for r in results if r["winner"] != "error"]
    errors = len(results) - len(valid)
    wins = sum(r["winner"] == "skill" for r in valid)
    losses = sum(r["winner"] == "baseline" for r in valid)
    numeric = (int, float)
    scored = [r for r in valid if isinstance(r["skill_score"], numeric) and isinstance(r["baseline_score"], numeric)]
    delta = sum(r["skill_score"] - r["baseline_score"] for r in scored) / max(len(scored), 1)
    print(f"\n{len(valid)} graded tasks: skill wins {wins}, baseline wins {losses}, ties {len(valid) - wins - losses}; "
          f"mean score delta {delta:+.2f}" + (f"; {errors} failed runs excluded" if errors else ""))
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps({"model": args.model, "judge_model": args.judge_model or args.model,
                                         "graded": len(valid), "errors": errors,
                                         "win_rate": wins / max(len(valid), 1), "mean_delta": delta,
                                         "results": results}, indent=2) + "\n", encoding="utf-8")
    return 1 if errors and not valid else 0


if __name__ == "__main__":
    sys.exit(main())
