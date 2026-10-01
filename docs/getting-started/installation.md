---
title: Install Research Agent Skills
description: Install research agent skills for Claude Code, Codex, Cursor, Gemini CLI, Copilot, OpenCode and Windsurf with one command, skills.sh, GitHub CLI, the Claude Code marketplace or a checksum-verified shell installer.
---

# Installation

## One command

```bash
npx research-agent-skills            # interactive: pick bundles/categories and agents
npx research-agent-skills install    # non-interactive: research-essentials for detected agents
```

Both commands install into the selected agent's **global user directory** by default. The interactive command
asks which bundles or categories and harnesses to use. Use `--project` for the current repository instead.
The installer has explicit targets for Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot, OpenCode,
Windsurf and generic `.agents/skills` consumers. Other harnesses need to support the Agent Skills folder format;
tool permissions and advanced metadata can differ.

## Choose what to install

```bash
npx research-agent-skills list --categories
npx research-agent-skills search "systematic review"
npx research-agent-skills install citation-verification apa7
npx research-agent-skills install --bundle biology-research --project
npx research-agent-skills install --bundle ml-research --harness codex --project
npx research-agent-skills install --category life-sciences --harness claude-code,codex
npx research-agent-skills install --project          # into ./.claude/skills, ./.agents/skills, ...
npx research-agent-skills install --version 1.0.0    # pin a release
```

Manage installs with `installed`, `update`, `uninstall <skills|--all>` and `doctor`.
The CLI only ever removes skills it installed itself.

The curated `--bundle` choices are `research-essentials`, `ml-research`, `ai-research`,
`biology-research`, `chemistry-research`, `medicine-research` and `physics-research`.
Use individual skill names or `--category` when the bundle is too broad or too narrow.

## Alternatives

| Method | Command |
|---|---|
| skills.sh (Vercel) | `npx skills add KalarisLabs/research-agent-skills --list`, then `npx skills add KalarisLabs/research-agent-skills --skill citation-verification` |
| GitHub CLI | `gh skill install KalarisLabs/research-agent-skills [skill]` |
| Claude Code | `/plugin marketplace add KalarisLabs/research-agent-skills` → `/plugin install research-essentials@research-agent-skills` |
| No Node.js (macOS/Linux) | `curl -fsSL https://raw.githubusercontent.com/KalarisLabs/research-agent-skills/main/install.sh \| sh` |
| No Node.js (Windows) | `irm https://raw.githubusercontent.com/KalarisLabs/research-agent-skills/main/install.ps1 \| iex` |

Installer options via environment variables: `RAS_VERSION`, `RAS_BUNDLE` (bundle or category, or `all`), `RAS_HARNESS`.
The standalone installers also default to global user directories. Vercel's skills CLI has its own
scope prompts and flags; review its choice before installing.

## skills.sh discovery

The public repository's `skills/<name>/SKILL.md` folders are discoverable by the Vercel skills CLI.
There is no repository setting that submits this collection to the directory. Once the complete repository
is published, run `npx skills add KalarisLabs/research-agent-skills --list` to check discovery, then
install a skill through that CLI. [Browse the live directory listing](https://skills.sh/kalarislabs/research-agent-skills).
The directory's rankings use the CLI's anonymous install telemetry.

## Python for skill scripts

Skills with a `scripts/` folder run Python 3.9+ (many are standard-library only). For skills with
dependencies, install [uv](https://docs.astral.sh/uv/). `npx research-agent-skills doctor` checks your setup.
