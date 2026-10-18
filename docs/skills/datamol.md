---
title: "datamol — AI agent skill for chemistry and drug discovery"
description: "Wraps RDKit through the datamol Python library (import datamol as dm) for molecular cheminformatics, returning native rdkit.Chem.Mol objects."
keywords: ["cheminformatics", "RDKit", "molecules", "SMILES", "drug discovery"]
---

# `datamol`

**Category:** [chemistry-and-drug-discovery](/skills#chemistry-and-drug-discovery) · **License:** Apache-2.0 license · **Version:** 1.2

**Tags:** cheminformatics, RDKit, molecules, SMILES, drug discovery

## When to use it

Wraps RDKit through the datamol Python library (import datamol as dm) for molecular cheminformatics, returning native rdkit.Chem.Mol objects. Covers SMILES/SELFIES/InChI conversion, sanitization and standardization, descriptors, fingerprints and similarity, Butina clustering and diverse subset picking, Bemis-Murcko scaffolds, BRICS/RECAP fragmentation, 3D conformers, reactions, SDF/CSV/Excel I/O including cloud paths, and parallel batch processing. Use when parsing or standardizing SMILES from external sources, computing descriptors or fingerprints for a compound library, clustering or selecting diverse molecules, making scaffold-based train/test splits, or generating conformers. Use when running a molecule-processing pipeline with n_jobs. For fine-grained control or custom parameters, use RDKit directly instead.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get a canonical, standardized SMILES out of a messy list of vendor SMILES using datamol?"*
- *"I have vendor_library.sdf with about 40k compounds and I need to split it into train/test for a QSAR model without scaffold leakage. Then I want 2048-bit ECFP fingerprints for each compound. It's slow, so please use all cores. Can you write the script?"*
- *"I've got 5,000 hit compounds from a screen and can only afford to order 96. I want those 96 to cover as much chemical space as possible and not be near-duplicates of each other. How should I pick them?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill datamol

# Kalaris Labs installer with checksum verification
npx research-agent-skills install datamol
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `chemistry-and-drug-discovery` category with `/plugin install chemistry-and-drug-discovery@research-agent-skills`.

## Related

- [`scikit-learn`](/skills/scikit-learn)
- [Skills for chemistry and drug discovery](/fields/chemistry)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/datamol/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
