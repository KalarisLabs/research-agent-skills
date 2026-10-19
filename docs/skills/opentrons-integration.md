---
title: "opentrons-integration — AI agent skill for lab automation"
description: "Author, review, migrate, simulate, and troubleshoot official Opentrons Python Protocol API v2 protocols for Flex and OT-2 robots."
keywords: ["Opentrons", "liquid handling", "lab robotics", "lab automation", "protocols"]
---

# `opentrons-integration`

**Category:** [lab-automation](/skills#lab-automation) · **License:** MIT · **Version:** 2.1 · **Includes scripts**

**Tags:** Opentrons, liquid handling, lab robotics, lab automation, protocols

## When to use it

Author, review, migrate, simulate, and troubleshoot official Opentrons Python Protocol API v2 protocols for Flex and OT-2 robots. Use for robot-specific liquid handling, deck and labware setup, pipettes, modules, runtime parameters, liquid classes, and Opentrons App analysis. Use pylabrobot instead when one workflow must support multiple robot vendors.

## Example requests

Ask your agent in plain language, for example:

- *"Can you write me an Opentrons Flex protocol to transfer 50 µL from a 96-well plate to another plate with a p1000 single channel?"*
- *"My OT-2 protocol fails in the Opentrons App with 'apiLevel 2.29 not supported' after I added `requirements = {"robotType": "OT-2", "apiLevel": "2.29"}`. It's in ot2_pcr_prep.py and also calls protocol.load_trash_bin('A3'). How do I fix it?"*
- *"I have a robot that will do a 1:2 serial dilution across a full 96-well plate with 8 channels, and I want the lab tech to be able to choose the number of dilution columns and the starting volume when they upload the protocol. Can you set that up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill opentrons-integration

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills opentrons-integration
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `lab-automation` category with `/plugin install lab-automation@research-agent-skills`.

## Related

- [`protocolsio-integration`](/skills/protocolsio-integration)
- [`pylabrobot`](/skills/pylabrobot)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/opentrons-integration/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
