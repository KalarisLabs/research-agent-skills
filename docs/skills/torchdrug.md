---
title: "torchdrug — AI agent skill for chemistry and drug discovery"
description: "Build and troubleshoot TorchDrug 0.2.1 workflows for molecular graphs, property prediction, self-supervised pretraining, molecule generation, retrosynthesis…"
keywords: ["drug discovery", "molecular graphs", "molecule generation", "retrosynthesis", "deep learning"]
---

# `torchdrug`

**Category:** [chemistry-and-drug-discovery](/skills#chemistry-and-drug-discovery) · **License:** Apache-2.0 license · **Version:** 1.2

**Tags:** drug discovery, molecular graphs, molecule generation, retrosynthesis, deep learning

## When to use it

Build and troubleshoot TorchDrug 0.2.1 workflows for molecular graphs, property prediction, self-supervised pretraining, molecule generation, retrosynthesis, protein representation learning, and knowledge graph reasoning. Use when code imports torchdrug or needs its datasets, models, tasks, or Engine.

## Example requests

Ask your agent in plain language, for example:

- *"How do I fine-tune a GIN on BBBP with torchdrug?"*
- *"I'm on Python 3.11 with torch 2.2 and `import torchdrug` fails with an error about torch_scatter (undefined symbol / no module named torch_scatter). My script train_clintox.py uses datasets.ClinTox, models.GIN and core.Engine. How do I fix it?"*
- *"I have a set of ~50k USPTO reaction records and want to train a model that proposes the precursor molecules for a target product, then evaluate top-k accuracy. What pipeline should I set up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill torchdrug

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills torchdrug
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `chemistry-and-drug-discovery` category with `/plugin install chemistry-and-drug-discovery@research-agent-skills`.

## Related

- [Skills for chemistry and drug discovery](/fields/chemistry)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/torchdrug/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
