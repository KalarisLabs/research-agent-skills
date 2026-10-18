---
title: "arboreto — AI agent skill for life sciences"
description: "Infer gene regulatory networks (GRNs) from gene expression data using scalable algorithms (GRNBoost2, GENIE3)."
keywords: ["gene regulatory networks", "GRNBoost2", "transcriptomics", "single-cell", "bioinformatics"]
---

# `arboreto`

**Category:** [life-sciences](/skills#life-sciences) · **License:** BSD-3-Clause license · **Version:** 1.1 · **Includes scripts**

**Tags:** gene regulatory networks, GRNBoost2, transcriptomics, single-cell, bioinformatics

## When to use it

Infer gene regulatory networks (GRNs) from gene expression data using scalable algorithms (GRNBoost2, GENIE3). Use when analyzing transcriptomics data (bulk RNA-seq, single-cell RNA-seq) to identify transcription factor-target gene relationships and regulatory interactions. Supports distributed computation for large-scale datasets.

## Example requests

Ask your agent in plain language, for example:

- *"How do I infer a TF-target network from my expression matrix with GRNBoost2?"*
- *"I have a 12,000-cell scRNA-seq dataset in pbmc.h5ad and a list of human TFs in allTFs_hg38.txt. I ran grnboost2 in a script on Windows and got a Dask error: 'An attempt has been made to start a new process before the current process has finished its bootstrapping phase.' How do I fix this and run it properly?"*
- *"I want to figure out which transcription factors are likely driving gene expression changes across my 200 bulk liver samples. I'd like a ranked list of regulator-to-target gene links I can then feed into a downstream regulon analysis. What should I do?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill arboreto

# Kalaris Labs installer with checksum verification
npx research-agent-skills install arboreto
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`bulk-rnaseq`](/skills/bulk-rnaseq)
- [`cellxgene-census`](/skills/cellxgene-census)
- [`scikit-learn`](/skills/scikit-learn)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/arboreto/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
