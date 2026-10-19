---
title: "infographics — AI agent skill for visualization and presentation"
description: "Generates infographics from natural-language prompts using Nano Banana Pro image generation, with optional Perplexity Sonar research for facts and a Gemini…"
keywords: ["infographics", "data visualization", "science communication", "figures"]
---

# `infographics`

**Category:** [visualization-and-presentation](/skills#visualization-and-presentation) · **License:** MIT · **Version:** 1.7 · **Includes scripts**

**Tags:** infographics, data visualization, science communication, figures

## When to use it

Generates infographics from natural-language prompts using Nano Banana Pro image generation, with optional Perplexity Sonar research for facts and a Gemini 3.6 Flash quality review that regenerates only when the score is below a document-type threshold. Supports 10 types (statistical, timeline, process, comparison, list, geographic, hierarchical, anatomical, resume, social), 8 industry styles, and colorblind-safe palettes (wong, ibm, tol). Use when turning data or statistics into a visual summary. Use when building timelines, process guides, or side-by-side comparisons. Use when making geographic or organizational chart graphics. Use when producing social media or marketing visuals. Not for technical flowcharts, pathway diagrams, or CONSORT/PRISMA diagrams; use scientific-schematics instead.

## Example requests

Ask your agent in plain language, for example:

- *"Make me an infographic of global renewable energy share by country, 2024."*
- *"I'm presenting at a lab meeting Friday. I need a one-slide visual timeline of CRISPR milestones from 2012 (Doudna/Charpentier) to the 2023 Casgevy approval. Use a colorblind-safe palette, save it to figures/crispr_timeline.png, and I want it to be good enough for a conference talk."*
- *"Our department wants a one-page graphic for the newsletter that shows how a new grant proposal moves from internal draft to sponsor submission, with the people responsible at each stage laid out in a clear visual that non-scientists can follow."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill infographics

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills infographics
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `visualization-and-presentation` category with `/plugin install visualization-and-presentation@research-agent-skills`.

## Related

- [`academic-plotting`](/skills/academic-plotting)
- [`generate-image`](/skills/generate-image)
- [`scientific-schematics`](/skills/scientific-schematics)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/infographics/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
