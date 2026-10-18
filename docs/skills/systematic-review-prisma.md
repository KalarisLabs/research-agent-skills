---
title: "systematic-review-prisma — AI agent skill for literature review"
description: "Plan, run and report systematic reviews and meta-analyses to PRISMA 2020 standards."
keywords: ["systematic review", "PRISMA 2020", "meta-analysis", "PROSPERO", "screening", "risk of bias", "evidence synthesis"]
---

# `systematic-review-prisma`

**Category:** [literature-review](/skills#literature-review) · **License:** MIT · **Version:** 1.0 · **Includes scripts**

**Tags:** systematic review, PRISMA 2020, meta-analysis, PROSPERO, screening, risk of bias, evidence synthesis

## When to use it

Plan, run and report systematic reviews and meta-analyses to PRISMA 2020 standards. Use when writing a review protocol (PROSPERO/OSF), building reproducible database search strings (PubMed, Embase, Scopus, Web of Science), deduplicating exports, organizing title/abstract and full-text screening, assessing risk of bias, drawing the PRISMA flow diagram, or completing the PRISMA 2020 checklist. Includes a dedup tool and a checked PRISMA diagram generator.

## Example requests

Ask your agent in plain language, for example:

- *"Plan a systematic review of exercise interventions for depression and make the PRISMA flow diagram."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill systematic-review-prisma

# Kalaris Labs installer with checksum verification
npx research-agent-skills install systematic-review-prisma
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `literature-review` category with `/plugin install literature-review@research-agent-skills`.

## Related

- [`firecrawl-research-index`](/skills/firecrawl-research-index)
- [`literature-review`](/skills/literature-review)
- [`plos`](/skills/plos)
- [`research-knowledge-graph`](/skills/research-knowledge-graph)
- [`scientific-critical-thinking`](/skills/scientific-critical-thinking)
- [`citation-verification`](/skills/citation-verification)
- [`peer-review`](/skills/peer-review)
- [`scientific-writing`](/skills/scientific-writing)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/systematic-review-prisma/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
