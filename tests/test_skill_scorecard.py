"""Unit tests for tools/skill_scorecard.py."""

from __future__ import annotations

import json
from pathlib import Path

import common
import skill_scorecard
import trigger_bench


def test_progress_bar_and_mini_bar():
    assert skill_scorecard.progress_bar(100.0, 100.0, width=10) == "██████████"
    assert skill_scorecard.progress_bar(0.0, 100.0, width=10) == "░░░░░░░░░░"
    assert skill_scorecard.progress_bar(50.0, 100.0, width=10) == "█████░░░░░"
    assert len(skill_scorecard.progress_bar(82.5, 100.0, width=20)) == 20

    assert skill_scorecard.mini_bar(10.0, 10.0) == "██████████"
    assert skill_scorecard.mini_bar(0.0, 10.0) == "░░░░░░░░░░"


def test_score_tier():
    badge, desc = skill_scorecard.score_tier(96.0)
    assert "S-Tier" in badge and "Exceptional" in desc

    badge, desc = skill_scorecard.score_tier(88.0)
    assert "A-Tier" in badge and "High Quality" in desc

    badge, desc = skill_scorecard.score_tier(81.0)
    assert "B-Tier" in badge and "Passing" in desc

    badge, desc = skill_scorecard.score_tier(65.0)
    assert "Needs Work" in badge and "Below Standard" in desc


def test_evaluate_existing_skill():
    skill_dir = common.SKILLS_DIR / "unslop-academic-writing"
    skill_obj = common.load_skill(skill_dir)
    all_skills = {s.name: s for s in common.load_skills()}
    index = trigger_bench.BM25({
        n: trigger_bench.tokens(n.replace("-", " ")) * 2 + trigger_bench.tokens(str(s.meta.get("description", "")))
        for n, s in all_skills.items()
    })
    tests_blob = ""

    sc = skill_scorecard.evaluate_skill(skill_obj, tests_blob, all_skills, index, min_score=80.0)
    assert sc.name == "unslop-academic-writing"
    assert sc.score >= 80.0
    assert sc.lines <= 500
    assert sc.passed is True
    assert sc.security["pass"] is True
    assert sc.spec["pass"] is True
    assert sc.routing["has_evals"] is True
    assert sc.routing["hit3"] == 1.0


def test_format_markdown_scorecard_empty():
    md = skill_scorecard.format_markdown_scorecard([])
    assert skill_scorecard.SCORECARD_COMMENT_MARKER in md
    assert "No skills under `skills/` were modified" in md


def test_format_markdown_scorecard_with_skill():
    skill_dir = common.SKILLS_DIR / "unslop-academic-writing"
    skill_obj = common.load_skill(skill_dir)
    all_skills = {s.name: s for s in common.load_skills()}
    index = trigger_bench.BM25({
        n: trigger_bench.tokens(n.replace("-", " ")) * 2 + trigger_bench.tokens(str(s.meta.get("description", "")))
        for n, s in all_skills.items()
    })

    sc = skill_scorecard.evaluate_skill(skill_obj, "", all_skills, index, min_score=80.0)
    md = skill_scorecard.format_markdown_scorecard([sc], min_score=80.0)

    assert skill_scorecard.SCORECARD_COMMENT_MARKER in md
    assert "## 🏆 Skill Scorecard Report" in md
    assert "unslop-academic-writing" in md
    assert "Rubric Breakdown" in md
    assert "Line Count & Size" in md
    assert "Trigger Routing Benchmark" in md
    assert "Security & Policy Verification" in md
    assert "How to Level Up This Skill" in md


def test_trigger_routing_missing_evals(tmp_path: Path):
    all_skills = {s.name: s for s in common.load_skills()}
    index = trigger_bench.BM25({
        n: trigger_bench.tokens(n.replace("-", " ")) * 2 + trigger_bench.tokens(str(s.meta.get("description", "")))
        for n, s in all_skills.items()
    })

    routing = skill_scorecard.evaluate_trigger_routing("non-existent-skill-xyz", all_skills, index)
    assert routing["has_evals"] is False
    assert routing["pass"] is False
    assert "Missing eval suite" in routing["error"]


