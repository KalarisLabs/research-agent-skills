---
title: "scanpy — AI agent skill for life sciences"
description: "Standard single-cell RNA-seq analysis pipeline."
keywords: ["single-cell RNA-seq", "scRNA-seq", "clustering", "UMAP", "bioinformatics"]
---

# `scanpy`

**Category:** [life-sciences](/skills#life-sciences) · **License:** BSD-3-Clause · **Version:** 1.6 · **Includes scripts**

**Tags:** single-cell RNA-seq, scRNA-seq, clustering, UMAP, bioinformatics

## When to use it

Standard single-cell RNA-seq analysis pipeline. Use for QC, normalization, dimensionality reduction (PCA/UMAP/t-SNE), clustering, differential expression, visualization, and converting R-friendly single-cell formats such as Seurat or SingleCellExperiment RDS files into h5ad for Scanpy. Best for exploratory scRNA-seq analysis with established workflows. For deep learning models use scvi-tools; for data format questions use anndata.

## Example requests

Ask your agent in plain language, for example:

- *"How do I cluster my PBMC h5ad and get UMAP plots?"*
- *"I have a mouse cortex 10x dataset in ./filtered_feature_bc_matrix/ (3 samples, 'sample' column to be added). I need to run QC with mito filtering at a threshold that makes sense for brain tissue, flag doublets, normalize, integrate the samples, and find markers per cluster. Running sc.tl.louvain gives me a deprecation warning. What should I do?"*
- *"A collaborator sent me a Seurat object saved as pbmc_annotated.rds with cell type labels in the metadata. I want to explore it in Python and look at the clusters and make a dotplot of marker genes. How should I get started?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill scanpy

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills scanpy
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`scvi-tools`](/skills/scvi-tools)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/scanpy/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
