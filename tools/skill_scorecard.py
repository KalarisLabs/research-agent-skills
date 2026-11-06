"""Automated Skill Scorecard: evaluate skills on quality, lines, routing, and security.

Calculates the static rubric score (tools/skill_quality.py), line count,
trigger routing benchmark (BM25 against evals/<skill>/evals.json), and security & spec
checks (tools/lint_injection.py, tools/validate.py). Formats a visual, gamified
Markdown scorecard designed for automated pull-request review comments.

Usage:
    uv run tools/skill_scorecard.py skills/my-skill              # evaluate one skill
    uv run tools/skill_scorecard.py --changed                    # evaluate PR-changed skills
    uv run tools/skill_scorecard.py --changed --output report.md # write markdown report
    uv run tools/skill_scorecard.py --changed --fail-under 80.0  # fail CI if < 80 standard
    uv run tools/skill_scorecard.py --post-comment-file report.md --pr-number 42
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

for _stream in (sys.stdout, sys.stderr):  # Windows consoles default to cp1252
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).resolve().parent))

import lint_injection  # noqa: E402
import skill_quality  # noqa: E402
import trigger_bench  # noqa: E402
import validate  # noqa: E402
from common import ROOT, SKILLS_DIR, Skill, load_skill, load_skills  # noqa: E402

SCORECARD_COMMENT_MARKER = "<!-- skill-scorecard-bot -->"
DEFAULT_QUALITY_BAR = 80.0
MAX_LINE_COUNT = 500
DEFAULT_BASE_REF = "origin/main"


def progress_bar(score: float, max_score: float = 100.0, width: int = 20) -> str:
    """Generate an ASCII progress bar."""
    ratio = max(0.0, min(1.0, score / max_score if max_score > 0 else 0.0))
    filled = int(round(ratio * width))
    return "█" * filled + "░" * (width - filled)


def mini_bar(score: float, max_score: float, width: int = 10) -> str:
    """Generate a compact 10-char progress bar for tables."""
    ratio = max(0.0, min(1.0, score / max_score if max_score > 0 else 0.0))
    filled = int(round(ratio * width))
    return "█" * filled + "░" * (width - filled)


def score_tier(score: float) -> tuple[str, str]:
    """Return tier badge and description based on rubric score."""
    if score >= 95.0:
        return "🏆 **S-Tier**", "Exceptional (Production-grade research skill)"
    if score >= 85.0:
        return "🥇 **A-Tier**", "High Quality (Exceeds repository standard)"
    if score >= 80.0:
        return "🥈 **B-Tier**", "Passing (Meets repository >80 standard)"
    return "⚠️ **Needs Work**", "Below Standard (Must reach ≥ 80.0 to merge)"


def evaluate_trigger_routing(
    skill_name: str,
    skills_dict: dict[str, Skill],
    index: trigger_bench.BM25,
) -> dict[str, Any]:
    """Run BM25 trigger routing benchmark on the skill's evals suite."""
    eval_file = ROOT / "evals" / skill_name / "evals.json"
    if not eval_file.is_file():
        return {
            "has_evals": False,
            "error": f"Missing eval suite at evals/{skill_name}/evals.json",
            "hit1": 0.0,
            "hit3": 0.0,
            "false_trigger": 0.0,
            "total_prompts": 0,
            "pos_count": 0,
            "neg_count": 0,
            "cases": [],
            "pass": False,
        }

    try:
        data = json.loads(eval_file.read_text(encoding="utf-8"))
    except Exception as err:
        return {
            "has_evals": False,
            "error": f"Unparseable eval suite: {err}",
            "hit1": 0.0,
            "hit3": 0.0,
            "false_trigger": 0.0,
            "total_prompts": 0,
            "pos_count": 0,
            "neg_count": 0,
            "cases": [],
            "pass": False,
        }

    evals = data.get("evals", [])
    if not evals:
        return {
            "has_evals": True,
            "error": "Eval suite contains no prompts",
            "hit1": 0.0,
            "hit3": 0.0,
            "false_trigger": 0.0,
            "total_prompts": 0,
            "pos_count": 0,
            "neg_count": 0,
            "cases": [],
            "pass": False,
        }

    cases = []
    for ev in evals:
        prompt = ev.get("prompt", "")
        should = ev.get("should_trigger", True)
        toks = trigger_bench.tokens(prompt)
        ranked = [n for n, sc in index.rank(toks)[:5] if sc > 0]
        rank = ranked.index(skill_name) + 1 if skill_name in ranked else None
        cases.append({
            "prompt": prompt,
            "should_trigger": should,
            "rank": rank,
            "top": ranked[:3],
        })

    pos = [c for c in cases if c["should_trigger"]]
    neg = [c for c in cases if not c["should_trigger"]]
    hit1 = sum(c["rank"] == 1 for c in pos) / max(len(pos), 1)
    hit3 = sum(c["rank"] is not None and c["rank"] <= 3 for c in pos) / max(len(pos), 1)
    false = sum(c["rank"] == 1 for c in neg) / max(len(neg), 1) if neg else 0.0

    passed = (hit3 >= 0.8 if pos else True) and (false <= 0.20)
    return {
        "has_evals": True,
        "hit1": round(hit1, 2),
        "hit3": round(hit3, 2),
        "false_trigger": round(false, 2),
        "total_prompts": len(cases),
        "pos_count": len(pos),
        "neg_count": len(neg),
        "cases": cases,
        "pass": passed,
    }


