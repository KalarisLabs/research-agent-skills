---
title: Installer CLI reference | Research Agent Skills
description: Command reference for npx research-agent-skills, covering install, list, search, update, uninstall and doctor.
---

The `research-agent-skills` CLI installs skills from a verified release into supported agent directories.
The npm CLI commands below become available after the first package release. Until then,
[install skills with skills.sh](/getting-started/installation). After release, run
`npx research-agent-skills` for interactive selection, or use these commands directly:

| Command | Purpose |
|---|---|
| `install [skill...]` | Install named skills, a bundle, or a category |
| `list --categories` | Show available categories |
| `search <query>` | Find skills by name, description or tags |
| `installed` | Show installed skills and target directories |
| `update` | Reinstall managed skills from the selected release |
| `uninstall [skill...]` | Remove managed skills |
| `doctor` | Check harnesses, dependencies and installed file integrity |

Without selection flags, `install` chooses `research-essentials`. Without `--project`, installation goes
to the selected agent's global user directory. Use `--harness codex` (or a comma-separated list) to target
specific agents. Use `--dry-run` to inspect changes before installing.

```bash
npx research-agent-skills install --bundle ai-research --harness codex --project
npx research-agent-skills install citation-verification --dry-run
```

See the [full CLI README](https://github.com/KalarisLabs/research-agent-skills/blob/main/cli/README.md)
for release and standalone installer details.
