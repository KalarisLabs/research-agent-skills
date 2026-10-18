---
title: "fluidsim — AI agent skill for physical sciences"
description: "Plan, configure, inspect, restart, and analyze bounded FluidSim computational-fluid-dynamics simulations with explicit numerical-validity and HPC safety…"
keywords: ["computational fluid dynamics", "CFD", "simulation", "HPC", "physics"]
---

# `fluidsim`

**Category:** [physical-sciences](/skills#physical-sciences) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** computational fluid dynamics, CFD, simulation, HPC, physics

## When to use it

Plan, configure, inspect, restart, and analyze bounded FluidSim computational-fluid-dynamics simulations with explicit numerical-validity and HPC safety checks. Use for FluidSim solver selection, parameter review, FFT/MPI setup, output diagnostics, or restart compatibility.

## Example requests

Ask your agent in plain language, for example:

- *"I need to run a 2D turbulence sim with fluidsim, 256x256 periodic box. Can you set it up safely?"*
- *"I have a run in ~/runs/ns2d_forced_512/ with state_phys_t*.nc files and spectra1D.h5. I tried `params.time_stepping.CFL = 0.5` and got an AttributeError from ParamContainer when restarting with a modified script. I want to restart to t=200 on 8 MPI ranks on our cluster. What's wrong and how do I restart safely?"*
- *"I'm simulating forced 3D homogeneous turbulence on a periodic cube in Python, and my collaborators want to know if our 128^3 spectral run is resolved enough to call it DNS. What should I check, and can you look at the output files?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill fluidsim

# Kalaris Labs installer with checksum verification
npx research-agent-skills install fluidsim
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `physical-sciences` category with `/plugin install physical-sciences@research-agent-skills`.

## Related

- [Skills for physics and astronomy](/fields/physics)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/fluidsim/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
