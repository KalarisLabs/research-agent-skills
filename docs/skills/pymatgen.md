---
title: "pymatgen — AI agent skill for physical sciences"
description: "Analyzes, validates, converts, and transforms crystal structures and molecules with pymatgen."
keywords: ["materials science", "crystal structures", "computational materials", "VASP", "physics"]
---

# `pymatgen`

**Category:** [physical-sciences](/skills#physical-sciences) · **License:** MIT · **Version:** 1.3 · **Includes scripts**

**Tags:** materials science, crystal structures, computational materials, VASP, physics

## When to use it

Analyzes, validates, converts, and transforms crystal structures and molecules with pymatgen. It covers CIF/POSCAR/XYZ/JSON conversion, symmetry-tolerance sweeps, local phase diagrams from computed entries, VASP and Q-Chem I/O, band structure and DOS parsing, and bounded Materials Project (mp-api) queries. Use when validating a CIF or checking disorder and oxidation states. Use when assigning space groups and testing symprec sensitivity. Use when converting structure files and checking for representation loss. Use when building a convex hull from total energies. Use when querying Materials Project with explicit fields and limits. Not for general molecular dynamics or non-materials cheminformatics.

## Example requests

Ask your agent in plain language, for example:

- *"Can you sanity-check this CIF before I run anything on it?"*
- *"I have LiFePO4_mp-19017.cif from a collaborator and my VASP relax keeps failing with 'too close atoms'. I need to convert it to POSCAR for VASP. Will anything get lost in the conversion, and can you do it without overwriting the original?"*
- *"I computed total energies for Li, Co, O2 and a few LiCoO2 and Li2O polymorphs with the same PBE setup and want to know which phases sit on the hull and how far above it the rest are. How should I do that offline?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pymatgen

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills pymatgen
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `physical-sciences` category with `/plugin install physical-sciences@research-agent-skills`.

## Related

- [`protocolsio-integration`](/skills/protocolsio-integration)
- [Skills for physics and astronomy](/fields/physics)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pymatgen/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