def test_main_cli_single_skill(tmp_path: Path):
    out_md = tmp_path / "scorecard.md"
    out_json = tmp_path / "scorecard.json"
    code = skill_scorecard.main([
        "unslop-academic-writing",
        "--output", str(out_md),
        "--json", str(out_json),
        "--min-score", "80.0",
    ])
    assert code == 0
    assert out_md.is_file()
    assert out_json.is_file()

    data = json.loads(out_json.read_text(encoding="utf-8"))
    assert data["all_passed"] is True
    assert len(data["skills"]) == 1
    assert data["skills"][0]["name"] == "unslop-academic-writing"


def test_main_cli_fail_under(tmp_path: Path):
    # Setting threshold to 105 must fail
    code = skill_scorecard.main([
        "unslop-academic-writing",
        "--fail-under", "105.0",
    ])
    assert code == 1


def test_find_changed_skills():
    # Should run subprocess and return a list (empty or non-empty) without raising
    changed = skill_scorecard.find_changed_skills("origin/main")
    assert isinstance(changed, list)


def test_format_markdown_scorecard_with_findings_and_errors():
    skill_dir = common.SKILLS_DIR / "unslop-academic-writing"
    skill_obj = common.load_skill(skill_dir)
    all_skills = {s.name: s for s in common.load_skills()}
    index = trigger_bench.BM25({
        n: trigger_bench.tokens(n.replace("-", " ")) * 2 + trigger_bench.tokens(str(s.meta.get("description", "")))
        for n, s in all_skills.items()
    })

    sc = skill_scorecard.evaluate_skill(skill_obj, "", all_skills, index, min_score=80.0)
    # Inject synthetic findings to exercise error rendering branches
    sc.security = {
        "pass": False,
        "blocking_findings": [{"rule": "bad-pattern", "message": "bad", "path": "SKILL.md", "line": 10}],
    }
    sc.spec = {
        "pass": False,
        "errors": ["Sample validation error"],
    }
    sc.routing = {
        "has_evals": False,
        "error": "Missing evals file",
        "hit1": 0.0,
        "hit3": 0.0,
        "false_trigger": 0.0,
        "cases": [],
        "pass": False,
    }
    sc.levelup_tips = ["Add more examples", "Clarify description"]

    md = skill_scorecard.format_markdown_scorecard([sc], min_score=80.0)
    assert "bad-pattern" in md
    assert "Sample validation error" in md
    assert "Missing eval suite" in md
    assert "Add more examples" in md


def test_trigger_routing_corrupt_evals(tmp_path: Path):
    eval_dir = tmp_path / "evals" / "bad-skill"
    eval_dir.mkdir(parents=True)
    (eval_dir / "evals.json").write_text("{corrupt json", encoding="utf-8")

    all_skills = {s.name: s for s in common.load_skills()}
    index = trigger_bench.BM25({
        n: trigger_bench.tokens(n.replace("-", " ")) * 2 + trigger_bench.tokens(str(s.meta.get("description", "")))
        for n, s in all_skills.items()
    })

    # Temporarily monkeypatch ROOT in skill_scorecard
    orig_root = skill_scorecard.ROOT
    try:
        skill_scorecard.ROOT = tmp_path
        routing = skill_scorecard.evaluate_trigger_routing("bad-skill", all_skills, index)
        assert routing["has_evals"] is False
        assert "Unparseable eval suite" in routing["error"]

        # Test empty evals list
        (eval_dir / "evals.json").write_text('{"evals": []}', encoding="utf-8")
        routing_empty = skill_scorecard.evaluate_trigger_routing("bad-skill", all_skills, index)
        assert routing_empty["has_evals"] is True
        assert "contains no prompts" in routing_empty["error"]
    finally:
        skill_scorecard.ROOT = orig_root

