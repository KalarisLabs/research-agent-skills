---
title: "unslop-academic-writing — AI agent skill for research writing"
description: "Remove AI slop from research writing so papers, theses, grant proposals, reviews and rebuttals read as written by a careful human expert."
keywords: ["AI slop", "academic writing", "tone", "voice", "humanize", "clarity", "editing", "scientific writing"]
---

# `unslop-academic-writing`

**Category:** [research-writing](/skills#research-writing) · **License:** MIT · **Version:** 1.0 · **Includes scripts**

**Tags:** AI slop, academic writing, tone, voice, humanize, clarity, editing, scientific writing

## When to use it

Remove AI slop from research writing so papers, theses, grant proposals, reviews and rebuttals read as written by a careful human expert. Covers stock vocabulary (delve, tapestry, pivotal, underscores), empty emphasis, hedge stacks, formulaic signposting, "not only X but also Y" constructions, em-dash pileups, monotone rhythm, and claims vaguer than the data. Use when drafting or revising academic text with an AI assistant, when a draft "sounds like ChatGPT", before submission, or to match an author's own voice. Includes a zero-dependency slop linter for Markdown, LaTeX, text and Word files.

## Example requests

Ask your agent in plain language, for example:

- *"My introduction sounds like ChatGPT wrote it: delve, pivotal role, tapestry. Rewrite it so it reads like a human researcher."*
- *"Remove the AI slop and em dashes from this thesis chapter without changing the claims."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill unslop-academic-writing

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills unslop-academic-writing
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `research-writing` category with `/plugin install research-writing@research-agent-skills`.

## Related

- [`abstract-and-title`](/skills/abstract-and-title)
- [`citation-verification`](/skills/citation-verification)
- [`cover-letter-to-editor`](/skills/cover-letter-to-editor)
- [`ml-paper-writing`](/skills/ml-paper-writing)
- [`peer-review`](/skills/peer-review)
- [`rebuttal-and-response-to-reviewers`](/skills/rebuttal-and-response-to-reviewers)
- [`reproducibility-statement`](/skills/reproducibility-statement)
- [`scientific-critical-thinking`](/skills/scientific-critical-thinking)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/unslop-academic-writing/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
