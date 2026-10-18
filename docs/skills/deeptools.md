---
title: "deeptools — AI agent skill for life sciences"
description: "Runs deepTools command-line programs on NGS alignment data: bamCoverage and bamCompare for BAM to bigWig/bedGraph with RPGC, CPM, RPKM or BPM normalization…"
keywords: ["NGS", "ChIP-seq", "coverage", "bigWig", "genomics", "bioinformatics"]
---

# `deeptools`

**Category:** [life-sciences](/skills#life-sciences) · **License:** BSD license · **Version:** 1.3 · **Includes scripts**

**Tags:** NGS, ChIP-seq, coverage, bigWig, genomics, bioinformatics

## When to use it

Runs deepTools command-line programs on NGS alignment data: bamCoverage and bamCompare for BAM to bigWig/bedGraph with RPGC, CPM, RPKM or BPM normalization, multiBamSummary with plotCorrelation and plotPCA, plotFingerprint, computeMatrix with plotHeatmap and plotProfile, and alignmentSieve with --ATACshift. Use when converting BAM files to normalized coverage tracks. Use when checking ChIP-seq quality or comparing replicates. Use when plotting signal around TSS or peak regions. Use when comparing treatment versus control samples. Use when building ChIP-seq, RNA-seq or ATAC-seq coverage workflows. Not for peak calling or differential expression analysis.

## Example requests

Ask your agent in plain language, for example:

- *"How do I turn my sorted BAM into a bigWig I can load in IGV?"*
- *"I have H3K27ac ChIP-seq for mouse (mm10) in treat_rep1.bam, treat_rep2.bam and input.bam, all paired-end and indexed. I need a bigWig of treatment over input as log2 ratio, and I want to check that the two replicates agree before I trust it. What commands should I run?"*
- *"I've got ATAC-seq alignments for human cells and want accessibility signal shown as a heatmap centered on transcription start sites, with the reads corrected for transposase insertion offset first. How should I do that?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill deeptools

# Kalaris Labs installer with checksum verification
npx research-agent-skills install deeptools
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/deeptools/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
