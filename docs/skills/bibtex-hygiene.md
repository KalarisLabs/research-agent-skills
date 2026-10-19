---
title: "bibtex-hygiene — AI agent skill for literature review"
description: "Clean, deduplicate and validate BibTeX/BibLaTeX bibliographies before submission."
keywords: ["BibTeX", "BibLaTeX", "citations", "references", "LaTeX", "bibliography"]
---

# `bibtex-hygiene`

**Category:** [literature-review](/skills#literature-review) · **License:** MIT · **Version:** 1.0 · **Includes scripts**

**Tags:** BibTeX, BibLaTeX, citations, references, LaTeX, bibliography

## When to use it

Clean, deduplicate and validate BibTeX/BibLaTeX bibliographies before submission. Use when a .bib file has duplicate keys or works, missing fields, broken DOIs, lost acronym capitalization (e.g. "bert" instead of "BERT"), inconsistent page dashes, arXiv preprints that now have published versions, or when LaTeX/biber emits bibliography warnings. Includes a zero-dependency linter and normalizer.

## Example requests

Ask your agent in plain language, for example:

- *"My refs.bib has duplicates and BERT shows up lowercase in the bibliography. Clean it."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill bibtex-hygiene

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills bibtex-hygiene
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `literature-review` category with `/plugin install literature-review@research-agent-skills`.

## Related

- [`acm-sigconf`](/skills/acm-sigconf)
- [`apa7`](/skills/apa7)
- [`arxiv-submission`](/skills/arxiv-submission)
- [`citation-management`](/skills/citation-management)
- [`citation-verification`](/skills/citation-verification)
- [`reference-manager-interop`](/skills/reference-manager-interop)
- [`elsevier-cas`](/skills/elsevier-cas)
- [`ieee-transactions`](/skills/ieee-transactions)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/bibtex-hygiene/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
