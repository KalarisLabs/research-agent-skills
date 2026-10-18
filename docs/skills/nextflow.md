---
title: "nextflow — AI agent skill for life sciences"
description: "Build, run, and debug Nextflow data pipelines and nf-core workflows end to end."
keywords: ["Nextflow", "nf-core", "bioinformatics pipelines", "workflow management", "genomics"]
---

# `nextflow`

**Category:** [life-sciences](/skills#life-sciences) · **License:** Apache-2.0 · **Version:** 1.2

**Tags:** Nextflow, nf-core, bioinformatics pipelines, workflow management, genomics

## When to use it

Build, run, and debug Nextflow data pipelines and nf-core workflows end to end. Use whenever the user mentions Nextflow, nf-core, .nf files, nextflow.config, DSL2, processes/channels/operators, samplesheets, or wants to run a community pipeline (e.g. nf-core/rnaseq, nf-core/sarek), write or test a module/subworkflow with nf-test, configure executors/containers (Docker, Singularity/Apptainer, Conda, Wave), scale a workflow to HPC/SLURM or cloud (AWS Batch, Google Batch, Azure, Kubernetes), or debug a failed/-resume run. Make sure to use this skill for any reproducible scientific/bioinformatics workflow work even if the user does not say the word "Nextflow", and for authoring nf-core-compliant pipelines, modules, configs, and linting.

## Example requests

Ask your agent in plain language, for example:

- *"how do I resume a nextflow run that crashed halfway?"*
- *"I'm running nf-core/rnaseq 3.14.0 on our SLURM cluster with Singularity for 24 human paired-end samples. My samplesheet.csv has columns sample,fastq_1,fastq_2,strandedness. The job dies with 'Process NFCORE_RNASEQ:RNASEQ:STAR_ALIGN terminated with an error exit status (137)'. How do I fix it and keep the finished steps?"*
- *"I have a pile of tumor/normal exome FASTQs and a reference genome. I want a reproducible, portable analysis setup that can run on my laptop for testing and then scale out to AWS without changing the code, with each tool in its own container. Where do I start?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill nextflow

# Kalaris Labs installer with checksum verification
npx research-agent-skills install nextflow
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`bulk-rnaseq`](/skills/bulk-rnaseq)
- [`latchbio-integration`](/skills/latchbio-integration)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/nextflow/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
