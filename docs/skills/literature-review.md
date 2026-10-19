---
title: "literature-review — AI agent skill for literature review"
description: "Runs systematic literature reviews by searching PubMed, arXiv, bioRxiv, and Semantic Scholar (plus web search via parallel-cli), screening studies, extracting…"
keywords: ["literature review", "systematic review", "PubMed", "arXiv", "evidence synthesis", "citations"]
---

# `literature-review`

**Category:** [literature-review](/skills#literature-review) · **License:** MIT · **Version:** 1.8 · **Includes scripts**

**Tags:** literature review, systematic review, PubMed, arXiv, evidence synthesis, citations

## When to use it

Runs systematic literature reviews by searching PubMed, arXiv, bioRxiv, and Semantic Scholar (plus web search via parallel-cli), screening studies, extracting data, synthesizing themes, and verifying citations with verify_citations.py. Produces a markdown and PDF review with a PRISMA-style flow diagram and a bibliography in APA, Nature, or Vancouver style. Use when conducting a systematic or scoping review, synthesizing research on a topic, writing the literature review section of a paper or thesis, identifying research gaps, or checking citations in a review. Not for looking up a single paper or database record; use the specific database skill instead.

## Example requests

Ask your agent in plain language, for example:

- *"Can you do a systematic review of intermittent fasting and cognitive decline in older adults? I need a PDF at the end."*
- *"I'm writing chapter 2 of my thesis on transformer-based protein language models for variant effect prediction. I've got about 40 papers in refs/plm_papers.bib from arXiv and bioRxiv. Draft the literature review section in Vancouver style, group it by theme rather than paper-by-paper, flag research gaps, and run verify_citations.py on the bibliography because my advisor caught two wrong DOIs last time."*
- *"My lab wants to know what's actually known about microplastics crossing the blood-brain barrier and where the evidence is thin. Nobody has mapped this out yet. Can you pull together what's out there and give us something we can circulate?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill literature-review

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills literature-review
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `literature-review` category with `/plugin install literature-review@research-agent-skills`.

## Related

- [`autoskill`](/skills/autoskill)
- [`citation-management`](/skills/citation-management)
- [`citation-verification`](/skills/citation-verification)
- [`paper-lookup`](/skills/paper-lookup)
- [`systematic-review-prisma`](/skills/systematic-review-prisma)
- [`markdown-mermaid-writing`](/skills/markdown-mermaid-writing)
- [`paper-corpus-rag`](/skills/paper-corpus-rag)
- [`parallel-web`](/skills/parallel-web)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/literature-review/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
