---
title: "gtars — AI agent skill for life sciences"
description: "Inspects and plans work with Gtars, the Rust/Python/CLI toolkit for genomic intervals: BED RegionSet set algebra (reduce, setdiff, intersect, closest…"
keywords: ["genomic intervals", "BED files", "peak sets", "genomics", "bioinformatics"]
---

# `gtars`

**Category:** [life-sciences](/skills#life-sciences) · **License:** MIT · **Version:** 1.3 · **Includes scripts**

**Tags:** genomic intervals, BED files, peak sets, genomics, bioinformatics

## When to use it

Inspects and plans work with Gtars, the Rust/Python/CLI toolkit for genomic intervals: BED RegionSet set algebra (reduce, setdiff, intersect, closest, cluster, gaps), overlap counts, consensus peak sets, coverage, tokenizers, fragment processing, and refget/BEDbase stores. Use when merging or comparing BED interval sets, building a consensus or universe from peaks, tokenizing regions for ML models, working with fragment files, or planning refget sequence-collection and BEDbase cache use. Use when checking BED coordinates, contigs, or strand before running gtars. Not for general BAM/VCF processing; use samtools or bedtools for that.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get the union of two peak BED files into one non-overlapping set with gtars?"*
- *"I have 24 ATAC-seq replicate peak files (hg38, narrowPeak trimmed to BED) in ./peaks/ from 8 donors. I want a consensus peak set to use as the universe for tokenizing cells for a scEmbed-style model, and then train/val/test splits. I tried `from gtars import RegionSet` and got an ImportError. Can you plan this out?"*
- *"I have a few thousand enhancer regions and a set of GWAS hit windows. I want to know which enhancers sit nearest each hit, plus the stretches of genome not covered by either list. Some of my files use '1' and others use 'chr1' for contigs. What's the safest way to go about it?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill gtars

# Kalaris Labs installer with checksum verification
npx research-agent-skills install gtars
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`genomic-coordinates`](/skills/genomic-coordinates)
- [`polars-bio`](/skills/polars-bio)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/gtars/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
