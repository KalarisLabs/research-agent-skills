"""Normalize an imported skill directory to repository conventions.

Applied by tools/import_upstream.py after copying a skill. Every transform is
idempotent so the importer can be re-run against new upstream revisions.
Rules (phrases, sections, patterns) live in third_party/rebrand-rules.yaml.

Transforms:
  * frontmatter -> agentskills.io spec (non-spec top-level keys move to metadata,
    metadata values coerced to strings, name == folder, maintainer/category set)
  * upstream promotional sections and self-citation instructions removed
  * upstream product names / identifiers replaced with this project's
  * Windows console safety for Python scripts that print non-ASCII text
  * known mechanical defects (e.g. doubled `uv uv pip`)
"""

from __future__ import annotations

import ast
import re
from pathlib import Path
from typing import Any

from common import (
    BRAND,
    REPO_SLUG,
    REPO_URL,
    SPEC_FIELDS,
    THIRD_PARTY,
    dump_frontmatter,
    load_yaml,
    split_frontmatter,
    write_text,
)

TEXT_SUFFIXES = {
    ".md", ".txt", ".py", ".json", ".yaml", ".yml", ".toml", ".cfg", ".ini", ".sh", ".bash",
    ".ps1", ".js", ".mjs", ".ts", ".r", ".R", ".tex", ".bib", ".sty", ".cls", ".csv", ".html",
    ".ipynb", ".sql", ".jl", ".m", ".bst", ".xml", ".xsd", ".svg", ".mplstyle", ".tsv", ".css", ".gitignore",
}

TEXT_NAMES = {"LICENSE", "NOTICE", "Makefile", ".gitignore"}

_RULES = load_yaml(THIRD_PARTY / "rebrand-rules.yaml")
_SUBST = {"{BRAND}": BRAND, "{REPO_SLUG}": REPO_SLUG, "{REPO_URL}": REPO_URL}


def _expand(value: str) -> str:
    for key, sub in _SUBST.items():
        value = value.replace(key, sub)
    return value


PROMO_SECTION_HEADINGS: tuple[str, ...] = tuple(_RULES["promo_sections"])
DROP_LINES = [re.compile(p, re.M) for p in _RULES.get("drop_line_regexes", [])]
STRIP = [re.compile(p) for p in _RULES.get("strip_regexes", [])]
_OVR_PATH = THIRD_PARTY / "description-overrides.yaml"
DESCRIPTION_OVERRIDES: dict[str, str] = (
    (load_yaml(_OVR_PATH) or {}).get("descriptions", {}) if _OVR_PATH.exists() else {})
REPLACEMENTS: list[tuple[str, str]] = [(old, _expand(new)) for old, new in _RULES["replacements"]]
# Vendor-level authorship (upstream orgs, or already rewritten to BRAND) becomes `maintainer`;
# individual community contributors are preserved as `contributor`.
UPSTREAM_AUTHOR_RE = re.compile(_RULES["upstream_author_regex"] + "|" + re.escape(BRAND), re.I)
UV_DOUBLE_RE = re.compile(r"\buv uv pip\b")
HEADING_RE = re.compile(r"^(#{1,6}) +(.+?)[ \t]*$", re.M)
# Zero-width / bidi control characters (scraped-web artifacts; also an injection vector).
# U+200D (ZWJ) is kept because emoji sequences depend on it.
INVISIBLE_RE = re.compile("[​‌‎‏‪-‮⁠-⁤⁦-⁩]")
UTF8_MARKER = "# research-agent-skills: utf-8 console output"
UTF8_SNIPPET = (
    f"{UTF8_MARKER}\n"
    "import sys as _ras_sys\n"
    "for _ras_stream in (_ras_sys.stdout, _ras_sys.stderr):\n"
    '    if hasattr(_ras_stream, "reconfigure"):\n'
    '        _ras_stream.reconfigure(encoding="utf-8", errors="replace")\n'
)


def strip_sections(text: str, headings: tuple[str, ...]) -> str:
    """Remove markdown sections: the heading through the next heading of the same or higher level."""
    changed = True
    while changed:
        changed = False
        matches = list(HEADING_RE.finditer(text))
        for i, m in enumerate(matches):
            if m.group(2) not in headings:
                continue
            level = len(m.group(1))
            end = next((n.start() for n in matches[i + 1:] if len(n.group(1)) <= level), len(text))
            text = text[:m.start()] + text[end:]
            changed = True
            break
    return text.rstrip() + "\n" if text.strip() else text


