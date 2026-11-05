---
title: "bgpt-paper-search — AI agent skill for literature review"
description: "Search scientific papers and retrieve structured experimental data extracted from full-text studies via the BGPT MCP server."
keywords: ["paper search", "literature review", "evidence synthesis", "structured data extraction", "MCP"]
---

# `bgpt-paper-search`

**Category:** [literature-review](/skills#literature-review) · **License:** MIT · **Version:** 1.1

**Tags:** paper search, literature review, evidence synthesis, structured data extraction, MCP

## When to use it

Search scientific papers and retrieve structured experimental data extracted from full-text studies via the BGPT MCP server. Returns 25+ fields per paper including methods, results, sample sizes, quality scores, and conclusions. Use for literature reviews, evidence synthesis, and finding experimental details not available in abstracts alone.

## Example requests

Ask your agent in plain language, for example:

- *"Find me papers on creatine supplementation and working memory with sample sizes and effect sizes."*
- *"I'm building an evidence table for a scoping review on CRISPR base editing for sickle cell disease, 2019-2025, human or humanized mouse studies only. I need the methods, n per arm, the main quantitative outcome and a quality rating for each study, pulled from the full text rather than abstracts. Can you set that up and run it? I'm on the free tier."*
- *"My PI wants to know which in vivo mouse models have been used to test GLP-1 agonists for neuroprotection and how many animals each study used. What does the literature say? I want details that go beyond what abstracts report."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill bgpt-paper-search

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills bgpt-paper-search
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `literature-review` category with `/plugin install literature-review@research-agent-skills`.

## Related

- [`folklore-variant-evidence`](/skills/folklore-variant-evidence)
- [`scientific-critical-thinking`](/skills/scientific-critical-thinking)
- [`statistical-analysis`](/skills/statistical-analysis)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/bgpt-paper-search/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
