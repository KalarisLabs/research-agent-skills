---
title: "fulltext-acquisition — AI agent skill for literature review"
description: "Get the full text of the papers you screened in and attach each file to the right record."
keywords: ["full text", "open access", "Unpaywall", "interlibrary loan", "PDF matching", "systematic review", "reference library"]
---

# `fulltext-acquisition`

**Category:** [literature-review](/skills#literature-review) · **License:** MIT · **Version:** 1.0 · **Includes scripts**

**Tags:** full text, open access, Unpaywall, interlibrary loan, PDF matching, systematic review, reference library

## When to use it

Get the full text of the papers you screened in and attach each file to the right record. Use after abstract screening or a PRISMA full-text stage, when a reading list has missing PDFs, when you need legal open-access copies, institutional link-resolver links or interlibrary-loan requests, when a folder of downloaded PDFs has useless names like download (7).pdf and must be identified by DOI, PMID or title, when files are misnamed, scanned or duplicated, when records have no DOI, or when papers must be reported as not retrieved. Builds the missing-paper worklist and refuses files its text does not support.

## Example requests

Ask your agent in plain language, for example:

- *"I screened 180 abstracts in. Which of them don't I have full text for, and how do I get them?"*
- *"Find legal open-access copies for my included studies."*
- *"I downloaded 40 PDFs with names like 'download (7).pdf'. Which paper is which?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill fulltext-acquisition

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills fulltext-acquisition
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `literature-review` category with `/plugin install literature-review@research-agent-skills`.

## Related

- [`citation-verification`](/skills/citation-verification)
- [`paper-card`](/skills/paper-card)
- [`paper-corpus-rag`](/skills/paper-corpus-rag)
- [`paper-lookup`](/skills/paper-lookup)
- [`reference-manager-interop`](/skills/reference-manager-interop)
- [`systematic-review-prisma`](/skills/systematic-review-prisma)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/fulltext-acquisition/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
