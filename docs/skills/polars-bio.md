---
title: "polars-bio — AI agent skill for life sciences"
description: "Python library polars-bio for genomic interval operations and bioinformatics file I/O on Polars DataFrames, built on Arrow and DataFusion."
---

# `polars-bio`

> Python library polars-bio for genomic interval operations and bioinformatics file I/O on Polars DataFrames, built on Arrow and DataFusion. Covers overlap, nearest, merge, cluster, coverage, complement, subtract, count_overlaps, per-base pileup depth, and read/scan/write of BED, VCF, BAM, CRAM, SAM, GFF/GTF, FASTA, FASTQ, plus SQL queries over those files. Use when intersecting or merging genomic intervals in Polars. Use when reading or streaming large BED, VCF, or BAM files, including from S3, GCS, or Azure. Use when computing read depth from BAM or CRAM. Use when running SQL on genomic files. Use when migrating bioframe code to a faster alternative. Not for pandas-only workflows that do not use Polars or DataFusion.

**Category:** [life-sciences](/skills#life-sciences) · **License:** Apache-2.0 · **Version:** 1.1

## Install

```bash
npx research-agent-skills install polars-bio
npx skills add KalarisLabs/research-agent-skills --skill polars-bio
```

## When to use it

Python library polars-bio for genomic interval operations and bioinformatics file I/O on Polars DataFrames, built on Arrow and DataFusion. Covers overlap, nearest, merge, cluster, coverage, complement, subtract, count_overlaps, per-base pileup depth, and read/scan/write of BED, VCF, BAM, CRAM, SAM, GFF/GTF, FASTA, FASTQ, plus SQL queries over those files. Use when intersecting or merging genomic intervals in Polars. Use when reading or streaming large BED, VCF, or BAM files, including from S3, GCS, or Azure. Use when computing read depth from BAM or CRAM. Use when running SQL on genomic files. Use when migrating bioframe code to a faster alternative. Not for pandas-only workflows that do not use Polars or DataFusion.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/polars-bio/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
