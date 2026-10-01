from __future__ import annotations

import enrich
import rebrand
from common import load_skill, split_frontmatter
from conftest import write_skill


def test_strip_marketing_lines_and_inline_stars():
    text = ("# Tool\n\n- **24,300+ GitHub stars**\n**Users**: 20,000+ organizations | **GitHub Stars**: 23k+\n"
            "- **GitHub**: https://github.com/x/y (23k+ stars)\nKeep this line.\n")
    out = rebrand.strip_marketing(text)
    assert "stars" not in out.lower() and "Users" not in out
    assert "https://github.com/x/y" in out and "Keep this line." in out


def test_unlink_dead_links_keeps_code_and_live_links(skills_root):
    d = write_skill(skills_root, "links-skill",
                    body="# T\n[live](references/a.md) [dead](references/missing.md) [web](https://x.org)\n"
                         "```\n[in code](references/missing.md)\n```\n",
                    files={"references/a.md": "# A\n"})
    assert enrich.unlink_dead_links(d) == 1
    body = (d / "SKILL.md").read_text(encoding="utf-8")
    assert "[live](references/a.md)" in body and " dead " in body and "[in code](references/missing.md)" in body


def test_split_oversized_moves_sections_and_relinks(skills_root):
    big = "\n".join(f"line {i}" for i in range(200))
    body = (f"# T\n\n## Quick start\n\nstart\n\n## API reference\n\nSee [helper](scripts/run.py) and "
            f"[ref](references/x.md).\n{big}\n\n## Examples\n\n{big}\n")
    d = write_skill(skills_root, "big-skill", body=body, files={"scripts/run.py": "print(1)\n",
                                                               "references/x.md": "# X\n"})
    moved = enrich.split_oversized(d, 150)
    assert moved and len((d / "SKILL.md").read_text(encoding="utf-8").splitlines()) <= 150
    ref = (d / "references" / "api-reference.md").read_text(encoding="utf-8")
    assert "(../scripts/run.py)" in ref and "(x.md)" in ref
    assert "## Quick start" in (d / "SKILL.md").read_text(encoding="utf-8")


def test_procedure_and_related_are_idempotent(skills_root):
    d = write_skill(skills_root, "thin-skill", body="# Thin\n\nJust some prose about a library.\n")
    s = load_skill(d)
    assert enrich.add_procedure(s) is True
    assert enrich.add_procedure(load_skill(d)) is False
    _, body = split_frontmatter((d / "SKILL.md").read_text(encoding="utf-8"))
    assert "## Agent operating procedure" in body and "| If this happens | Do this |" in body
    assert "Never fabricate" in body
    assert enrich.add_related(load_skill(d), [("other-skill", "Does other things.")]) is True
    assert enrich.add_related(load_skill(d), [("other-skill", "Does other things.")]) is False


def test_strong_skill_gets_no_procedure(skills_root):
    body = ("# Strong\n\n1. a\n2. b\n3. c\n\n| x | y |\n|---|---|\n| 1 | 2 |\n\nAlways verify against the "
            "official docs.\n")
    d = write_skill(skills_root, "strong-skill", body=body)
    assert enrich.add_procedure(load_skill(d)) is False


def test_every_category_has_a_procedure():
    import yaml
    from common import THIRD_PARTY
    cats = set(yaml.safe_load((THIRD_PARTY / "categories.yaml").read_text(encoding="utf-8"))["categories"])
    procs = set(yaml.safe_load((THIRD_PARTY / "operating-procedures.yaml").read_text(encoding="utf-8"))["categories"])
    assert cats - {"journal-formats", "research-writing"} <= procs | {"journal-formats", "research-writing"}
    assert cats <= procs
