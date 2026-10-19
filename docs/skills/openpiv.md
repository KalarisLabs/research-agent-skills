---
title: "openpiv — AI agent skill for physical sciences"
description: "Particle Image Velocimetry (PIV) analysis with OpenPIV."
keywords: ["particle image velocimetry", "PIV", "fluid dynamics", "flow visualization", "physics"]
---

# `openpiv`

**Category:** [physical-sciences](/skills#physical-sciences) · **License:** BSD-3-Clause · **Version:** 1.1 · **Includes scripts**

**Tags:** particle image velocimetry, PIV, fluid dynamics, flow visualization, physics

## When to use it

Particle Image Velocimetry (PIV) analysis with OpenPIV. Use when extracting velocity fields from PIV image pairs, analyzing fluid dynamics or flow visualization experiments, cross-correlating interrogation windows, validating and replacing spurious PIV vectors, or computing vorticity, strain rate, and turbulence statistics from measured velocity fields.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get a velocity field out of two PIV frames?"*
- *"I have two TIFFs from our water-tunnel run, cyl_0001_a.tif and cyl_0001_b.tif, dt = 0.5 ms, and the calibration is 12 px/mm. I used multi-pass in windef with settings.dt set, but my u,v are still around 4 – this looks like pixels, not mm/s. What's wrong, and how do I validate the vectors afterwards? I used a (-30, 30) limit."*
- *"I've got a grid of 2D velocity vectors measured from seeded flow around a cylinder. I want to know where the flow is rotating and how much, and whether the field is turbulent. What should I compute and how should I be careful?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill openpiv

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills openpiv
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `physical-sciences` category with `/plugin install physical-sciences@research-agent-skills`.

## Related

- [Skills for physics and astronomy](/fields/physics)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/openpiv/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
