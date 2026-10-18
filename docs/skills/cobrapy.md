---
title: "cobrapy — AI agent skill for life sciences"
description: "Runs constraint-based metabolic modeling with COBRApy (Python, import cobra) on genome-scale models in SBML, JSON, YAML, or MATLAB format."
keywords: ["metabolic modeling", "flux balance analysis", "systems biology", "genome-scale models"]
---

# `cobrapy`

**Category:** [life-sciences](/skills#life-sciences) · **License:** GPL-2.0 license · **Version:** 1.3

**Tags:** metabolic modeling, flux balance analysis, systems biology, genome-scale models

## When to use it

Runs constraint-based metabolic modeling with COBRApy (Python, import cobra) on genome-scale models in SBML, JSON, YAML, or MATLAB format. Covers FBA, pFBA, geometric FBA, FVA, flux sampling, gene and reaction knockouts, production envelopes, growth media, gapfilling, and building models. Use when loading or exporting a genome-scale metabolic model. Use when predicting growth or flux distributions with FBA or FVA. Use when screening gene or reaction knockouts. Use when tuning growth media or exchange constraints. Use when gap-filling an infeasible model or checking model consistency. Not for kinetic or ODE-based simulation of metabolism.

## Example requests

Ask your agent in plain language, for example:

- *"How do I run FBA on e_coli_core and print the growth rate?"*
- *"I have iML1515.xml (SBML) for E. coli K-12 MG1655. I need to run a single-gene knockout screen under minimal glucose medium and list which genes are essential, i.e. growth under 1% of wild type. read_sbml_model works but my script gives 'infeasible' for the wild type after I changed the medium. What should I do?"*
- *"I reconstructed a metabolic network for a new bacterial strain, but it won't grow on any carbon source. I want to figure out which minimal set of reactions from a universal database I could add so that it produces biomass, and check whether the model has blocked reactions or mass-imbalanced ones."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill cobrapy

# Kalaris Labs installer with checksum verification
npx research-agent-skills install cobrapy
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`13c-metabolic-flux`](/skills/13c-metabolic-flux)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/cobrapy/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
