"""Shared helpers for repository tooling: paths, frontmatter I/O, skill discovery."""

from __future__ import annotations

import re
import sys
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

for _stream in (sys.stdout, sys.stderr):  # Windows consoles default to cp1252
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
THIRD_PARTY = ROOT / "third_party"

BRAND = "Kalaris Labs"
CREATOR = "Sayan Chowdhury"
OWNER_GITHUB = "saynchowdhury"
DOCS_URL = "https://docs.kalarislabs.com/research-agent-skills"
REPO_SLUG = "KalarisLabs/research-agent-skills"
REPO_URL = f"https://github.com/{REPO_SLUG}"
PROJECT_NAME = "Research Agent Skills"

# Fields allowed at the top level of SKILL.md frontmatter (agentskills.io spec).
SPEC_FIELDS = ("name", "description", "license", "compatibility", "allowed-tools", "metadata")

_FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---[ \t]*\r?\n?", re.S)


class FrontmatterError(ValueError):
    pass


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Return (frontmatter dict, body). Raises FrontmatterError if missing/invalid."""
    text = text.lstrip("﻿")
    m = _FM_RE.match(text)
    if not m:
        raise FrontmatterError("missing YAML frontmatter delimited by '---'")
    try:
        data = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as exc:
        raise FrontmatterError(f"invalid YAML frontmatter: {exc}") from exc
    if not isinstance(data, dict):
        raise FrontmatterError("frontmatter must be a mapping")
    return data, text[m.end():]


def dump_frontmatter(data: dict[str, Any], body: str) -> str:
    ordered = {k: data[k] for k in SPEC_FIELDS if k in data}
    ordered.update({k: v for k, v in data.items() if k not in ordered})
    fm = yaml.safe_dump(ordered, sort_keys=False, allow_unicode=True, width=10_000).strip()
    return f"---\n{fm}\n---\n{body}"


@dataclass
class Skill:
    """Skill."""
    path: Path          # skill directory
    meta: dict[str, Any]
    body: str

    @property
    def name(self) -> str:
        return str(self.meta.get("name", ""))

    @property
    def metadata(self) -> dict[str, Any]:
        md = self.meta.get("metadata")
        return md if isinstance(md, dict) else {}

    @property
    def category(self) -> str:
        return str(self.metadata.get("category", "uncategorized"))


def iter_skill_dirs(root: Path = SKILLS_DIR) -> Iterator[Path]:
    for p in sorted(root.iterdir()) if root.exists() else []:
        if p.is_dir() and (p / "SKILL.md").is_file():
            yield p


def load_skill(skill_dir: Path) -> Skill:
    meta, body = split_frontmatter((skill_dir / "SKILL.md").read_text(encoding="utf-8"))
    return Skill(skill_dir, meta, body)


def load_skills(root: Path = SKILLS_DIR) -> list[Skill]:
    return [load_skill(d) for d in iter_skill_dirs(root)]


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def write_text(path: Path, text: str) -> bool:
    """Write text with LF endings; return True if the file changed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    data = text.encode("utf-8")
    if path.exists() and path.read_bytes() == data:  # compare bytes: read_text() would hide CRLF
        return False
    with path.open("w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return True
