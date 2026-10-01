---
title: "datamol — AI agent skill for chemistry and drug discovery"
description: "Wraps RDKit through the datamol Python library (import datamol as dm) for molecular cheminformatics, returning native rdkit.Chem.Mol objects."
---

# `datamol`

> Wraps RDKit through the datamol Python library (import datamol as dm) for molecular cheminformatics, returning native rdkit.Chem.Mol objects. Covers SMILES/SELFIES/InChI conversion, sanitization and standardization, descriptors, fingerprints and similarity, Butina clustering and diverse subset picking, Bemis-Murcko scaffolds, BRICS/RECAP fragmentation, 3D conformers, reactions, SDF/CSV/Excel I/O including cloud paths, and parallel batch processing. Use when parsing or standardizing SMILES from external sources, computing descriptors or fingerprints for a compound library, clustering or selecting diverse molecules, making scaffold-based train/test splits, or generating conformers. Use when running a molecule-processing pipeline with n_jobs. For fine-grained control or custom parameters, use RDKit directly instead.

**Category:** [chemistry-and-drug-discovery](/skills#chemistry-and-drug-discovery) · **License:** Apache-2.0 license · **Version:** 1.2

## Install

```bash
npx research-agent-skills install datamol
npx skills add KalarisLabs/research-agent-skills --skill datamol
```

## When to use it

Wraps RDKit through the datamol Python library (import datamol as dm) for molecular cheminformatics, returning native rdkit.Chem.Mol objects. Covers SMILES/SELFIES/InChI conversion, sanitization and standardization, descriptors, fingerprints and similarity, Butina clustering and diverse subset picking, Bemis-Murcko scaffolds, BRICS/RECAP fragmentation, 3D conformers, reactions, SDF/CSV/Excel I/O including cloud paths, and parallel batch processing. Use when parsing or standardizing SMILES from external sources, computing descriptors or fingerprints for a compound library, clustering or selecting diverse molecules, making scaffold-based train/test splits, or generating conformers. Use when running a molecule-processing pipeline with n_jobs. For fine-grained control or custom parameters, use RDKit directly instead.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/datamol/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
