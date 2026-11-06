"""Score how strongly each skill is written (static rubric, 0-100) and find overlapping skills.

This is the first of the three verification tiers (see benchmarks/README.md):
  1. static quality (this tool): deterministic, runs on every PR
  2. trigger routing (tools/trigger_bench.py): does the right skill get picked?
  3. task outcomes (benchmarks/task_evals): does the skill improve answers?

Rubric (100 points):
  description 30  length, "Use when" triggers, concrete named entities, no marketing words
  structure   30  numbered workflow, tables/checklists, handoffs, verification/honesty rules, headings
  disclosure  15  <= 500 lines, references/ for long skills, links resolve
  scripts     15  docstring with usage, argparse CLI, exercised by tests or documented commands (N/A = full)
  freshness   10  verify-against-official-source language for time-sensitive facts, compatibility field
  penalty     -5  prose slop index > 30 (skills that quote slop as examples are exempt)

Usage:
    uv run tools/skill_quality.py                         # report for all skills
    uv run tools/skill_quality.py --origin original --min-score 75   # CI gate for original skills
    uv run tools/skill_quality.py --json benchmarks/results/skill-quality.json \
        --markdown benchmarks/results/skill-quality.md
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import ROOT, SKILLS_DIR, THIRD_PARTY, Skill, load_skills  # noqa: E402

sys.path.insert(0, str(ROOT / "tests"))
from script_inventory import help_testable  # noqa: E402

MARKETING = re.compile(r"\b(comprehensive|powerful|advanced|cutting-edge|state-of-the-art|seamless(ly)?|robust|"
                       r"world-class|best-in-class|revolutionary|ultimate|next-generation)\b", re.I)
TRIGGER = re.compile(r"\b(use (it |this )?(when|for|to|if)|when (the user|you|a user)|trigger)", re.I)
VERIFY = re.compile(r"\b(verify|official|current (author )?guide|author guidelines|check the|documentation at|"
                    r"never (fabricate|invent|guess)|do not (fabricate|invent)|cite the source|confirm)\b", re.I)
TIME_SENSITIVE = re.compile(r"\b(version|v\d+\.\d+|20[12]\d|page limit|word limit|deadline|pricing|api key|"
                            r"endpoint|release)\b", re.I)
SLOP_EXEMPT = {"unslop-academic-writing"}
TOKEN = re.compile(r"[a-z][a-z0-9+-]{2,}")
STOP = set("the and for with use when this that from into your are can will not you any all how what which its "
           "their them they has have been also such via using used uses more most other than then each per".split())


def _load_slop():
    """Load slop."""
    path = SKILLS_DIR / "unslop-academic-writing" / "scripts" / "slop_check.py"
    if not path.exists():
        return None
    sys.dont_write_bytecode = True  # never leave __pycache__ inside skills/
    spec = importlib.util.spec_from_file_location("slop_check", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["slop_check"] = mod  # dataclasses resolve types through sys.modules
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


SLOP = _load_slop()


def tests_text() -> str:
    """Handle tests text."""
    return "\n".join(p.read_text(encoding="utf-8") for p in (ROOT / "tests").glob("*.py"))


def _score_description(desc: str, parts: dict[str, float], notes: list[str]) -> None:
    """Score the description (30 points): length, triggers, named entities and marketing words."""
    n = len(desc)
    if 200 <= n <= 1024:
        parts["desc_length"] = 10
    elif 120 <= n < 200:
        parts["desc_length"] = 7
    elif n >= 60:
        parts["desc_length"] = 3
    else:
        parts["desc_length"] = 0
    if n < 200:
        notes.append(f"description is short ({n} chars): add triggers and named tools/artifacts")
    parts["desc_triggers"] = 8 if TRIGGER.search(desc) else 0
    if not parts["desc_triggers"]:
        notes.append("description lacks 'Use when ...' trigger phrasing")
    entities = set(re.findall(r"\b(?:[A-Z][A-Za-z0-9]*[A-Z0-9][A-Za-z0-9]*|[A-Z][a-z]+(?:[A-Z][a-z]+)+|"
                              r"\.[a-z]{2,5}\b|[A-Za-z]+\d+[A-Za-z\d]*)", desc))
    parts["desc_specific"] = min(6, len(entities) * 1.5)
    if len(entities) < 3:
        notes.append("description names few concrete tools, formats or venues")
    marketing = MARKETING.findall(desc)
    parts["desc_no_marketing"] = max(0, 6 - 3 * len(marketing))
    if marketing:
        words = sorted({m[0] if isinstance(m, tuple) else m for m in marketing})
        notes.append(f"marketing words in description: {', '.join(words)}")


def _score_structure(body: str, parts: dict[str, float], notes: list[str]) -> None:
    """Score the body structure (30 points): workflow, tables, handoffs, verification and headings."""
    numbered = len(re.findall(r"^\s*\d+[.)] ", body, re.M))
    if numbered >= 3:
        parts["workflow"] = 8
    elif numbered:
        parts["workflow"] = 4
    else:
        parts["workflow"] = 0
    if numbered < 3:
        notes.append("no numbered workflow (3+ steps)")
    tables = len(re.findall(r"^\|.*\|\s*$", body, re.M)) >= 3
    checklist = bool(re.search(r"^\s*[-*] \[[ x]\]", body, re.M))
    parts["tables_checklists"] = 6 if (tables or checklist) else 0
    parts["handoffs"] = 4 if re.search(r"^#+ .*(related|see also|next steps|hand ?off)", body, re.I | re.M) else 0
    parts["verification"] = 6 if VERIFY.search(body) else 0
    if not parts["verification"]:
        notes.append("no verification/honesty guidance (verify, never fabricate, official source)")
    headings = len(re.findall(r"^#{2,3} ", body, re.M))
    if headings >= 4:
        parts["headings"] = 6
    elif headings >= 2:
        parts["headings"] = 3
    else:
        parts["headings"] = 0


def _score_disclosure(s: Skill, body: str, lines: int, parts: dict[str, float], notes: list[str]) -> None:
    """Score progressive disclosure (15 points): size, references directory and resolvable links."""
    if lines <= 500:
        parts["size"] = 8
    elif lines <= 700:
        parts["size"] = 3
    else:
        parts["size"] = 0
    has_refs = (s.path / "references").is_dir()
    parts["references"] = 4 if lines <= 250 or has_refs else 0
    broken = [t for t in re.findall(r"\]\(((?:references|scripts|assets|templates)/[^)#\s]+)", body)
              if not (s.path / t).exists()]
    parts["links"] = 0 if broken else 3
    if broken:
        notes.append(f"broken links: {', '.join(broken[:3])}")


def _score_scripts(s: Skill, body: str, tests_blob: str, parts: dict[str, float], notes: list[str]) -> None:
    """Score the skill's scripts (15 points): usage docstrings, argparse CLIs and test or doc coverage."""
    scripts = sorted((s.path / "scripts").glob("*.py")) if (s.path / "scripts").is_dir() else []
    scripts = [p for p in scripts if not p.name.startswith("_")]
    if not scripts:
        parts["scripts"] = 15
        return
    doc = sum(bool(re.search(r'"""[\s\S]*?(usage|example)', p.read_text(encoding="utf-8", errors="replace")[:3000],
                             re.I)) for p in scripts) / len(scripts)
    cli = sum("argparse" in p.read_text(encoding="utf-8", errors="replace") for p in scripts) / len(scripts)
    # Exercised = named in a test, documented in SKILL.md, or run by the offline --help smoke test.
    exercised = sum((p.name in tests_blob) or (p.name in body) or help_testable(p) for p in scripts) / len(scripts)
    parts["scripts"] = round(5 * doc + 4 * cli + 6 * exercised, 1)
    if exercised < 1:
        notes.append("some scripts are neither tested nor shown in SKILL.md")


