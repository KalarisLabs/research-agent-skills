---
title: "systematic-review-prisma — AI agent skill for literature review"
description: "Plan, run and report systematic reviews and meta-analyses to PRISMA 2020 standards."
keywords: ["systematic review", "PRISMA 2020", "meta-analysis", "PROSPERO", "screening", "risk of bias", "evidence synthesis"]
---

# `systematic-review-prisma`

**Category:** [literature-review](/skills#literature-review) · **License:** MIT · **Version:** 1.0 · **Includes scripts**

**Tags:** systematic review, PRISMA 2020, meta-analysis, PROSPERO, screening, risk of bias, evidence synthesis

## When to use it

Plan, run and report systematic reviews and meta-analyses to PRISMA 2020 standards. Use when writing a review protocol (PROSPERO/OSF), building reproducible database search strings (PubMed, Embase, Scopus, Web of Science), writing the search strategy table for the supplement, deduplicating exports, organizing title/abstract and full-text screening with two reviewers (Cohen's kappa, conflicts), using an LLM or AI to screen abstracts, choosing a risk-of-bias tool (RoB 2, ROBINS-I), drawing the PRISMA flow diagram when counts do not add up, or completing the PRISMA 2020 checklist. Includes a dedup tool and a checked flow-diagram generator that requires a logged query for every database count.

## Example requests

Ask your agent in plain language, for example:

- *"Plan a systematic review of exercise interventions for depression and make the PRISMA flow diagram."*
- *"My PRISMA diagram script refuses to run and says PubMed has no search_log entry."*
- *"Generate the search strategy table for my supplement."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill systematic-review-prisma

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills systematic-review-prisma
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `literature-review` category with `/plugin install literature-review@research-agent-skills`.

## Related

- [`firecrawl-research-index`](/skills/firecrawl-research-index)
- [`fulltext-acquisition`](/skills/fulltext-acquisition)
- [`literature-review`](/skills/literature-review)
- [`paper-card`](/skills/paper-card)
- [`paper-corpus-rag`](/skills/paper-corpus-rag)
- [`plos`](/skills/plos)
- [`research-knowledge-graph`](/skills/research-knowledge-graph)
- [`citation-verification`](/skills/citation-verification)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/systematic-review-prisma/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
