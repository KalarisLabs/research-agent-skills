---
title: "seaborn — AI agent skill for visualization and presentation"
description: "Statistical visualization with pandas integration."
keywords: ["statistical visualization", "plotting", "data visualization", "Python"]
---

# `seaborn`

**Category:** [visualization-and-presentation](/skills#visualization-and-presentation) · **License:** BSD-3-Clause license · **Version:** 1.3

**Tags:** statistical visualization, plotting, data visualization, Python

## When to use it

Statistical visualization with pandas integration. Use for quick exploration of distributions, relationships, and categorical comparisons with attractive defaults. Best for box plots, violin plots, pair plots, heatmaps. Built on matplotlib. For interactive plots use plotly; for publication styling use scientific-visualization.

## Example requests

Ask your agent in plain language, for example:

- *"Can you make a pair plot of my iris dataframe colored by species?"*
- *"I have expression_counts.csv with columns sample_id, condition (control/treated/rescue), gene, log2_expr. I want to compare log2_expr across the three conditions for each gene, with individual points visible, and I keep getting a FutureWarning about 'palette' without 'hue' when I run sns.boxplot(x='condition', y='log2_expr', data=df, palette='Set2'). Fix it and show the distributions."*
- *"I've got a table of 40 patient biomarkers and I want to see which ones move together and group similar ones, as a color-coded grid I can drop into a lab meeting slide. What should I do?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill seaborn

# Kalaris Labs installer with checksum verification
npx research-agent-skills install seaborn
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `visualization-and-presentation` category with `/plugin install visualization-and-presentation@research-agent-skills`.

## Related

- [`scientific-visualization`](/skills/scientific-visualization)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/seaborn/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
