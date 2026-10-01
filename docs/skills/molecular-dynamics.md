---
title: "molecular-dynamics — AI agent skill for chemistry and drug discovery"
description: "Runs and analyzes molecular dynamics simulations using OpenMM and MDAnalysis."
---

# `molecular-dynamics`

> Runs and analyzes molecular dynamics simulations using OpenMM and MDAnalysis. Covers system preparation with PDBFixer and OpenFF/GAFF2, force field choice (AMBER14, CHARMM36m, ff19SB), energy minimization, NVT/NPT equilibration, production MD, and trajectory analysis (RMSD, RMSF, protein-ligand contacts). Use when simulating a protein or protein-ligand system on GPU, assessing how a mutation affects protein dynamics, characterizing ligand binding mode, quantifying per-residue flexibility, or modeling membrane proteins and disordered proteins. Not for GROMACS or NAMD workflows, which the skill lists only as alternatives.

**Category:** [chemistry-and-drug-discovery](/skills#chemistry-and-drug-discovery) · **License:** MIT · **Version:** 1.1

## Install

```bash
npx research-agent-skills install molecular-dynamics
npx skills add KalarisLabs/research-agent-skills --skill molecular-dynamics
```

## When to use it

Runs and analyzes molecular dynamics simulations using OpenMM and MDAnalysis. Covers system preparation with PDBFixer and OpenFF/GAFF2, force field choice (AMBER14, CHARMM36m, ff19SB), energy minimization, NVT/NPT equilibration, production MD, and trajectory analysis (RMSD, RMSF, protein-ligand contacts). Use when simulating a protein or protein-ligand system on GPU, assessing how a mutation affects protein dynamics, characterizing ligand binding mode, quantifying per-residue flexibility, or modeling membrane proteins and disordered proteins. Not for GROMACS or NAMD workflows, which the skill lists only as alternatives.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/molecular-dynamics/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
