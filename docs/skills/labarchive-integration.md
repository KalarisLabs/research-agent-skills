---
title: "labarchive-integration — AI agent skill for lab automation"
description: "Securely integrate with the official LabArchives ELN REST-like API and Inventory API v1."
keywords: ["electronic lab notebook", "LabArchives", "lab data", "lab automation"]
---

# `labarchive-integration`

**Category:** [lab-automation](/skills#lab-automation) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** electronic lab notebook, LabArchives, lab data, lab automation

## When to use it

Securely integrate with the official LabArchives ELN REST-like API and Inventory API v1. Use for regional endpoint selection, signed-request construction, user authorization and UID flows, local LA container validation, and verified LabArchives integration workflows.

## Example requests

Ask your agent in plain language, for example:

- *"How do I sign a LabArchives API call in Python?"*
- *"I'm getting an authentication failure from our university's LabArchives notebook API when I call users/user_access_info. We're in the UK. My script builds https://api.labarchives.com/api/users/user_access_info and signs akid+'users/user_access_info'+expires with the password. What's wrong, and how should I fix it?"*
- *"Our lab wants a nightly script that pulls our storage locations and vendor list out of our LabArchives inventory system into a spreadsheet. Where do I start, and what do I need to watch out for?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill labarchive-integration

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills labarchive-integration
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `lab-automation` category with `/plugin install lab-automation@research-agent-skills`.

## Related

- [`benchling-integration`](/skills/benchling-integration)
- [`omero-integration`](/skills/omero-integration)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/labarchive-integration/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