def _slop_penalty(s: Skill, body: str, notes: list[str]) -> tuple[float, float | None]:
    """Return (penalty, slop index) for the prose slop check, which skills quoting slop are exempt from."""
    if SLOP is None or s.name in SLOP_EXEMPT:
        return 0.0, None
    slop_index = SLOP.analyse(re.sub(r"```.*?```", "", body, flags=re.S))["slop_index"]
    if slop_index > 30:
        notes.append(f"prose slop index {slop_index} (run unslop-academic-writing/scripts/slop_check.py)")
        return 5, slop_index
    return 0.0, slop_index


def score_skill(s: Skill, tests_blob: str) -> dict:
    """Score one skill against the static rubric and return its parts, notes and total."""
    desc = " ".join(str(s.meta.get("description", "")).split())
    body = s.body
    lines = (s.path / "SKILL.md").read_text(encoding="utf-8").count("\n") + 1
    parts: dict[str, float] = {}
    notes: list[str] = []

    _score_description(desc, parts, notes)
    _score_structure(body, parts, notes)
    _score_disclosure(s, body, lines, parts, notes)
    _score_scripts(s, body, tests_blob, parts, notes)

    # Freshness (10)
    needs_verify = bool(TIME_SENSITIVE.search(body))
    parts["freshness"] = 5 if (not needs_verify or VERIFY.search(body)) else 0
    parts["compatibility"] = 5 if s.meta.get("compatibility") else 2

    penalty, slop_index = _slop_penalty(s, body, notes)
    total = round(sum(parts.values()) - penalty, 1)
    return {"name": s.name, "category": s.category, "score": total, "parts": parts, "penalty": penalty,
            "slop_index": slop_index, "lines": lines, "notes": notes}


