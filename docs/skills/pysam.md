---
title: "pysam — AI agent skill for life sciences"
description: "Python/HTSlib workflows for genomic files."
keywords: ["SAM/BAM", "VCF", "genomics", "sequencing data", "bioinformatics"]
---

# `pysam`

**Category:** [life-sciences](/skills#life-sciences) · **License:** MIT · **Version:** 2.1 · **Includes scripts**

**Tags:** SAM/BAM, VCF, genomics, sequencing data, bioinformatics

## When to use it

Python/HTSlib workflows for genomic files. Use when reading, querying, filtering, or writing SAM/BAM/CRAM, VCF/BCF, FASTA/FASTQ, or tabix data with pysam, including pileup, coverage, indexing, and CRAM references.

## Example requests

Ask your agent in plain language, for example:

- *"How do I pull all reads overlapping chr7:55,019,000-55,019,100 from a BAM in Python?"*
- *"I have sample42.cram aligned to GRCh38 and I'm getting 'failed to populate reference' when I iterate over it in a script, on a machine with no internet. I want to convert it to BAM and then count per-base depth over chr1:1,000,000-1,000,500, ignoring reads with MAPQ&lt;20 and bases with Q&lt;20. What should I do?"*
- *"I have a multi-sample VCF and need a smaller file containing only 3 of the cohort's samples, keeping only PASS variants. I'd also like to add a new INFO annotation. I want to do this in Python and keep the output indexed so I can query it by region later."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pysam

# Kalaris Labs installer with checksum verification
npx research-agent-skills install pysam
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`polars-bio`](/skills/polars-bio)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pysam/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
