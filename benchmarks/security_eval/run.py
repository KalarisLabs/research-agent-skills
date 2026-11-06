"""Security evaluation of the skill library: scanner coverage, agreement and reviewed false-positive rates.

Runs three scanners over skills/ and compares them per skill:
  - lint      tools/lint_injection.py (prompt injection, hidden content, dangerous code), all findings
  - scanner   Cisco AI Defense skill-scanner (static + behavioral)
  - bandit    Bandit on Python files

Reports, per scanner, how many skills it flags (HIGH+ severity and any severity), pairwise agreement
(Cohen's kappa and Jaccard over the 281 skills), the share of HIGH findings that a human review
accepted as not exploitable (security/*baseline*.json), and how many adapted skills needed patches.

Usage (network for uvx on first run):
    uv run benchmarks/security_eval/run.py --json benchmarks/results/security-eval.json
    uv run benchmarks/security_eval/run.py --reuse      # reuse .cache/security/*.json
"""

from __future__ import annotations

import argparse
import itertools
import json
import re
import subprocess
import sys
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):  # Windows consoles default to cp1252
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / ".cache" / "security"
SKILLS = ROOT / "skills"
HIGH = {"HIGH", "CRITICAL"}


def run_scanners() -> None:
    """Run scanners."""
    CACHE.mkdir(parents=True, exist_ok=True)
    cmds = [
        ["uv", "run", "tools/lint_injection.py", "--no-baseline", "--json", str(CACHE / "lint.json")],
        ["uvx", "bandit==1.9.4", "-r", "skills", "-f", "json", "-o", str(CACHE / "bandit.json"), "-q"],
        ["uvx", "--from", "cisco-ai-skill-scanner==2.1.0", "skill-scanner", "scan-all", "skills", "--recursive",
         "--use-behavioral", "--format", "json", "--output", str(CACHE / "skill-scanner.json")],
    ]
    for cmd in cmds:  # scanners exit non-zero when they find something; the JSON is what matters
        subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", timeout=3600, check=False)


def skill_of(path: str) -> str | None:
    """Handle skill of."""
    m = re.search(r"(?:^|[/\\])skills[/\\]([^/\\]+)[/\\]", path.replace("\\", "/") + "/")
    return m.group(1) if m else None


def load_findings() -> dict[str, list[tuple[str, str, str]]]:
    """scanner -> [(skill, severity, rule)]"""
    out: dict[str, list[tuple[str, str, str]]] = {}
    lint = json.loads((CACHE / "lint.json").read_text(encoding="utf-8"))
    out["lint"] = [(skill_of(f["path"]), f["severity"].upper(), f["rule"]) for f in lint if skill_of(f["path"])]
    bandit = json.loads((CACHE / "bandit.json").read_text(encoding="utf-8"))
    out["bandit"] = [(skill_of(r["filename"]), r["issue_severity"].upper(), r["test_id"]) for r in bandit["results"]
                     if skill_of(r["filename"])]
    ss = json.loads((CACHE / "skill-scanner.json").read_text(encoding="utf-8"))
    rows = []
    for r in ss.get("results", []):
        skill = r.get("skill_name") or Path(str(r.get("skill_path", ""))).name
        rows += [(skill, str(f.get("severity")).upper(), f.get("rule_id")) for f in r.get("findings", [])]
    out["scanner"] = rows
    return out


def kappa(a: set[str], b: set[str], universe: set[str]) -> float:
    """Handle kappa."""
    n = len(universe)
    both = len(a & b)
    neither = len(universe - a - b)
    po = (both + neither) / n
    pa, pb = len(a) / n, len(b) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


def patched_skills() -> dict[str, list[str]]:
    """patch file -> skills it touches"""
    out = {}
    for p in sorted((ROOT / "third_party" / "patches").glob("*.patch")):
        names = set(re.findall(r"^\+\+\+ b/skills/([^/]+)/", p.read_text(encoding="utf-8"), re.M))
        out[p.name] = sorted(names)
    return out


