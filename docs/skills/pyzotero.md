---
title: "pyzotero — AI agent skill for literature review"
description: "Reads and writes Zotero libraries from Python with pyzotero 1.13.0 and the Zotero Web API v3: items, collections, tags, attachments, saved searches, full-text…"
keywords: ["Zotero", "reference management", "citations", "BibTeX", "literature"]
---

# `pyzotero`

**Category:** [literature-review](/skills#literature-review) · **License:** MIT · **Version:** 1.2

**Tags:** Zotero, reference management, citations, BibTeX, literature

## When to use it

Reads and writes Zotero libraries from Python with pyzotero 1.13.0 and the Zotero Web API v3: items, collections, tags, attachments, saved searches, full-text content, and BibTeX, CSL-JSON, and bibliography export. Also covers the pyzotero CLI and MCP server for a local Zotero 7. Use when fetching or searching library items programmatically; when creating, updating, or deleting references, collections, or tags; when uploading PDF attachments or downloading files; when exporting citations as BibTeX or CSL-JSON; when building research automation around a Zotero user or group library. Not for formatting citations in a manuscript or verifying references against external databases.

## Example requests

Ask your agent in plain language, for example:

- *"How do I dump every item in my Zotero library to a BibTeX file with Python?"*
- *"I have a group library (the URL is zotero.org/groups/4829311/ml-benchmarks) and a folder of 40 PDFs in ./papers/ named like smith2021.pdf. I want a script that creates a top-level collection called 'Benchmarks 2025', adds a journalArticle item for each PDF with the title taken from the filename, and uploads each PDF as a child attachment. I keep getting a 403 when I try to write. What should I check?"*
- *"I keep my reading list in Zotero and want a nightly script that finds everything I tagged 'to-read' more than 30 days ago, moves those papers into an 'Overdue' collection, and then removes the tag. I'm comfortable with Python but haven't touched the Zotero API."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pyzotero

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills pyzotero
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `literature-review` category with `/plugin install literature-review@research-agent-skills`.

## Related

- [`citation-management`](/skills/citation-management)
- [`literature-review`](/skills/literature-review)
- [`reference-manager-interop`](/skills/reference-manager-interop)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pyzotero/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