def evaluate_security(skill_dir: Path) -> dict[str, Any]:
    """Run prompt-injection lint and unreviewed network domain checks."""
    files = lint_injection.iter_files([skill_dir])
    raw_findings: list[lint_injection.Finding] = []
    hosts_by_file: dict[str, set[str]] = {}
    for f in files:
        found, hosts = lint_injection.scan_file(f)
        raw_findings.extend(found)
        if hosts:
            hosts_by_file[lint_injection.rel(f)] = hosts

    baseline = set()
    if lint_injection.BASELINE.exists():
        try:
            base_data = json.loads(lint_injection.BASELINE.read_text(encoding="utf-8"))
            baseline = set(base_data.get("accepted", [])) | {
                f["fingerprint"] for f in base_data.get("findings", []) if isinstance(f, dict) and "fingerprint" in f
            }
        except (json.JSONDecodeError, OSError) as err:
            print(f"Warning: could not read security baseline: {err}", file=sys.stderr)

    allowed_domains = lint_injection.load_allowed()
    unseen_domains = sorted({
        h for hs in hosts_by_file.values()
        for h in hs
        if not lint_injection.host_allowed(h, allowed_domains)
    })

    blocking = []
    for f in raw_findings:
        if f.fingerprint not in baseline and f.severity in ("HIGH", "MEDIUM"):
            blocking.append({
                "rule": f.rule,
                "severity": f.severity,
                "path": f.path,
                "line": f.line,
                "message": f.message,
                "snippet": f.snippet,
            })

    for d in unseen_domains:
        blocking.append({
            "rule": "RAS012",
            "severity": "HIGH",
            "path": skill_dir.name,
            "line": 1,
            "message": f"Script contacts unreviewed domain '{d}'",
            "snippet": f"Add domain to security/allowed-domains.txt if legitimate: {d}",
        })

    return {
        "files_scanned": len(files),
        "total_findings": len(raw_findings),
        "blocking_findings": blocking,
        "unseen_domains": unseen_domains,
        "pass": len(blocking) == 0,
    }


def evaluate_spec_policy(skill_dir: Path) -> dict[str, Any]:
    """Validate skill against agentskills spec, size limits, and repository policy."""
    rep = validate.Report()
    categories = validate.load_categories()
    baseline = validate.load_size_baseline()
    validate.validate_skill(skill_dir, rep, categories, baseline)
    return {
        "errors": rep.errors,
        "warnings": rep.warnings,
        "pass": len(rep.errors) == 0,
    }


# (part name, threshold below which the tip applies, tip text) in report order.
_DESCRIPTION_STRUCTURE_TIPS: tuple[tuple[str, float, str], ...] = (
    ("desc_triggers", 8,
     "🎯 **+8 pts**: Add explicit `Use when ...` trigger phrases in frontmatter `description`."),
    ("desc_length", 10,
     "📝 **+3-7 pts**: Expand description to 200–1024 characters with trigger contexts and targets."),
    ("desc_specific", 6,
     "🔧 **+1.5-6 pts**: Name specific tools, file formats (e.g. `.csv`, `.pdb`), APIs, or venues."),
    ("desc_no_marketing", 6,
     "✨ **+3-6 pts**: Remove marketing adjectives (*comprehensive*, *powerful*, *robust*, etc.)."),
    ("workflow", 8,
     "📋 **+4-8 pts**: Add a numbered step-by-step workflow (`1.`, `2.`, `3.`) with 3+ steps."),
    ("tables_checklists", 6,
     "📊 **+6 pts**: Include a markdown decision table (`| ... |`) or checklist (`- [ ]`)."),
    ("verification", 6,
     "🛡️ **+6 pts**: Include verification guidance (*verify against official source*, *never guess*)."),
    ("handoffs", 4,
     "🤝 **+4 pts**: Add a `## Related skills` or `## Next steps` section describing handoffs."),
    ("headings", 6,
     "📑 **+3-6 pts**: Organize instructions with at least 4 markdown headings (`##` or `###`)."),
)
_SCRIPT_FRESHNESS_TIPS: tuple[tuple[str, float, str], ...] = (
    ("scripts", 15,
     "💻 **+1-15 pts**: Ensure scripts in `scripts/` have docstrings, use `argparse`, and are tested."),
    ("compatibility", 5,
     "⚙️ **+3 pts**: Add a `compatibility:` field to YAML frontmatter stating supported platforms."),
    ("freshness", 5,
     "🔄 **+5 pts**: For time-sensitive content, add instructions to verify against official docs."),
)


