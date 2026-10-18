---
title: "paperclip — AI agent skill for literature review"
description: "Search and read full-text biomedical papers, FDA/PMDA/EMA regulatory documents, clinical trial registries, and UniProt/PDB/ChEMBL entries with the Paperclip…"
keywords: ["full-text papers", "regulatory documents", "clinical trials", "biomedical literature"]
---

# `paperclip`

**Category:** [literature-review](/skills#literature-review) · **License:** MIT · **Version:** 1.3

**Tags:** full-text papers, regulatory documents, clinical trials, biomedical literature

## When to use it

Search and read full-text biomedical papers, FDA/PMDA/EMA regulatory documents, clinical trial registries, and UniProt/PDB/ChEMBL entries with the Paperclip CLI from GXL. Covers installing and authenticating the `paperclip` binary with a PAPERCLIP_API_KEY, the read-only virtual filesystem under /papers, /fda, /trials, /proteins and /clipboard, source-scoped semantic search, corpus-wide grep, metadata lookup and SQL, map/reduce reading across many papers, figure vision analysis, opt-in paper repositories with claim verification, and line-pinned citations. Use when asked to install paperclip, run paperclip search/grep/map/reduce/sql/repo, find or read biomedical literature, regulatory filings or clinical trials through paperclip, or produce citations with line numbers.

## Example requests

Ask your agent in plain language, for example:

- *"get paperclip set up on this machine, I've got a key in my .env"*
- *"I'm writing the related-work section of my manuscript on CAR-T for lupus. I need the 5 most relevant full-text PMC papers from the last two years, with the exact sentence-level support for each claim, so reviewers can check my citations."*
- *"Which papers in the corpus mention the accession GSE123456 anywhere in their text, including data availability statements? Also compare what the FDA approved label and the EU documents say about dosing for semaglutide."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill paperclip

# Kalaris Labs installer with checksum verification
npx research-agent-skills install paperclip
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `literature-review` category with `/plugin install literature-review@research-agent-skills`.

## Related

- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/paperclip/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
