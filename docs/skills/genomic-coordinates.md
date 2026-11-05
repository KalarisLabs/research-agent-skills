---
title: "genomic-coordinates — AI agent skill for scientific databases"
description: "Convert genomic intervals between coordinate conventions, normalise and compare variant representations, and detect assembly or contig-naming mismatches…"
keywords: ["genomic coordinates", "liftover", "variant normalization", "genome assemblies", "bioinformatics"]
---

# `genomic-coordinates`

**Category:** [scientific-databases](/skills#scientific-databases) · **License:** MIT · **Version:** 1.1 · **Includes scripts**

**Tags:** genomic coordinates, liftover, variant normalization, genome assemblies, bioinformatics

## When to use it

Convert genomic intervals between coordinate conventions, normalise and compare variant representations, and detect assembly or contig-naming mismatches before they corrupt an analysis. Use whenever coordinates cross a format, tool, or assembly boundary - converting between BED, GFF/GTF, VCF, SAM/BAM, WIG, PSL, genePred, Picard interval_list, or region strings; reconciling 0-based half-open with 1-based inclusive; left-aligning or trimming indels; checking whether two variant records describe the same change; mapping genomic to transcript, CDS, or protein positions; auditing a BED/GTF/VCF for convention violations; or diagnosing GRCh37 vs hg19 vs GRCh38 vs T2T, chr-prefix, and liftover problems. Triggers include "off by one", "0-based", "1-based", "half-open", "coordinate system", "left-align", "normalize variant", "bcftools norm", "chr prefix", "wrong genome build", "liftover", "REF mismatch", and "HGVS".

## Example requests

Ask your agent in plain language, for example:

- *"My peak caller output BED looks one base off when I load it next to my GTF annotations in IGV. What's going on?"*
- *"I'm merging ClinVar (GRCh38 VCF) with my cohort's VCF, but a bunch of known pathogenic indels in my samples (e.g. BRCA1 deletions in repeat regions) show up as novel. I'm doing a plain join on CHROM/POS/REF/ALT in pandas. bcftools says 'REF does not match the reference' for a few records too. How do I fix this?"*
- *"I have a transcript-level HGVS c.742C>T for a TP53 variant from a clinical report and need the genomic position so I can look it up in my aligned data. Which transcript, which strand, and how do I get to the genomic coordinate safely?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill genomic-coordinates

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills genomic-coordinates
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `scientific-databases` category with `/plugin install scientific-databases@research-agent-skills`.

## Related

- [`alphagenome`](/skills/alphagenome)
- [`folklore-variant-evidence`](/skills/folklore-variant-evidence)
- [`geniml`](/skills/geniml)
- [`polars-bio`](/skills/polars-bio)
- [`gtars`](/skills/gtars)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/genomic-coordinates/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
