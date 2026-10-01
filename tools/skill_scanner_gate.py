"""Gate CI on Cisco AI Defense skill-scanner results.

The scanner (https://github.com/cisco-ai-defense/skill-scanner) runs separately
and writes a JSON report; this script fails on HIGH/CRITICAL findings that are
not in the reviewed baseline (security/skill-scanner-baseline.json). Baseline
keys are `skill|rule|file`, so accepted findings survive unrelated line edits.

Usage:
    uvx --from cisco-ai-skill-scanner skill-scanner scan-all skills --recursive --format json --output r.json
    uv run tools/skill_scanner_gate.py r.json
    uv run tools/skill_scanner_gate.py r.json --update-baseline   # after manual review only
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import ROOT  # noqa: E402

BASELINE = ROOT / "security" / "skill-scanner-baseline.json"
BLOCKING = {"CRITICAL", "HIGH"}


def finding_key(skill: str, finding: dict) -> str:
    path = str(finding.get("file_path") or "").replace("\\", "/").lower()
    return f"{skill}|{finding.get('rule_id')}|{path}"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("report", type=Path)
    ap.add_argument("--update-baseline", action="store_true")
    args = ap.parse_args(argv)

    report = json.loads(args.report.read_text(encoding="utf-8"))
    results = report.get("results", [])
    blocking: list[tuple[str, dict]] = []
    for r in results:
        skill = r.get("skill_name") or Path(str(r.get("skill_path", ""))).name
        blocking += [(skill, f) for f in r.get("findings", []) if str(f.get("severity")).upper() in BLOCKING]

    if args.update_baseline:
        keys = sorted({finding_key(s, f) for s, f in blocking})
        BASELINE.parent.mkdir(exist_ok=True)
        BASELINE.write_text(json.dumps({"_comment": "Reviewed HIGH/CRITICAL skill-scanner findings (skill|rule|file). "
                                                    "Update only after manual review.", "accepted": keys}, indent=2)
                            + "\n", encoding="utf-8", newline="\n")
        print(f"baseline updated: {len(keys)} accepted keys")
        return 0

    accepted = set(json.loads(BASELINE.read_text(encoding="utf-8"))["accepted"]) if BASELINE.exists() else set()
    new = [(s, f) for s, f in blocking if finding_key(s, f) not in accepted]
    for skill, f in new:
        where = f"{f.get('file_path')}:{f.get('line_number') or ''}"
        desc = str(f.get("description", ""))[:200]
        print(f"{f.get('severity'):<8} {skill} {f.get('rule_id')} {where}\n         {desc}")
    print(f"\n{len(results)} skills scanned: {len(blocking)} high/critical findings, "
          f"{len(blocking) - len(new)} baselined, {len(new)} new")
    return 1 if new else 0


if __name__ == "__main__":
    sys.exit(main())
