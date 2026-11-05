---
title: "latchbio-integration — AI agent skill for lab automation"
description: "Build, register, debug, and operate bioinformatics workflows on Latch using the Python SDK, CLI, Latch Data and Registry, Nextflow, Snakemake, programmatic…"
keywords: ["bioinformatics workflows", "cloud computing", "Nextflow", "Snakemake", "Latch"]
---

# `latchbio-integration`

**Category:** [lab-automation](/skills#lab-automation) · **License:** MIT · **Version:** 2.1 · **Includes scripts**

**Tags:** bioinformatics workflows, cloud computing, Nextflow, Snakemake, Latch

## When to use it

Build, register, debug, and operate bioinformatics workflows on Latch using the Python SDK, CLI, Latch Data and Registry, Nextflow, Snakemake, programmatic execution, and Latch MCP. Use when authoring or deploying Latch workflows, configuring resources or interfaces, moving data, integrating Registry, or launching and monitoring runs.

## Example requests

Ask your agent in plain language, for example:

- *"How do I give my Latch task more memory and a GPU?"*
- *"I have a Snakemake pipeline for ATAC-seq on mouse samples (Snakefile plus config.yaml, Dockerfile already written). I want to get it onto Latch so my collaborators can launch it from a form. `latch register --snakefile Snakefile --staging` ran but it fails to find a workflow entrypoint. What's going wrong and what should I do?"*
- *"We have a few hundred FASTQ files sitting in a cloud workspace and a sample table with metadata. I want to script a batch of alignment runs over them from Python, track each one until it finishes, and pull the results back into the sample table. Can you lay out the approach?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill latchbio-integration

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills latchbio-integration
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `lab-automation` category with `/plugin install lab-automation@research-agent-skills`.

## Related

- [`benchling-integration`](/skills/benchling-integration)
- [`dnanexus-integration`](/skills/dnanexus-integration)
- [`nextflow`](/skills/nextflow)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/latchbio-integration/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
