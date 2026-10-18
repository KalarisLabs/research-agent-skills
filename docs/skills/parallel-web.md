---
title: "parallel-web — AI agent skill for literature review"
description: "Runs the parallel-cli tool for web workflows: web search, URL and PDF extraction, deep research reports, structured data enrichment of supplied rows, FindAll…"
keywords: ["web research", "deep research", "data enrichment", "web extraction"]
---

# `parallel-web`

**Category:** [literature-review](/skills#literature-review) · **License:** MIT · **Version:** 1.3

**Tags:** web research, deep research, data enrichment, web extraction

## When to use it

Runs the parallel-cli tool for web workflows: web search, URL and PDF extraction, deep research reports, structured data enrichment of supplied rows, FindAll entity discovery, and recurring web monitors. Prefers primary literature and institutional sources for scientific queries. Use when looking up current web evidence or a bounded research question. Use when fetching content from a known URL, PDF, or JavaScript-rendered page. Use when adding web-sourced fields to a list of companies, people, or products. Use when discovering entities that match natural-language criteria. Use when an explicitly exhaustive multi-source report is requested. Use when tracking web changes on a recurring schedule. Not for one-time checks of a known page that need no CLI, or for offline literature databases.

## Example requests

Ask your agent in plain language, for example:

- *"Find me the latest on CRISPR base editing for sickle cell, what's been published in the last year?"*
- *"I've got compounds.csv with 140 rows (columns: compound_name, CAS). I need to add the originating lab, first publication year, and the PubChem CID for each one, pulled from the web. Can you do that?"*
- *"Pull the full text out of https://www.biorxiv.org/content/10.1101/2025.03.14.643210v1.full.pdf and tell me what sample sizes and statistical tests they used."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill parallel-web

# Kalaris Labs installer with checksum verification
npx research-agent-skills install parallel-web
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `literature-review` category with `/plugin install literature-review@research-agent-skills`.

## Related

- [`exa-search`](/skills/exa-search)
- [`literature-review`](/skills/literature-review)
- [`research-lookup`](/skills/research-lookup)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/parallel-web/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
