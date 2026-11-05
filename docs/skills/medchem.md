---
title: "medchem — AI agent skill for chemistry and drug discovery"
description: "Filters and triages small-molecule libraries with the Python medchem library (datamol-io, v2.0.5) on top of RDKit and datamol."
keywords: ["medicinal chemistry", "drug-likeness", "PAINS", "structural alerts", "compound filtering"]
---

# `medchem`

**Category:** [chemistry-and-drug-discovery](/skills#chemistry-and-drug-discovery) · **License:** Apache-2.0 license · **Version:** 1.2 · **Includes scripts**

**Tags:** medicinal chemistry, drug-likeness, PAINS, structural alerts, compound filtering

## When to use it

Filters and triages small-molecule libraries with the Python medchem library (datamol-io, v2.0.5) on top of RDKit and datamol. Covers drug-likeness rules (Lipinski, Veber, CNS, lead-like) via RuleFilters, structural alerts (ChEMBL-derived sets, NIBR, PAINS, Brenk), chemical group detection, ZINC-based complexity thresholds, scaffold constraints, and the medchem query language (QueryFilter). Use when screening a compound library for drug-likeness, removing PAINS or other structural-alert compounds, prioritizing hits for hit-to-lead or lead optimization, detecting functional groups, or combining criteria in one query. Not for computing general descriptors or fingerprints; use RDKit directly.

## Example requests

Ask your agent in plain language, for example:

- *"How do I strip PAINS hits out of a SMILES list with medchem?"*
- *"I have hits.csv with ~40k compounds (columns: id, smiles) from a biochemical screen. I need to keep those passing Lipinski and Veber, drop anything with NIBR severity >= 10 or Brenk alerts, and keep the reasons for each rejection for the audit trail. It's slow on my laptop. What should I run?"*
- *"I'm prioritizing a set of kinase inhibitor hits for lead optimization. I want only compounds that are CNS-friendly, have no reactive or toxic substructures, and contain a benzene ring or an amide. Can I express all of that as a single combined filter instead of chaining several steps?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill medchem

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills medchem
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `chemistry-and-drug-discovery` category with `/plugin install chemistry-and-drug-discovery@research-agent-skills`.

## Related

- [Skills for chemistry and drug discovery](/fields/chemistry)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/medchem/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
