---
title: "onekgpd — AI agent skill for scientific databases"
description: "Query the 1000 Genomes Project dataset (3,202 whole-genome-sequenced individuals, GRCh38) at the level of individual participants."
keywords: ["1000 Genomes", "population genetics", "genomic variants", "human genomics"]
---

# `onekgpd`

**Category:** [scientific-databases](/skills#scientific-databases) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** 1000 Genomes, population genetics, genomic variants, human genomics

## When to use it

Query the 1000 Genomes Project dataset (3,202 whole-genome-sequenced individuals, GRCh38) at the level of individual participants. Use when a question is about individuals or variants in the 1000 Genomes Project cohort: which individuals carry variants matching specific criteria in a gene or region, which individuals are homozygous-reference at a position, which variants exist in the dataset or carried by specified individuals in a gene or region, the relatedness between two specified individuals. Variants are returned with 1000 Genomes allele frequencies (AF), gnomAD v4.1 exome and genome AF, AlphaMissense score, and HGVSp annotations.

## Example requests

Ask your agent in plain language, for example:

- *"Who in 1000 Genomes is homozygous for rare missense variants in CFTR? Rare = gnomAD genome AF under 0.1%."*
- *"kinship HG00096 NA21130"*
- *"I'm following up a hit in BRCA1 for a paper. I have the region chr17:43044295-43125364 from an old UCSC hg19 browser session. I want to see which variants ClinVar calls pathogenic or likely pathogenic that are carried by HG00096, HG00097 and NA12878 in the 1000 Genomes high-coverage cohort, with their AlphaMissense scores."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill onekgpd

# Kalaris Labs installer with checksum verification
npx research-agent-skills install onekgpd
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `scientific-databases` category with `/plugin install scientific-databases@research-agent-skills`.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/onekgpd/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
