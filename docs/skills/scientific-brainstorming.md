---
title: "scientific-brainstorming — AI agent skill for ideation and design"
description: "Facilitates evidence-aware scientific ideation with independent generation, structured discussion, explicit assumptions, transparent evaluation, adversarial…"
keywords: ["brainstorming", "research ideation", "research directions", "scientific method"]
---

# `scientific-brainstorming`

**Category:** [ideation-and-design](/skills#ideation-and-design) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** brainstorming, research ideation, research directions, scientific method

## When to use it

Facilitates evidence-aware scientific ideation with independent generation, structured discussion, explicit assumptions, transparent evaluation, adversarial review, and decision logs. Use for early-stage research brainstorming or prioritizing candidate directions; hand off empirical validation, study design, ethics or regulatory review, and clinical questions to appropriate experts or skills.

## Example requests

Ask your agent in plain language, for example:

- *"Our lab needs new ideas for why our organoid batches vary so much. How should we brainstorm this without the PI steering everyone?"*
- *"I have 14 candidate directions in ideas_v2.xlsx for our soil microbiome carbon-sequestration grant (due to a USDA panel in March). Four of us rated them 1-5 on feasibility and novelty and the averages are all between 3.1 and 3.6. Help me prioritize and document the decision for the PI."*
- *"We're a small team starting a new project on microplastics and gut health and have no clear direction yet. I want to come out of a two-hour meeting with a handful of promising, defensible research angles and a record of why we chose them. How do we run that?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill scientific-brainstorming

# Kalaris Labs installer with checksum verification
npx research-agent-skills install scientific-brainstorming
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ideation-and-design` category with `/plugin install ideation-and-design@research-agent-skills`.

## Related

- [`arbor`](/skills/arbor)
- [`brainstorming-research-ideas`](/skills/brainstorming-research-ideas)
- [`hypothesis-generation`](/skills/hypothesis-generation)
- [`experimental-design`](/skills/experimental-design)
- [`literature-review`](/skills/literature-review)
- [`peer-review`](/skills/peer-review)
- [`statistical-analysis`](/skills/statistical-analysis)
- [`statistical-power`](/skills/statistical-power)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/scientific-brainstorming/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
