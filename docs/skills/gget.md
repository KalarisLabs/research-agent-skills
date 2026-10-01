---
title: "gget — AI agent skill for scientific databases"
description: "Queries 20+ bioinformatics databases and analysis services through the gget CLI and Python package, covering Ensembl gene search, info and sequences (ref,…"
---

# `gget`

> Queries 20+ bioinformatics databases and analysis services through the gget CLI and Python package, covering Ensembl gene search, info and sequences (ref, search, info, seq), BLAST, BLAT, MUSCLE, DIAMOND, PDB, AlphaFold, ELM, ARCHS4, CELLxGENE, Enrichr, Bgee, OpenTargets, cBioPortal, COSMIC, viral sequence downloads (virus), and 8cube mouse specificity and expression data. Use when looking up gene or transcript details, running a quick BLAST/BLAT search, fetching AlphaFold or PDB structures, running enrichment analysis on a gene list, downloading viral sequences with filters, or exploring disease and drug associations interactively. Not for batch processing or fine-grained BLAST control (use biopython) or multi-database Python pipelines (use bioservices).

**Category:** [scientific-databases](/skills#scientific-databases) · **License:** BSD-2-Clause license · **Version:** 1.5

## Install

```bash
npx research-agent-skills install gget
npx skills add KalarisLabs/research-agent-skills --skill gget
```

## When to use it

Queries 20+ bioinformatics databases and analysis services through the gget CLI and Python package, covering Ensembl gene search, info and sequences (ref, search, info, seq), BLAST, BLAT, MUSCLE, DIAMOND, PDB, AlphaFold, ELM, ARCHS4, CELLxGENE, Enrichr, Bgee, OpenTargets, cBioPortal, COSMIC, viral sequence downloads (virus), and 8cube mouse specificity and expression data. Use when looking up gene or transcript details, running a quick BLAST/BLAT search, fetching AlphaFold or PDB structures, running enrichment analysis on a gene list, downloading viral sequences with filters, or exploring disease and drug associations interactively. Not for batch processing or fine-grained BLAST control (use biopython) or multi-database Python pipelines (use bioservices).

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/gget/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
