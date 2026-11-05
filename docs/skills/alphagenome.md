---
title: "alphagenome — AI agent skill for life sciences"
description: "Look up precomputed AlphaGenome Atlas effects for any GRCh38 single-nucleotide variant (AVI score with Phred and 18 SHAP feature attributions, plus raw and…"
keywords: ["variant effect prediction", "genomics", "regulatory genomics", "GRCh38", "functional annotation"]
---

# `alphagenome`

**Category:** [life-sciences](/skills#life-sciences) · **License:** MIT · **Version:** 1.0 · **Includes scripts**

**Tags:** variant effect prediction, genomics, regulatory genomics, GRCh38, functional annotation

## When to use it

Look up precomputed AlphaGenome Atlas effects for any GRCh38 single-nucleotide variant (AVI score with Phred and 18 SHAP feature attributions, plus raw and quantile scores for RNA-seq, DNase, ATAC, ChIP-TF, ChIP-histone, CAGE, PRO-cap, splicing, polyadenylation and contact-map tracks), score variants or scan windows on demand with the AlphaGenome model for human and mouse (variant scoring, in silico mutagenesis, REF-versus-ALT track prediction), and build Atlas website deep links. Use when the user mentions AlphaGenome, AlphaGenome Atlas, AVI or AlphaGenome Variant Impact, DeepMind variant effect prediction, or wants to prioritise or mechanistically interpret non-coding, regulatory, splicing, enhancer, promoter, or chromatin-accessibility effects of SNVs from a VCF, credible set, or region. Research use only; not a clinical tool.

## Example requests

Ask your agent in plain language, for example:

- *"What's the AlphaGenome AVI score for chr22:36201698:A>C?"*
- *"I have a VCF, fine_map_credible_set.vcf, with 40 SNVs from a lipid GWAS locus (hg38, intronic/intergenic). I want to know which are likely to alter enhancer activity in liver. Can you rank them and show me which tracks in HepG2 or liver drive the effect? I have an API key set in my environment, and I'm getting 'ValueError: API key not valid' on one machine."*
- *"I've got a noncoding variant in a mouse mm10-lifted region and also a 3 bp deletion in human that I suspect disrupt a promoter. How can I predict what happens to expression and chromatin accessibility computationally with DeepMind's sequence-to-function model, comparing reference and mutant tracks?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill alphagenome

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills alphagenome
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`database-lookup`](/skills/database-lookup)
- [`folklore-variant-evidence`](/skills/folklore-variant-evidence)
- [`genomic-coordinates`](/skills/genomic-coordinates)
- [`genomic-intelligence`](/skills/genomic-intelligence)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/alphagenome/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
