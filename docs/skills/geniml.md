---
title: "geniml — AI agent skill for life sciences"
description: "Plans and audits local genomic-interval machine learning workflows with Geniml (0.8.4) and Gtars: validates BED files against chromosome sizes and assembl…"
---

# `geniml`

> Plans and audits local genomic-interval machine learning workflows with Geniml (0.8.4) and Gtars: validates BED files against chromosome sizes and assembly contracts, plans Region2Vec, scEmbed, and BEDspace runs, checks model, tokenizer, and universe.bed compatibility, and assesses consensus universes (CC, CCF, ML, HMM, assess-universe). Bundled scripts only validate or plan; they do not train. Use when checking BED coordinates, contigs, or assembly before analysis. Use when planning Region2Vec or scEmbed training on tokenized Parquet data. Use when verifying that a checkpoint, config.yaml, and universe match. Use when building or assessing a consensus peak universe. Use when reviewing BEDbase or Hugging Face download risks. Not for general BED manipulation or peak calling; use bedtools or similar tools.

**Category:** [life-sciences](/skills#life-sciences) · **License:** MIT · **Version:** 1.2

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill geniml
```

## When to use it

Plans and audits local genomic-interval machine learning workflows with Geniml (0.8.4) and Gtars: validates BED files against chromosome sizes and assembly contracts, plans Region2Vec, scEmbed, and BEDspace runs, checks model, tokenizer, and universe.bed compatibility, and assesses consensus universes (CC, CCF, ML, HMM, assess-universe). Bundled scripts only validate or plan; they do not train. Use when checking BED coordinates, contigs, or assembly before analysis. Use when planning Region2Vec or scEmbed training on tokenized Parquet data. Use when verifying that a checkpoint, config.yaml, and universe match. Use when building or assessing a consensus peak universe. Use when reviewing BEDbase or Hugging Face download risks. Not for general BED manipulation or peak calling; use bedtools or similar tools.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/geniml/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
