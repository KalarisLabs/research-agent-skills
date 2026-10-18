---
title: "deepchem — AI agent skill for chemistry and drug discovery"
description: "Molecular ML with diverse featurizers and pre-built datasets."
keywords: ["molecular machine learning", "ADMET", "property prediction", "drug discovery", "cheminformatics"]
---

# `deepchem`

**Category:** [chemistry-and-drug-discovery](/skills#chemistry-and-drug-discovery) · **License:** MIT · **Version:** 1.5 · **Includes scripts**

**Tags:** molecular machine learning, ADMET, property prediction, drug discovery, cheminformatics

## When to use it

Molecular ML with diverse featurizers and pre-built datasets. Use for property prediction (ADMET, toxicity) with traditional ML or GNNs when you want extensive featurization options and MoleculeNet benchmarks. Best for quick experiments with pre-trained models, diverse molecular representations. For graph-first PyTorch workflows use torchdrug; for benchmark datasets use pytdc.

## Example requests

Ask your agent in plain language, for example:

- *"Train a quick solubility model on the Delaney dataset and tell me the test RMSE."*
- *"I have compounds.csv with columns 'smiles' and 'herg_ic50_class' (about 4,000 rows, heavily imbalanced, ~8% positives). I tried a random 80/20 split and got 0.97 AUC, which seems too good. Can you rebuild this in DeepChem with a proper split and compare ECFP+RF against a GCN? I'm on Python 3.11 and getting 'No module named torch' warnings when I import deepchem."*
- *"I want to predict whether small molecules cross the blood-brain barrier, and I'd like to try lots of different ways of turning structures into numeric inputs (fingerprints, descriptors, graph representations) and compare them on a standard benchmark set. Where do I start?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill deepchem

# Kalaris Labs installer with checksum verification
npx research-agent-skills install deepchem
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `chemistry-and-drug-discovery` category with `/plugin install chemistry-and-drug-discovery@research-agent-skills`.

## Related

- [Skills for chemistry and drug discovery](/fields/chemistry)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/deepchem/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
