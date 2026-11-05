---
title: "gget — AI agent skill for scientific databases"
description: "Queries 20+ bioinformatics databases and analysis services through the gget CLI and Python package, covering Ensembl gene search, info and sequences (ref…"
keywords: ["bioinformatics databases", "Ensembl", "BLAST", "AlphaFold", "gene lookup"]
---

# `gget`

**Category:** [scientific-databases](/skills#scientific-databases) · **License:** BSD-2-Clause license · **Version:** 1.5 · **Includes scripts**

**Tags:** bioinformatics databases, Ensembl, BLAST, AlphaFold, gene lookup

## When to use it

Queries 20+ bioinformatics databases and analysis services through the gget CLI and Python package, covering Ensembl gene search, info and sequences (ref, search, info, seq), BLAST, BLAT, MUSCLE, DIAMOND, PDB, AlphaFold, ELM, ARCHS4, CELLxGENE, Enrichr, Bgee, OpenTargets, cBioPortal, COSMIC, viral sequence downloads (virus), and 8cube mouse specificity and expression data. Use when looking up gene or transcript details, running a quick BLAST/BLAT search, fetching AlphaFold or PDB structures, running enrichment analysis on a gene list, downloading viral sequences with filters, or exploring disease and drug associations interactively. Not for batch processing or fine-grained BLAST control (use biopython) or multi-database Python pipelines (use bioservices).

## Example requests

Ask your agent in plain language, for example:

- *"quick blast of this protein sequence against nr: MKTAYIAKQRQISFVKSHFSRQLEERLGLIEVQ"*
- *"I have a list of 150 differentially expressed genes from my mouse liver RNA-seq in de_genes.txt (gene symbols). I'm on a cluster node with pip. Can you run GO biological process and KEGG enrichment on them directly from the terminal and save a CSV? I'd also like to see the top 10 terms."*
- *"I'm studying a possible drug target, EGFR. What diseases and drugs are linked to it, and is there a predicted or experimental 3D structure I could look at?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill gget

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills gget
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `scientific-databases` category with `/plugin install scientific-databases@research-agent-skills`.

## Related

- [`pathway-enrichment`](/skills/pathway-enrichment)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/gget/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