def _part_tips(parts: dict[str, float], rules: tuple[tuple[str, float, str], ...]) -> list[str]:
    """Return the tips whose rubric part scored below its threshold."""
    return [tip for key, threshold, tip in rules if parts.get(key, 0) < threshold]


def compute_levelup_tips(
    parts: dict[str, float],
    lines: int,
    routing: dict[str, Any],
    security: dict[str, Any],
    spec: dict[str, Any],
    notes: list[str],
) -> list[str]:
    """Generate gamified actionable tips to boost the skill score to 80+ / 95+."""
    tips: list[str] = _part_tips(parts, _DESCRIPTION_STRUCTURE_TIPS)

    # Progressive disclosure (max 15)
    if lines > MAX_LINE_COUNT:
        tips.append(
            f"✂️ **+5-8 pts**: `SKILL.md` has {lines} lines (limit: {MAX_LINE_COUNT}). "
            "Move technical detail to `references/`."
        )
    elif parts.get("references", 0) < 4:
        tips.append("📂 **+4 pts**: Keep `SKILL.md` concise (≤ 250 lines) or add a `references/` directory.")

    # Scripts (max 15) and Freshness & Compatibility (max 10)
    tips.extend(_part_tips(parts, _SCRIPT_FRESHNESS_TIPS))

    # Trigger routing evals
    if not routing.get("has_evals"):
        tips.append("🧪 **Essential**: Create `evals/<name>/evals.json` with 3 test prompts and 1 near-miss prompt.")
    elif not routing.get("pass"):
        tips.append("🎯 **Routing Tuning**: Skill missed some prompts or triggered on near misses; align keywords.")

    # Security & Policy
    if not security.get("pass"):
        tips.append("🚨 **Security Blocking**: Resolve security findings or register domains in allowed-domains.txt.")
    if not spec.get("pass"):
        tips.append("⚠️ **Spec Compliance**: Fix frontmatter/spec errors reported in the validation check.")

    return tips


@dataclass
class SkillScorecard:
    """Skill scorecard."""
    name: str
    category: str
    score: float
    lines: int
    tier_badge: str
    tier_desc: str
    passed: bool
    parts: dict[str, float]
    penalty: float
    slop_index: float | None
    notes: list[str]
    routing: dict[str, Any]
    security: dict[str, Any]
    spec: dict[str, Any]
    levelup_tips: list[str] = field(default_factory=list)


def evaluate_skill(
    s: Skill,
    tests_blob: str,
    skills_dict: dict[str, Skill],
    index: trigger_bench.BM25,
    min_score: float = DEFAULT_QUALITY_BAR,
) -> SkillScorecard:
    """Run full evaluation suite on a single skill."""
    quality = skill_quality.score_skill(s, tests_blob)
    score = quality["score"]
    lines = quality["lines"]
    tier_badge, tier_desc = score_tier(score)

    routing = evaluate_trigger_routing(s.name, skills_dict, index)
    security = evaluate_security(s.path)
    spec = evaluate_spec_policy(s.path)

    passed = (score >= min_score) and (lines <= MAX_LINE_COUNT) and security["pass"] and spec["pass"]
    tips = compute_levelup_tips(quality["parts"], lines, routing, security, spec, quality["notes"])

    return SkillScorecard(
        name=s.name,
        category=s.category,
        score=score,
        lines=lines,
        tier_badge=tier_badge,
        tier_desc=tier_desc,
        passed=passed,
        parts=quality["parts"],
        penalty=quality["penalty"],
        slop_index=quality["slop_index"],
        notes=quality["notes"],
        routing=routing,
        security=security,
        spec=spec,
        levelup_tips=tips,
    )


