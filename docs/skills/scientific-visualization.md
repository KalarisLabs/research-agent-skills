---
title: "scientific-visualization — AI agent skill for visualization and presentation"
description: "Create and audit truthful, accessible, publication-ready scientific figures with Matplotlib, Seaborn, or Plotly."
keywords: ["scientific figures", "data visualization", "publication figures", "accessibility", "plotting"]
---

# `scientific-visualization`

**Category:** [visualization-and-presentation](/skills#visualization-and-presentation) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** scientific figures, data visualization, publication figures, accessibility, plotting

## When to use it

Create and audit truthful, accessible, publication-ready scientific figures with Matplotlib, Seaborn, or Plotly. Use for figure design, multi-panel layouts, uncertainty and missing-data displays, color/contrast review, image metadata validation, and journal export planning.

## Example requests

Ask your agent in plain language, for example:

- *"Can you check if my figure palette is colorblind-safe and has enough contrast?"*
- *"I have fig3.pdf for my Nature Communications revision with 4 panels made in Matplotlib (results/fig3_raw.csv has the data). The editor says the figure is too low resolution and fonts aren't embedded. How do I check what's wrong and re-export it at 180 mm width?"*
- *"My growth-curve data has a few timepoints where the plate reader failed, and I want a clean figure showing treated vs control with error bars for a paper. The lines currently look smooth and complete, which feels a bit too good. What should I change?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill scientific-visualization

# Kalaris Labs installer with checksum verification
npx research-agent-skills install scientific-visualization
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `visualization-and-presentation` category with `/plugin install visualization-and-presentation@research-agent-skills`.

## Related

- [`academic-plotting`](/skills/academic-plotting)
- [`acm-sigconf`](/skills/acm-sigconf)
- [`bulk-rnaseq`](/skills/bulk-rnaseq)
- [`cell-press`](/skills/cell-press)
- [`ieee-transactions`](/skills/ieee-transactions)
- [`matplotlib`](/skills/matplotlib)
- [`nature-portfolio`](/skills/nature-portfolio)
- [`pathway-enrichment`](/skills/pathway-enrichment)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/scientific-visualization/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
