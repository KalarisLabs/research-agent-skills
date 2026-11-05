---
title: "diffdock — AI agent skill for chemistry and drug discovery"
description: "DiffDock and DiffDock-L molecular docking."
keywords: ["molecular docking", "virtual screening", "structural biology", "drug discovery"]
---

# `diffdock`

**Category:** [chemistry-and-drug-discovery](/skills#chemistry-and-drug-discovery) · **License:** MIT · **Version:** 1.3 · **Includes scripts**

**Tags:** molecular docking, virtual screening, structural biology, drug discovery

## When to use it

DiffDock and DiffDock-L molecular docking. Use for protein-small-molecule pose prediction from PDB or sequence plus SMILES/SDF/MOL2, batch docking, virtual screening, and pose-confidence interpretation. Not for binding affinity prediction.

## Example requests

Ask your agent in plain language, for example:

- *"Dock this SMILES CC(=O)Oc1ccccc1C(=O)O into my protein.pdb and give me the top poses."*
- *"I have 240 compounds in screen_hits.csv (columns: name, smiles) and a kinase structure 5ZZZ_clean.pdb. I ran inference.py and got CUDA out of memory partway through the batch. How do I set this up as a batch run and get it to finish, and then rank the results?"*
- *"I only have the amino acid sequence of my target, no crystal structure, and a small molecule I drew in an SDF. I want to know where on the protein it likely sits and how sure the model is about that, since I don't know the binding site."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill diffdock

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills diffdock
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `chemistry-and-drug-discovery` category with `/plugin install chemistry-and-drug-discovery@research-agent-skills`.

## Related

- [Skills for chemistry and drug discovery](/fields/chemistry)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/diffdock/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
