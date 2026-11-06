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


def compute_levelup_tips(
    parts: dict[str, float],
    lines: int,
    routing: dict[str, Any],
    security: dict[str, Any],
    spec: dict[str, Any],
    notes: list[str],
) -> list[str]:
    """Generate gamified actionable tips to boost the skill score to 80+ / 95+."""
    tips: list[str] = []

    # Description (max 30)
    if parts.get("desc_triggers", 0) < 8:
        tips.append("🎯 **+8 pts**: Add explicit `Use when ...` trigger phrases in frontmatter `description`.")
    if parts.get("desc_length", 0) < 10:
        tips.append("📝 **+3-7 pts**: Expand description to 200–1024 characters with trigger contexts and targets.")
    if parts.get("desc_specific", 0) < 6:
        tips.append("🔧 **+1.5-6 pts**: Name specific tools, file formats (e.g. `.csv`, `.pdb`), APIs, or venues.")
    if parts.get("desc_no_marketing", 0) < 6:
        tips.append("✨ **+3-6 pts**: Remove marketing adjectives (*comprehensive*, *powerful*, *robust*, etc.).")

    # Structure (max 30)
    if parts.get("workflow", 0) < 8:
        tips.append("📋 **+4-8 pts**: Add a numbered step-by-step workflow (`1.`, `2.`, `3.`) with 3+ steps.")
    if parts.get("tables_checklists", 0) < 6:
        tips.append("📊 **+6 pts**: Include a markdown decision table (`| ... |`) or checklist (`- [ ]`).")
    if parts.get("verification", 0) < 6:
        tips.append("🛡️ **+6 pts**: Include verification guidance (*verify against official source*, *never guess*).")
    if parts.get("handoffs", 0) < 4:
        tips.append("🤝 **+4 pts**: Add a `## Related skills` or `## Next steps` section describing handoffs.")
    if parts.get("headings", 0) < 6:
        tips.append("📑 **+3-6 pts**: Organize instructions with at least 4 markdown headings (`##` or `###`).")

    # Progressive disclosure (max 15)
    if lines > MAX_LINE_COUNT:
        tips.append(
            f"✂️ **+5-8 pts**: `SKILL.md` has {lines} lines (limit: {MAX_LINE_COUNT}). "
            "Move technical detail to `references/`."
        )
    elif parts.get("references", 0) < 4:
        tips.append("📂 **+4 pts**: Keep `SKILL.md` concise (≤ 250 lines) or add a `references/` directory.")

    # Scripts (max 15)
    if parts.get("scripts", 0) < 15:
        tips.append("💻 **+1-15 pts**: Ensure scripts in `scripts/` have docstrings, use `argparse`, and are tested.")

    # Freshness & Compatibility (max 10)
    if parts.get("compatibility", 0) < 5:
        tips.append("⚙️ **+3 pts**: Add a `compatibility:` field to YAML frontmatter stating supported platforms.")
    if parts.get("freshness", 0) < 5:
        tips.append("🔄 **+5 pts**: For time-sensitive content, add instructions to verify against official docs.")

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
        lines.extend([
            "> [!NOTE]",
            "> No skills under `skills/` were modified in this pull request.",
            "> Quality checks on skill definitions were skipped.",
            "",
            "---",
            "*Generated by `tools/skill_scorecard.py` · [Research Agent Skills]"
            "(https://github.com/KalarisLabs/research-agent-skills)*",
        ])
        return "\n".join(lines)

    lines.extend([
        "### 📊 Scorecard Overview",
        "",
        "| Skill | Quality Score | Tier | Lines | Trigger Routing | Security | Policy | Status |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
    ])

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

    for sc in scorecards:
        bar = progress_bar(sc.score)
        lines.extend([
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
        ])

        desc_score = sum(
            sc.parts.get(k, 0)
            for k in ("desc_length", "desc_triggers", "desc_specific", "desc_no_marketing")
        )
        struct_score = sum(
            sc.parts.get(k, 0)
            for k in ("workflow", "tables_checklists", "handoffs", "verification", "headings")
        )
        disc_score = sum(sc.parts.get(k, 0) for k in ("size", "references", "links"))
        script_score = sc.parts.get("scripts", 15.0)
        fresh_score = sum(sc.parts.get(k, 0) for k in ("freshness", "compatibility"))

        lines.append(
            f"| **Description** | {desc_score:.1f} | 30.0 | `{mini_bar(desc_score, 30.0)}` | "
            f"{'✅ Triggers & entities present' if desc_score >= 24 else '⚠️ Needs triggers or concrete entities'} |"
        )
        lines.append(
            f"| **Structure & Flow** | {struct_score:.1f} | 30.0 | `{mini_bar(struct_score, 30.0)}` | "
            f"{'✅ Numbered steps & verify rules' if struct_score >= 24 else '⚠️ Add workflow steps or checklist'} |"
        )
        lines.append(
            f"| **Progressive Disclosure** | {disc_score:.1f} | 15.0 | `{mini_bar(disc_score, 15.0)}` | "
            f"{'✅ Clean size & references' if disc_score >= 12 else '⚠️ Exceeds lines or broken links'} |"
        )
        lines.append(
            f"| **Scripts & Tooling** | {script_score:.1f} | 15.0 | `{mini_bar(script_score, 15.0)}` | "
            f"{'✅ Exercised CLI scripts' if script_score >= 12 else '⚠️ Check argparse / docstrings'} |"
        )
        lines.append(
            f"| **Freshness & Compat** | {fresh_score:.1f} | 10.0 | `{mini_bar(fresh_score, 10.0)}` | "
            f"{'✅ Compatibility declared' if fresh_score >= 8 else '⚠️ Add compatibility metadata'} |"
        )

        if sc.penalty > 0:
            lines.append(
                f"| **Prose Slop Penalty** | -{sc.penalty:.1f} | -5.0 | `----------` | "
                f"⚠️ High slop index ({sc.slop_index}); run slop_check.py |"
            )
        else:
            lines.append("| **Prose Slop Penalty** | 0.0 | 0.0 | `[Clean]` | 🛡️ Clean prose (no AI fluff) |")

        lines.extend([
            "",
            "##### 📏 Line Count & Size",
            f"- **`SKILL.md` length**: **{sc.lines} lines** (Repository limit: ≤ {MAX_LINE_COUNT} lines) "
            + ("✅" if sc.lines <= MAX_LINE_COUNT else f"❌ **Exceeds limit by {sc.lines - MAX_LINE_COUNT} lines**"),
            "- **Structure**: Keep `SKILL.md` focused as an index/workflow; place detail under `references/`.",
            "",
            "##### 🧭 Trigger Routing Benchmark",
        ])

        if sc.routing.get("has_evals"):
            r = sc.routing
            pos_hit1 = int(r["hit1"] * r["pos_count"])
            pos_hit3 = int(r["hit3"] * r["pos_count"])
            hit1_pct = int(r["hit1"] * 100)
            hit3_pct = int(r["hit3"] * 100)
            lines.extend([
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
            ])
            for c in r["cases"]:
                exp = "✅ Trigger" if c["should_trigger"] else "🛑 Near Miss"
                rank_str = f"#{c['rank']}" if c["rank"] is not None else "None"
                top_str = ", ".join(f"`{m}`" for m in c["top"]) or "None"
                lines.append(f"| {exp} | {c['prompt'][:80]} | {rank_str} | {top_str} |")
            lines.extend(["</details>", ""])
        else:
            lines.extend([
                f"- ⚠️ **Missing eval suite**: `evals/{sc.name}/evals.json` was not found.",
                "- *Requirement*: Every new skill needs `evals/<name>/evals.json` with realistic prompts.",
                "",
            ])

        sec_findings_cnt = len(sc.security["blocking_findings"])
        spec_errs_cnt = len(sc.spec["errors"])
        lines.extend([
            "##### 🛡️ Security & Policy Verification",
            "- **Prompt Injection & Code Safety (`lint_injection.py`)**: "
            + ("0 findings detected ✅" if sc.security["pass"] else f"**{sec_findings_cnt} security findings** ❌"),
            "- **Spec & Integrity Checks (`validate.py`)**: "
            + ("0 errors ✅" if sc.spec["pass"] else f"**{spec_errs_cnt} errors** ❌"),
        ])

        if sc.security["blocking_findings"]:
            lines.extend(["", "**Security Findings:**"])
            for bf in sc.security["blocking_findings"]:
                lines.append(f"- 🔴 `[{bf['rule']}]` {bf['message']} (`{bf['path']}:{bf['line']}`)")

        if sc.spec["errors"]:
            lines.extend(["", "**Policy Validation Errors:**"])
            for err in sc.spec["errors"]:
                lines.append(f"- ❌ {err}")

        lines.extend([
            "",
            "##### 🚀 How to Level Up This Skill",
        ])
        if sc.levelup_tips:
            for tip in sc.levelup_tips[:6]:
                lines.append(f"- {tip}")
        else:
            lines.append("- 🌟 **Flawless submission!** This skill meets all top-tier rubric criteria.")
        lines.append("")

    lines.extend([
        "---",
        "*🤖 Scorecard bot automatically evaluated this PR using `tools/skill_scorecard.py`.*",
    ])

    return "\n".join(lines)


