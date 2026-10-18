---
title: "genomic-intelligence — AI agent skill for life sciences"
description: "Predict regulatory features, gene structure, and expression directly from DNA sequence using Genomic Intelligence's hosted transformer DNA language models —…"
keywords: ["DNA language models", "regulatory genomics", "gene structure", "sequence analysis"]
---

# `genomic-intelligence`

**Category:** [life-sciences](/skills#life-sciences) · **License:** MIT · **Version:** 1.2

**Tags:** DNA language models, regulatory genomics, gene structure, sequence analysis

## When to use it

Predict regulatory features, gene structure, and expression directly from DNA sequence using Genomic Intelligence's hosted transformer DNA language models — no local GPU or model weights. Six tasks over a REST API and a hosted MCP server (keyless public demo): promoter regions, splice donor/acceptor sites, enhancer activity, chromatin state, sequence-to-expression (log TPM), and de-novo gene annotation, plus a composite find-genes-then-predict-expression workflow. Use when the user has a gene symbol, a genomic region, or a DNA/FASTA sequence and wants any of these predictions, mentions Genomic Intelligence, genomicintelligence.ai, api.genomicintelligence.ai, or mcp.genomicintelligence.ai.

## Example requests

Ask your agent in plain language, for example:

- *"Find the promoters in the first 20 kb upstream of human MYC using a DNA language model API."*
- *"I have locus.fa, a 60 kb FASTA of a human locus (line-wrapped, with a '>' header). I want expression predicted for the gene at the center in K562 cells, and I only have the public demo, no API key. I tried POSTing to /v1/tasks/expression/predict and got a 422."*
- *"I just got a new Drosophila genomic region of about 80 kb with no annotation. I'd like to know which genes are in it, and then get an expression estimate for each one. I don't want to download any model weights or use my GPU."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill genomic-intelligence

# Kalaris Labs installer with checksum verification
npx research-agent-skills install genomic-intelligence
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`alphagenome`](/skills/alphagenome)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/genomic-intelligence/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