def _tfidf_vectors(skills: list[Skill]) -> dict[str, dict[str, float]]:
    """Build L2-normalised tf-idf vectors from each skill's description."""
    docs = {s.name: [t for t in TOKEN.findall(str(s.meta.get("description", "")).lower()) if t not in STOP]
            for s in skills}
    df = Counter(t for toks in docs.values() for t in set(toks))
    n = len(docs)
    vecs = {}
    for name, toks in docs.items():
        tf = Counter(toks)
        v = {t: (1 + math.log(c)) * math.log(n / df[t]) for t, c in tf.items()}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
        vecs[name] = {t: x / norm for t, x in v.items()}
    return vecs


def tfidf_overlap(skills: list[Skill], threshold: float) -> list[tuple[str, str, float]]:
    """Return skill pairs whose description cosine similarity is at least `threshold`, highest first."""
    vecs = _tfidf_vectors(skills)
    names = sorted(vecs)
    pairs = []
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            va, vb = vecs[a], vecs[b]
            sim = sum(x * vb.get(t, 0.0) for t, x in va.items())
            if sim >= threshold:
                pairs.append((a, b, round(sim, 3)))
    return sorted(pairs, key=lambda p: -p[2])


def _select_skills(args: argparse.Namespace, skills: list[Skill]) -> list[Skill]:
    """Filter skills by name and by origin (original vs adapted from upstream)."""
    manifest = json.loads((THIRD_PARTY / "upstream-manifest.json").read_text(encoding="utf-8"))
    adapted = {s["name"] for s in manifest["skills"] if s["rewrite_status"] == "imported"}
    return [s for s in skills if (not args.skills or s.name in args.skills)
            and (args.origin == "all" or (s.name in adapted) == (args.origin == "adapted"))]


def _print_report(args: argparse.Namespace, results: list[dict], overlaps: list[tuple[str, str, float]]) -> None:
    """Print the score table, summary line and overlapping description pairs."""
    for r in results if args.skills else results[:25]:
        print(f"{r['score']:5.1f}  {r['name']:<42} {'; '.join(r['notes'][:2])}")
    scores = [r["score"] for r in results]
    if scores:
        print(f"\n{len(results)} skills: mean {sum(scores) / len(scores):.1f}, min {min(scores):.1f}, "
              f"< 60: {sum(x < 60 for x in scores)}, >= 85: {sum(x >= 85 for x in scores)}")
    if overlaps:
        print(f"\n{len(overlaps)} skill pairs with overlapping descriptions (cosine >= {args.overlap}):")
        for a, b, sim in overlaps[:15]:
            print(f"  {sim:.2f}  {a} <-> {b}")


def _write_outputs(args: argparse.Namespace, results: list[dict], overlaps: list[tuple[str, str, float]]) -> None:
    """Write the optional JSON and Markdown reports."""
    report = {"skills": results, "overlaps": [{"a": a, "b": b, "similarity": s} for a, b, s in overlaps]}
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    if args.markdown:
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        md = ["# Skill quality report", "", "Generated by `tools/skill_quality.py`. Static rubric, 0-100.", "",
              "| Score | Skill | Category | Top issues |", "|---:|---|---|---|"]
        md += [f"| {r['score']} | `{r['name']}` | {r['category']} | {'; '.join(r['notes'][:2]) or '-'} |"
               for r in sorted(results, key=lambda r: -r["score"])]
        args.markdown.write_text("\n".join(md) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    """Run the command-line interface."""
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("skills", nargs="*", help="skill names (default: all)")
    ap.add_argument("--origin", choices=["all", "original", "adapted"], default="all")
    ap.add_argument("--min-score", type=float, help="exit 1 if any selected skill scores below this")
    ap.add_argument("--overlap", type=float, default=0.55, help="description-similarity threshold to report")
    ap.add_argument("--json", type=Path)
    ap.add_argument("--markdown", type=Path)
    args = ap.parse_args(argv)

    skills = load_skills()
    selected = _select_skills(args, skills)
    blob = tests_text()
    results = sorted((score_skill(s, blob) for s in selected), key=lambda r: r["score"])
    overlaps = tfidf_overlap(skills, args.overlap)

    _print_report(args, results, overlaps)
    _write_outputs(args, results, overlaps)
    if args.min_score is not None:
        failing = [r for r in results if r["score"] < args.min_score]
        for r in failing:
            print(f"FAIL {r['name']}: {r['score']} < {args.min_score}: {'; '.join(r['notes'])}")
        return 1 if failing else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
