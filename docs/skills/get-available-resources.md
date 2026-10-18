---
title: "get-available-resources — AI agent skill for data science and ml"
description: "Detect host inventory and effective CPU, memory, disk, scheduler, container, and accelerator limits when a user asks for resource-aware planning or before a…"
keywords: ["compute resources", "GPU detection", "resource planning", "HPC"]
---

# `get-available-resources`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** MIT · **Version:** 1.3 · **Includes scripts**

**Tags:** compute resources, GPU detection, resource planning, HPC

## When to use it

Detect host inventory and effective CPU, memory, disk, scheduler, container, and accelerator limits when a user asks for resource-aware planning or before a clearly resource-sensitive local workload. Produces a redacted JSON snapshot and conservative planning helpers without stress tests or assuming visible host hardware is usable.

## Example requests

Ask your agent in plain language, for example:

- *"How many CPUs and how much RAM can I actually use here?"*
- *"I'm about to launch a joblib parallel run of 400 scRNA-seq pseudobulk DE fits from de_fits.py inside our Slurm cluster. Last time it died with 'Killed' (OOM) on a node that showed 128 cores in htop. Can you work out how many workers I can safely use, keeping about 8 GiB aside for the OS and main process?"*
- *"I want to fine-tune a protein language model on this workstation. Before I pick a batch size and decide whether to try GPU training, can you tell me what hardware the process can really reach, including any accelerators and free disk for checkpoints?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill get-available-resources

# Kalaris Labs installer with checksum verification
npx research-agent-skills install get-available-resources
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/get-available-resources/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
