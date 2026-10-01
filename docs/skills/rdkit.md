---
title: "rdkit — AI agent skill for chemistry and drug discovery"
description: "Guides use of RDKit (Python) for reading and writing SMILES, MOL/SDF, and InChI, computing descriptors (MW, LogP, TPSA), generating Morgan/MACCS/atom-pair…"
---

# `rdkit`

> Guides use of RDKit (Python) for reading and writing SMILES, MOL/SDF, and InChI, computing descriptors (MW, LogP, TPSA), generating Morgan/MACCS/atom-pair fingerprints, running SMARTS substructure searches, applying reaction SMARTS, and building 2D/3D coordinates with ETKDG. Use when parsing or sanitizing molecules that fail default sanitization, calculating Tanimoto similarity or clustering compounds, filtering libraries by substructure, embedding and optimizing conformers, or computing Murcko scaffolds and molecule hashes. Use when fine-grained control over sanitization or algorithms is needed. For simpler standard workflows, use datamol instead, which wraps RDKit.

**Category:** [chemistry-and-drug-discovery](/skills#chemistry-and-drug-discovery) · **License:** BSD-3-Clause license · **Version:** 1.3

## Install

```bash
npx research-agent-skills install rdkit
npx skills add KalarisLabs/research-agent-skills --skill rdkit
```

## When to use it

Guides use of RDKit (Python) for reading and writing SMILES, MOL/SDF, and InChI, computing descriptors (MW, LogP, TPSA), generating Morgan/MACCS/atom-pair fingerprints, running SMARTS substructure searches, applying reaction SMARTS, and building 2D/3D coordinates with ETKDG. Use when parsing or sanitizing molecules that fail default sanitization, calculating Tanimoto similarity or clustering compounds, filtering libraries by substructure, embedding and optimizing conformers, or computing Murcko scaffolds and molecule hashes. Use when fine-grained control over sanitization or algorithms is needed. For simpler standard workflows, use datamol instead, which wraps RDKit.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/rdkit/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
