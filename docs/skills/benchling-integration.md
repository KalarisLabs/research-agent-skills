---
title: "benchling-integration — AI agent skill for lab automation"
description: "Benchling Python SDK and REST API integration for registry entities, inventory, ELN entries, workflows, Benchling Apps, and Data Warehouse queries."
keywords: ["Benchling", "electronic lab notebook", "LIMS", "lab automation", "biotech"]
---

# `benchling-integration`

**Category:** [lab-automation](/skills#lab-automation) · **License:** MIT · **Version:** 1.5

**Tags:** Benchling, electronic lab notebook, LIMS, lab automation, biotech

## When to use it

Benchling Python SDK and REST API integration for registry entities, inventory, ELN entries, workflows, Benchling Apps, and Data Warehouse queries. Use when automating lab data with benchling-sdk or the v2 API.

## Example requests

Ask your agent in plain language, for example:

- *"How do I list all DNA sequences in a Benchling project using the Python SDK?"*
- *"I have plasmids.csv with columns name, bases, schema_id, and folder_id for about 400 plasmids. I need to bulk register them as DNA sequences in our Benchling registry with a naming prefix. My script using benchling-sdk 1.25.0 keeps failing partway with a 429 error, and some rows were already created. How should I fix it?"*
- *"Our lab keeps freezer sample locations and plate contents in Benchling. I want a nightly script that pulls every container in a given freezer box, checks for ones that are empty or expired, and writes a CSV audit report for my PI. Where do I start?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill benchling-integration

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills benchling-integration
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `lab-automation` category with `/plugin install lab-automation@research-agent-skills`.

## Related

- [`labarchive-integration`](/skills/labarchive-integration)
- [`latchbio-integration`](/skills/latchbio-integration)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/benchling-integration/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
