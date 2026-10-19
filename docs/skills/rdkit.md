---
title: "rdkit — AI agent skill for chemistry and drug discovery"
description: "Guides use of RDKit (Python) for reading and writing SMILES, MOL/SDF, and InChI, computing descriptors (MW, LogP, TPSA), generating Morgan/MACCS/atom-pair…"
keywords: ["cheminformatics", "RDKit", "SMILES", "molecular descriptors", "fingerprints", "drug discovery"]
---

# `rdkit`

**Category:** [chemistry-and-drug-discovery](/skills#chemistry-and-drug-discovery) · **License:** BSD-3-Clause license · **Version:** 1.3 · **Includes scripts**

**Tags:** cheminformatics, RDKit, SMILES, molecular descriptors, fingerprints, drug discovery

## When to use it

Guides use of RDKit (Python) for reading and writing SMILES, MOL/SDF, and InChI, computing descriptors (MW, LogP, TPSA), generating Morgan/MACCS/atom-pair fingerprints, running SMARTS substructure searches, applying reaction SMARTS, and building 2D/3D coordinates with ETKDG. Use when parsing or sanitizing molecules that fail default sanitization, calculating Tanimoto similarity or clustering compounds, filtering libraries by substructure, embedding and optimizing conformers, or computing Murcko scaffolds and molecule hashes. Use when fine-grained control over sanitization or algorithms is needed. For simpler standard workflows, use datamol instead, which wraps RDKit.

## Example requests

Ask your agent in plain language, for example:

- *"Chem.MolFromSmiles keeps returning None for my nitro-containing SMILES. How do I find out what's wrong and still load the molecule?"*
- *"I have compounds.sdf with about 40k molecules from a vendor. I need to keep only those containing a carboxylic acid but no primary amine, then write the hits to a new SDF with their MW, cLogP and TPSA as properties. Some records fail to parse. Can you write the script?"*
- *"I've got a list of ~2,000 screening hits and want to group them into structural clusters, then pick one representative from each cluster. The distance cutoff matters to me and I want to control how the fingerprints are built."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill rdkit

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills rdkit
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `chemistry-and-drug-discovery` category with `/plugin install chemistry-and-drug-discovery@research-agent-skills`.

## Related

- [Skills for chemistry and drug discovery](/fields/chemistry)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/rdkit/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
