---
title: "molecular-dynamics — AI agent skill for chemistry and drug discovery"
description: "Runs and analyzes molecular dynamics simulations using OpenMM and MDAnalysis."
keywords: ["molecular dynamics", "OpenMM", "MDAnalysis", "simulation", "computational chemistry"]
---

# `molecular-dynamics`

**Category:** [chemistry-and-drug-discovery](/skills#chemistry-and-drug-discovery) · **License:** MIT · **Version:** 1.1

**Tags:** molecular dynamics, OpenMM, MDAnalysis, simulation, computational chemistry

## When to use it

Runs and analyzes molecular dynamics simulations using OpenMM and MDAnalysis. Covers system preparation with PDBFixer and OpenFF/GAFF2, force field choice (AMBER14, CHARMM36m, ff19SB), energy minimization, NVT/NPT equilibration, production MD, and trajectory analysis (RMSD, RMSF, protein-ligand contacts). Use when simulating a protein or protein-ligand system on GPU, assessing how a mutation affects protein dynamics, characterizing ligand binding mode, quantifying per-residue flexibility, or modeling membrane proteins and disordered proteins. Not for GROMACS or NAMD workflows, which the skill lists only as alternatives.

## Example requests

Ask your agent in plain language, for example:

- *"I need to run a 100 ns MD of lysozyme on my GPU. Where do I start?"*
- *"I have 4ake_apo.pdb and a ligand file lig.sdf for a kinase I'm studying. I want to simulate the complex in explicit water with OpenMM, parameterize the ligand with GAFF2 via the OpenFF toolkit, and then compute per-residue RMSF and ligand-protein contacts from the production trajectory in MDAnalysis. Last time I got a 'No template found for residue' error from createSystem. How should I set this up?"*
- *"We found a point mutation in a transporter that patients carry, and we suspect it makes a loop floppier. I have the wild-type structure and want to see whether the mutant moves around more over time compared with wild-type, using atomistic simulation. How would you approach it?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill molecular-dynamics

# Kalaris Labs installer with checksum verification
npx research-agent-skills install molecular-dynamics
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `chemistry-and-drug-discovery` category with `/plugin install chemistry-and-drug-discovery@research-agent-skills`.

## Related

- [`rowan`](/skills/rowan)
- [Skills for chemistry and drug discovery](/fields/chemistry)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/molecular-dynamics/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
