---
title: "pytdc — AI agent skill for scientific databases"
description: "Uses the PyTDC package (import tdc, Therapeutics Data Commons) to discover therapeutic ML tasks from tdc.metadata, plan and load approved datasets, apply…"
keywords: ["therapeutics", "drug discovery datasets", "benchmarks", "machine learning", "ADMET"]
---

# `pytdc`

**Category:** [scientific-databases](/skills#scientific-databases) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** therapeutics, drug discovery datasets, benchmarks, machine learning, ADMET

## When to use it

Uses the PyTDC package (import tdc, Therapeutics Data Commons) to discover therapeutic ML tasks from tdc.metadata, plan and load approved datasets, apply task-aware splits (random, scaffold, cold_split, combination, time), run evaluator metrics, evaluate benchmark groups such as admet_group, and run bounded molecular-oracle scoring. Use when selecting a TDC task or dataset, planning a download-free split, scoring predictions with TDC evaluators, running a benchmark group evaluation, or checking dataset licenses and cache effects before downloading. Use when scoring molecules with TDC oracles like QED. Not for generic RDKit cheminformatics or training molecule generators.

## Example requests

Ask your agent in plain language, for example:

- *"What TDC tasks exist for toxicity? Don't download anything yet."*
- *"I'm working on a Caco2_Wang permeability model and need a scaffold split with seed 42 for my paper. I'm on Python 3.12 and got `ModuleNotFoundError: No module named 'pkg_resources'` when importing tdc. Can you help me get this working and set up the split? Check the dataset license and how much it will download first."*
- *"I have predictions from my model on the 22 ADMET benchmark endpoints from the standard leaderboard and want to get the official scores across five seeds so I can compare against published results. How should I do that?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pytdc

# Kalaris Labs installer with checksum verification
npx research-agent-skills install pytdc
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `scientific-databases` category with `/plugin install scientific-databases@research-agent-skills`.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pytdc/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
