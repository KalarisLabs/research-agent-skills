---
title: "cellxgene-census — AI agent skill for scientific databases"
description: "Query the CZ CELLxGENE Census programmatically for versioned public single-cell and spatial transcriptomics data."
keywords: ["single-cell", "transcriptomics", "public datasets", "spatial transcriptomics", "bioinformatics"]
---

# `cellxgene-census`

**Category:** [scientific-databases](/skills#scientific-databases) · **License:** MIT · **Version:** 1.3

**Tags:** single-cell, transcriptomics, public datasets, spatial transcriptomics, bioinformatics

## When to use it

Query the CZ CELLxGENE Census programmatically for versioned public single-cell and spatial transcriptomics data. Use when you need population-scale cell metadata, gene expression slices, Census summary counts, source H5AD URIs/downloads, embeddings, spatial Census data, or reference atlas comparisons across organisms, tissues, diseases, assays, and cell types. For analyzing your own local single-cell data use scanpy, anndata, or scvi-tools.

## Example requests

Ask your agent in plain language, for example:

- *"How many primary human B cells are in the latest Census LTS release, broken down by tissue?"*
- *"I'm writing a methods section for a lung fibrosis paper. I need all primary Homo sapiens cells from lung with disease 'pulmonary fibrosis' from CELLxGENE, only the columns cell_type, donor_id, dataset_id and assay, plus expression for SFTPC and KRT5, loaded into an AnnData I can pass to scanpy. My laptop has 16 GB RAM and my first attempt with get_anndata crashed with a memory error."*
- *"I want to train a cell type classifier on millions of public human brain single-cell profiles without downloading every dataset by hand. What's the right way to stream that data into PyTorch and keep the training set reproducible?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill cellxgene-census

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills cellxgene-census
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `scientific-databases` category with `/plugin install scientific-databases@research-agent-skills`.

## Related

- [`anndata`](/skills/anndata)
- [`arboreto`](/skills/arboreto)
- [`scvi-tools`](/skills/scvi-tools)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/cellxgene-census/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