def _empty_scorecard_lines(lines: list[str]) -> list[str]:
    """Append the 'nothing changed' note to the report header lines."""
    lines.extend([
        "> [!NOTE]",
        "> No skills under `skills/` were modified in this pull request.",
        "> Quality checks on skill definitions were skipped.",
        "",
        "---",
        "*Generated by `tools/skill_scorecard.py` · [Research Agent Skills]"
        "(https://github.com/KalarisLabs/research-agent-skills)*",
    ])
    return lines


def _overview_lines(scorecards: list[SkillScorecard]) -> list[str]:
    """Render the summary table with one row per skill."""
    lines = [
        "### 📊 Scorecard Overview",
        "",
        "| Skill | Quality Score | Tier | Lines | Trigger Routing | Security | Policy | Status |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
    ]
    for sc in scorecards:
        status_badge = "🟢 **PASS**" if sc.passed else "🔴 **NEEDS WORK**"
        line_badge = f"{sc.lines} / {MAX_LINE_COUNT} lines" + (" ✅" if sc.lines <= MAX_LINE_COUNT else " ❌")

        if sc.routing.get("has_evals"):
            route_badge = f"Hit@3: {int(sc.routing['hit3'] * 100)}%" + (" ✅" if sc.routing["pass"] else " ⚠️")
        else:
            route_badge = "⚠️ No Evals"

        sec_badge = "0 findings ✅" if sc.security["pass"] else f"{len(sc.security['blocking_findings'])} issues ❌"
        spec_badge = "Valid ✅" if sc.spec["pass"] else f"{len(sc.spec['errors'])} errors ❌"

        lines.append(
            f"| [`{sc.name}`](skills/{sc.name}) | **{sc.score:.1f}** / 100 | {sc.tier_badge} | {line_badge} | "
            f"{route_badge} | {sec_badge} | {spec_badge} | {status_badge} |"
        )
    lines.append("")
    return lines


def _rubric_lines(sc: SkillScorecard) -> list[str]:
    """Render the rubric breakdown rows (earned, max, bar, feedback) for one skill."""
    parts = sc.parts
    desc_score = sum(parts.get(k, 0) for k in ("desc_length", "desc_triggers", "desc_specific", "desc_no_marketing"))
    struct_keys = ("workflow", "tables_checklists", "handoffs", "verification", "headings")
    struct_score = sum(parts.get(k, 0) for k in struct_keys)
    disc_score = sum(parts.get(k, 0) for k in ("size", "references", "links"))
    script_score = parts.get("scripts", 15.0)
    fresh_score = sum(parts.get(k, 0) for k in ("freshness", "compatibility"))

    # (label, earned, max, pass threshold, feedback when passing, feedback otherwise)
    rows = [
        ("Description", desc_score, 30.0, 24,
         "✅ Triggers & entities present", "⚠️ Needs triggers or concrete entities"),
        ("Structure & Flow", struct_score, 30.0, 24,
         "✅ Numbered steps & verify rules", "⚠️ Add workflow steps or checklist"),
        ("Progressive Disclosure", disc_score, 15.0, 12,
         "✅ Clean size & references", "⚠️ Exceeds lines or broken links"),
        ("Scripts & Tooling", script_score, 15.0, 12,
         "✅ Exercised CLI scripts", "⚠️ Check argparse / docstrings"),
        ("Freshness & Compat", fresh_score, 10.0, 8,
         "✅ Compatibility declared", "⚠️ Add compatibility metadata"),
    ]
    lines = [
        f"| **{label}** | {score:.1f} | {mx:.1f} | `{mini_bar(score, mx)}` | {good if score >= threshold else bad} |"
        for label, score, mx, threshold, good, bad in rows
    ]
    if sc.penalty > 0:
        lines.append(
            f"| **Prose Slop Penalty** | -{sc.penalty:.1f} | -5.0 | `----------` | "
            f"⚠️ High slop index ({sc.slop_index}); run slop_check.py |"
        )
    else:
        lines.append("| **Prose Slop Penalty** | 0.0 | 0.0 | `[Clean]` | 🛡️ Clean prose (no AI fluff) |")
    return lines


