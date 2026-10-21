"""Tests for tools/generate_skill_data.py (model-assisted data, validated mechanically) and
tools/import_upstream.py (pinned upstream import). The Claude CLI and the network are never touched."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from types import SimpleNamespace

import generate_skill_data as gen
import import_upstream as imp
import pytest
import yaml

GOOD = ("Plan and run a reproducible analysis of a dataset with documented steps and checks, covering input "
        "validation, the statistical workflow and a methods paragraph. Use when the user asks to analyse data end "
        "to end, validate inputs, or write the methods section for a paper.")


# --- generate_skill_data -------------------------------------------------------------------------------------------

def test_valid_description_accepts_a_good_one_and_names_each_problem():
    assert gen.valid_description(GOOD) == []
    problems = gen.valid_description("Short <b>powerful</b> seamless tool.")
    assert any(p.startswith("length") for p in problems)
    assert "no 'Use when' trigger" in problems
    assert "angle bracket" in problems


def test_parse_json_extracts_object_from_chatty_text():
    assert gen.parse_json('Sure!\n```json\n{"a": {"b": 1}}\n```\nDone') == {"a": {"b": 1}}
    with pytest.raises(AttributeError):
        gen.parse_json("no json here")


def test_excerpt_omits_code_and_truncates():
    out = gen.excerpt("intro\n```py\nsecret()\n```\n" + "x" * 50, limit=30)
    assert "secret" not in out and "[code block omitted]" in out and len(out) <= 30


def test_needs_description_uses_validation():
    assert gen.needs_description(SimpleNamespace(meta={"description": "too short"}))
    assert not gen.needs_description(SimpleNamespace(meta={"description": GOOD}))


def test_claude_requires_the_cli(monkeypatch):
    monkeypatch.setattr(gen.shutil, "which", lambda _: None)
    with pytest.raises(SystemExit, match="claude CLI not found"):
        gen.claude("hi", "m")


def test_claude_passes_prompt_on_stdin_and_returns_result(monkeypatch):
    seen = {}

    def fake_run(cmd, **kw):
        seen["cmd"], seen["input"] = cmd, kw["input"]
        return SimpleNamespace(stdout=json.dumps({"result": "answer"}))

    monkeypatch.setattr(gen.shutil, "which", lambda _: "/usr/bin/claude")
    monkeypatch.setattr(gen.subprocess, "run", fake_run)
    assert gen.claude("question", "some-model") == "answer"
    assert seen["input"] == "question" and "--no-session-persistence" in seen["cmd"] and "some-model" in seen["cmd"]


def _skill(name: str):
    return SimpleNamespace(name=name, meta={"description": "x"}, body="# T\nBody", category="research-writing")


def test_adapted_names_reads_the_manifest(monkeypatch, tmp_path):
    (tmp_path / "upstream-manifest.json").write_text(json.dumps({"skills": [
        {"name": "a", "rewrite_status": "imported"}, {"name": "b", "rewrite_status": "original"}]}), encoding="utf-8")
    monkeypatch.setattr(gen, "THIRD_PARTY", tmp_path)
    assert gen.adapted_names() == {"a"}


def test_cmd_descriptions_writes_valid_overrides_and_reports_failures(monkeypatch, tmp_path, capsys):
    out = tmp_path / "overrides.yaml"
    monkeypatch.setattr(gen, "OVERRIDES", out)
    monkeypatch.setattr(gen, "load_skills", lambda: [_skill("good-skill"), _skill("bad-skill")])
    monkeypatch.setattr(gen, "adapted_names", lambda: {"good-skill", "bad-skill"})

    def fake_claude(prompt, model):
        return json.dumps({"description": GOOD if "good-skill" in prompt else "too short"})

    monkeypatch.setattr(gen, "claude", fake_claude)
    args = argparse.Namespace(model="m", workers=1, skills=None, force=False)
    assert gen.cmd_descriptions(args) == 0
    text = capsys.readouterr().out
    assert "ok good-skill" in text and "FAILED bad-skill" in text
    saved = yaml.safe_load(out.read_text(encoding="utf-8"))
    assert saved["descriptions"] == {"good-skill": GOOD} and saved["model"] == "m"


def test_cmd_evals_writes_suites_and_rejects_incomplete_ones(monkeypatch, tmp_path, capsys):
    monkeypatch.setattr(gen, "ROOT", tmp_path)
    monkeypatch.setattr(gen, "load_skills", lambda: [_skill("alpha"), _skill("beta")])
    monkeypatch.setattr(gen, "tfidf_overlap", lambda skills, t: [("alpha", "beta", 0.5)])
    good = {"evals": [{"prompt": f"p{i}", "expected_output": "e"} for i in range(3)]
            + [{"prompt": "near", "expected_output": "e", "should_trigger": False, "better_skill": "beta"}]}
    bad = {"evals": [{"prompt": "only one", "expected_output": "e"}]}
    monkeypatch.setattr(gen, "claude", lambda prompt, model: json.dumps(good if "Skill name: alpha" in prompt else bad))
    args = argparse.Namespace(model="m", workers=1, skills=None, force=False)
    assert gen.cmd_evals(args) == 0
    out = capsys.readouterr().out
    assert "2 eval suites to generate" in out and "ok alpha" in out and "FAILED beta" in out
    written = [p for p in (tmp_path / "evals").glob("*/evals.json")]
    for p in written:
        data = json.loads(p.read_text(encoding="utf-8"))
        assert data["provenance"].endswith("pending review")
        neg = [e for e in data["evals"] if e.get("should_trigger") is False]
        assert neg and neg[0].get("better_skill") == "beta"
    # a second run skips suites that already exist (alpha) and retries the failed one (beta)
    assert gen.cmd_evals(args) == 0
    assert "1 eval suites to generate" in capsys.readouterr().out


# --- import_upstream -----------------------------------------------------------------------------------------------

def _git(cwd, *args):
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def _upstream_repo(path):
    path.mkdir(parents=True)
    _git(path, "init", "-q")
    _git(path, "config", "user.email", "t@example.org")
    _git(path, "config", "user.name", "t")
    for rel in ("alpha", "nested/beta", "skip-me"):
        d = path / "skills" / rel
        d.mkdir(parents=True)
        (d / "SKILL.md").write_text(f"---\nname: {rel.split('/')[-1]}\ndescription: d\n---\n# T\n", encoding="utf-8")
    _git(path, "add", "-A")
    _git(path, "commit", "-q", "-m", "init")
    return _git(path, "rev-parse", "HEAD")


def test_checkout_fetches_the_pinned_ref_into_the_cache(monkeypatch, tmp_path):
    repo = tmp_path / "upstream"
    ref = _upstream_repo(repo)
    monkeypatch.setattr(imp, "CACHE", tmp_path / "cache")
    path = imp.checkout({"id": "up", "repo": str(repo), "ref": ref}, None)
    assert (path / "skills" / "alpha" / "SKILL.md").exists()
    assert imp.checkout({"id": "up", "repo": str(repo), "ref": ref}, None) == path  # reuses the checkout


def test_checkout_from_source_dir_verifies_the_pinned_commit(tmp_path):
    repo = tmp_path / "pre" / "up"
    ref = _upstream_repo(repo)
    assert imp.checkout({"id": "up", "ref": ref}, tmp_path / "pre") == repo
    with pytest.raises(SystemExit, match="expected pinned"):
        imp.checkout({"id": "up", "ref": "0" * 40}, tmp_path / "pre")
    with pytest.raises(SystemExit, match="missing checkout"):
        imp.checkout({"id": "nope", "ref": ref}, tmp_path / "pre")


def test_discover_final_name_and_category(tmp_path):
    repo = tmp_path / "up"
    _upstream_repo(repo)
    source = {"id": "up", "layout": "nested", "root": "skills", "include_glob": "[an]*",
              "renames": {"alpha": "alpha-renamed"}}
    found = imp.discover(source, repo)
    assert [rel for rel, _ in found] == ["alpha", "nested/beta"]
    assert imp.final_name(source, "alpha", found[0][1]) == "alpha-renamed"
    assert imp.final_name(source, "nested/beta", found[1][1]) == "beta"  # name from frontmatter
    assert imp.final_name({"layout": "flat", "renames": {}}, "flatname", found[0][1]) == "flatname"
    cats = {"assign": {"research-writing": ["beta"]}, "by_prefix": {"nested": "data-science"}}
    assert imp.category_for("beta", "x/beta", cats) == "research-writing"
    assert imp.category_for("other", "nested/other", cats) == "data-science"
    with pytest.raises(SystemExit, match="no category"):
        imp.category_for("other", "zzz/other", cats)


def test_first_sentence_trims_long_text():
    assert imp._first_sentence("One sentence.  Another one.") == "One sentence."
    long = imp._first_sentence("word " * 100)
    assert len(long) == 140 and long.endswith("…")


def test_apply_patches_runs_only_the_matching_phase(monkeypatch, tmp_path, capsys):
    (tmp_path / "01-before.patch").write_text("", encoding="utf-8")
    (tmp_path / "post-02-after.patch").write_text("", encoding="utf-8")
    monkeypatch.setattr(imp, "PATCHES", tmp_path)
    calls = []
    monkeypatch.setattr(imp.subprocess, "run", lambda cmd, **kw: calls.append(cmd[-1]))
    imp.apply_patches()
    imp.apply_patches(after_enrichment=True)
    assert [Path(c).name for c in calls] == ["01-before.patch", "post-02-after.patch"]
    assert "applied 01-before.patch" in capsys.readouterr().out


def _import_env(monkeypatch, tmp_path, *, old_skills=None, extra_source=None):
    """Point import_upstream at a throwaway upstream, skills dir and manifest."""
    repo = tmp_path / "upstream"
    ref = _upstream_repo(repo)
    tp = tmp_path / "third_party"
    tp.mkdir()
    source = {"id": "up", "repo": str(repo), "ref": ref, "layout": "nested", "root": "skills",
              "exclude": {"skip-me": "not wanted"}, "copyright": "c", "license_file": "l", **(extra_source or {})}
    (tp / "sources.yaml").write_text(yaml.safe_dump({"sources": [source]}), encoding="utf-8")
    (tp / "categories.yaml").write_text(yaml.safe_dump(
        {"assign": {"research-writing": ["alpha"]}, "by_prefix": {"nested": "data-science"}}), encoding="utf-8")
    skills_dir = tmp_path / "skills"
    skills_dir.mkdir()
    manifest = tp / "upstream-manifest.json"
    if old_skills is not None:
        manifest.write_text(json.dumps({"skills": old_skills}), encoding="utf-8")
    monkeypatch.setattr(imp, "THIRD_PARTY", tp)
    monkeypatch.setattr(imp, "SKILLS_DIR", skills_dir)
    monkeypatch.setattr(imp, "MANIFEST", manifest)
    monkeypatch.setattr(imp, "PATCHES", tp / "patches")
    monkeypatch.setattr(imp, "CACHE", tmp_path / "cache")
    monkeypatch.setattr(imp, "rebrand_skill", lambda dest, name, category: None)
    enriched = []
    monkeypatch.setattr(imp, "enrich_imported", lambda names: enriched.extend(names))
    monkeypatch.setattr("sys.argv", ["import_upstream"])
    return skills_dir, manifest, enriched


def test_main_imports_skills_and_writes_the_provenance_manifest(monkeypatch, tmp_path, capsys):
    skills_dir, manifest, enriched = _import_env(monkeypatch, tmp_path)
    imp.main()
    assert sorted(p.name for p in skills_dir.iterdir()) == ["alpha", "beta"]  # skip-me is excluded
    data = json.loads(manifest.read_text(encoding="utf-8"))
    assert [(s["name"], s["category"], s["rewrite_status"]) for s in data["skills"]] == [
        ("alpha", "research-writing", "imported"), ("beta", "data-science", "imported")]
    assert enriched == ["alpha", "beta"] and "imported 2 skills" in capsys.readouterr().out


def test_main_keeps_protected_originals_and_removes_stale_imports(monkeypatch, tmp_path, capsys):
    skills_dir, manifest, _ = _import_env(monkeypatch, tmp_path, old_skills=[
        {"name": "alpha", "rewrite_status": "original"}, {"name": "gone", "rewrite_status": "imported"}])
    (skills_dir / "alpha").mkdir()
    (skills_dir / "alpha" / "SKILL.md").write_text("original, hand-written\n", encoding="utf-8")
    (skills_dir / "gone").mkdir()
    imp.main()
    assert (skills_dir / "alpha" / "SKILL.md").read_text(encoding="utf-8") == "original, hand-written\n"
    assert not (skills_dir / "gone").exists() and "removed stale skill gone" in capsys.readouterr().out
    assert {s["name"]: s["rewrite_status"] for s in json.loads(manifest.read_text(encoding="utf-8"))["skills"]} == {
        "alpha": "original", "beta": "imported"}


def test_main_refuses_name_collisions_with_original_skills(monkeypatch, tmp_path):
    skills_dir, _, _ = _import_env(monkeypatch, tmp_path, old_skills=[{"name": "other", "rewrite_status": "original"}])
    (skills_dir / "beta").mkdir()  # an original skill already uses the name an upstream skill would take
    with pytest.raises(SystemExit, match="already exists as an original skill"):
        imp.main()


def test_main_rejects_invalid_names(monkeypatch, tmp_path):
    _import_env(monkeypatch, tmp_path, extra_source={"renames": {"alpha": "Bad_Name"}})
    with pytest.raises(SystemExit, match="invalid skill name"):
        imp.main()
