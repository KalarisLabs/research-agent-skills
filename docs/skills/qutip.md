---
title: "qutip — AI agent skill for physical sciences"
description: "Simulate and audit closed and open quantum-system models with QuTiP 5, including deterministic, trajectory, steady-state, spectral, and phase-space workflows."
keywords: ["quantum dynamics", "open quantum systems", "quantum simulation", "physics"]
---

# `qutip`

**Category:** [physical-sciences](/skills#physical-sciences) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** quantum dynamics, open quantum systems, quantum simulation, physics

## When to use it

Simulate and audit closed and open quantum-system models with QuTiP 5, including deterministic, trajectory, steady-state, spectral, and phase-space workflows. Use for local quantum-dynamics work where physical assumptions, dimensions, and numerical convergence must be explicit.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get a damped driven qubit's Rabi oscillations in QuTiP with T1 and T2 decay?"*
- *"I'm modeling a transmon coupled to a readout cavity in qutip 5.3 for my paper. H = tensor(a.dag()*a, qeye(2)) + ... and I call mesolve(H, psi0, tlist, [kappa*a], [n]) but the photon number comes out wrong and ptrace([1]) gives me a 2x2 state when I wanted the cavity. How do I fix this and show the Fock cutoff is adequate?"*
- *"I have a driven, lossy resonator and I want the emission spectrum of its steady state, and I want to be sure the numbers aren't an artifact of how I discretized the time window. What should I do?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill qutip

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills qutip
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `physical-sciences` category with `/plugin install physical-sciences@research-agent-skills`.

## Related

- [Skills for physics and astronomy](/fields/physics)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/qutip/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
