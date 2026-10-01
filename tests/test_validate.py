from __future__ import annotations

import validate
from conftest import write_skill

CATS = {"research-writing", "literature-review"}


def run(skill_dir, baseline=frozenset()):
    rep = validate.Report()
    validate.validate_skill(skill_dir, rep, CATS, set(baseline))
    return rep


def test_valid_skill_passes(skills_root):
    rep = run(write_skill(skills_root, "good-skill"))
    assert rep.errors == [] and rep.warnings == []


def test_name_must_match_folder(skills_root):
    d = write_skill(skills_root, "folder-name", frontmatter=(
        "name: other-name\ndescription: x\nmetadata:\n  version: '1'\n  category: research-writing\n"
        "  maintainer: Kalaris Labs\n"))
    assert any("must match folder" in e for e in run(d).errors)


def test_name_charset_and_length(skills_root):
    long_name = "a" * 65
    d = write_skill(skills_root, long_name, frontmatter=(
        f"name: {long_name}\ndescription: x\nmetadata:\n  version: '1'\n  category: research-writing\n"
        "  maintainer: Kalaris Labs\n"))
    assert any("exceeds 64" in e for e in run(d).errors)
    d2 = write_skill(skills_root, "Bad_Name", frontmatter=(
        "name: Bad_Name\ndescription: x\nmetadata:\n  version: '1'\n  category: research-writing\n"
        "  maintainer: Kalaris Labs\n"))
    assert any("kebab-case" in e for e in run(d2).errors)


def test_description_limit(skills_root):
    d = write_skill(skills_root, "long-desc", frontmatter=(
        f"name: long-desc\ndescription: {'x' * 1025}\nmetadata:\n  version: '1'\n  category: research-writing\n"
        "  maintainer: Kalaris Labs\n"))
    assert any("max 1024" in e for e in run(d).errors)


def test_non_spec_field_and_metadata_types(skills_root):
    d = write_skill(skills_root, "extra-field", frontmatter=(
        "name: extra-field\ndescription: x\nauthor: someone\nmetadata:\n  version: 1.0\n"
        "  category: research-writing\n  maintainer: Kalaris Labs\n"))
    errors = run(d).errors
    assert any("non-spec top-level field 'author'" in e for e in errors)
    assert any("metadata.version must be a string" in e for e in errors)


def test_unknown_category(skills_root):
    d = write_skill(skills_root, "bad-cat", frontmatter=(
        "name: bad-cat\ndescription: x\nmetadata:\n  version: '1'\n  category: nope\n  maintainer: Kalaris Labs\n"))
    assert any("not defined" in e for e in run(d).errors)


def test_line_budget_and_baseline(skills_root):
    body = "# T\n" + "line\n" * 600
    d = write_skill(skills_root, "big-skill", body=body)
    assert any("budget" in e for e in run(d).errors)
    rep = run(d, baseline={"big-skill"})
    assert not rep.errors and any("budget" in w for w in rep.warnings)


def test_disallowed_file_type_and_size(skills_root):
    big = b"0" * (2 * 1024 * 1024 + 1)
    d = write_skill(skills_root, "files-skill", files={"scripts/tool.exe": b"MZ", "assets/huge.png": big})
    errors = run(d).errors
    assert any("tool.exe" in e and "not allowed" in e for e in errors)
    assert any("huge.png" in e and "per-file limit" in e for e in errors)


def test_links(skills_root):
    body = ("# T\n[ok](references/a.md) [missing](references/b.md) [web](https://x.org) "
            "[escape](../../etc/passwd) `[code](not/a/link.md)`\n")
    d = write_skill(skills_root, "link-skill", body=body, files={"references/a.md": "# A\n"})
    rep = run(d)
    assert any("escapes the skills directory" in e for e in rep.errors)
    assert any("broken relative link 'references/b.md'" in w for w in rep.warnings)
    assert not any("not/a/link.md" in w for w in rep.warnings)


def test_absolute_user_path_warns(skills_root):
    d = write_skill(skills_root, "path-skill", body="# T\nSee /Users/alice/data.csv and /home/ubuntu/x\n")
    warnings = run(d).warnings
    assert any("/Users/alice/" in w for w in warnings)
    assert not any("/home/ubuntu/" in w for w in warnings)


def test_missing_frontmatter(skills_root):
    d = skills_root / "no-fm"
    d.mkdir()
    (d / "SKILL.md").write_text("# No frontmatter\n", encoding="utf-8")
    assert any("missing YAML frontmatter" in e for e in run(d).errors)


def test_repository_skills_are_valid():
    """The committed corpus must always validate (errors only)."""
    assert validate.main(["--quiet"]) == 0
