from __future__ import annotations

import textwrap
from pathlib import Path

import pytest


def write_skill(root: Path, name: str, frontmatter: str | None = None, body: str = "# Title\n\nBody text.\n",
                files: dict[str, str | bytes] | None = None) -> Path:
    """Create skills/<name>/SKILL.md (+ extra files) under root and return the skill dir."""
    d = root / name
    d.mkdir(parents=True)
    if frontmatter is None:
        frontmatter = textwrap.dedent(f"""\
            name: {name}
            description: Does a thing. Use when testing the validator.
            license: MIT
            metadata:
              version: "1.0"
              category: research-writing
              maintainer: Kalaris Labs
            """)
    (d / "SKILL.md").write_bytes(f"---\n{frontmatter}---\n{body}".encode())  # no newline translation
    for rel, content in (files or {}).items():
        p = d / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(content, bytes):
            p.write_bytes(content)
        else:
            p.write_bytes(content.encode())
    return d


@pytest.fixture
def skills_root(tmp_path: Path) -> Path:
    root = tmp_path / "skills"
    root.mkdir()
    return root
