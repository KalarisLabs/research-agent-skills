---
title: "rowan — AI agent skill for chemistry and drug discovery"
description: "Rowan is a cloud-native molecular modeling and medicinal-chemistry workflow platform with a Python API."
keywords: ["molecular modeling", "pKa prediction", "docking", "computational chemistry", "drug discovery"]
---

# `rowan`

**Category:** [chemistry-and-drug-discovery](/skills#chemistry-and-drug-discovery) · **License:** Proprietary (API key required) · **Version:** 1.5

**Tags:** molecular modeling, pKa prediction, docking, computational chemistry, drug discovery

## When to use it

Rowan is a cloud-native molecular modeling and medicinal-chemistry workflow platform with a Python API. Use for pKa and macropKa prediction, conformer and tautomer ensembles, docking and analogue docking, protein-ligand cofolding, MSA generation, molecular dynamics, permeability, descriptor workflows, and related small-molecule or protein modeling tasks. Ideal for programmatic batch screening, multi-step chemistry pipelines, and workflows that would otherwise require maintaining local HPC/GPU infrastructure.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get the pKa of aspirin with Rowan?"*
- *"I have 40 analogues of my kinase lead in analogs.csv (SMILES column) and a prepared receptor, kinase.pdb, with a co-crystal ligand as reference. I tried passing the SMILES strings straight into the analogue docking workflow and got a ValueError before submission. Fix this and run the whole series on Rowan, then pull out the best pose and score for each."*
- *"I need to know how my carboxylic acid/amine drug candidate will be charged across pH 0-14, and whether it will cross membranes and how soluble it is at pH 7.4. I don't want to set up any local compute. How would I do that programmatically for a few hundred compounds?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill rowan

# Kalaris Labs installer with checksum verification
npx research-agent-skills install rowan
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `chemistry-and-drug-discovery` category with `/plugin install chemistry-and-drug-discovery@research-agent-skills`.

## Related

- [`molecular-dynamics`](/skills/molecular-dynamics)
- [Skills for chemistry and drug discovery](/fields/chemistry)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/rowan/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
