---
title: "bulk-rnaseq — AI agent skill for life sciences"
description: "End-to-end bulk RNA-seq orchestrator — takes raw FASTQ reads through QC and trimming (FastQC, fastp/Trim Galore), alignment and quantification (STAR, Salmon…"
keywords: ["RNA-seq", "transcriptomics", "differential expression", "alignment", "bioinformatics"]
---

# `bulk-rnaseq`

**Category:** [life-sciences](/skills#life-sciences) · **License:** MIT · **Version:** 1.1 · **Includes scripts**

**Tags:** RNA-seq, transcriptomics, differential expression, alignment, bioinformatics

## When to use it

End-to-end bulk RNA-seq orchestrator — takes raw FASTQ reads through QC and trimming (FastQC, fastp/Trim Galore), alignment and quantification (STAR, Salmon, featureCounts), assembles a gene-level counts matrix, then hands off to differential expression (pydeseq2), pathway/GSEA enrichment (pathway-enrichment), and publication figures (scientific-visualization). Use whenever the user has bulk RNA-seq reads or quant output and wants a complete, reproducible differential-expression workflow — e.g. "analyze my RNA-seq", "FASTQ to DESeq2", "run nf-core/rnaseq", "STAR/Salmon quantification", "build a counts matrix for DESeq2", or "go from reads to differentially expressed genes and enriched pathways". Routes between an nf-core/rnaseq (Nextflow) path and a standalone STAR/Salmon path, and covers experimental design, strandedness, and QC gates. For single-cell RNA-seq use the scanpy skill instead.

## Example requests

Ask your agent in plain language, for example:

- *"I have 12 paired-end FASTQ files from a mouse liver drug-treatment experiment. Can you take me from reads all the way to differentially expressed genes?"*
- *"I ran Salmon on 8 samples (quant.sf files in salmon_out/sample*/) against GRCh38 Ensembl release 110. How do I get a counts.csv and metadata file that PyDESeq2 will accept? PyDESeq2 errors out saying my counts aren't integers."*
- *"My collaborator sequenced treated vs. untreated tumor organoids in triplicate, but the treated ones were all run on a different lane and day than the controls. I want to know which pathways are changing between the two groups. How should I proceed?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill bulk-rnaseq

# Kalaris Labs installer with checksum verification
npx research-agent-skills install bulk-rnaseq
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`arboreto`](/skills/arboreto)
- [`database-lookup`](/skills/database-lookup)
- [`pathway-enrichment`](/skills/pathway-enrichment)
- [`scientific-visualization`](/skills/scientific-visualization)
- [`scientific-writing`](/skills/scientific-writing)
- [`statistical-analysis`](/skills/statistical-analysis)
- [`nextflow`](/skills/nextflow)
- [`pydeseq2`](/skills/pydeseq2)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/bulk-rnaseq/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
