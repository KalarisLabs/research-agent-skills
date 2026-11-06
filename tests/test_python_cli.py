"""Tests for research-agent-skills Python packaging and CLI."""

from __future__ import annotations

from research_agent_skills.catalog import load_catalog
from research_agent_skills.cli import main
from research_agent_skills.harness import get_harnesses, resolve_harnesses


def test_catalog_loads_skills() -> None:
    catalog = load_catalog()
    assert len(catalog.skills) >= 280
    assert len(catalog.categories) >= 12
    assert "research-essentials" in catalog.bundles


def test_catalog_search() -> None:
    catalog = load_catalog()
    hits = catalog.search("citation")
    assert len(hits) > 0
    assert any(s.name == "citation-verification" for s in hits)


def test_harness_resolution() -> None:
    harnesses = get_harnesses()
    assert len(harnesses) >= 8

    resolved_auto = resolve_harnesses("auto", harnesses)
    assert len(resolved_auto) >= 1

    resolved_claude = resolve_harnesses("claude-code", harnesses)
    assert len(resolved_claude) == 1
    assert resolved_claude[0].id == "claude-code"


def test_cli_list_invocation(capsys) -> None:
    ret = main(["list", "--categories"])
    assert ret == 0
    captured = capsys.readouterr()
    assert "research-writing" in captured.out


def test_cli_search_invocation(capsys) -> None:
    ret = main(["search", "unslop"])
    assert ret == 0
    captured = capsys.readouterr()
    assert "unslop-academic-writing" in captured.out


def test_cli_doctor_invocation(capsys) -> None:
    ret = main(["doctor"])
    assert ret == 0
    captured = capsys.readouterr()
    assert "Doctor Diagnostics" in captured.out


def test_harness_catalog_20() -> None:
    harnesses = get_harnesses()
    assert len(harnesses) == 20
    ids = {h.id for h in harnesses}
    assert "claude-science" in ids
    assert "openscience" in ids
    assert "t3-code" in ids
    assert "hermes" in ids
    assert "aider" in ids
    assert "openhands" in ids
    assert "roo-code" in ids


def test_cli_configure_invocation(tmp_path, monkeypatch, capsys) -> None:
    monkeypatch.chdir(tmp_path)
    ret = main(["configure", "--harness", "claude-science,t3-code,aider,antigravity"])
    assert ret == 0
    captured = capsys.readouterr()
    assert "CLAUDE.md" in captured.out
    assert (tmp_path / "CLAUDE.md").exists()
    assert (tmp_path / ".t3" / "config.json").exists()
    assert (tmp_path / "CONVENTIONS.md").exists()



def test_package_version_matches_repository_version() -> None:
    """The wheel, npm package and plugin manifests must all ship the VERSION file's version."""
    import json
    import tomllib
    from pathlib import Path

    import research_agent_skills

    root = Path(__file__).resolve().parents[1]
    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    assert research_agent_skills.__version__ == version
    assert tomllib.loads((root / "pyproject.toml").read_text(encoding="utf-8"))["project"]["version"] == version
    assert json.loads((root / "cli" / "package.json").read_text(encoding="utf-8"))["version"] == version
    assert json.loads((root / "plugin.json").read_text(encoding="utf-8"))["version"] == version


def test_web_catalog_and_packaged_catalog_are_in_sync() -> None:
    """The website and the wheel serve copies of catalog/skills.json; stale copies mean a stale site or package."""
    from pathlib import Path

    root = Path(__file__).resolve().parents[1]
    source = (root / "catalog" / "skills.json").read_bytes()
    assert (root / "web" / "skills.json").read_bytes() == source
    assert (root / "src" / "research_agent_skills" / "data" / "skills.json").read_bytes() == source
