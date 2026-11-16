"""The docs may only quote the real number of skills."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import check_skill_count as csc  # noqa: E402


def test_prose_claims_match_the_skills_on_disk():
    assert csc.scan(csc.real_count()) == []


def test_stale_total_is_found_but_subsets_are_not(tmp_path, monkeypatch):
    doc = tmp_path / "README.md"
    text = "\n".join(["Browse all 281 skills.", "A procedure added to 186 skills.", "281 skills, 3.5K installs"])
    doc.write_text(text + "\n", encoding="utf-8")
    monkeypatch.setattr(csc, "ROOT", tmp_path)
    monkeypatch.setattr(csc, "FILES", ["README.md"])
    found = csc.scan(283)
    assert [(f[1]) for f in found] == [1]
    assert "283 skills" in found[0][3]


def test_changelog_only_checks_the_unreleased_section(tmp_path, monkeypatch):
    log = tmp_path / "CHANGELOG.md"
    log.write_text("## [Unreleased]\nAll 281 skills.\n## [1.1.0]\nAll 281 skills.\n", encoding="utf-8")
    monkeypatch.setattr(csc, "ROOT", tmp_path)
    monkeypatch.setattr(csc, "FILES", ["CHANGELOG.md"])
    assert [f[1] for f in csc.scan(283)] == [2]
