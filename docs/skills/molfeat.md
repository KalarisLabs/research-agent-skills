---
title: "molfeat — AI agent skill for chemistry and drug discovery"
description: "Converts SMILES strings or RDKit/datamol molecules into numerical features using molfeat (0.11.0), which provides calculators, scikit-learn compatible…"
keywords: ["molecular featurization", "fingerprints", "descriptors", "cheminformatics", "machine learning"]
---

# `molfeat`

**Category:** [chemistry-and-drug-discovery](/skills#chemistry-and-drug-discovery) · **License:** Apache-2.0 license · **Version:** 1.2

**Tags:** molecular featurization, fingerprints, descriptors, cheminformatics, machine learning

## When to use it

Converts SMILES strings or RDKit/datamol molecules into numerical features using molfeat (0.11.0), which provides calculators, scikit-learn compatible transformers, and pretrained embedding models. Covers fingerprints (ECFP, MACCS, MAP4), RDKit and Mordred descriptors, pharmacophore descriptors, and pretrained models such as ChemBERTa and GIN, with parallel processing and caching. Use when building QSAR or QSPR models from SMILES. Use when choosing among molecular featurizers for a property prediction task. Use when generating embeddings for virtual screening, similarity search, or chemical space clustering. Use when adding a featurizer to a scikit-learn pipeline. Not for general cheminformatics tasks such as reading or editing structures, which belong to RDKit itself.

## Example requests

Ask your agent in plain language, for example:

- *"what's the best molfeat featurizer for a small solubility dataset?"*
- *"I have a file kinase_hits.csv with a 'smiles' column, about 40k rows. I'm trying to run `from molfeat.trans.pretrained import PretrainedHFTransformer` with ChemBERTa-77M-MLM to get embeddings for clustering, but pip install molfeat fails on my Python 3.11 env. How do I fix it and get the embeddings?"*
- *"I want to turn a list of drug-like SMILES into numeric vectors that I can drop into a scikit-learn Pipeline with a random forest to predict IC50, and I need it to run on all my CPU cores and not crash on a few bad SMILES. How should I set that up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill molfeat

# Kalaris Labs installer with checksum verification
npx research-agent-skills install molfeat
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `chemistry-and-drug-discovery` category with `/plugin install chemistry-and-drug-discovery@research-agent-skills`.

## Related

- [Skills for chemistry and drug discovery](/fields/chemistry)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/molfeat/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
