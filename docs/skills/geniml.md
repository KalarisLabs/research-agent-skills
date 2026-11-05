---
title: "geniml — AI agent skill for life sciences"
description: "Plans and audits local genomic-interval machine learning workflows with Geniml (0.8.4) and Gtars: validates BED files against chromosome sizes and assembly…"
keywords: ["genomic intervals", "BED files", "machine learning", "embeddings", "genomics"]
---

# `geniml`

**Category:** [life-sciences](/skills#life-sciences) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** genomic intervals, BED files, machine learning, embeddings, genomics

## When to use it

Plans and audits local genomic-interval machine learning workflows with Geniml (0.8.4) and Gtars: validates BED files against chromosome sizes and assembly contracts, plans Region2Vec, scEmbed, and BEDspace runs, checks model, tokenizer, and universe.bed compatibility, and assesses consensus universes (CC, CCF, ML, HMM, assess-universe). Bundled scripts only validate or plan; they do not train. Use when checking BED coordinates, contigs, or assembly before analysis. Use when planning Region2Vec or scEmbed training on tokenized Parquet data. Use when verifying that a checkpoint, config.yaml, and universe match. Use when building or assessing a consensus peak universe. Use when reviewing BEDbase or Hugging Face download risks. Not for general BED manipulation or peak calling; use bedtools or similar tools.

## Example requests

Ask your agent in plain language, for example:

- *"Can you check my peaks.bed against hg38.chrom.sizes before I run anything? Worried about chr naming."*
- *"I exported tokenized ATAC regions to data/tokens.parquet (list column 'tokens') using universe.bed from our GRCh38 lab pipeline and want to train Region2Vec. Before I burn GPU time, I got 'size mismatch for projection.weight' when loading models/r2v/checkpoint.pt with a config.yaml from a colleague. Help me figure out what's wrong and plan the run."*
- *"We have peak calls from 40 ChIP-seq experiments across several labs and want one common set of regions to use as a shared vocabulary for embedding models, then measure how well it fits our data. What's a safe way to go about it?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill geniml

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills geniml
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`genomic-coordinates`](/skills/genomic-coordinates)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/geniml/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
