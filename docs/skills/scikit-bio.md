---
title: "scikit-bio — AI agent skill for life sciences"
description: "Python library scikit-bio for biological sequence and community-ecology analysis: DNA/RNA/protein sequences, pair_align alignment, phylogenetic trees (NJ…"
keywords: ["bioinformatics", "microbial ecology", "diversity analysis", "phylogenetics", "sequences"]
---

# `scikit-bio`

**Category:** [life-sciences](/skills#life-sciences) · **License:** BSD-3-Clause license · **Version:** 1.2

**Tags:** bioinformatics, microbial ecology, diversity analysis, phylogenetics, sequences

## When to use it

Python library scikit-bio for biological sequence and community-ecology analysis: DNA/RNA/protein sequences, pair_align alignment, phylogenetic trees (NJ, UPGMA, GME/BME, Newick), alpha/beta diversity including Faith's PD and UniFrac, PCoA/CCA/RDA ordination, PERMANOVA/ANOSIM/Mantel tests, ancom and dirmult differential abundance, BIOM tables, and FASTA/FASTQ/GenBank I/O. Use when computing microbiome diversity from a BIOM or feature table. Use when running PCoA and PERMANOVA on a distance matrix. Use when building or comparing phylogenetic trees from sequences. Use when reading, converting, or aligning FASTA/FASTQ/GenBank/Newick data. Use when testing differential abundance in compositional count data. Not for general-purpose sequence scripting where Biopython is enough.

## Example requests

Ask your agent in plain language, for example:

- *"How do I run PERMANOVA on a distance matrix in skbio?"*
- *"I have a QIIME2 export, feature-table.biom, plus a rooted tree.nwk from the same ASVs and metadata.tsv with a 'treatment' column. I need Faith's PD per sample, weighted UniFrac between samples, then a PCoA and a test of whether treatment groups differ. My faith_pd call raises an error about taxa not found in the tree. What's the right code?"*
- *"I have 16S amplicon counts from gut samples in two diet groups. I want to know which taxa are significantly more abundant in one group, and I know the data are compositional and have lots of zeros. What should I do?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill scikit-bio

# Kalaris Labs installer with checksum verification
npx research-agent-skills install scikit-bio
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`biopython`](/skills/biopython)
- [`etetoolkit`](/skills/etetoolkit)
- [`waypoint-bio`](/skills/waypoint-bio)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/scikit-bio/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
