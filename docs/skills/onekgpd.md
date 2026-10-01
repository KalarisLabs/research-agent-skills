---
title: "onekgpd — AI agent skill for scientific databases"
description: "Query the 1000 Genomes Project dataset (3,202 whole-genome-sequenced individuals, GRCh38) at the level of individual participants."
---

# `onekgpd`

> Query the 1000 Genomes Project dataset (3,202 whole-genome-sequenced individuals, GRCh38) at the level of individual participants. Use when a question is about individuals or variants in the 1000 Genomes Project cohort: which individuals carry variants matching specific criteria in a gene or region, which individuals are homozygous-reference at a position, which variants exist in the dataset or carried by specified individuals in a gene or region, the relatedness between two specified individuals. Variants are returned with 1000 Genomes allele frequencies (AF), gnomAD v4.1 exome and genome AF, AlphaMissense score, and HGVSp annotations.

**Category:** [scientific-databases](/skills#scientific-databases) · **License:** MIT · **Version:** 1.2

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill onekgpd
```

## When to use it

Query the 1000 Genomes Project dataset (3,202 whole-genome-sequenced individuals, GRCh38) at the level of individual participants. Use when a question is about individuals or variants in the 1000 Genomes Project cohort: which individuals carry variants matching specific criteria in a gene or region, which individuals are homozygous-reference at a position, which variants exist in the dataset or carried by specified individuals in a gene or region, the relatedness between two specified individuals. Variants are returned with 1000 Genomes allele frequencies (AF), gnomAD v4.1 exome and genome AF, AlphaMissense score, and HGVSp annotations.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/onekgpd/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