def strip_marketing(text: str) -> str:
    """Drop whole marketing lines (star counts, user numbers) and strip inline star counts."""
    kept = [ln for ln in text.splitlines(keepends=True) if not any(rx.match(ln.rstrip("\r\n")) for rx in DROP_LINES)]
    text = "".join(kept)
    for rx in STRIP:
        text = rx.sub("", text)
    return text


def rewrite_text(text: str) -> str:
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    text = INVISIBLE_RE.sub("", text)
    return UV_DOUBLE_RE.sub("uv pip", text)


def _stringify(value: Any) -> Any:
    if isinstance(value, dict):
        return value  # structured harness metadata (e.g. `openclaw`) is kept as-is
    if isinstance(value, (list, tuple)):
        return ", ".join(str(v) for v in value)
    if value is None:
        return ""
    return str(value)


def normalize_frontmatter(meta: dict[str, Any], name: str, category: str) -> dict[str, Any]:
    meta = dict(meta)
    md: dict[str, Any] = dict(meta.get("metadata") or {})

    # Hoist non-spec top-level keys into metadata.
    for key in list(meta):
        if key in SPEC_FIELDS:
            continue
        value = meta.pop(key)
        if key == "author":
            if not UPSTREAM_AUTHOR_RE.search(str(value)):
                md.setdefault("contributor", value)
            continue
        md.setdefault(key, value)

    # Replace upstream-vendor authorship keys with maintainer; keep individual contributors.
    for key in ("skill-author", "adapted-by"):
        if key in md:
            value = str(md.pop(key))
            if key == "skill-author" and not UPSTREAM_AUTHOR_RE.search(value):
                md.setdefault("contributor", value)

    md["version"] = str(md.get("version") or "1.0")
    md["maintainer"] = BRAND
    md["category"] = category
    md = {k: _stringify(v) for k, v in md.items()}
    ordered = {k: md.pop(k) for k in ("version", "category", "maintainer") if k in md}
    ordered.update(md)

    lic = meta.get("license")
    if lic is None or str(lic).strip().lower() in ("mit", "mit license"):
        meta["license"] = "MIT"
    meta["name"] = name
    if name in DESCRIPTION_OVERRIDES:
        meta["description"] = DESCRIPTION_OVERRIDES[name]
    if isinstance(meta.get("allowed-tools"), list):
        meta["allowed-tools"] = " ".join(meta["allowed-tools"])
    meta["metadata"] = ordered
    return meta


def _utf8_insert_line(source: str) -> int | None:
    """Line index after module docstring and __future__ imports, or None if unparseable."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None
    insert_after = 0
    for i, node in enumerate(tree.body):
        is_doc = (i == 0 and isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant)
                  and isinstance(node.value.value, str))
        is_future = isinstance(node, ast.ImportFrom) and node.module == "__future__"
        if is_doc or is_future:
            insert_after = node.end_lineno or node.lineno
        else:
            break
    if insert_after == 0:
        lines = source.splitlines()
        # keep shebang / encoding cookie at the top
        while insert_after < len(lines) and (lines[insert_after].startswith("#!") or
                                             re.match(r"#.*coding[:=]", lines[insert_after])):
            insert_after += 1
    return insert_after


def ensure_utf8_console(source: str) -> str:
    """Make scripts that print non-ASCII text safe on Windows cp1252 consoles."""
    if UTF8_MARKER in source or "print(" not in source or source.isascii():
        return source
    idx = _utf8_insert_line(source)
    if idx is None:
        return source
    lines = source.splitlines(keepends=True)
    prefix = "".join(lines[:idx])
    if prefix and not prefix.endswith("\n"):
        prefix += "\n"
    return prefix + UTF8_SNIPPET + "".join(lines[idx:])


def rebrand_skill(skill_dir: Path, name: str, category: str) -> None:
    for path in sorted(skill_dir.rglob("*")):
        if not path.is_file() or (path.suffix not in TEXT_SUFFIXES and path.name not in TEXT_NAMES):
            continue
        try:
            text = path.read_bytes().decode("utf-8")  # no newline translation: CRLF is normalized below
        except UnicodeDecodeError:
            continue
        new = text.replace("\r\n", "\n")
        if path.suffix == ".md":
            new = strip_sections(new, PROMO_SECTION_HEADINGS)
            new = strip_marketing(new)
        new = rewrite_text(new)
        if path.suffix == ".py" and "scripts" in path.relative_to(skill_dir).parts:
            new = ensure_utf8_console(new)
        if path.name == "SKILL.md" and path.parent == skill_dir:
            meta, body = split_frontmatter(new)
            new = dump_frontmatter(normalize_frontmatter(meta, name, category), body)
        if new != text:
            write_text(path, new)
