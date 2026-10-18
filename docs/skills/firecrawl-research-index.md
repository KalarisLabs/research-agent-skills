---
title: "firecrawl-research-index — AI agent skill for literature review"
description: "Query Firecrawl Research Index paper endpoints for topic discovery, source metadata, question-matched passages, and citation-neighbor expansion."
keywords: ["Firecrawl", "Research Index", "academic search", "paper discovery", "arXiv", "PubMed", "life sciences", "citation discovery"]
---

# `firecrawl-research-index`

**Category:** [literature-review](/skills#literature-review) · **License:** MIT · **Version:** 1.0

**Tags:** Firecrawl, Research Index, academic search, paper discovery, arXiv, PubMed, life sciences, citation discovery

## When to use it

Query Firecrawl Research Index paper endpoints for topic discovery, source metadata, question-matched passages, and citation-neighbor expansion. Use when a researcher explicitly asks for Firecrawl Research or its hosted arXiv and biomedical paper records.

## Example requests

Ask your agent in plain language, for example:

- *"Use Firecrawl Research to find recent papers on CRISPR base editing off-target effects, and give me a short list with source IDs and abstracts I can screen."*
- *"In Firecrawl's paper index, inspect arxiv:1706.03762, find passages about the attention mechanism, then look for related work that cites it."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill firecrawl-research-index

# Kalaris Labs installer with checksum verification
npx research-agent-skills install firecrawl-research-index
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `literature-review` category with `/plugin install literature-review@research-agent-skills`.

## Related

- [`database-lookup`](/skills/database-lookup)
- [`citation-verification`](/skills/citation-verification)
- [`paper-corpus-rag`](/skills/paper-corpus-rag)
- [`paper-lookup`](/skills/paper-lookup)
- [`systematic-review-prisma`](/skills/systematic-review-prisma)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/firecrawl-research-index/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
