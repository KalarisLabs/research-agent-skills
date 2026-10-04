"""Enrich adapted skills after import so they read as agent SOPs, not tutorials.

Run by tools/import_upstream.py after rebranding and patches (deterministic, idempotent):

  1. unlink_dead_links   relative links to files that do not exist become plain text
  2. split_oversized     SKILL.md over budget: move the largest reference-like sections to references/
  3. add_procedure       category-specific operating procedure (numbered phases, failure table,
                         integrity rules) for skills missing a workflow, verification rules or tables
  4. add_related         "Related skills" handoffs computed from description similarity

Procedures live in third_party/operating-procedures.yaml.
"""

from __future__ import annotations

import re
from pathlib import Path

from common import THIRD_PARTY, Skill, dump_frontmatter, load_yaml, split_frontmatter, write_text

MAX_LINES = 500
PROCEDURE_HEADING = "## Agent operating procedure"
RELATED_HEADING = "## Related skills"
KEEP_SECTIONS = re.compile(r"(when to use|overview|quick ?start|getting started|workflow|core concept|rules|"
                           r"related|operating|best practice|common (issues|pitfalls)|troubleshoot)", re.I)
ESSENTIAL_SECTIONS = re.compile(r"(when to use|quick ?start|workflow|related|operating)", re.I)
LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+)\)")
VERIFY = re.compile(r"\b(verify|official|never (fabricate|invent|guess)|do not (fabricate|invent)|confirm)\b", re.I)
_PROC = load_yaml(THIRD_PARTY / "operating-procedures.yaml")


def _split_fenced(text: str) -> list[tuple[bool, str]]:
    """Split markdown into (in_code, chunk) runs so edits never touch code blocks."""
    parts, buf, in_code = [], [], False
    for line in text.splitlines(keepends=True):
        if line.lstrip().startswith(("```", "~~~")):
            if not in_code:
                if buf:
                    parts.append((False, "".join(buf)))
                buf, in_code = [line], True
            else:
                buf.append(line)
                parts.append((True, "".join(buf)))
                buf, in_code = [], False
            continue
        buf.append(line)
    if buf:
        parts.append((in_code, "".join(buf)))
    return parts


def _is_local(target: str) -> bool:
    return not re.match(r"^(?:[a-z][a-z0-9+.-]*:|#|/|\{|<)", target, re.I)


