"""Validate skills against the Agent Skills spec and repository policy.

Usage:
    uv run tools/validate.py                 # all skills
    uv run tools/validate.py skills/foo ...  # specific skills
    uv run tools/validate.py --strict        # warnings fail too

Exit code 1 if any error (or any warning with --strict).
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (  # noqa: E402
    ROOT,
    SKILLS_DIR,
    SPEC_FIELDS,
    THIRD_PARTY,
    FrontmatterError,
    load_yaml,
    split_frontmatter,
)

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_NAME, MAX_DESC, MAX_COMPAT, MAX_LINES = 64, 1024, 500, 500
MAX_FILE_BYTES = 2 * 1024 * 1024
MAX_SKILL_BYTES = 15 * 1024 * 1024
STRUCTURED_METADATA_KEYS = {"openclaw"}  # harness-specific nested metadata
TEXT_EXT = {
    ".md", ".txt", ".py", ".json", ".yaml", ".yml", ".toml", ".csv", ".tsv", ".tex", ".sty", ".cls",
    ".bst", ".bib", ".sh", ".js", ".mjs", ".ts", ".html", ".css", ".r", ".jl", ".sql", ".ipynb",
    ".mplstyle", ".cfg", ".ini", ".xml", ".xsd", ".svg",
}
BINARY_EXT = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".webp"}
EXTENSIONLESS_OK = {"LICENSE", "Makefile", ".gitignore", "NOTICE"}
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
GENERIC_USERS = (r"(?:user|username|you|your_?username|me|name|runner|ubuntu|ec2-user|root|jovyan|"
                 r"dnanexus|unsloth)\b")
ABS_PATH_RE = re.compile(rf"(?<![\w/.])(?:[A-Za-z]:\\Users\\(?!{GENERIC_USERS})[^\\\s]+|"
                         rf"/home/(?!{GENERIC_USERS})[a-z][\w-]+/|/Users/(?!{GENERIC_USERS})[A-Za-z][\w-]+/)", re.I)
CODE_RE = re.compile(r"```.*?```|~~~.*?~~~|`[^`\n]*`", re.S)


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def err(self, skill: str, msg: str) -> None:
        self.errors.append(f"{skill}: {msg}")

    def warn(self, skill: str, msg: str) -> None:
        self.warnings.append(f"{skill}: {msg}")


def load_categories() -> set[str]:
    return set(load_yaml(THIRD_PARTY / "categories.yaml")["categories"])


def load_size_baseline() -> set[str]:
    path = ROOT / "tools" / "size_baseline.txt"
    if not path.exists():
        return set()
    return {ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip() and not ln.startswith("#")}


def check_frontmatter(skill_dir: Path, meta: dict, rep: Report, categories: set[str]) -> None:
    sid = skill_dir.name
    name = meta.get("name")
    if not isinstance(name, str) or not name:
        rep.err(sid, "frontmatter 'name' is required")
    else:
        if not NAME_RE.match(name):
            rep.err(sid, f"name '{name}' must be lowercase kebab-case (a-z, 0-9, single hyphens)")
        if len(name) > MAX_NAME:
            rep.err(sid, f"name exceeds {MAX_NAME} characters")
        if name != skill_dir.name:
            rep.err(sid, f"name '{name}' must match folder name '{skill_dir.name}'")

    desc = meta.get("description")
    if not isinstance(desc, str) or not desc.strip():
        rep.err(sid, "frontmatter 'description' is required")
    elif len(desc) > MAX_DESC:
        rep.err(sid, f"description is {len(desc)} chars (max {MAX_DESC})")
    elif re.search(r"[<>]", desc):
        rep.warn(sid, "description contains angle brackets, which some harnesses reject")

    for key in meta:
        if key not in SPEC_FIELDS:
            rep.err(sid, f"non-spec top-level field '{key}' (move it under metadata)")

    compat = meta.get("compatibility")
    if compat is not None and (not isinstance(compat, str) or len(compat) > MAX_COMPAT):
        rep.err(sid, f"compatibility must be a string of at most {MAX_COMPAT} chars")
    tools = meta.get("allowed-tools")
    if tools is not None and not isinstance(tools, str):
        rep.err(sid, "allowed-tools must be a space-separated string")
    if meta.get("license") is not None and not isinstance(meta["license"], str):
        rep.err(sid, "license must be a string")

    md = meta.get("metadata")
    if not isinstance(md, dict):
        rep.err(sid, "metadata mapping is required (version, category, maintainer)")
        return
    for key, value in md.items():
        if key in STRUCTURED_METADATA_KEYS:
            continue
        if not isinstance(value, str):
            rep.err(sid, f"metadata.{key} must be a string (quote numbers)")
    if md.get("category") not in categories:
        rep.err(sid, f"metadata.category '{md.get('category')}' is not defined in third_party/categories.yaml")
    for required in ("version", "maintainer"):
        if not md.get(required):
            rep.err(sid, f"metadata.{required} is required")


def check_files(skill_dir: Path, rep: Report) -> None:
    sid, total = skill_dir.name, 0
    for path in sorted(skill_dir.rglob("*")):
        rel = path.relative_to(skill_dir).as_posix()
        if "__pycache__" in path.parts:  # local bytecode, git-ignored, never shipped
            continue
        if path.is_symlink():
            rep.err(sid, f"{rel}: symlinks are not allowed")
            continue
        if not path.is_file():
            continue
        size = path.stat().st_size
        total += size
        if size > MAX_FILE_BYTES:
            rep.err(sid, f"{rel}: {size // 1024} KiB exceeds per-file limit of {MAX_FILE_BYTES // 1024} KiB")
        ext = path.suffix.lower()
        if ext in BINARY_EXT:
            continue
        if ext not in TEXT_EXT and path.name not in EXTENSIONLESS_OK:
            rep.err(sid, f"{rel}: file type '{ext or path.name}' is not allowed (see CONTRIBUTING.md)")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            rep.err(sid, f"{rel}: text files must be UTF-8")
            continue
        m = ABS_PATH_RE.search(text)
        if m:
            rep.warn(sid, f"{rel}: machine-specific absolute path '{m.group(0)}'")
        if ext == ".md":
            for target in LINK_RE.findall(CODE_RE.sub("", text)):
                # skip URLs, anchors, site-root-relative links and templated placeholders
                if re.match(r"^(?:[a-z][a-z0-9+.-]*:|#|/)", target, re.I) or "{" in target or "<" in target:
                    continue
                target_path = target.split("#", 1)[0]
                if not target_path:
                    continue
                resolved = (path.parent / target_path).resolve()
                if not resolved.is_relative_to(skill_dir.parent.resolve()):
                    rep.err(sid, f"{rel}: link '{target}' escapes the skills directory")
                elif not resolved.exists():
                    rep.warn(sid, f"{rel}: broken relative link '{target}'")
                elif not resolved.is_relative_to(skill_dir.resolve()):
                    rep.warn(sid, f"{rel}: cross-skill link '{target}' breaks when installed on its own")
    if total > MAX_SKILL_BYTES:
        rep.err(sid, f"skill folder is {total // 1024 // 1024} MiB (max {MAX_SKILL_BYTES // 1024 // 1024} MiB)")


def validate_skill(skill_dir: Path, rep: Report, categories: set[str], baseline: set[str]) -> None:
    sid = skill_dir.name
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        rep.err(sid, "missing SKILL.md")
        return
    text = skill_md.read_text(encoding="utf-8")
    try:
        meta, body = split_frontmatter(text)
    except FrontmatterError as exc:
        rep.err(sid, str(exc))
        return
    check_frontmatter(skill_dir, meta, rep, categories)
    lines = len(text.splitlines())
    if lines > MAX_LINES:
        msg = f"SKILL.md has {lines} lines (budget {MAX_LINES}); move detail into references/"
        (rep.warn if sid in baseline else rep.err)(sid, msg)
    if not body.strip():
        rep.err(sid, "SKILL.md body is empty")
    check_files(skill_dir, rep)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*", type=Path, help="skill directories (default: all)")
    ap.add_argument("--strict", action="store_true", help="treat warnings as errors")
    ap.add_argument("--quiet", action="store_true", help="only print the summary and errors")
    args = ap.parse_args(argv)

    dirs = [p.resolve() for p in args.paths] or sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    rep, categories, baseline = Report(), load_categories(), load_size_baseline()
    for d in dirs:
        validate_skill(d, rep, categories, baseline)

    for e in rep.errors:
        print(f"ERROR   {e}")
    if not args.quiet:
        for w in rep.warnings:
            print(f"WARNING {w}")
    print(f"\n{len(dirs)} skills checked: {len(rep.errors)} errors, {len(rep.warnings)} warnings")
    return 1 if rep.errors or (args.strict and rep.warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
