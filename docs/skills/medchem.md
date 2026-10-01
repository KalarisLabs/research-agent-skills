---
title: "medchem — AI agent skill for chemistry and drug discovery"
description: "Filters and triages small-molecule libraries with the Python medchem library (datamol-io, v2.0.5) on top of RDKit and datamol."
---

# `medchem`

> Filters and triages small-molecule libraries with the Python medchem library (datamol-io, v2.0.5) on top of RDKit and datamol. Covers drug-likeness rules (Lipinski, Veber, CNS, lead-like) via RuleFilters, structural alerts (ChEMBL-derived sets, NIBR, PAINS, Brenk), chemical group detection, ZINC-based complexity thresholds, scaffold constraints, and the medchem query language (QueryFilter). Use when screening a compound library for drug-likeness, removing PAINS or other structural-alert compounds, prioritizing hits for hit-to-lead or lead optimization, detecting functional groups, or combining criteria in one query. Not for computing general descriptors or fingerprints; use RDKit directly.

**Category:** [chemistry-and-drug-discovery](/skills#chemistry-and-drug-discovery) · **License:** Apache-2.0 license · **Version:** 1.2

## Install

```bash
npx research-agent-skills install medchem
npx skills add KalarisLabs/research-agent-skills --skill medchem
```

## When to use it

Filters and triages small-molecule libraries with the Python medchem library (datamol-io, v2.0.5) on top of RDKit and datamol. Covers drug-likeness rules (Lipinski, Veber, CNS, lead-like) via RuleFilters, structural alerts (ChEMBL-derived sets, NIBR, PAINS, Brenk), chemical group detection, ZINC-based complexity thresholds, scaffold constraints, and the medchem query language (QueryFilter). Use when screening a compound library for drug-likeness, removing PAINS or other structural-alert compounds, prioritizing hits for hit-to-lead or lead optimization, detecting functional groups, or combining criteria in one query. Not for computing general descriptors or fingerprints; use RDKit directly.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/medchem/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