def main() -> int:
    """Run (or reuse) the scanners and write coverage, agreement, reviewed false-positive and patch statistics."""
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--reuse", action="store_true", help="reuse scanner output in .cache/security")
    ap.add_argument("--json", type=Path)
    args = ap.parse_args()
    if not args.reuse:
        run_scanners()

    universe = {p.name for p in SKILLS.iterdir() if (p / "SKILL.md").is_file()}
    manifest = json.loads((ROOT / "third_party" / "upstream-manifest.json").read_text(encoding="utf-8"))
    adapted = {s["name"] for s in manifest["skills"] if s["rewrite_status"] == "imported"}
    findings = load_findings()

    per = {}
    flagged_high, flagged_any = {}, {}
    for name, rows in findings.items():
        flagged_any[name] = {s for s, _, _ in rows} & universe
        flagged_high[name] = {s for s, sev, _ in rows if sev in HIGH} & universe
        per[name] = {"findings": len(rows), "high_findings": sum(sev in HIGH for _, sev, _ in rows),
                     "skills_flagged_any": len(flagged_any[name]), "skills_flagged_high": len(flagged_high[name])}

    agreement = {}
    for x, y in itertools.combinations(sorted(findings), 2):
        for level, sets in (("high", flagged_high), ("any", flagged_any)):
            a, b = sets[x], sets[y]
            agreement[f"{x}~{y}|{level}"] = {
                "both": len(a & b), "only_" + x: len(a - b), "only_" + y: len(b - a),
                "jaccard": round(len(a & b) / len(a | b), 3) if a | b else None,
                "kappa": round(kappa(a, b, universe), 3)}
    high_any = set().union(*flagged_high.values())
    all_three_high = set.intersection(*flagged_high.values())

    # Reviewed false positives: HIGH skill-scanner findings whose key is in the reviewed baseline.
    accepted = set(json.loads((ROOT / "security" / "skill-scanner-baseline.json").read_text(encoding="utf-8"))
                   ["accepted"])
    ss = json.loads((CACHE / "skill-scanner.json").read_text(encoding="utf-8"))
    sys.path.insert(0, str(ROOT / "tools"))
    from skill_scanner_gate import finding_key  # noqa: E402
    keys = set()
    for r in ss.get("results", []):
        skill = r.get("skill_name") or Path(str(r.get("skill_path", ""))).name
        keys |= {finding_key(skill, f) for f in r.get("findings", []) if str(f.get("severity")).upper() in HIGH}
    reviewed = {"scanner_high_keys": len(keys), "accepted_after_review": len(keys & accepted),
                "unreviewed": len(keys - accepted),
                "review_note": "security/skill-scanner-review-2026-10-01.md: 8 eval() examples fixed by "
                               "post-0008 patch; the remaining keys were reviewed and judged not exploitable"}

    patches = patched_skills()
    patched = set().union(*patches.values()) if patches else set()
    report = {
        "skills": len(universe), "adapted_skills": len(adapted),
        "scanners": per, "agreement": agreement,
        "skills_flagged_high_by_any": len(high_any), "skills_flagged_high_by_all_three": len(all_three_high),
        "scanner_high_review": reviewed,
        "patches": {"files": len(patches), "adapted_skills_patched": len(patched & adapted),
                    "share_of_adapted": round(len(patched & adapted) / max(len(adapted), 1), 3),
                    "by_patch": patches},
    }
    for name, s in per.items():
        print(f"{name:<8} findings={s['findings']:<5} high={s['high_findings']:<4} "
              f"skills flagged: any={s['skills_flagged_any']:<4} high={s['skills_flagged_high']}")
    for k, v in agreement.items():
        print(f"{k:<26} both={v['both']:<4} jaccard={v['jaccard']} kappa={v['kappa']}")
    print(f"HIGH by any scanner: {len(high_any)} skills; by all three: {len(all_three_high)}")
    print(f"skill-scanner HIGH keys: {reviewed['scanner_high_keys']}, accepted after review "
          f"{reviewed['accepted_after_review']}, unreviewed {reviewed['unreviewed']}")
    print(f"patches: {len(patches)} files touching {len(patched & adapted)} of {len(adapted)} adapted skills")
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
