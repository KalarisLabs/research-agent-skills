---
title: "scvi-tools — AI agent skill for life sciences"
description: "Trains and applies scvi-tools probabilistic deep generative models (scVI, scANVI, totalVI, MultiVI, PeakVI, DestVI, Solo, CellAssign, MrVI and others) on…"
keywords: ["single-cell", "deep generative models", "batch correction", "cell type annotation"]
---

# `scvi-tools`

**Category:** [life-sciences](/skills#life-sciences) · **License:** BSD-3-Clause license · **Version:** 1.2

**Tags:** single-cell, deep generative models, batch correction, cell type annotation

## When to use it

Trains and applies scvi-tools probabilistic deep generative models (scVI, scANVI, totalVI, MultiVI, PeakVI, DestVI, Solo, CellAssign, MrVI and others) on AnnData or MuData single-cell data using PyTorch. Covers batch correction, integration, cell type annotation, probabilistic differential expression, and scRNA-seq, ATAC-seq, CITE-seq, spatial and methylation data. Use when integrating batches or datasets with scVI, annotating cells with scANVI, jointly modeling RNA and protein or ATAC, deconvolving spatial spots, or testing differential expression with uncertainty. For standard preprocessing and clustering pipelines, use scanpy instead.

## Example requests

Ask your agent in plain language, for example:

- *"How do I fix batch effects across 4 donors using scVI?"*
- *"I have pbmc_cite.h5mu with RNA and a 'protein_expression' layer from 3 10x CITE-seq lanes. I ran TOTALVI.setup_mudata and then model.train() and got a NaN loss after a few epochs. The protein counts include some isotype controls. What should I check, and how do I get a joint latent space and denoised protein values afterward?"*
- *"I have a reference scRNA-seq atlas with cell type labels and a new unlabeled query dataset from a different lab. I want to transfer the labels onto the query cells and get a confidence for each assignment, without retraining everything from scratch if possible."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill scvi-tools

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills scvi-tools
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`anndata`](/skills/anndata)
- [`cellxgene-census`](/skills/cellxgene-census)
- [`scanpy`](/skills/scanpy)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/scvi-tools/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
