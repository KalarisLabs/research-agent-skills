"""Agent harness detection and skills directory resolution across scientific, control plane, and coding environments."""

from __future__ import annotations

import os
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

HarnessCategory = Literal["science", "control-plane", "coding-ide", "cli-agent", "generic"]


@dataclass
class Harness:
    id: str
    label: str
    global_dir: Path
    project_dir: str
    category: HarnessCategory = "generic"
    detect_paths: list[Path] = field(default_factory=list)
    detect_bins: list[str] = field(default_factory=list)

    def is_present(self) -> bool:
        if any(p.exists() for p in self.detect_paths):
            return True
        if any(shutil.which(b) is not None for b in self.detect_bins):
            return True
        return False


def get_harnesses(home: Path | None = None) -> list[Harness]:
    h = home or Path.home()
    local_app_data = Path(os.environ["LOCALAPPDATA"]) if "LOCALAPPDATA" in os.environ else None
    app_data = Path(os.environ["APPDATA"]) if "APPDATA" in os.environ else None

    return [
        # --- Scientific Research Workbenches ---
        Harness(
            id="claude-science",
            label="Claude Science",
            category="science",
            global_dir=h / ".claude-science" / "skills",
            project_dir=".claude-science/skills",
            detect_paths=[
                h / ".claude-science",
                h / ".config" / "claude-science",
                Path("/Applications/Claude Science.app"),
                h / "Library" / "Application Support" / "Claude Science",
                *( [local_app_data / "ClaudeScience"] if local_app_data else [] ),
            ],
            detect_bins=["claude-science"],
        ),
        Harness(
            id="openscience",
            label="Open Science (openscience.sh)",
            category="science",
            global_dir=h / ".openscience" / "skills",
            project_dir=".openscience/skills",
            detect_paths=[h / ".openscience", h / ".synsci"],
            detect_bins=["openscience", "synsci"],
        ),

        # --- Control Planes & Multi-Agent Surfaces ---
        Harness(
            id="t3-code",
            label="T3 Code",
            category="control-plane",
            global_dir=h / ".t3" / "skills",
            project_dir=".t3/skills",
            detect_paths=[
                h / ".t3",
                h / ".config" / "t3",
                *( [app_data / "T3Code"] if app_data else [] ),
            ],
            detect_bins=["t3", "t3code", "t3-code"],
        ),
        Harness(
            id="antigravity",
            label="Google Antigravity",
            category="coding-ide",
            global_dir=h / ".gemini" / "config" / "skills",
            project_dir=".gemini/config/skills",
            detect_paths=[h / ".gemini" / "antigravity", h / ".gemini" / "config", h / ".gemini"],
            detect_bins=["agy", "antigravity"],
        ),
        Harness(
            id="hermes",
            label="Nous Hermes Agent",
            category="cli-agent",
            global_dir=h / ".hermes" / "skills",
            project_dir=".hermes/skills",
            detect_paths=[h / ".hermes", h / ".config" / "hermes"],
            detect_bins=["hermes"],
        ),

        # --- Developer & CLI Agent Harnesses ---
        Harness(
            id="claude-code",
            label="Claude Code",
            category="cli-agent",
            global_dir=h / ".claude" / "skills",
            project_dir=".claude/skills",
            detect_paths=[h / ".claude"],
            detect_bins=["claude"],
        ),
        Harness(
            id="codex",
            label="OpenAI Codex",
            category="cli-agent",
            global_dir=h / ".codex" / "skills",
            project_dir=".agents/skills",
            detect_paths=[h / ".codex"],
            detect_bins=["codex"],
        ),
        Harness(
            id="cursor",
            label="Cursor",
            category="coding-ide",
            global_dir=h / ".cursor" / "skills",
            project_dir=".agents/skills",
            detect_paths=[h / ".cursor"],
            detect_bins=["cursor", "cursor-agent"],
        ),
        Harness(
            id="gemini-cli",
            label="Gemini CLI",
            category="cli-agent",
            global_dir=h / ".gemini" / "skills",
            project_dir=".agents/skills",
            detect_paths=[h / ".gemini"],
            detect_bins=["gemini"],
        ),
        Harness(
            id="copilot",
            label="GitHub Copilot",
            category="coding-ide",
            global_dir=h / ".copilot" / "skills",
            project_dir=".agents/skills",
            detect_paths=[h / ".copilot"],
            detect_bins=["copilot"],
        ),
        Harness(
            id="openhands",
            label="OpenHands (OpenDevin)",
            category="cli-agent",
            global_dir=h / ".openhands" / "skills",
            project_dir=".openhands/microagents",
            detect_paths=[h / ".openhands"],
            detect_bins=["openhands"],
        ),
        Harness(
            id="goose",
            label="Goose",
            category="cli-agent",
            global_dir=h / ".config" / "goose" / "skills",
            project_dir=".goose/skills",
            detect_paths=[h / ".config" / "goose", h / ".goose"],
            detect_bins=["goose"],
        ),
        Harness(
            id="aider",
            label="Aider",
            category="cli-agent",
            global_dir=h / ".aider" / "skills",
            project_dir=".aider/skills",
            detect_paths=[h / ".aider"],
            detect_bins=["aider"],
        ),
        Harness(
            id="opencode",
            label="OpenCode",
            category="cli-agent",
            global_dir=h / ".config" / "opencode" / "skills",
            project_dir=".agents/skills",
            detect_paths=[h / ".config" / "opencode"],
            detect_bins=["opencode"],
        ),
        Harness(
            id="windsurf",
            label="Windsurf",
            category="coding-ide",
            global_dir=h / ".codeium" / "windsurf" / "skills",
            project_dir=".windsurf/skills",
            detect_paths=[h / ".codeium" / "windsurf"],
            detect_bins=["windsurf"],
        ),
        Harness(
            id="roo-code",
            label="Roo Code / Cline",
            category="coding-ide",
            global_dir=h / ".roo" / "skills",
            project_dir=".roo/skills",
            detect_paths=[h / ".roo", h / ".cline"],
            detect_bins=["roo", "cline"],
        ),
        Harness(
            id="zed",
            label="Zed Assistant",
            category="coding-ide",
            global_dir=h / ".config" / "zed" / "skills",
            project_dir=".zed/prompts",
            detect_paths=[h / ".config" / "zed"],
            detect_bins=["zed"],
        ),
        Harness(
            id="trae",
            label="Trae",
            category="coding-ide",
            global_dir=h / ".trae" / "skills",
            project_dir=".trae/rules",
            detect_paths=[h / ".trae"],
            detect_bins=["trae"],
        ),
        Harness(
            id="continue",
            label="Continue.dev",
            category="coding-ide",
            global_dir=h / ".continue" / "skills",
            project_dir=".continue/prompts",
            detect_paths=[h / ".continue"],
            detect_bins=["continue"],
        ),
        Harness(
            id="agents",
            label="Generic (.agents/skills: Cline, Amp, Goose, Roo)",
            category="generic",
            global_dir=h / ".agents" / "skills",
            project_dir=".agents/skills",
            detect_paths=[h / ".agents"],
            detect_bins=[],
        ),
    ]


def detect_harnesses(all_harnesses: list[Harness] | None = None) -> list[Harness]:
    all_h = all_harnesses or get_harnesses()
    return [h for h in all_h if h.id != "agents" and h.is_present()]


def resolve_harnesses(spec: str | None, all_harnesses: list[Harness] | None = None) -> list[Harness]:
    all_h = all_harnesses or get_harnesses()
    if not spec or spec == "auto":
        found = detect_harnesses(all_h)
        if found:
            return found
        # Fallback to claude-code or generic agents
        return [h for h in all_h if h.id in ("claude-code", "agents")]
    if spec == "all":
        return all_h

    chosen: list[Harness] = []
    by_id = {h.id: h for h in all_h}
    for item in spec.split(","):
        clean_id = item.strip().lower()
        if clean_id not in by_id:
            known = ", ".join(by_id.keys())
            raise ValueError(f"unknown harness '{clean_id}'. Known: {known}")
        chosen.append(by_id[clean_id])
    return chosen
