---
title: "folklore-variant-evidence — AI agent skill for life sciences"
description: "Retrieve ClinGen gene-disease validity assertions for a public gene or disease, and review source-linked public evidence and literature for one supported…"
keywords: ["clinical genomics", "variant interpretation", "ClinGen", "germline variants", "genetics"]
---

# `folklore-variant-evidence`

**Category:** [life-sciences](/skills#life-sciences) · **License:** MIT · **Version:** 1.0

**Tags:** clinical genomics, variant interpretation, ClinGen, germline variants, genetics

## When to use it

Retrieve ClinGen gene-disease validity assertions for a public gene or disease, and review source-linked public evidence and literature for one supported GRCh38 germline nuclear SNV or simple indel through Folklore Clinical Variant Interpretation MCP. Use when a scientific agent must branch deterministically on resolved, ambiguous, not-found, invalid, unsupported, or unavailable variant outcomes; chain a resolved public variant into related literature or publication details; or preserve evidence provenance without accepting patient, phenotype, family, segregation, or private case data.

## Example requests

Ask your agent in plain language, for example:

- *"Which genes does ClinGen say are definitively linked to Lynch syndrome? Just list the assertions."*
- *"I'm writing up my methods for a paper on BRCA1 and need to check NC_000017.12:g.43057062T>C (GRCh38) in a public evidence source that gives provenance. Can you pull the evidence, and if it resolves, find the literature that directly mentions that exact variant? I'd also like details on the top PMID, including retraction status."*
- *"I have a public dbSNP rsID, rs80357914, and I'm not sure what it maps to. Look it up and tell me what the evidence says, but don't just guess if it's unclear which variant I mean."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill folklore-variant-evidence

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills folklore-variant-evidence
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`alphagenome`](/skills/alphagenome)
- [`bgpt-paper-search`](/skills/bgpt-paper-search)
- [`database-lookup`](/skills/database-lookup)
- [`genomic-coordinates`](/skills/genomic-coordinates)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/folklore-variant-evidence/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
