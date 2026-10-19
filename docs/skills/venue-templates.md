---
title: "venue-templates — AI agent skill for journal formats"
description: "Prepare journal manuscripts, conference papers, research posters, and grant documents using venue-specific formatting guidance and bundled LaTeX scaffolds."
keywords: ["journal templates", "LaTeX templates", "conference papers", "academic formatting", "posters"]
---

# `venue-templates`

**Category:** [journal-formats](/skills#journal-formats) · **License:** MIT · **Version:** 1.3 · **Includes scripts**

**Tags:** journal templates, LaTeX templates, conference papers, academic formatting, posters

## When to use it

Prepare journal manuscripts, conference papers, research posters, and grant documents using venue-specific formatting guidance and bundled LaTeX scaffolds. Use when selecting an official template, checking current page or anonymity rules, adapting academic writing to a venue, or inspecting a submission PDF.

## Example requests

Ask your agent in plain language, for example:

- *"What's the page limit for ICML main track this year?"*
- *"I'm submitting to NeurIPS 2026 and have my draft in main.tex with a copy of neurips_article.tex from your bundled assets. I've downloaded neurips_2026.sty. Compile gives 'File neurips_2026.sty not found' in one folder. Can you get it building, make sure the submission is anonymous, and check the PDF is within the main-text page limit?"*
- *"I'm writing my first R21 for an NIH institute and have a rough idea of the aims. I want to get the one-page aims document into shape and make sure I'm not missing any required pieces or exceeding limits before sending it to my grants office."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill venue-templates

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills venue-templates
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `journal-formats` category with `/plugin install journal-formats@research-agent-skills`.

## Related

- [`abstract-and-title`](/skills/abstract-and-title)
- [`acm-sigconf`](/skills/acm-sigconf)
- [`arxiv-submission`](/skills/arxiv-submission)
- [`cell-press`](/skills/cell-press)
- [`cover-letter-to-editor`](/skills/cover-letter-to-editor)
- [`elsevier-cas`](/skills/elsevier-cas)
- [`ieee-transactions`](/skills/ieee-transactions)
- [`latex-posters`](/skills/latex-posters)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/venue-templates/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
