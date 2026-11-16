---
title: "paper-card — AI agent skill for literature review"
description: "Write a structured, verified summary (card) of one research paper where every claim carries a page, a verbatim quote and the numbers it rests on, checked by…"
keywords: ["paper summary", "evidence extraction", "verification", "quotes", "numbers", "literature review", "research integrity"]
---

# `paper-card`

**Category:** [literature-review](/skills#literature-review) · **License:** MIT · **Version:** 1.0 · **Includes scripts**

**Tags:** paper summary, evidence extraction, verification, quotes, numbers, literature review, research integrity

## When to use it

Write a structured, verified summary (card) of one research paper where every claim carries a page, a verbatim quote and the numbers it rests on, checked by script against the source text and then by a second independent reviewer. Use when summarizing a paper so its results can be cited, building an evidence table (study design, sample size, main effect, stated limitations) across included studies, extracting results from full text, or when an AI summary must be trustworthy enough to cite, including when the abstract and results disagree. Catches invented numbers, misquotes and correct numbers attached to the wrong claim.

## Example requests

Ask your agent in plain language, for example:

- *"Summarize this paper so I can cite its results. I'm worried you'll get a number wrong."*
- *"Build an evidence table for 25 included studies: design, sample size, main effect and limitations."*
- *"check_card.py says quote-not-found for one of my claims."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill paper-card

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills paper-card
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `literature-review` category with `/plugin install literature-review@research-agent-skills`.

## Related

- [`fulltext-acquisition`](/skills/fulltext-acquisition)
- [`citation-verification`](/skills/citation-verification)
- [`literature-review`](/skills/literature-review)
- [`paper-corpus-rag`](/skills/paper-corpus-rag)
- [`scholar-evaluation`](/skills/scholar-evaluation)
- [`systematic-review-prisma`](/skills/systematic-review-prisma)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/paper-card/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
