---
title: "pydeseq2 — AI agent skill for life sciences"
description: "Runs differential expression analysis on bulk RNA-seq count data with PyDESeq2, the Python port of DESeq2."
keywords: ["differential expression", "RNA-seq", "DESeq2", "transcriptomics", "bioinformatics"]
---

# `pydeseq2`

**Category:** [life-sciences](/skills#life-sciences) · **License:** MIT · **Version:** 1.4 · **Includes scripts**

**Tags:** differential expression, RNA-seq, DESeq2, transcriptomics, bioinformatics

## When to use it

Runs differential expression analysis on bulk RNA-seq count data with PyDESeq2, the Python port of DESeq2. Covers formulaic single- and multi-factor designs, contrasts, Wald tests, Benjamini-Hochberg FDR correction, optional apeGLM LFC shrinkage, pandas and AnnData (H5AD) integration, CSV export, volcano and MA plots, and a command-line script. Use when comparing gene expression between conditions such as treated vs control, adjusting for batch or covariates, porting an R DESeq2 workflow to Python, or building a Python pipeline for differential expression from raw integer counts. Not for single-cell data or for R-based DESeq2 itself.

## Example requests

Ask your agent in plain language, for example:

- *"How do I run DESeq2 in Python on my counts table?"*
- *"I have counts.csv (60k genes x 12 samples, STAR/featureCounts output, mouse liver) and meta.csv with columns condition (ctrl/KO) and batch (b1/b2/b3). I get 'Index mismatch between counts and metadata' when I build the dataset. Please fix it and give me KO vs ctrl results adjusted for batch, with a volcano plot."*
- *"We sequenced 8 tumor and 8 normal biopsies and have a gene-level raw count matrix. I want a ranked list of genes that differ between tumor and normal, with fold changes that are shrunk so the noisy low-count genes don't dominate the ranking, and a table I can send to a collaborator."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pydeseq2

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills pydeseq2
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`bulk-rnaseq`](/skills/bulk-rnaseq)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pydeseq2/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