def _routing_lines(sc: SkillScorecard) -> list[str]:
    """Render the trigger-routing section, including the per-prompt case table."""
    if not sc.routing.get("has_evals"):
        return [
            f"- ⚠️ **Missing eval suite**: `evals/{sc.name}/evals.json` was not found.",
            "- *Requirement*: Every new skill needs `evals/<name>/evals.json` with realistic prompts.",
            "",
        ]
    r = sc.routing
    pos_hit1 = int(r["hit1"] * r["pos_count"])
    pos_hit3 = int(r["hit3"] * r["pos_count"])
    hit1_pct = int(r["hit1"] * 100)
    hit3_pct = int(r["hit3"] * 100)
    lines = [
        f"- **Eval Suite**: `evals/{sc.name}/evals.json` ({r['total_prompts']} test prompts)",
        f"- **Sensitivity (Positive Prompts)**: Hit@1 = **{hit1_pct}%** ({pos_hit1}/{r['pos_count']}) · "
        f"Hit@3 = **{hit3_pct}%** ({pos_hit3}/{r['pos_count']}) "
        + ("✅" if r["hit3"] >= 0.8 else "⚠️ Low routing recall"),
        f"- **Specificity (Near Misses)**: False-trigger rate = **{int(r['false_trigger'] * 100)}%** "
        + ("✅" if r["false_trigger"] <= 0.2 else "⚠️ Falsely triggers on negative cases"),
        "",
        "<details>",
        f"<summary><b>View {len(r['cases'])} Routing Test Cases</b></summary>",
        "",
        "| Expected | Prompt | Rank | Top 3 Matches |",
        "| :---: | :--- | :---: | :--- |",
    ]
    for c in r["cases"]:
        exp = "✅ Trigger" if c["should_trigger"] else "🛑 Near Miss"
        rank_str = f"#{c['rank']}" if c["rank"] is not None else "None"
        top_str = ", ".join(f"`{m}`" for m in c["top"]) or "None"
        lines.append(f"| {exp} | {c['prompt'][:80]} | {rank_str} | {top_str} |")
    lines.extend(["</details>", ""])
    return lines


def _security_lines(sc: SkillScorecard) -> list[str]:
    """Render the security and policy verification section with any blocking findings and spec errors."""
    sec_findings_cnt = len(sc.security["blocking_findings"])
    spec_errs_cnt = len(sc.spec["errors"])
    lines = [
        "##### 🛡️ Security & Policy Verification",
        "- **Prompt Injection & Code Safety (`lint_injection.py`)**: "
        + ("0 findings detected ✅" if sc.security["pass"] else f"**{sec_findings_cnt} security findings** ❌"),
        "- **Spec & Integrity Checks (`validate.py`)**: "
        + ("0 errors ✅" if sc.spec["pass"] else f"**{spec_errs_cnt} errors** ❌"),
    ]
    if sc.security["blocking_findings"]:
        lines.extend(["", "**Security Findings:**"])
        for bf in sc.security["blocking_findings"]:
            lines.append(f"- 🔴 `[{bf['rule']}]` {bf['message']} (`{bf['path']}:{bf['line']}`)")
    if sc.spec["errors"]:
        lines.extend(["", "**Policy Validation Errors:**"])
        for err in sc.spec["errors"]:
            lines.append(f"- ❌ {err}")
    return lines


def _levelup_lines(sc: SkillScorecard) -> list[str]:
    """Render the 'How to Level Up' section from the skill's tips."""
    lines = [
        "",
        "##### 🚀 How to Level Up This Skill",
    ]
    if sc.levelup_tips:
        lines.extend(f"- {tip}" for tip in sc.levelup_tips[:6])
    else:
        lines.append("- 🌟 **Flawless submission!** This skill meets all top-tier rubric criteria.")
    lines.append("")
    return lines


def _skill_detail_lines(sc: SkillScorecard) -> list[str]:
    """Render the full detail block for one skill."""
    bar = progress_bar(sc.score)
    lines = [
        "---",
        f"### 🔍 Skill Detail: `{sc.name}`",
        "",
        f"#### 🎯 Overall Score: **{sc.score:.1f} / 100** ({sc.tier_badge})",
        f"> `{bar}` **{sc.score:.1f}%**",
        f"> *Tier summary: {sc.tier_desc}*",
        "",
        "##### 📑 Rubric Breakdown",
        "",
        "| Rubric Category | Earned | Max | Progress | Status / Feedback |",
        "| :--- | :---: | :---: | :---: | :--- |",
    ]
    lines.extend(_rubric_lines(sc))
    lines.extend([
        "",
        "##### 📏 Line Count & Size",
        f"- **`SKILL.md` length**: **{sc.lines} lines** (Repository limit: ≤ {MAX_LINE_COUNT} lines) "
        + ("✅" if sc.lines <= MAX_LINE_COUNT else f"❌ **Exceeds limit by {sc.lines - MAX_LINE_COUNT} lines**"),
        "- **Structure**: Keep `SKILL.md` focused as an index/workflow; place detail under `references/`.",
        "",
        "##### 🧭 Trigger Routing Benchmark",
    ])
    lines.extend(_routing_lines(sc))
    lines.extend(_security_lines(sc))
    lines.extend(_levelup_lines(sc))
    return lines


