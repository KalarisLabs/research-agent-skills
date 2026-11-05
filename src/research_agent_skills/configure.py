"""Auto-configuration engine for agent harness instruction anchors and manifests."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from .catalog import SkillEntry
from .harness import Harness

START_TAG = "<!-- research-agent-skills:start -->"
END_TAG = "<!-- research-agent-skills:end -->"


@dataclass
class ConfigureResult:
    file: str
    action: Literal["created", "updated", "unchanged"]
    harness: str


def update_tagged_section(
    content: str,
    section: str,
    start_tag: str = START_TAG,
    end_tag: str = END_TAG,
) -> str:
    """Replace or append a tagged block in a file without disturbing user content outside the tags."""
    block = f"{start_tag}\n{section.strip()}\n{end_tag}"
    start = content.find(start_tag)
    end = content.find(end_tag)
    if start != -1 and end != -1 and end >= start:
        return content[:start] + block + content[end + len(end_tag):]
    return f"{content.strip()}\n\n{block}\n" if content.strip() else f"{block}\n"


def _write_or_update(file_path: Path, new_content: str) -> Literal["created", "updated", "unchanged"]:
    file_path.parent.mkdir(parents=True, exist_ok=True)
    if not file_path.exists():
        file_path.write_text(new_content, encoding="utf-8")
        return "created"
    existing = file_path.read_text(encoding="utf-8")
    if existing == new_content:
        return "unchanged"
    file_path.write_text(new_content, encoding="utf-8")
    return "updated"


def _update_markdown_anchor(
    file_path: Path,
    header: str,
    target_dir: str,
    skills: list[SkillEntry] | None = None,
) -> Literal["created", "updated", "unchanged"]:
    file_path.parent.mkdir(parents=True, exist_ok=True)
    existing = file_path.read_text(encoding="utf-8") if file_path.exists() else ""
    skill_list = ""
    if skills:
        sample = skills[:15]
        items = "\n".join(f"- `{s.name}`: {s.description[:80]}" for s in sample)
        more = f"\n... and {len(skills) - 15} more." if len(skills) > 15 else ""
        skill_list = f"\nKey installed skills ({len(skills)} total):\n{items}{more}"

    section = (
        f"## {header}\n"
        f"Domain scientific research skills are available in `{target_dir}`.\n"
        "Consult the corresponding `SKILL.md` before generating code, "
        f"running simulations, or querying scientific APIs.{skill_list}"
    )

    updated = update_tagged_section(existing, section)
    if existing == updated:
        return "unchanged"
    file_path.write_text(updated, encoding="utf-8")
    return "updated" if existing else "created"


def configure_harness(
    harness: Harness,
    cwd: Path | None = None,
    skills: list[SkillEntry] | None = None,
) -> list[ConfigureResult]:
    root = cwd or Path.cwd()
    results: list[ConfigureResult] = []

    if harness.id == "claude-code":
        claude_md = root / "CLAUDE.md"
        action = _update_markdown_anchor(claude_md, "Research Agent Skills", harness.project_dir, skills)
        results.append(ConfigureResult(file="CLAUDE.md", action=action, harness=harness.id))

    elif harness.id == "claude-science":
        claude_md = root / "CLAUDE.md"
        a1 = _update_markdown_anchor(claude_md, "Claude Science Research Skills", harness.project_dir, skills)
        results.append(ConfigureResult(file="CLAUDE.md", action=a1, harness=harness.id))

        spec_file = root / ".claude-science" / "specialists.json"
        if not spec_file.exists():
            spec_config = {
                "$schema": "https://claude.ai/schemas/science-specialists.json",
                "version": "1.0",
                "specialists": {
                    "genomics": {"skillsRoot": harness.project_dir, "categories": ["genetics", "biology-research"]},
                    "cheminformatics": {"skillsRoot": harness.project_dir, "categories": ["chemistry-research"]},
                    "literature": {
                        "skillsRoot": harness.project_dir,
                        "categories": ["literature-review", "research-writing"],
                    },
                },
            }
            action = _write_or_update(spec_file, json.dumps(spec_config, indent=2) + "\n")
            results.append(ConfigureResult(file=".claude-science/specialists.json", action=action, harness=harness.id))

    elif harness.id == "openscience":
        file = root / ".openscience" / "skills.json"
        config = {
            "skillsDirectory": harness.project_dir,
            "catalogVersion": "1.1.0",
            "skills": [s.name for s in skills] if skills else [],
        }
        action = _write_or_update(file, json.dumps(config, indent=2) + "\n")
        results.append(ConfigureResult(file=".openscience/skills.json", action=action, harness=harness.id))

    elif harness.id == "t3-code":
        file = root / ".t3" / "config.json"
        if not file.exists():
            config = {
                "$schema": "https://t3.chat/schema/harness.json",
                "name": "Scientific Research Workspace",
                "skillsRoot": harness.project_dir,
                "worktreeSync": True,
                "reverseMcp": {"enabled": True, "skillsDir": harness.project_dir},
            }
            action = _write_or_update(file, json.dumps(config, indent=2) + "\n")
            results.append(ConfigureResult(file=".t3/config.json", action=action, harness=harness.id))

    elif harness.id == "aider":
        file = root / "CONVENTIONS.md"
        action = _update_markdown_anchor(file, "Research Conventions & Skills", harness.project_dir, skills)
        results.append(ConfigureResult(file="CONVENTIONS.md", action=action, harness=harness.id))

    elif harness.id == "cursor":
        file = root / ".cursorrules"
        action = _update_markdown_anchor(file, "Research Agent Skills", harness.project_dir, skills)
        results.append(ConfigureResult(file=".cursorrules", action=action, harness=harness.id))

    elif harness.id == "windsurf":
        file = root / ".windsurfrules"
        action = _update_markdown_anchor(file, "Research Agent Skills", harness.project_dir, skills)
        results.append(ConfigureResult(file=".windsurfrules", action=action, harness=harness.id))

    elif harness.id == "openhands":
        file = root / ".openhands" / "microagents" / "repo.md"
        action = _update_markdown_anchor(file, "OpenHands Scientific Microagent Skills", harness.project_dir, skills)
        results.append(ConfigureResult(file=".openhands/microagents/repo.md", action=action, harness=harness.id))

    elif harness.id == "roo-code":
        file = root / ".roomodes"
        if not file.exists():
            config = {
                "customModes": [
                    {
                        "slug": "scientist",
                        "name": "Research Scientist",
                        "roleDefinition": (
                            "You are a scientific research agent with access to domain-specific research skills."
                        ),
                        "groups": ["read", "edit", "command"],
                        "customInstructions": (
                            f"Consult skills under {harness.project_dir} before writing code or running experiments."
                        ),
                    }
                ]
            }
            action = _write_or_update(file, json.dumps(config, indent=2) + "\n")
            results.append(ConfigureResult(file=".roomodes", action=action, harness=harness.id))

    elif harness.id == "goose":
        file = root / ".goosehints"
        action = _update_markdown_anchor(file, "Goose Research Hints", harness.project_dir, skills)
        results.append(ConfigureResult(file=".goosehints", action=action, harness=harness.id))

    else:
        # Default for codex, copilot, gemini-cli, antigravity, opencode, hermes, zed, trae, continue, agents
        file = root / "AGENTS.md"
        action = _update_markdown_anchor(file, "Research Agent Skills", harness.project_dir, skills)
        results.append(ConfigureResult(file="AGENTS.md", action=action, harness=harness.id))

    return results


def auto_configure_all(
    harnesses: list[Harness],
    cwd: Path | None = None,
    skills: list[SkillEntry] | None = None,
) -> list[ConfigureResult]:
    results: list[ConfigureResult] = []
    handled_files: set[str] = set()

    for h in harnesses:
        for r in configure_harness(h, cwd, skills):
            key = f"{r.harness}:{r.file}"
            if key not in handled_files:
                handled_files.add(key)
                results.append(r)
    return results
