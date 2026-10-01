---
title: "pytdc — AI agent skill for scientific databases"
description: "Uses the PyTDC package (import tdc, Therapeutics Data Commons) to discover therapeutic ML tasks from tdc.metadata, plan and load approved datasets, apply…"
---

# `pytdc`

> Uses the PyTDC package (import tdc, Therapeutics Data Commons) to discover therapeutic ML tasks from tdc.metadata, plan and load approved datasets, apply task-aware splits (random, scaffold, cold_split, combination, time), run evaluator metrics, evaluate benchmark groups such as admet_group, and run bounded molecular-oracle scoring. Use when selecting a TDC task or dataset, planning a download-free split, scoring predictions with TDC evaluators, running a benchmark group evaluation, or checking dataset licenses and cache effects before downloading. Use when scoring molecules with TDC oracles like QED. Not for generic RDKit cheminformatics or training molecule generators.

**Category:** [scientific-databases](/skills#scientific-databases) · **License:** MIT · **Version:** 1.2

## Install

```bash
npx research-agent-skills install pytdc
npx skills add KalarisLabs/research-agent-skills --skill pytdc
```

## When to use it

Uses the PyTDC package (import tdc, Therapeutics Data Commons) to discover therapeutic ML tasks from tdc.metadata, plan and load approved datasets, apply task-aware splits (random, scaffold, cold_split, combination, time), run evaluator metrics, evaluate benchmark groups such as admet_group, and run bounded molecular-oracle scoring. Use when selecting a TDC task or dataset, planning a download-free split, scoring predictions with TDC evaluators, running a benchmark group evaluation, or checking dataset licenses and cache effects before downloading. Use when scoring molecules with TDC oracles like QED. Not for generic RDKit cheminformatics or training molecule generators.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pytdc/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
