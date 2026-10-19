---
title: "anndata — AI agent skill for life sciences"
description: "Data structure for annotated matrices in single-cell analysis. Use when working with .h5ad files or integrating with the scverse ecosystem."
keywords: ["single-cell", "h5ad", "scverse", "bioinformatics", "data formats"]
---

# `anndata`

**Category:** [life-sciences](/skills#life-sciences) · **License:** BSD-3-Clause license · **Version:** 1.2

**Tags:** single-cell, h5ad, scverse, bioinformatics, data formats

## When to use it

Data structure for annotated matrices in single-cell analysis. Use when working with .h5ad files or integrating with the scverse ecosystem. This is the data format skill—for analysis workflows use scanpy; for probabilistic models use scvi-tools; for population-scale queries use cellxgene-census.

## Example requests

Ask your agent in plain language, for example:

- *"How do I read a .h5ad file in backed mode so it doesn't load into RAM?"*
- *"I have three batches saved as batch1.h5ad, batch2.h5ad and batch3.h5ad with different gene panels. I ran `adata1.concatenate(adata2, adata3)` and got a FutureWarning, and the result is missing a lot of genes. How do I combine them properly, keep track of which batch each cell came from, and keep the union of genes?"*
- *"I've got a cell-by-gene count matrix in a CSV, a separate table of cell metadata (donor, tissue, sequencing run), and a gene annotation table. I want to bundle everything into one object that I can slice by cell or gene and save as a single file for collaborators in the scverse ecosystem. How should I set that up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill anndata

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills anndata
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`cellxgene-census`](/skills/cellxgene-census)
- [`scvi-tools`](/skills/scvi-tools)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/anndata/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
