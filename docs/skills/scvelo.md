---
title: "scvelo — AI agent skill for life sciences"
description: "Performs RNA velocity analysis with scVelo on single-cell RNA-seq AnnData objects that have spliced and unspliced layers (from velocyto, STARsolo, kallist…"
---

# `scvelo`

> Performs RNA velocity analysis with scVelo on single-cell RNA-seq AnnData objects that have spliced and unspliced layers (from velocyto, STARsolo, kallisto|bustools, or alevin-fry). Covers stochastic and dynamical velocity models, velocity graphs and embedding arrows, latent time, PAGA trajectory graphs, and driver gene ranking. Use when inferring differentiation direction from snapshot data, estimating latent time from splicing kinetics, finding driver genes of a trajectory, or adding velocity arrows to a Scanpy UMAP. Not for fate probability modeling (use CellRank) or datasets without unspliced counts.

**Category:** [life-sciences](/skills#life-sciences) · **License:** BSD-3-Clause · **Version:** 1.2

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill scvelo
```

## When to use it

Performs RNA velocity analysis with scVelo on single-cell RNA-seq AnnData objects that have spliced and unspliced layers (from velocyto, STARsolo, kallisto|bustools, or alevin-fry). Covers stochastic and dynamical velocity models, velocity graphs and embedding arrows, latent time, PAGA trajectory graphs, and driver gene ranking. Use when inferring differentiation direction from snapshot data, estimating latent time from splicing kinetics, finding driver genes of a trajectory, or adding velocity arrows to a Scanpy UMAP. Not for fate probability modeling (use CellRank) or datasets without unspliced counts.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/scvelo/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
