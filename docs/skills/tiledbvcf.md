---
title: "tiledbvcf — AI agent skill for life sciences"
description: "Stores and queries genomic variant data in TileDB-VCF datasets using the tiledbvcf Python API and CLI (create, store, export, list, stat)."
---

# `tiledbvcf`

> Stores and queries genomic variant data in TileDB-VCF datasets using the tiledbvcf Python API and CLI (create, store, export, list, stat). Covers ingesting single-sample VCF/BCF files with .csi or .tbi indexes, adding samples incrementally, querying regions and samples in parallel, and exporting to VCF/BCF or TSV, on local disk or S3, Azure, and GCS. Use when building a variant database for a cohort, adding new samples to an existing dataset, querying specific regions across many samples, exporting subsets of a large VCF collection, or preparing population genomics data such as allele frequency or GWAS inputs. Not for multi-sample VCFs, which are unsupported, or for one-off parsing of a single VCF file.

**Category:** [life-sciences](/skills#life-sciences) · **License:** MIT · **Version:** 1.1

## Install

```bash
npx research-agent-skills install tiledbvcf
npx skills add KalarisLabs/research-agent-skills --skill tiledbvcf
```

## When to use it

Stores and queries genomic variant data in TileDB-VCF datasets using the tiledbvcf Python API and CLI (create, store, export, list, stat). Covers ingesting single-sample VCF/BCF files with .csi or .tbi indexes, adding samples incrementally, querying regions and samples in parallel, and exporting to VCF/BCF or TSV, on local disk or S3, Azure, and GCS. Use when building a variant database for a cohort, adding new samples to an existing dataset, querying specific regions across many samples, exporting subsets of a large VCF collection, or preparing population genomics data such as allele frequency or GWAS inputs. Not for multi-sample VCFs, which are unsupported, or for one-off parsing of a single VCF file.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/tiledbvcf/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
