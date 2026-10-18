---
title: "pylabrobot — AI agent skill for lab automation"
description: "Develop and review PyLabRobot lab-automation resources, liquid-handling plans, offline simulations, and supported-device integrations."
keywords: ["lab automation", "liquid handling", "lab robotics", "protocols"]
---

# `pylabrobot`

**Category:** [lab-automation](/skills#lab-automation) · **License:** MIT · **Version:** 1.3 · **Includes scripts**

**Tags:** lab automation, liquid handling, lab robotics, protocols

## When to use it

Develop and review PyLabRobot lab-automation resources, liquid-handling plans, offline simulations, and supported-device integrations. Use for PyLabRobot protocols or API questions; keep physical execution behind an explicit operator safety gate.

## Example requests

Ask your agent in plain language, for example:

- *"How do I load a 96-well plate onto a Hamilton STAR deck in PyLabRobot?"*
- *"I have a manifest.json for a 96-well serial dilution (200 uL tips, 384-well destination plate) that I want to run on our Hamilton Vantage. Can you check the volumes and write the PyLabRobot script? I'm on Windows 11 with Python 3.11. My earlier script failed with 'ImportError: cannot import name ChatterboxBackend'."*
- *"We want our liquid-handling robot to automatically cherry-pick hits from a source plate into a new assay plate overnight with no one around. Can you set it up so it just starts running as soon as the script is launched?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pylabrobot

# Kalaris Labs installer with checksum verification
npx research-agent-skills install pylabrobot
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `lab-automation` category with `/plugin install lab-automation@research-agent-skills`.

## Related

- [`opentrons-integration`](/skills/opentrons-integration)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pylabrobot/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
