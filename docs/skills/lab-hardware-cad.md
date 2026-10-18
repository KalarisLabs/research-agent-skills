---
title: "lab-hardware-cad — AI agent skill for lab automation"
description: "Design custom laboratory hardware as parametric build123d models and export fabrication-ready STEP, STL, and DXF files - microfluidic chips and molds…"
keywords: ["lab hardware", "CAD", "3D printing", "microfluidics", "open hardware"]
---

# `lab-hardware-cad`

**Category:** [lab-automation](/skills#lab-automation) · **License:** MIT · **Version:** 1.3 · **Includes scripts**

**Tags:** lab hardware, CAD, 3D printing, microfluidics, open hardware

## When to use it

Design custom laboratory hardware as parametric build123d models and export fabrication-ready STEP, STL, and DXF files - microfluidic chips and molds, optomechanical mounts and breadboard adapters, cuvette and microplate holders, tube racks, animal-behavior rigs, and 3D-printed instrument fixtures. Use when a research task needs a physical part that must mate with standardized labware, an optical table, a cage system, or a printer, CNC, or laser process.

## Example requests

Ask your agent in plain language, for example:

- *"I need a 3D-printable adapter that holds a standard 96-well plate on my microscope stage insert. Can you model it?"*
- *"I have a PDMS mold design for a T-junction droplet generator, 50 µm tall x 100 µm wide channels, 1/16" OD tubing inlets. Write me a parametric build123d script `droplet_mold_model.py` and export STEP plus a DXF for the photomask. Our mold will be made by SLA printing because the cleanroom is booked."*
- *"We want to hold a 1-inch filter in the beam path of our setup and bolt it to the optical table. I don't know what the hole spacing on our table is. What should we make?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill lab-hardware-cad

# Kalaris Labs installer with checksum verification
npx research-agent-skills install lab-hardware-cad
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `lab-automation` category with `/plugin install lab-automation@research-agent-skills`.

## Related

- [`fictiv`](/skills/fictiv)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/lab-hardware-cad/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
