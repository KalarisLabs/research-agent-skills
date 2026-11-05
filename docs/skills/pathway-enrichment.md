---
title: "pathway-enrichment — AI agent skill for life sciences"
description: "Run pathway and gene-set enrichment analysis on gene lists or ranked gene data, then interpret the results."
keywords: ["pathway enrichment", "gene set enrichment", "GSEA", "functional analysis", "bioinformatics"]
---

# `pathway-enrichment`

**Category:** [life-sciences](/skills#life-sciences) · **License:** MIT · **Version:** 1.1 · **Includes scripts**

**Tags:** pathway enrichment, gene set enrichment, GSEA, functional analysis, bioinformatics

## When to use it

Run pathway and gene-set enrichment analysis on gene lists or ranked gene data, then interpret the results. Use whenever the user has a set of genes (differentially expressed genes from PyDESeq2/Scanpy, CRISPR-screen hits, cluster marker genes, proteomics hits) and wants to know which biological pathways, GO terms, or gene sets are over-represented or enriched. Covers over-representation analysis (ORA / Enrichr / Fisher / hypergeometric), ranked Gene Set Enrichment Analysis (GSEA / preranked), single-sample scoring (ssGSEA/GSVA), and functional profiling via gseapy, g:Profiler, Enrichr libraries, MSigDB, GO, KEGG, Reactome, and WikiPathways — plus gene-ID mapping, choosing the right background universe, multiple-testing correction, redundancy reduction, dotplots/enrichment maps, and publication-ready tables. Use this for "pathway analysis", "enrichment analysis", "GO enrichment", "KEGG/Reactome pathways", "GSEA", "over-representation", "functional annotation", or "what pathways are my genes in".

## Example requests

Ask your agent in plain language, for example:

- *"what pathways are enriched in my 214 upregulated genes? mouse, treated vs control"*
- *"I ran PyDESeq2 on my patient-derived organoid RNA-seq (res_df.csv, index = Ensembl IDs, columns baseMean, log2FoldChange, stat, pvalue, padj). I want GSEA against MSigDB Hallmark and Reactome, and gp.prerank gives me 'Warning: no genes overlap' with an empty result table. How do I fix this and get a figure for the paper?"*
- *"I have a CRISPR knockout screen with about 18,000 genes scored by MAGeCK. The top 150 hits are essential genes. Can you help me work out what biological processes these hits point to and whether they're just general housekeeping machinery?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pathway-enrichment

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills pathway-enrichment
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`bioservices`](/skills/bioservices)
- [`bulk-rnaseq`](/skills/bulk-rnaseq)
- [`gget`](/skills/gget)
- [`database-lookup`](/skills/database-lookup)
- [`literature-review`](/skills/literature-review)
- [`scientific-visualization`](/skills/scientific-visualization)
- [`scientific-writing`](/skills/scientific-writing)
- [`statistical-analysis`](/skills/statistical-analysis)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pathway-enrichment/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
