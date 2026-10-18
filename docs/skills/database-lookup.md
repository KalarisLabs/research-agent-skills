---
title: "database-lookup — AI agent skill for scientific databases"
description: "Query documented public database APIs with explicit endpoints, filters, pagination, and provenance."
keywords: ["scientific databases", "APIs", "data retrieval", "reproducibility", "provenance"]
---

# `database-lookup`

**Category:** [scientific-databases](/skills#scientific-databases) · **License:** MIT · **Version:** 1.6

**Tags:** scientific databases, APIs, data retrieval, reproducibility, provenance

## When to use it

Query documented public database APIs with explicit endpoints, filters, pagination, and provenance. Use when a scientific, regulatory, financial, or other database-backed fact must be retrieved reproducibly from a named source rather than inferred from general knowledge.

## Example requests

Ask your agent in plain language, for example:

- *"Pull all ClinVar pathogenic and likely pathogenic variants for BRCA2 and tell me exactly how you got them."*
- *"I'm building Table 2 for our manuscript (supp_targets.csv has 48 gene symbols). For each gene I need the Ensembl gene ID, the UniProt accession for human, and the max overall Open Targets association score with Parkinson's disease. My GraphQL GET calls keep returning 405 errors. Please fix this and log the queries so a reviewer can rerun them."*
- *"What was the US unemployment rate each month in 2023, and I need to cite where the numbers come from so my co-author can re-pull them."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill database-lookup

# Kalaris Labs installer with checksum verification
npx research-agent-skills install database-lookup
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `scientific-databases` category with `/plugin install scientific-databases@research-agent-skills`.

## Related

- [`alphagenome`](/skills/alphagenome)
- [`bulk-rnaseq`](/skills/bulk-rnaseq)
- [`firecrawl-research-index`](/skills/firecrawl-research-index)
- [`protocolsio-integration`](/skills/protocolsio-integration)
- [`folklore-variant-evidence`](/skills/folklore-variant-evidence)
- [`pathway-enrichment`](/skills/pathway-enrichment)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/database-lookup/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
