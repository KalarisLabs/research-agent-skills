---
title: "waypoint-bio — AI agent skill for life sciences"
description: "Use when working with Outpost Bio's open microbiome foundation models - the Waypoint checkpoints (Waypoint-6m, Waypoint-45m, Waypoint-170m), the Atlas…"
keywords: ["microbiome", "foundation models", "metagenomics", "benchmarks"]
---

# `waypoint-bio`

**Category:** [life-sciences](/skills#life-sciences) · **License:** MIT · **Version:** 1.1 · **Includes scripts**

**Tags:** microbiome, foundation models, metagenomics, benchmarks

## When to use it

Use when working with Outpost Bio's open microbiome foundation models - the Waypoint checkpoints (Waypoint-6m, Waypoint-45m, Waypoint-170m), the Atlas pretraining corpus, the Compass eight-task benchmark, or the `waypoint` CLI from the `waypoint-bio` package. Covers embedding microbiome samples, fine-tuning on taxonomic abundance data, benchmarking a checkpoint on Compass, pretraining a GPT-2 model on taxonomic abundance profiles, and converting MetaPhlAn, Kraken2, QIIME 2, or MGnify abundance tables into waypoint format.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get embeddings for my gut 16S samples from the 45M Waypoint model?"*
- *"I have a MetaPhlAn merged table, merged_abundance_table.txt, from 240 shotgun stool samples (IBD vs healthy, several timepoints per patient). I want to fine-tune Waypoint-6m to classify IBD. `waypoint prepare-dataset` choked on the pipe-separated clade names. How do I convert it and set this up properly?"*
- *"I've got about 60k public gut metagenome profiles from MGnify and want to train my own transformer that treats each sample like a sentence of taxa ordered by abundance, then see how it compares with the published numbers on the standard eight-task set. Where do I start?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill waypoint-bio

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills waypoint-bio
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`scikit-bio`](/skills/scikit-bio)
- [`distributed-llm-pretraining-torchtitan`](/skills/distributed-llm-pretraining-torchtitan)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/waypoint-bio/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
