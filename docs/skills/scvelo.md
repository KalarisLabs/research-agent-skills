---
title: "scvelo — AI agent skill for life sciences"
description: "Performs RNA velocity analysis with scVelo on single-cell RNA-seq AnnData objects that have spliced and unspliced layers (from velocyto, STARsolo…"
keywords: ["RNA velocity", "single-cell", "cell trajectories", "transcriptomics"]
---

# `scvelo`

**Category:** [life-sciences](/skills#life-sciences) · **License:** BSD-3-Clause · **Version:** 1.2 · **Includes scripts**

**Tags:** RNA velocity, single-cell, cell trajectories, transcriptomics

## When to use it

Performs RNA velocity analysis with scVelo on single-cell RNA-seq AnnData objects that have spliced and unspliced layers (from velocyto, STARsolo, kallisto|bustools, or alevin-fry). Covers stochastic and dynamical velocity models, velocity graphs and embedding arrows, latent time, PAGA trajectory graphs, and driver gene ranking. Use when inferring differentiation direction from snapshot data, estimating latent time from splicing kinetics, finding driver genes of a trajectory, or adding velocity arrows to a Scanpy UMAP. Not for fate probability modeling (use CellRank) or datasets without unspliced counts.

## Example requests

Ask your agent in plain language, for example:

- *"How do I add RNA velocity arrows to my Scanpy UMAP? I have a loom file from velocyto."*
- *"I have pancreas_endocrine.h5ad (mouse E15.5 endocrinogenesis, ~3,700 cells) with spliced and unspliced layers from STARsolo Velocyto. I ran scv.tl.velocity with mode='stochastic' and the arrows look random and point backwards from Ductal toward Ngn3 progenitors. Switch to the dynamical model, compute latent time, and give me the top driver genes per cluster. Running recover_dynamics hits a memory error on my laptop."*
- *"I have single-cell data from differentiating blood progenitors and only one snapshot timepoint. I want to figure out which cells are the earliest and in which direction they are moving, using the intronic versus exonic read information, and get a continuous ordering of the cells along that process."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill scvelo

# Kalaris Labs installer with checksum verification
npx research-agent-skills install scvelo
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/scvelo/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
