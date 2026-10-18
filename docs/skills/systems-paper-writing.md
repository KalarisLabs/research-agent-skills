---
title: "systems-paper-writing — AI agent skill for research writing"
description: "Provides paragraph-level structural blueprints for 10-12 page systems papers targeting OSDI, SOSP, ASPLOS, NSDI, and EuroSys."
keywords: ["Systems Paper Writing", "OSDI", "SOSP", "ASPLOS", "NSDI", "EuroSys", "Structural Blueprint", "Academic Writing", "LaTeX"]
---

# `systems-paper-writing`

**Category:** [research-writing](/skills#research-writing) · **License:** MIT · **Version:** 1.1.0

**Tags:** Systems Paper Writing, OSDI, SOSP, ASPLOS, NSDI, EuroSys, Structural Blueprint, Academic Writing, LaTeX

## When to use it

Provides paragraph-level structural blueprints for 10-12 page systems papers targeting OSDI, SOSP, ASPLOS, NSDI, and EuroSys. Covers page budgets per section, writing patterns (gap analysis, observation-driven, contribution list, thesis formula), evaluation structure, venue checklists, reviewer guidelines, deadlines, and LaTeX templates for OSDI, NSDI, ASPLOS, and SOSP. Use when planning the section and page layout of a systems paper. Use when drafting an introduction, motivation, design, or evaluation section. Use when checking a draft against venue page limits and a pre-submission checklist. Use when anticipating how systems reviewers will assess a paper. Use when looking up conference formats or deadlines. For NeurIPS/ICML/ICLR papers or citation verification, use ml-paper-writing instead.

## Example requests

Ask your agent in plain language, for example:

- *"How should I split pages across sections for an OSDI submission?"*
- *"I'm drafting the intro for our NSDI paper on a GPU cluster scheduler (intro.tex). Existing schedulers like Gandiva and Tiresias miss a few things for our workloads. Can you lay out the paragraphs so the gaps get stated clearly and tie to our design sections? We plan to list 4 contributions at the end."*
- *"My systems paper draft is done and I want to know how a PC member will judge it. What will they look for, and what should I fix before I hit submit?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill systems-paper-writing

# Kalaris Labs installer with checksum verification
npx research-agent-skills install systems-paper-writing
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `research-writing` category with `/plugin install research-writing@research-agent-skills`.

## Related

- [`ml-paper-writing`](/skills/ml-paper-writing)
- [`research-grants`](/skills/research-grants)
- [`venue-templates`](/skills/venue-templates)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/systems-paper-writing/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
