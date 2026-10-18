---
title: "biopython — AI agent skill for life sciences"
description: "Provides Biopython (Bio.Seq, Bio.SeqIO, Bio.Align, Bio.Entrez, Bio.Blast, Bio.PDB, Bio.Phylo, Bio.motifs, Bio.SeqUtils, Bio.Restriction) for sequence…"
keywords: ["sequence analysis", "bioinformatics", "BLAST", "NCBI", "phylogenetics", "Python"]
---

# `biopython`

**Category:** [life-sciences](/skills#life-sciences) · **License:** Biopython License Agreement · **Version:** 1.3

**Tags:** sequence analysis, bioinformatics, BLAST, NCBI, phylogenetics, Python

## When to use it

Provides Biopython (Bio.Seq, Bio.SeqIO, Bio.Align, Bio.Entrez, Bio.Blast, Bio.PDB, Bio.Phylo, Bio.motifs, Bio.SeqUtils, Bio.Restriction) for sequence handling, file parsing, NCBI access, BLAST, structures, and phylogenetic trees in Python. Reads, writes, and converts FASTA, GenBank, FASTQ, PDB, mmCIF, Newick, and NEXUS files. Use when manipulating or translating DNA, RNA, or protein sequences, converting sequence file formats, fetching records from NCBI via Entrez, running or parsing BLAST searches, doing pairwise or multiple sequence alignment, analyzing PDB structures, or building and editing phylogenetic trees. For quick lookups use gget; for multi-service integration use bioservices.

## Example requests

Ask your agent in plain language, for example:

- *"How do I reverse-complement a DNA string and translate it in Python?"*
- *"I have a GenBank file called plasmid_pUC19.gb and need a FASTA of just the CDS translations for each annotated gene, plus a GFF-free list of locus_tags. I'm getting 'ValueError: Sequence content is undefined' on some features when I call feature.extract(record.seq). What's going on and how do I fix it?"*
- *"I've got about 40 accession numbers for the cytochrome b gene from different mammals. I want to pull them from NCBI, line them up, and draw a tree showing how the species relate to each other, all in one Python script."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill biopython

# Kalaris Labs installer with checksum verification
npx research-agent-skills install biopython
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`scikit-bio`](/skills/scikit-bio)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/biopython/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