def find_changed_skills(base_ref: str = "origin/main") -> list[str]:
    """Identify skills modified in git diff between base_ref and HEAD."""
    skills = set()
    candidate_refs = [base_ref]
    if not base_ref.startswith("origin/") and "/" not in base_ref:
        candidate_refs.append(f"origin/{base_ref}")
    candidate_refs.extend(["HEAD~1", "main", "origin/main"])

    for ref in candidate_refs:
        try:
            res = subprocess.run(
                ["git", "diff", "--name-only", f"{ref}...HEAD"],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=True,
            )
            files = res.stdout.splitlines()
            for f in files:
                p = Path(f).as_posix()
                if p.startswith("skills/"):
                    parts = p.split("/")
                    if len(parts) >= 2 and parts[1]:
                        skills.add(parts[1])
                elif p.startswith("evals/"):
                    parts = p.split("/")
                    if len(parts) >= 2 and parts[1]:
                        skills.add(parts[1])
            if skills or files:
                return sorted(skills)
        except subprocess.SubprocessError:
            continue

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
    req = urllib.request.Request(f"{api_url}?per_page=100", headers=headers, method="GET")  # noqa: S310

    existing_id = None
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:  # noqa: S310
            comments = json.loads(resp.read().decode("utf-8"))
            for c in comments:
                if SCORECARD_COMMENT_MARKER in c.get("body", ""):
                    existing_id = c.get("id")
                    break
    except urllib.error.HTTPError as err:
        if err.code == 403:
            print(
                f"Notice: GitHub token lacks write access to {repo} PR #{pr} (fork PR). "
                "Scorecard comment will be handled by workflow_run.",
                file=sys.stderr,
            )
            return False
        print(f"Failed to fetch PR comments for {repo} PR #{pr}: {err}", file=sys.stderr)
        return False
    except (urllib.error.URLError, TimeoutError, OSError) as err:
        print(f"Network error querying PR comments: {err}", file=sys.stderr)
        return False

    try:
        if existing_id:
            patch_url = f"https://api.github.com/repos/{repo}/issues/comments/{existing_id}"
            payload = json.dumps({"body": body}).encode("utf-8")
            patch_headers = {**headers, "Content-Type": "application/json"}
            patch_req = urllib.request.Request(patch_url, data=payload, headers=patch_headers, method="PATCH")
            with urllib.request.urlopen(patch_req, timeout=30) as resp:  # noqa: S310
                if resp.status in (200, 201):
                    print(f"Successfully updated scorecard comment on {repo} PR #{pr} (comment ID {existing_id})")
                    return True
        else:
            payload = json.dumps({"body": body}).encode("utf-8")
            post_headers = {**headers, "Content-Type": "application/json"}
            post_req = urllib.request.Request(api_url, data=payload, headers=post_headers, method="POST")
            with urllib.request.urlopen(post_req, timeout=30) as resp:  # noqa: S310
                if resp.status in (200, 201):
                    created = json.loads(resp.read().decode("utf-8"))
                    print(f"Successfully posted scorecard comment on {repo} PR #{pr} (comment ID {created.get('id')})")
                    return True
    except urllib.error.HTTPError as err:
        if err.code == 403:
            print(f"Notice: GITHUB_TOKEN has read-only permission for {repo} PR #{pr}.", file=sys.stderr)
            return False
        print(f"Failed to post/update scorecard comment on PR #{pr}: {err}", file=sys.stderr)
        return False
    except (urllib.error.URLError, TimeoutError, OSError) as err:
        print(f"Error posting scorecard comment to PR #{pr}: {err}", file=sys.stderr)
        return False

    return False


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("skills", nargs="*", help="skill names or paths to evaluate")
    ap.add_argument("--changed", action="store_true", help="evaluate skills modified relative to base branch")
    ap.add_argument("--base", default="origin/main", help="base git ref for diff (default: origin/main)")
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
    args = ap.parse_args(argv)

    if args.post_comment_file:
        if not args.post_comment_file.is_file():
            print(f"Error: comment file not found: {args.post_comment_file}", file=sys.stderr)
            return 2
        body = args.post_comment_file.read_text(encoding="utf-8")
        ok = post_or_update_comment(body, pr_number=args.pr_number)
        return 0 if ok else 1

    all_skills = load_skills()
    skills_dict = {s.name: s for s in all_skills}

    target_names: list[str] = []
    if args.skills:
        for s in args.skills:
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
    elif args.changed:
        changed = find_changed_skills(args.base)
        target_names = [name for name in changed if name in skills_dict or (SKILLS_DIR / name).is_dir()]
    elif args.all:
        target_names = sorted(skills_dict.keys())
    else:
        changed = find_changed_skills(args.base)
        if changed:
            target_names = [name for name in changed if name in skills_dict or (SKILLS_DIR / name).is_dir()]

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

    if scorecards:
        for sc in scorecards:
            status_str = "PASS" if sc.passed else "NEEDS WORK"
            print(f"{sc.score:5.1f}  {sc.name:<40} {sc.tier_badge} [{status_str}] ({sc.lines} lines)")
    else:
        print("No skills targeted for scorecard evaluation.")

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

    if args.post_comment:
        post_or_update_comment(md_report, pr_number=args.pr_number)

    fail_threshold = args.fail_under if args.fail_under is not None else (args.min_score if args.changed else None)
    if fail_threshold is not None and scorecards:
        failing = [sc for sc in scorecards if sc.score < fail_threshold or not sc.passed]
        if failing:
            print(f"\nScorecard gate FAILED: {len(failing)} skill(s) did not meet standards:")
            for sc in failing:
                reasons = []
                if sc.score < fail_threshold:
                    reasons.append(f"score {sc.score:.1f} < {fail_threshold:.1f}")
                if sc.lines > MAX_LINE_COUNT:
                    reasons.append(f"lines {sc.lines} > {MAX_LINE_COUNT}")
                if not sc.security["pass"]:
                    reasons.append(f"{len(sc.security['blocking_findings'])} security findings")
                if not sc.spec["pass"]:
                    reasons.append(f"{len(sc.spec['errors'])} spec errors")
                print(f"  - {sc.name}: {', '.join(reasons)}")
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
