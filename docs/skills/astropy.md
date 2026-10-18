---
title: "astropy — AI agent skill for physical sciences"
description: "Core Python library for astronomy and astrophysics workflows that need Astropy APIs, including units/quantities, coordinates, FITS I/O, tables, time systems…"
keywords: ["astronomy", "astrophysics", "FITS", "coordinates", "cosmology", "physics"]
---

# `astropy`

**Category:** [physical-sciences](/skills#physical-sciences) · **License:** BSD-3-Clause license · **Version:** 1.3

**Tags:** astronomy, astrophysics, FITS, coordinates, cosmology, physics

## When to use it

Core Python library for astronomy and astrophysics workflows that need Astropy APIs, including units/quantities, coordinates, FITS I/O, tables, time systems, WCS, and cosmology. Use when implementing or debugging astronomical data analysis code with Astropy.

## Example requests

Ask your agent in plain language, for example:

- *"How do I convert a list of RA/Dec in ICRS to Galactic l, b?"*
- *"I'm opening ngc1300_drz.fits with fits.open and want the science image from the 'SCI' extension plus the EXPTIME keyword. Then I need to turn pixel (512, 480) into RA/Dec. I'm getting 'WARNING: FITSFixedWarning: 'datfix' made the change...' when I build the WCS. What's going on and how should I write this?"*
- *"I have a catalog of supernova redshifts and need to know how far away they are in Mpc and how long ago the light left, assuming a flat universe with H0=70 and Om0=0.3. I'd also like to go back from a given distance to a redshift."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill astropy

# Kalaris Labs installer with checksum verification
npx research-agent-skills install astropy
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `physical-sciences` category with `/plugin install physical-sciences@research-agent-skills`.

## Related

- [`uncertainty-and-units`](/skills/uncertainty-and-units)
- [Skills for physics and astronomy](/fields/physics)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/astropy/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
