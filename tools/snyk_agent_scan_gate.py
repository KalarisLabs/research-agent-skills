"""Gate Snyk Agent Scan's JSON report on complete coverage and high risks.

Run after `snyk-agent-scan scan skills --json`. Medium and low findings are
reported for review; high and critical risks or incomplete scans fail CI.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def check(report: dict, skills_root: Path) -> tuple[list[str], list[str]]:
    expected = {p.name for p in skills_root.iterdir() if (p / "SKILL.md").is_file()}
    errors: list[str] = []
    warnings: list[str] = []
    seen: set[str] = set()
    paths = report.get("scan_path_responses")
    if not isinstance(paths, list) or not paths:
        return ["Missing scan_path_responses"], warnings

    for path in paths:
        if path.get("error"):
            errors.append(f"Scan path {path.get('path')}: {path['error']}")
        for server in path.get("server_risks", []):
            errors.append(f"Unexpected MCP server in skill-only scan: {server.get('name')}")
        for skill in path.get("skill_risks", []):
            name = skill.get("name")
            if not isinstance(name, str) or name in seen:
                errors.append(f"Missing or duplicate skill name: {name}")
                continue
            seen.add(name)
            if skill.get("error"):
                errors.append(f"Skill {name}: {skill['error']}")
            risks = skill.get("risk_indexes")
            if not isinstance(risks, dict):
                errors.append(f"Skill {name}: missing risk_indexes")
                continue
            for risk_name, detail in risks.items():
                score = detail.get("score") if isinstance(detail, dict) else None
                if not isinstance(score, int) or not 0 <= score <= 1000:
                    errors.append(f"Skill {name}: invalid score for {risk_name}: {score}")
                    continue
                finding = f"Skill {name}: {risk_name} ({score}/1000)"
                (errors if score >= 600 else warnings).append(finding)

    missing = expected - seen
    extra = seen - expected
    if missing:
        errors.append(f"Unscanned skills: {', '.join(sorted(missing))}")
    if extra:
        errors.append(f"Unexpected skills: {', '.join(sorted(extra))}")
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    parser.add_argument("--skills-root", type=Path, default=Path("skills"))
    args = parser.parse_args()
    try:
        report = json.loads(args.report.read_text(encoding="utf-8"))
        errors, warnings = check(report, args.skills_root)
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        print(f"Invalid Snyk Agent Scan report: {exc}", file=sys.stderr)
        return 2
    for finding in warnings:
        print(f"WARNING: {finding}")
    for finding in errors:
        print(f"ERROR: {finding}", file=sys.stderr)
    print(f"Snyk Agent Scan: {len(warnings)} lower-risk findings, {len(errors)} blocking findings")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