def unlink_dead_links(skill_dir: Path) -> int:
    """Unlink dead links for *skill_dir* and return int."""
    fixed = 0
    for md in sorted(skill_dir.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        out = []
        for in_code, chunk in _split_fenced(text):
            if in_code:
                out.append(chunk)
                continue

            def repl(m: re.Match, base: Path = md.parent) -> str:
                """Repl for *m*, *base* and return str."""
                nonlocal fixed
                bang, label, target = m.groups()
                path = target.split("#", 1)[0]
                if bang or not path or not _is_local(target) or (base / path).exists():
                    return m.group(0)
                fixed += 1
                return label
            out.append(LINK_RE.sub(repl, chunk))
        new = "".join(out)
        if new != text:
            write_text(md, new)
    return fixed


def _sections(body: str) -> list[tuple[str, int, int]]:
    """Level-2 sections outside code fences: (title, start line, end line) over body lines."""
    lines = body.splitlines()
    heads, in_code = [], False
    for i, line in enumerate(lines):
        if line.lstrip().startswith(("```", "~~~")):
            in_code = not in_code
        elif not in_code and line.startswith("## "):
            heads.append((line[3:].strip(), i))
    return [(t, s, heads[k + 1][1] if k + 1 < len(heads) else len(lines)) for k, (t, s) in enumerate(heads)]


def _slug(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:60] or "section"


def _relink_moved(text: str) -> str:
    """Links in a section moved into references/ must stay valid from their new location."""
    out = []
    for in_code, chunk in _split_fenced(text):
        if not in_code:
            def fix(m: re.Match) -> str:
                bang, label, target = m.groups()
                if not _is_local(target):
                    return m.group(0)
                new = target[len("references/"):] if target.startswith("references/") else f"../{target}"
                return f"{bang}[{label}]({new})"
            chunk = LINK_RE.sub(fix, chunk)
        out.append(chunk)
    return "".join(out)


def split_oversized(skill_dir: Path, budget: int) -> list[str]:
    """Split oversized for *skill_dir*, *budget* and return list[str]."""
    path = skill_dir / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    meta, body = split_frontmatter(text)
    head_lines = len(text.splitlines()) - len(body.splitlines())
    moved: list[str] = []
    while head_lines + len(body.splitlines()) > budget:
        secs = [s for s in _sections(body)[1:] if not KEEP_SECTIONS.search(s[0]) and s[2] - s[1] > 12]
        if not secs:  # fall back to anything except the essentials an agent needs up front
            secs = [s for s in _sections(body)[1:] if not ESSENTIAL_SECTIONS.search(s[0]) and s[2] - s[1] > 8]
        if not secs:
            break
        title, start, end = max(secs, key=lambda s: s[2] - s[1])
        lines = body.splitlines()
        slug = _slug(title)
        ref = skill_dir / "references" / f"{slug}.md"
        n = 2
        while ref.exists():
            ref = skill_dir / "references" / f"{slug}-{n}.md"
            n += 1
        section = "\n".join(lines[start + 1:end]).strip("\n")
        write_text(ref, f"# {title}\n\n{_relink_moved(section)}\n")
        pointer = [f"## {title}", "",
                   f"Details, code examples and parameter tables: [references/{ref.name}](references/{ref.name}). "
                   "Read it when this step applies.", ""]
        body = "\n".join(lines[:start] + pointer + lines[end:]) + "\n"
        moved.append(ref.name)
    if moved:
        write_text(path, dump_frontmatter(meta, body))
    return moved


def procedure_block(category: str) -> str:
    """Procedure block for *category* and return str."""
    c = _PROC["categories"].get(category, {})
    common = _PROC["common"]
    steps = [
        f"1. **Check the environment.** {c.get('check', 'Confirm tool versions and inputs.')}",
        "2. **Pin down the inputs.** Confirm formats, identifiers and parameters from the data or the user. "
        "Ask rather than guess any value that changes the result.",
        f"3. **Run a small version first.** {c.get('small', 'Test on a small input before the full run.')}",
        "4. **Execute the full task** using the instructions and references above.",
        f"5. **Validate the result.** {c.get('validate', 'Check outputs against expectations and references.')}",
        "6. **Report.** State what was run (versions, commands, parameters), what was checked, "
        "and what is still uncertain.",
    ]
    rows = c.get("failures", []) + common["failures"]
    table = ["| If this happens | Do this |", "|---|---|"] + [f"| {a} | {b} |" for a, b in rows]
    rules = [f"- {r}" for r in common["rules"][:1] + c.get("rules", []) + common["rules"][1:]]
    return "\n".join([PROCEDURE_HEADING, "", *steps, "", *table, "", "**Integrity rules**", "", *rules, ""])


def needs_procedure(body: str) -> bool:
    numbered = len(re.findall(r"^\s*\d+[.)] ", body, re.M)) >= 3
    tables = len(re.findall(r"^\|.*\|\s*$", body, re.M)) >= 3 or bool(re.search(r"^\s*[-*] \[[ x]\]", body, re.M))
    return not (numbered and tables and VERIFY.search(body))


def add_procedure(skill: Skill) -> bool:
    """Add procedure for *skill* and return bool."""
    path = skill.path / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    meta, body = split_frontmatter(text)
    if PROCEDURE_HEADING in body or not needs_procedure(body):
        return False
    write_text(path, dump_frontmatter(meta, body.rstrip() + "\n\n" + procedure_block(skill.category)))
    return True


def add_related(skill: Skill, related: list[tuple[str, str]]) -> bool:
    """Add related for *skill*, *related* and return bool."""
    path = skill.path / "SKILL.md"
    meta, body = split_frontmatter(path.read_text(encoding="utf-8"))
    if not related or re.search(r"^#+ .*(related|see also)", body, re.I | re.M):
        return False
    lines = [RELATED_HEADING, ""] + [f"- `{name}`: {desc}" for name, desc in related]
    write_text(path, dump_frontmatter(meta, body.rstrip() + "\n\n" + "\n".join(lines) + "\n"))
    return True


def procedure_lines(category: str) -> int:
    return len(procedure_block(category).splitlines()) + 8  # + related skills block
