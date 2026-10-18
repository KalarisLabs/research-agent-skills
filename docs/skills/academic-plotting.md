---
title: "academic-plotting — AI agent skill for visualization and presentation"
description: "Generates publication-quality figures for ML papers from research context."
keywords: ["Academic Writing", "Visualization", "Matplotlib", "Seaborn", "Plotting", "Figures", "Diagrams", "NeurIPS", "ICML", "ICLR", "LaTeX"]
---

# `academic-plotting`

**Category:** [visualization-and-presentation](/skills#visualization-and-presentation) · **License:** MIT · **Version:** 1.0.0

**Tags:** Academic Writing, Visualization, Matplotlib, Seaborn, Plotting, Figures, Diagrams, NeurIPS, ICML, ICLR, LaTeX

## When to use it

Generates publication-quality figures for ML papers from research context. Given a paper section or description, extracts system components and relationships to generate architecture diagrams via Gemini. Given experiment results or data, auto-selects chart type and generates data-driven figures via matplotlib/seaborn. Use when creating any figure for a conference paper.

## Example requests

Ask your agent in plain language, for example:

- *"I need a figure for the overview section of my paper. Here's the method text: 'Our framework has a Retriever that fetches documents, a Reranker that scores them, and a Generator that writes the answer. If the Generator's confidence is low, it sends a query back to the Retriever.' Can you make the diagram?"*
- *"Plot results.csv (columns: step, method, val_loss, with 3 seeds each) as training curves for our ICML submission. 'ours' should stand out, and I need it to fit in a single column. Also the fonts look wrong when I include the PDF in LaTeX."*
- *"Here are my numbers: GPT-4 gets 86.4 on MMLU and 67.0 on HumanEval, our model gets 88.1 and 71.2, Llama-3 gets 79.3 and 62.1. What's the best way to show this in the paper, and can you draw it?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill academic-plotting

# Kalaris Labs installer with checksum verification
npx research-agent-skills install academic-plotting
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `visualization-and-presentation` category with `/plugin install visualization-and-presentation@research-agent-skills`.

## Related

- [`latex-posters`](/skills/latex-posters)
- [`ml-paper-writing`](/skills/ml-paper-writing)
- [`scientific-schematics`](/skills/scientific-schematics)
- [`scientific-visualization`](/skills/scientific-visualization)
- [`infographics`](/skills/infographics)
- [`markdown-mermaid-writing`](/skills/markdown-mermaid-writing)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/academic-plotting/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
