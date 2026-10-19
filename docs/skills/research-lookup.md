---
title: "research-lookup — AI agent skill for literature review"
description: "Compile current scholarly evidence for a scientific manuscript or research brief."
keywords: ["literature search", "scholarly evidence", "research briefs", "references"]
---

# `research-lookup`

**Category:** [literature-review](/skills#literature-review) · **License:** MIT · **Version:** 1.5 · **Includes scripts**

**Tags:** literature search, scholarly evidence, research briefs, references

## When to use it

Compile current scholarly evidence for a scientific manuscript or research brief. Use when the user explicitly asks to gather literature, references, background evidence, competing findings, or a manuscript research packet. Uses Parallel Search by default, Parallel Extract for source verification, Parallel Research for explicitly deep/exhaustive work, optional explicit Parallel Chat, and optional Perplexity only when requested or allowed as a failure fallback.

## Example requests

Ask your agent in plain language, for example:

- *"Need ~60 solid references on CRISPR base editing off-target effects for my review intro. Can you pull them together?"*
- *"I'm drafting a Nature Communications paper on gut microbiome alterations in Parkinson's disease (human cohort, 16S sequencing, n=212 cases vs 198 controls, outcome: alpha diversity and Prevotella abundance). My context is in study_context.json. Please gather the recent primary studies, meta-analyses, and any null or contradictory findings, and give me a claim-to-source map for the Introduction and Discussion."*
- *"I'm writing up a grant-style background on whether intermittent fasting improves insulin sensitivity in adults. I want to know where the evidence agrees, where it conflicts, and what the open gaps are, with real citations I can drop into my bibliography."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill research-lookup

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills research-lookup
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `literature-review` category with `/plugin install literature-review@research-agent-skills`.

## Related

- [`exa-search`](/skills/exa-search)
- [`parallel-web`](/skills/parallel-web)
- [`citation-management`](/skills/citation-management)
- [`literature-review`](/skills/literature-review)
- [`scientific-writing`](/skills/scientific-writing)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/research-lookup/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
