from __future__ import annotations

import rebrand
from common import BRAND, split_frontmatter
from conftest import write_skill


def test_strip_sections_removes_until_same_or_higher_heading():
    heading = rebrand.PROMO_SECTION_HEADINGS[0]
    text = f"# Top\n\nKeep.\n\n## {heading}\n\nDrop me.\n\n### Nested\n\nDrop too.\n\n## Next\n\nKeep 2.\n"
    out = rebrand.strip_sections(text, (heading,))
    assert "Drop" not in out and "Keep." in out and "## Next" in out and "Keep 2." in out


def test_strip_sections_at_end_of_file():
    heading = rebrand.PROMO_SECTION_HEADINGS[0]
    out = rebrand.strip_sections(f"# T\n\nBody\n\n## {heading}\n\ncite us\n", (heading,))
    assert out == "# T\n\nBody\n"


def test_rewrite_text_applies_rules_and_fixes():
    old, new = rebrand.REPLACEMENTS[-3]
    text = f"by {old}. Run `uv uv pip install x`.​"
    out = rebrand.rewrite_text(text)
    assert old not in out and new in out
    assert "uv pip install x" in out and "uv uv" not in out
    assert "​" not in out


def test_rewrite_keeps_emoji_zwj():
    s = "\U0001f468‍\U0001f4bb"
    assert rebrand.rewrite_text(s) == s


def test_normalize_frontmatter_hoists_and_attributes():
    meta = {"name": "x", "description": "d", "version": "1.2.0", "author": BRAND, "tags": ["a", "b"],
            "metadata": {"skill-author": "Jane Doe", "openclaw": {"requires": {"bins": ["x"]}}}}
    out = rebrand.normalize_frontmatter(meta, "final-name", "research-writing")
    md = out["metadata"]
    assert out["name"] == "final-name" and out["license"] == "MIT"
    assert set(out) <= {"name", "description", "license", "compatibility", "allowed-tools", "metadata"}
    assert md["version"] == "1.2.0" and md["tags"] == "a, b" and md["category"] == "research-writing"
    assert md["maintainer"] == BRAND and md["contributor"] == "Jane Doe"
    assert isinstance(md["openclaw"], dict)


def test_vendor_author_is_not_kept_as_contributor():
    meta = {"name": "x", "description": "d", "metadata": {"skill-author": BRAND}}
    md = rebrand.normalize_frontmatter(meta, "x", "research-writing")["metadata"]
    assert "contributor" not in md


def test_utf8_snippet_inserted_after_docstring_and_future():
    src = '#!/usr/bin/env python\n"""Doc."""\nfrom __future__ import annotations\nimport os\nprint("✓ ok")\n'
    out = rebrand.ensure_utf8_console(src)
    lines = out.splitlines()
    assert lines[0].startswith("#!") and lines[1] == '"""Doc."""'
    assert lines[2] == "from __future__ import annotations"
    assert lines[3] == rebrand.UTF8_MARKER
    compile(out, "x.py", "exec")
    assert rebrand.ensure_utf8_console(out) == out  # idempotent


def test_utf8_snippet_skips_ascii_and_invalid():
    assert rebrand.ensure_utf8_console('print("ok")\n') == 'print("ok")\n'
    bad = 'print("✓" \n'
    assert rebrand.ensure_utf8_console(bad) == bad


def test_rebrand_skill_end_to_end_is_idempotent(skills_root):
    heading = rebrand.PROMO_SECTION_HEADINGS[0]
    d = write_skill(skills_root, "src-name",
                    frontmatter="name: src-name\ndescription: A skill.\nversion: 2\n",
                    body=f"\n# T\r\n\r\nText\r\n\r\n## {heading}\r\n\r\ncite\r\n",
                    files={"scripts/run.py": 'print("✓")\r\n'})
    rebrand.rebrand_skill(d, "src-name", "literature-review")
    first = {p: p.read_bytes() for p in d.rglob("*") if p.is_file()}
    assert all(b"\r\n" not in v for v in first.values())
    meta, body = split_frontmatter((d / "SKILL.md").read_text(encoding="utf-8"))
    assert meta["metadata"]["category"] == "literature-review" and heading not in body
    rebrand.rebrand_skill(d, "src-name", "literature-review")
    assert {p: p.read_bytes() for p in d.rglob("*") if p.is_file()} == first
