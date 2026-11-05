---
title: "scientific-slides — AI agent skill for visualization and presentation"
description: "Build slide decks and presentations for research talks."
keywords: ["presentations", "slides", "conference talks", "thesis defense", "academic presentations"]
---

# `scientific-slides`

**Category:** [visualization-and-presentation](/skills#visualization-and-presentation) · **License:** MIT · **Version:** 1.8 · **Includes scripts**

**Tags:** presentations, slides, conference talks, thesis defense, academic presentations

## When to use it

Build slide decks and presentations for research talks. Use this for making PowerPoint slides, conference presentations, seminar talks, research presentations, thesis defense slides, or any scientific talk. Provides slide structure, design templates, timing guidance, and visual validation. Works with PowerPoint and LaTeX Beamer.

## Example requests

Ask your agent in plain language, for example:

- *"I need slides for my 12-minute talk at a neuroscience meeting next month. Can you help?"*
- *"My committee meets on the 14th for my PhD defense. I have results in results/figs/ (fig1_ablation.png, fig2_roc_curves.png, fig3_umap.png) and a draft thesis in thesis.pdf covering single-cell RNA-seq of zebrafish fin regeneration. Build me a defense deck in Beamer, and make sure nothing overflows or looks cramped when you're done."*
- *"I have to present our lab's findings on CRISPR screens to the department for an hour on Friday. I'd like something that tells a clear story, not a wall of bullets, and I want to know how long to spend on each section so I don't run over."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill scientific-slides

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills scientific-slides
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `visualization-and-presentation` category with `/plugin install visualization-and-presentation@research-agent-skills`.

## Related

- [`abstract-and-title`](/skills/abstract-and-title)
- [`autoskill`](/skills/autoskill)
- [`generate-image`](/skills/generate-image)
- [`histolab`](/skills/histolab)
- [`pptx-posters`](/skills/pptx-posters)
- [`presenting-conference-talks`](/skills/presenting-conference-talks)
- [`latex-posters`](/skills/latex-posters)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/scientific-slides/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
