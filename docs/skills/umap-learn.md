---
title: "umap-learn — AI agent skill for data science and ml"
description: "Reduces and embeds high-dimensional data with umap-learn (UMAP) in Python, including 2D/3D visualization, supervised and semi-supervised UMAP, DensMAP…"
keywords: ["UMAP", "dimensionality reduction", "embeddings", "data visualization"]
---

# `umap-learn`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** BSD-3-Clause license · **Version:** 1.3

**Tags:** UMAP, dimensionality reduction, embeddings, data visualization

## When to use it

Reduces and embeds high-dimensional data with umap-learn (UMAP) in Python, including 2D/3D visualization, supervised and semi-supervised UMAP, DensMAP, AlignedUMAP, Parametric UMAP (Keras), transform() on new data, and inverse transforms. Use when visualizing high-dimensional data as a 2D or 3D embedding, preprocessing features for HDBSCAN clustering, using partial labels to guide an embedding, aligning embeddings across time points or batches, or projecting unseen samples into a trained embedding. Tune n_neighbors, min_dist, n_components, and metric. Not for linear PCA or t-SNE-specific workflows.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get a 2D UMAP plot of my 5000x300 feature matrix?"*
- *"I'm analysing scRNA-seq from mouse cortex in cells.h5ad, with 20k cells after PCA to 50 components. I want to cluster with HDBSCAN. I ran UMAP with defaults to 2D and got many tiny fragmented clusters. What should I change? Please write the code."*
- *"I have mass-spec proteomics profiles for 10,000 samples, and only about 300 have a confirmed disease subtype label. I'd like a low-dimensional map that uses those few labels to pull similar samples together. Later I need to place new patients' samples onto the same map without refitting. How should I do this?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill umap-learn

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills umap-learn
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [`sentence-transformers`](/skills/sentence-transformers)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/umap-learn/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