def format_markdown_scorecard(scorecards: list[SkillScorecard], min_score: float = DEFAULT_QUALITY_BAR) -> str:
    """Render a clean, visual Markdown scorecard comment."""
    target_msg = (
        f"Repository Quality Target: **Score ≥ {min_score:.1f}** · "
        f"**Line count ≤ {MAX_LINE_COUNT}** · **Clean Security**"
    )
    lines: list[str] = [
        SCORECARD_COMMENT_MARKER,
        "## 🏆 Skill Scorecard Report",
        "",
        "Automated quality scorecard for **Research Agent Skills** pull requests.",
        target_msg,
        "",
    ]

    if not scorecards:
        return "\n".join(_empty_scorecard_lines(lines))

    lines.extend(_overview_lines(scorecards))
    for sc in scorecards:
        lines.extend(_skill_detail_lines(sc))

    lines.extend([
        "---",
        "*🤖 Scorecard bot automatically evaluated this PR using `tools/skill_scorecard.py`.*",
    ])

    return "\n".join(lines)


def _git_diff_files(ref: str) -> list[str] | None:
    """Return files changed between `ref` and HEAD, or None when the git diff fails."""
    try:
        res = subprocess.run(
            ["git", "diff", "--name-only", f"{ref}...HEAD"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.SubprocessError:
        return None
    return res.stdout.splitlines()


def _skills_in_paths(files: list[str]) -> set[str]:
    """Extract skill names from changed paths under skills/ or evals/."""
    skills = set()
    for f in files:
        p = Path(f).as_posix()
        if not p.startswith(("skills/", "evals/")):
            continue
        parts = p.split("/")
        if len(parts) >= 2 and parts[1]:
            skills.add(parts[1])
    return skills


def find_changed_skills(base_ref: str = DEFAULT_BASE_REF) -> list[str]:
    """Identify skills modified in git diff between base_ref and HEAD."""
    skills: set[str] = set()
    candidate_refs = [base_ref]
    if not base_ref.startswith("origin/") and "/" not in base_ref:
        candidate_refs.append(f"origin/{base_ref}")
    candidate_refs.extend(["HEAD~1", "main", DEFAULT_BASE_REF])

    for ref in candidate_refs:
        files = _git_diff_files(ref)
        if files is None:
            continue
        skills |= _skills_in_paths(files)
        if skills or files:
            return sorted(skills)

    return sorted(skills)


def detect_pr_number() -> int | None:
    """Extract PR number from GitHub Actions environment if present."""
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if event_path and Path(event_path).is_file():
        try:
            data = json.loads(Path(event_path).read_text(encoding="utf-8"))
            if "pull_request" in data and "number" in data["pull_request"]:
                return int(data["pull_request"]["number"])
            if "issue" in data and "number" in data["issue"]:
                return int(data["issue"]["number"])
        except (json.JSONDecodeError, OSError, KeyError):
            pass

    ref = os.environ.get("GITHUB_REF", "")
    m = re.match(r"^refs/pull/(\d+)/(?:merge|head)$", ref)
    if m:
        return int(m.group(1))

    return None


def _find_existing_comment(api_url: str, headers: dict[str, str], repo: str, pr: int) -> tuple[bool, Any]:
    """Look for a prior scorecard comment; return (ok, comment id or None), ok=False on request failure."""
    req = urllib.request.Request(f"{api_url}?per_page=100", headers=headers, method="GET")  # noqa: S310
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:  # noqa: S310
            comments = json.loads(resp.read().decode("utf-8"))
            for c in comments:
                if SCORECARD_COMMENT_MARKER in c.get("body", ""):
                    return True, c.get("id")
    except urllib.error.HTTPError as err:
        if err.code == 403:
            print(
                f"Notice: GitHub token lacks write access to {repo} PR #{pr} (fork PR). "
                "Scorecard comment will be handled by workflow_run.",
                file=sys.stderr,
            )
            return False, None
        print(f"Failed to fetch PR comments for {repo} PR #{pr}: {err}", file=sys.stderr)
        return False, None
    except OSError as err:
        print(f"Network error querying PR comments: {err}", file=sys.stderr)
        return False, None
    return True, None


def _update_comment(repo: str, pr: int, comment_id: Any, body: str, headers: dict[str, str]) -> bool:
    """PATCH an existing scorecard comment; raises on HTTP/network errors for the caller to report."""
    patch_url = f"https://api.github.com/repos/{repo}/issues/comments/{comment_id}"
    payload = json.dumps({"body": body}).encode("utf-8")
    patch_headers = {**headers, "Content-Type": "application/json"}
    patch_req = urllib.request.Request(patch_url, data=payload, headers=patch_headers, method="PATCH")
    with urllib.request.urlopen(patch_req, timeout=30) as resp:  # noqa: S310
        if resp.status in (200, 201):
            print(f"Successfully updated scorecard comment on {repo} PR #{pr} (comment ID {comment_id})")
            return True
    return False


def _create_comment(api_url: str, repo: str, pr: int, body: str, headers: dict[str, str]) -> bool:
    """POST a new scorecard comment; raises on HTTP/network errors for the caller to report."""
    payload = json.dumps({"body": body}).encode("utf-8")
    post_headers = {**headers, "Content-Type": "application/json"}
    post_req = urllib.request.Request(api_url, data=payload, headers=post_headers, method="POST")
    with urllib.request.urlopen(post_req, timeout=30) as resp:  # noqa: S310
        if resp.status in (200, 201):
            created = json.loads(resp.read().decode("utf-8"))
            print(f"Successfully posted scorecard comment on {repo} PR #{pr} (comment ID {created.get('id')})")
            return True
    return False


def post_or_update_comment(
    body: str,
    pr_number: int | None = None,
    repo_slug: str | None = None,
    token: str | None = None,
) -> bool:
    """Post or update the scorecard comment on a GitHub PR."""
    repo = repo_slug or os.environ.get("GITHUB_REPOSITORY")
    pr = pr_number or detect_pr_number()
    auth_token = token or os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")

    if not repo or not pr or not auth_token:
        print(
            "Scorecard comment skipped: GITHUB_REPOSITORY, PR number, or GITHUB_TOKEN not available.",
            file=sys.stderr,
        )
        return False

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "research-agent-skills-scorecard-bot",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    api_url = f"https://api.github.com/repos/{repo}/issues/{pr}/comments"
    ok, existing_id = _find_existing_comment(api_url, headers, repo, pr)
    if not ok:
        return False

    try:
        if existing_id:
            return _update_comment(repo, pr, existing_id, body, headers)
        return _create_comment(api_url, repo, pr, body, headers)
    except urllib.error.HTTPError as err:
        if err.code == 403:
            print(f"Notice: GITHUB_TOKEN has read-only permission for {repo} PR #{pr}.", file=sys.stderr)
            return False
        print(f"Failed to post/update scorecard comment on PR #{pr}: {err}", file=sys.stderr)
        return False
    except OSError as err:
        print(f"Error posting scorecard comment to PR #{pr}: {err}", file=sys.stderr)
        return False


def _build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for the scorecard tool."""
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("skills", nargs="*", help="skill names or paths to evaluate")
    ap.add_argument("--changed", action="store_true", help="evaluate skills modified relative to base branch")
    ap.add_argument("--base", default=DEFAULT_BASE_REF, help="base git ref for diff (default: origin/main)")
    ap.add_argument("--all", action="store_true", help="evaluate all skills in repository")
    ap.add_argument(
        "--min-score",
        type=float,
        default=DEFAULT_QUALITY_BAR,
        help=f"minimum quality score threshold (default: {DEFAULT_QUALITY_BAR})",
    )
    ap.add_argument(
        "--fail-under",
        type=float,
        help="exit 1 if any evaluated skill scores under this threshold or fails policy",
    )
    ap.add_argument("--output", type=Path, help="write markdown report to file")
    ap.add_argument("--json", type=Path, help="write structured JSON report to file")
    ap.add_argument("--pr-number", type=int, help="pull request number for comment posting")
    ap.add_argument("--post-comment", action="store_true", help="post or update scorecard comment to GitHub PR")
    ap.add_argument("--post-comment-file", type=Path, help="post an existing markdown report file to GitHub PR")
    return ap


def _post_comment_file(args: argparse.Namespace) -> int:
    """Post an existing markdown report file as the PR comment and return the exit code."""
    if not args.post_comment_file.is_file():
        print(f"Error: comment file not found: {args.post_comment_file}", file=sys.stderr)
        return 2
    body = args.post_comment_file.read_text(encoding="utf-8")
    ok = post_or_update_comment(body, pr_number=args.pr_number)
    return 0 if ok else 1


def _resolve_named_skills(names: list[str], skills_dict: dict[str, Skill]) -> list[str]:
    """Resolve skill names or paths given on the command line, loading skills missing from the index."""
    target_names: list[str] = []
    for s in names:
        clean = s.replace("\\", "/").rstrip("/").split("/")[-1]
        if clean in skills_dict:
            target_names.append(clean)
        elif (SKILLS_DIR / clean).is_dir():
            try:
                loaded = load_skill(SKILLS_DIR / clean)
                skills_dict[loaded.name] = loaded
                target_names.append(loaded.name)
            except Exception as err:
                print(f"Warning: could not load skill {clean}: {err}", file=sys.stderr)
        else:
            print(f"Warning: skill '{clean}' not found in skills directory", file=sys.stderr)
    return target_names


def _changed_target_names(base: str, skills_dict: dict[str, Skill]) -> list[str]:
    """Return the changed skills (relative to `base`) that exist on disk or in the index."""
    changed = find_changed_skills(base)
    return [name for name in changed if name in skills_dict or (SKILLS_DIR / name).is_dir()]


def _resolve_targets(args: argparse.Namespace, skills_dict: dict[str, Skill]) -> list[str]:
    """Decide which skills to evaluate from the positional names, --changed, --all or the git diff."""
    if args.skills:
        return _resolve_named_skills(args.skills, skills_dict)
    if args.changed:
        return _changed_target_names(args.base, skills_dict)
    if args.all:
        return sorted(skills_dict.keys())
    return _changed_target_names(args.base, skills_dict)


def _write_reports(args: argparse.Namespace, scorecards: list[SkillScorecard], md_report: str) -> None:
    """Print the summary table and write the optional markdown and JSON reports."""
    if not scorecards:
        print("No skills targeted for scorecard evaluation.")
    for sc in scorecards:
        status_str = "PASS" if sc.passed else "NEEDS WORK"
        print(f"{sc.score:5.1f}  {sc.name:<40} {sc.tier_badge} [{status_str}] ({sc.lines} lines)")

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(md_report + "\n", encoding="utf-8")
        print(f"Scorecard markdown written to: {args.output}")

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        json_data = {
            "min_score": args.min_score,
            "skills": [asdict(sc) for sc in scorecards],
            "all_passed": all(sc.passed for sc in scorecards) if scorecards else True,
        }
        args.json.write_text(json.dumps(json_data, indent=2) + "\n", encoding="utf-8")
        print(f"Scorecard JSON written to: {args.json}")


def _failure_reasons(sc: SkillScorecard, fail_threshold: float) -> list[str]:
    """List why a scorecard fails the gate."""
    reasons = []
    if sc.score < fail_threshold:
        reasons.append(f"score {sc.score:.1f} < {fail_threshold:.1f}")
    if sc.lines > MAX_LINE_COUNT:
        reasons.append(f"lines {sc.lines} > {MAX_LINE_COUNT}")
    if not sc.security["pass"]:
        reasons.append(f"{len(sc.security['blocking_findings'])} security findings")
    if not sc.spec["pass"]:
        reasons.append(f"{len(sc.spec['errors'])} spec errors")
    return reasons


def _gate_exit_code(args: argparse.Namespace, scorecards: list[SkillScorecard]) -> int:
    """Apply the --fail-under / --changed quality gate and return the exit code."""
    if args.fail_under is not None:
        fail_threshold = args.fail_under
    elif args.changed:
        fail_threshold = args.min_score
    else:
        fail_threshold = None
    if fail_threshold is None or not scorecards:
        return 0
    failing = [sc for sc in scorecards if sc.score < fail_threshold or not sc.passed]
    if not failing:
        return 0
    print(f"\nScorecard gate FAILED: {len(failing)} skill(s) did not meet standards:")
    for sc in failing:
        print(f"  - {sc.name}: {', '.join(_failure_reasons(sc, fail_threshold))}")
    return 1


def main(argv: list[str] | None = None) -> int:
    """Run the command-line interface."""
    args = _build_parser().parse_args(argv)

    if args.post_comment_file:
        return _post_comment_file(args)

    all_skills = load_skills()
    skills_dict = {s.name: s for s in all_skills}
    target_names = _resolve_targets(args, skills_dict)

    bm25_index = trigger_bench.BM25({
        n: trigger_bench.tokens(n.replace("-", " ")) * 2 + trigger_bench.tokens(str(s.meta.get("description", "")))
        for n, s in skills_dict.items()
    })

    tests_blob = skill_quality.tests_text()
    scorecards: list[SkillScorecard] = []

    for name in target_names:
        skill_obj = skills_dict.get(name) or load_skill(SKILLS_DIR / name)
        sc = evaluate_skill(skill_obj, tests_blob, skills_dict, bm25_index, min_score=args.min_score)
        scorecards.append(sc)

    md_report = format_markdown_scorecard(scorecards, min_score=args.min_score)
    _write_reports(args, scorecards, md_report)

    if args.post_comment:
        post_or_update_comment(md_report, pr_number=args.pr_number)

    return _gate_exit_code(args, scorecards)


if __name__ == "__main__":
    sys.exit(main())
