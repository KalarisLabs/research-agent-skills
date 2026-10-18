---
title: "tiledbvcf — AI agent skill for life sciences"
description: "Stores and queries genomic variant data in TileDB-VCF datasets using the tiledbvcf Python API and CLI (create, store, export, list, stat)."
keywords: ["genomic variants", "VCF", "variant storage", "population genomics"]
---

# `tiledbvcf`

**Category:** [life-sciences](/skills#life-sciences) · **License:** MIT · **Version:** 1.1

**Tags:** genomic variants, VCF, variant storage, population genomics

## When to use it

Stores and queries genomic variant data in TileDB-VCF datasets using the tiledbvcf Python API and CLI (create, store, export, list, stat). Covers ingesting single-sample VCF/BCF files with .csi or .tbi indexes, adding samples incrementally, querying regions and samples in parallel, and exporting to VCF/BCF or TSV, on local disk or S3, Azure, and GCS. Use when building a variant database for a cohort, adding new samples to an existing dataset, querying specific regions across many samples, exporting subsets of a large VCF collection, or preparing population genomics data such as allele frequency or GWAS inputs. Not for multi-sample VCFs, which are unsupported, or for one-off parsing of a single VCF file.

## Example requests

Ask your agent in plain language, for example:

- *"How do I add 20 new samples to an existing TileDB-VCF dataset without redoing the old ones?"*
- *"I've got 400 single-sample gVCFs from our mouse cohort in s3://lab-mouse/vcfs/ (each with a .tbi). I ran `tiledbvcf store` into s3://lab-mouse/db and it died with an out-of-memory error partway through. How should I set it up so I can resume and then pull chr2:1000000-2000000 for 50 named samples into a TSV with sample, pos, ref, alt, and genotype?"*
- *"We're preparing inputs for a GWAS and a rare-variant burden test. Our sequencing center delivers one VCF per individual, about 600 people, and every analysis starts by pulling the same few hundred candidate gene regions across everyone. Re-scanning the files each time is painfully slow. What's a better way to organize this data?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill tiledbvcf

# Kalaris Labs installer with checksum verification
npx research-agent-skills install tiledbvcf
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`polars-bio`](/skills/polars-bio)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/tiledbvcf/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
