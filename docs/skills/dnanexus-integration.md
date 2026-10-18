---
title: "dnanexus-integration — AI agent skill for lab automation"
description: "Build and operate reproducible genomics workloads on DNAnexus with the dx CLI, dxpy, apps/applets, native workflows, dxCompiler, and Nextflow."
keywords: ["genomics", "cloud computing", "bioinformatics pipelines", "workflows", "DNAnexus"]
---

# `dnanexus-integration`

**Category:** [lab-automation](/skills#lab-automation) · **License:** MIT · **Version:** 2.1 · **Includes scripts**

**Tags:** genomics, cloud computing, bioinformatics pipelines, workflows, DNAnexus

## When to use it

Build and operate reproducible genomics workloads on DNAnexus with the dx CLI, dxpy, apps/applets, native workflows, dxCompiler, and Nextflow. Use for DNAnexus data transfers, dxapp.json development, execution monitoring, workflow import, and project automation.

## Example requests

Ask your agent in plain language, for example:

- *"How do I download a whole folder from my DNAnexus project to my laptop?"*
- *"I'm getting `DXExecDependencyError` when my applet starts on Ubuntu 24.04. My dxapp.json has execDepends with pip packages: pysam, pandas, and an old numpy pin. Built with `dx build -f`. Can you help me fix it and tidy up the config?"*
- *"I have a WGS pipeline written in WDL for 40 samples and I want it to run on our cloud genomics platform where my data already lives under a project called cohort-2026. I need it to be launched in bulk, with the cost capped and a way to see which runs failed. Where do I start?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill dnanexus-integration

# Kalaris Labs installer with checksum verification
npx research-agent-skills install dnanexus-integration
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `lab-automation` category with `/plugin install lab-automation@research-agent-skills`.

## Related

- [`latchbio-integration`](/skills/latchbio-integration)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/dnanexus-integration/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
