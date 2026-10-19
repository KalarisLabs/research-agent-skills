---
title: "reference-manager-interop — AI agent skill for literature review"
description: "Move and sync reference libraries between Zotero, Mendeley, EndNote, JabRef, Paperpile and writing tools (LaTeX/BibTeX, Word, Google Docs, Pandoc, Quarto…"
keywords: ["Zotero", "Mendeley", "EndNote", "JabRef", "BibTeX", "RIS", "CSL-JSON", "Pandoc", "Quarto", "Overleaf", "reference manager"]
---

# `reference-manager-interop`

**Category:** [literature-review](/skills#literature-review) · **License:** MIT · **Version:** 1.0 · **Includes scripts**

**Tags:** Zotero, Mendeley, EndNote, JabRef, BibTeX, RIS, CSL-JSON, Pandoc, Quarto, Overleaf, reference manager

## When to use it

Move and sync reference libraries between Zotero, Mendeley, EndNote, JabRef, Paperpile and writing tools (LaTeX/BibTeX, Word, Google Docs, Pandoc, Quarto, Overleaf). Use when converting RIS, BibTeX, BibLaTeX or CSL-JSON files, migrating a library, setting up auto-exported .bib files, choosing a citation style (CSL), or fixing citations lost between tools. Includes a zero-dependency BibTeX/RIS/CSL-JSON converter.

## Example requests

Ask your agent in plain language, for example:

- *"Convert my Mendeley RIS export to BibTeX for Overleaf."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill reference-manager-interop

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills reference-manager-interop
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `literature-review` category with `/plugin install literature-review@research-agent-skills`.

## Related

- [`apa7`](/skills/apa7)
- [`bibtex-hygiene`](/skills/bibtex-hygiene)
- [`pyzotero`](/skills/pyzotero)
- [`citation-management`](/skills/citation-management)
- [`citation-verification`](/skills/citation-verification)
- [`research-knowledge-graph`](/skills/research-knowledge-graph)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/reference-manager-interop/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
