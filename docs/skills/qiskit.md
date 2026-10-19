---
title: "qiskit — AI agent skill for physical sciences"
description: "Build, simulate, transpile, and execute quantum circuits with Qiskit and IBM Quantum Runtime."
keywords: ["quantum computing", "quantum circuits", "IBM Quantum", "physics"]
---

# `qiskit`

**Category:** [physical-sciences](/skills#physical-sciences) · **License:** Apache-2.0 · **Version:** 2.1 · **Includes scripts**

**Tags:** quantum computing, quantum circuits, IBM Quantum, physics

## When to use it

Build, simulate, transpile, and execute quantum circuits with Qiskit and IBM Quantum Runtime. Use for Qiskit 2.x circuits and operators, V2 Sampler or Estimator primitives, target-aware transpilation, local or noisy simulation, IBM QPU execution, Runtime sessions or batches, error mitigation, and Qiskit ecosystem packages.

## Example requests

Ask your agent in plain language, for example:

- *"How do I run a Bell state circuit locally in Qiskit and get the counts?"*
- *"I'm getting 'The instruction cx is not supported by the target' when I submit my VQE ansatz ansatz.py to ibm_brisbane through EstimatorV2 with a SparsePauliOp H2 Hamiltonian. The job fails right away. What am I doing wrong and how do I fix it?"*
- *"I have a parameterized circuit for a variational energy minimization and want to run the optimization loop on real IBM quantum hardware without wasting queue time between iterations or re-compiling every step. What's the right way to structure the runs, and how can I reduce the effect of hardware noise on the energies?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill qiskit

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills qiskit
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `physical-sciences` category with `/plugin install physical-sciences@research-agent-skills`.

## Related

- [`pi-agent`](/skills/pi-agent)
- [Skills for physics and astronomy](/fields/physics)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/qiskit/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
