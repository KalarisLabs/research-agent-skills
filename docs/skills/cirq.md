---
title: "cirq — AI agent skill for physical sciences"
description: "Google quantum computing framework."
keywords: ["quantum computing", "quantum circuits", "noise modeling", "physics"]
---

# `cirq`

**Category:** [physical-sciences](/skills#physical-sciences) · **License:** Apache-2.0 license · **Version:** 1.1

**Tags:** quantum computing, quantum circuits, noise modeling, physics

## When to use it

Google quantum computing framework. Use when targeting Google Quantum AI hardware, designing noise-aware circuits, or running quantum characterization experiments. Best for Google hardware, noise modeling, and low-level circuit design. For IBM hardware use qiskit; for quantum ML with autodiff use pennylane; for physics simulations use qutip.

## Example requests

Ask your agent in plain language, for example:

- *"How do I add depolarizing noise to every gate in a Cirq circuit and compare the result to the ideal one?"*
- *"I'm running cirq 1.6.1 with cirq-google and my 12-qubit circuit in qaoa_maxcut.py fails on a Willow processor target with 'Operation not supported by device gateset' (a CZ-decomposed circuit with a raw CNOT left in). How do I get it to compile and validate before submitting through Quantum Engine?"*
- *"I want to measure how good the two-qubit gates are on my 20-qubit chip by running random circuits of increasing depth and fitting the fidelity decay. Can you set up the characterization experiment and analysis in Python using Google's stack?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill cirq

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills cirq
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `physical-sciences` category with `/plugin install physical-sciences@research-agent-skills`.

## Related

- [Skills for physics and astronomy](/fields/physics)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/cirq/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
