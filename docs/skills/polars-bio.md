---
title: "polars-bio — AI agent skill for life sciences"
description: "Python library polars-bio for genomic interval operations and bioinformatics file I/O on Polars DataFrames, built on Arrow and DataFusion."
keywords: ["genomic intervals", "bioinformatics", "Polars", "genomics file formats"]
---

# `polars-bio`

**Category:** [life-sciences](/skills#life-sciences) · **License:** Apache-2.0 · **Version:** 1.1

**Tags:** genomic intervals, bioinformatics, Polars, genomics file formats

## When to use it

Python library polars-bio for genomic interval operations and bioinformatics file I/O on Polars DataFrames, built on Arrow and DataFusion. Covers overlap, nearest, merge, cluster, coverage, complement, subtract, count_overlaps, per-base pileup depth, and read/scan/write of BED, VCF, BAM, CRAM, SAM, GFF/GTF, FASTA, FASTQ, plus SQL queries over those files. Use when intersecting or merging genomic intervals in Polars. Use when reading or streaming large BED, VCF, or BAM files, including from S3, GCS, or Azure. Use when computing read depth from BAM or CRAM. Use when running SQL on genomic files. Use when migrating bioframe code to a faster alternative. Not for pandas-only workflows that do not use Polars or DataFusion.

## Example requests

Ask your agent in plain language, for example:

- *"How do I find which of my peaks fall inside gene bodies using polars? I have two Polars DataFrames of intervals."*
- *"I have a 40 GB sample.bam with a sample.bam.bai next to it on S3 (s3://lab-data/run7/sample.bam). I need per-base depth for chr20 without loading everything into RAM, and I'd like to filter it with SQL afterwards. Last time my script was killed by the OOM killer."*
- *"My bioframe pipeline for merging ATAC-seq peaks across 200 samples and then clustering them is too slow. What's a faster drop-in way to do this on a big table?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill polars-bio

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills polars-bio
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`genomic-coordinates`](/skills/genomic-coordinates)
- [`gtars`](/skills/gtars)
- [`pysam`](/skills/pysam)
- [`tiledbvcf`](/skills/tiledbvcf)
- [`vaex`](/skills/vaex)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/polars-bio/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
