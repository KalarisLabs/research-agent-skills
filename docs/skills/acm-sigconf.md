---
title: "acm-sigconf — AI agent skill for journal formats"
description: "Format ACM conference papers and journal articles with the acmart LaTeX class (sigconf, sigplan, acmsmall, acmlarge, acmtog, manuscript/review/anonymous…"
keywords: ["ACM", "acmart", "sigconf", "CHI", "KDD", "SIGGRAPH", "TAPS", "LaTeX", "journal formatting"]
---

# `acm-sigconf`

**Category:** [journal-formats](/skills#journal-formats) · **License:** MIT · **Version:** 1.0

**Tags:** ACM, acmart, sigconf, CHI, KDD, SIGGRAPH, TAPS, LaTeX, journal formatting

## When to use it

Format ACM conference papers and journal articles with the acmart LaTeX class (sigconf, sigplan, acmsmall, acmlarge, acmtog, manuscript/review/anonymous modes) or the ACM Word template, covering CCS concepts, keywords, ACM Reference Format, rights management and copyright blocks, anonymization for double-blind review, accessibility (alt text), the TAPS production workflow and common acmart errors. Use when writing for CHI, SIGGRAPH, KDD, SIGMOD, CCS, FAccT, WWW, SIGIR, CSCW, PLDI or any ACM venue or journal.

## Example requests

Ask your agent in plain language, for example:

- *"Set up my CHI 2026 submission in acmart with anonymous review mode and CCS concepts."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill acm-sigconf

# Kalaris Labs installer with checksum verification
npx research-agent-skills install acm-sigconf
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `journal-formats` category with `/plugin install journal-formats@research-agent-skills`.

## Related

- [`arxiv-submission`](/skills/arxiv-submission)
- [`bibtex-hygiene`](/skills/bibtex-hygiene)
- [`ml-paper-writing`](/skills/ml-paper-writing)
- [`rebuttal-and-response-to-reviewers`](/skills/rebuttal-and-response-to-reviewers)
- [`scientific-visualization`](/skills/scientific-visualization)
- [`venue-templates`](/skills/venue-templates)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/acm-sigconf/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
