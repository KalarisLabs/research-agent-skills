---
title: "pacsomatic — AI agent skill for life sciences"
description: "Operator toolkit for nf-core/pacsomatic matched tumor-normal workflows from BAM inputs."
keywords: ["tumor-normal", "somatic variants", "nf-core", "long-read sequencing", "cancer genomics"]
---

# `pacsomatic`

**Category:** [life-sciences](/skills#life-sciences) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** tumor-normal, somatic variants, nf-core, long-read sequencing, cancer genomics

## When to use it

Operator toolkit for nf-core/pacsomatic matched tumor-normal workflows from BAM inputs. Use this skill when the user needs to validate run inputs, generate pacsomatic-compliant samplesheets, prepare reproducible Nextflow launch artifacts, run locally or submit to schedulers (LSF/Slurm/PBS/SGE), and triage execution failures. Triggers on requests to run pacsomatic, prepare launch commands/scripts, perform dry-run checks, or troubleshoot pipeline startup and scheduler submission errors.

## Example requests

Ask your agent in plain language, for example:

- *"do a dry run of pacsomatic on my tumor/normal pair first and tell me what's missing"*
- *"I have PacBio HiFi BAMs for patient P017: /data/p017/P017_T.hifi.bam (sample P017_T) and /data/p017/P017_N.hifi.bam (sample P017_N), reference is /ref/GRCh38.fa. Submit it to our Slurm cluster, partition 'long', account 'onc-lab', output in /scratch/p017_out, and give me the job id. Last time sbatch failed with 'Invalid account or account/partition combination specified'."*
- *"I've got long-read tumor and matched normal BAMs for one patient and want somatic variant calls through the nf-core long-read somatic workflow. Can you get everything set up so I can rerun it later exactly the same way?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pacsomatic

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills pacsomatic
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pacsomatic/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
