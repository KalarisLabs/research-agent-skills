---
title: "autoskill — AI agent skill for research automation"
description: "Observe the user's screen via screenpipe, detect repeated research workflows, match them against existing research-agent-skills, and draft new skills (or…"
---

# `autoskill`

> Observe the user's screen via screenpipe, detect repeated research workflows, match them against existing research-agent-skills, and draft new skills (or composition recipes that chain existing ones) for the patterns not yet covered. Use when the user asks to analyze their recent work and propose skills based on what they actually do. Requires the screenpipe daemon (https://github.com/screenpipe/screenpipe) running locally on port 3030 — the skill has no other data source and will refuse to run if screenpipe is unreachable. All detection runs locally; only redacted cluster summaries reach the LLM.

**Category:** [research-automation](/skills#research-automation) · **License:** MIT · **Version:** 1.4

## Install

```bash
npx research-agent-skills install autoskill
npx skills add KalarisLabs/research-agent-skills --skill autoskill
```

## When to use it

Observe the user's screen via screenpipe, detect repeated research workflows, match them against existing research-agent-skills, and draft new skills (or composition recipes that chain existing ones) for the patterns not yet covered. Use when the user asks to analyze their recent work and propose skills based on what they actually do. Requires the screenpipe daemon (https://github.com/screenpipe/screenpipe) running locally on port 3030 — the skill has no other data source and will refuse to run if screenpipe is unreachable. All detection runs locally; only redacted cluster summaries reach the LLM.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/autoskill/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
