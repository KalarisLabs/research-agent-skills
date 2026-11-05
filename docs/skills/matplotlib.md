---
title: "matplotlib — AI agent skill for visualization and presentation"
description: "Low-level plotting library for full customization."
keywords: ["plotting", "data visualization", "scientific figures", "publication figures", "Python"]
---

# `matplotlib`

**Category:** [visualization-and-presentation](/skills#visualization-and-presentation) · **License:** https://github.com/matplotlib/matplotlib/tree/main/LICENSE · **Version:** 1.2 · **Includes scripts**

**Tags:** plotting, data visualization, scientific figures, publication figures, Python

## When to use it

Low-level plotting library for full customization. Use when you need fine-grained control over every plot element, creating novel plot types, or integrating with specific scientific workflows. Export to PNG/PDF/SVG for publication. For quick statistical plots use seaborn; for interactive plots use plotly; for publication-ready multi-panel figures with journal styling, use scientific-visualization.

## Example requests

Ask your agent in plain language, for example:

- *"Make me a log-scale scatter plot with a fitted line and save it as a vector PDF."*
- *"I'm in Jupyter with a DataFrame `df` from results/rnaseq_counts.csv. I need a 2x2 grid: a volcano plot (log2FC vs -log10 padj) with the significant genes in red, a MA plot, a PCA scatter and a library-size bar chart. The shared x labels overlap, and fig.savefig('fig2.png') gives a cropped legend. Please fix both and export at 300 dpi."*
- *"I have a 3D array of electric potential values on a grid and need a picture that shows the field lines and the equipotential surfaces together, with the arrows scaled by field strength. Nothing off the shelf does exactly this, so I'm expecting to write the drawing code myself."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill matplotlib

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills matplotlib
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `visualization-and-presentation` category with `/plugin install visualization-and-presentation@research-agent-skills`.

## Related

- [`scientific-schematics`](/skills/scientific-schematics)
- [`scientific-visualization`](/skills/scientific-visualization)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/matplotlib/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
