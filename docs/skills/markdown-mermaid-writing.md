---
title: "markdown-mermaid-writing — AI agent skill for research writing"
description: "Writes scientific documents and documentation as markdown with embedded Mermaid diagrams as the canonical, git-diffable source format."
keywords: ["Markdown", "Mermaid diagrams", "technical writing", "documentation", "diagrams"]
---

# `markdown-mermaid-writing`

**Category:** [research-writing](/skills#research-writing) · **License:** Apache-2.0 · **Version:** 1.1

**Tags:** Markdown, Mermaid diagrams, technical writing, documentation, diagrams

## When to use it

Writes scientific documents and documentation as markdown with embedded Mermaid diagrams as the canonical, git-diffable source format. Covers a markdown style guide, a Mermaid style guide, 24 Mermaid diagram type references (flowchart, sequence, ER, Gantt, state, mindmap, radar, sankey, XY chart, and others), and 9 templates (research paper, status report, decision record, how-to, pull request, issue, kanban, presentation, project documentation). Use when writing a report, manuscript, README, or analysis in markdown. Use when adding a workflow, pipeline, timeline, or architecture diagram to a document. Use when choosing the right Mermaid diagram type or fixing Mermaid syntax such as radar-beta or xychart-beta. Use when starting from a document template or checking citations and heading rules. Not for scatter plots of real data or photorealistic images; use Python plotting or scientific-schematics for those.

## Example requests

Ask your agent in plain language, for example:

- *"Can you turn my pipeline notes into a README with a diagram of the steps?"*
- *"I'm drafting analysis_report.md for our RNA-seq differential expression results (12 samples, DESeq2). I want it to be git-diffable, with a methods section, a footnoted reference list, and a figure showing how the reads go from FASTQ to the count matrix. I tried `radar` for comparing three aligners across five metrics and GitHub says there's a parse error. Please fix it."*
- *"We have a grant proposal with milestones spread over 18 months and overlapping work packages, and I'd like reviewers to see the schedule at a glance in the doc itself, without pasting in an image."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill markdown-mermaid-writing

# Kalaris Labs installer with checksum verification
npx research-agent-skills install markdown-mermaid-writing
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `research-writing` category with `/plugin install research-writing@research-agent-skills`.

## Related

- [`academic-plotting`](/skills/academic-plotting)
- [`citation-verification`](/skills/citation-verification)
- [`literature-review`](/skills/literature-review)
- [`scientific-schematics`](/skills/scientific-schematics)
- [`scientific-writing`](/skills/scientific-writing)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/markdown-mermaid-writing/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
