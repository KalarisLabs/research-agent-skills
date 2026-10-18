---
title: "bioservices — AI agent skill for scientific databases"
description: "Unified Python interface to 40+ bioinformatics services."
keywords: ["bioinformatics databases", "UniProt", "KEGG", "ID mapping", "life sciences"]
---

# `bioservices`

**Category:** [scientific-databases](/skills#scientific-databases) · **License:** GPLv3 license · **Version:** 1.4 · **Includes scripts**

**Tags:** bioinformatics databases, UniProt, KEGG, ID mapping, life sciences

## When to use it

Unified Python interface to 40+ bioinformatics services. Use when querying multiple databases (UniProt, KEGG, ChEMBL, Reactome) in a single workflow with consistent API. Best for cross-database analysis, ID mapping across services. For quick single-database lookups use gget; for sequence/file manipulation use biopython.

## Example requests

Ask your agent in plain language, for example:

- *"How do I map a list of UniProt accessions to KEGG gene IDs with bioservices?"*
- *"I have a CSV called hits.csv with a column of human UniProt IDs (P04637, P38398, Q00987, etc.). For each one I need the KEGG pathways it belongs to, the Reactome pathway names, and any ChEMBL target ID. My script crashed with 'AttributeError: module bioservices has no attribute PSICQUIC' when I tried to add interactions too. Can you write the pipeline?"*
- *"I'm studying imatinib and want one table that links its KEGG compound entry to the ChEBI and ChEMBL identifiers, plus whatever protein targets are listed, all pulled programmatically from the public databases. How should I go about it in Python?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill bioservices

# Kalaris Labs installer with checksum verification
npx research-agent-skills install bioservices
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `scientific-databases` category with `/plugin install scientific-databases@research-agent-skills`.

## Related

- [`pathway-enrichment`](/skills/pathway-enrichment)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/bioservices/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
