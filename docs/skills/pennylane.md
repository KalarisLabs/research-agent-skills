---
title: "pennylane — AI agent skill for physical sciences"
description: "Hardware-agnostic quantum ML framework with automatic differentiation."
keywords: ["quantum machine learning", "quantum computing", "variational algorithms", "physics"]
---

# `pennylane`

**Category:** [physical-sciences](/skills#physical-sciences) · **License:** Apache-2.0 license · **Version:** 1.2

**Tags:** quantum machine learning, quantum computing, variational algorithms, physics

## When to use it

Hardware-agnostic quantum ML framework with automatic differentiation. Use when training quantum circuits via gradients, building hybrid quantum-classical models, or needing device portability across IBM/Google/Rigetti/IonQ. Best for variational algorithms (VQE, QAOA), quantum neural networks, and integration with PyTorch or JAX. For hardware-specific optimizations use qiskit (IBM) or cirq (Google); for open quantum systems use qutip.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get gradients of a quantum circuit's expectation value w.r.t. its parameters and train it with Adam?"*
- *"I have a 4-qubit angle-embedding classifier in qml.qnode with a torch.nn.Linear head, for iris_features.csv (4 features, 3 classes). Training with the torch interface gives 'RuntimeError: element 0 of tensors does not require grad' and the loss stays flat. Can you fix it so it trains end to end and then run it on a hardware-style device?"*
- *"I want to find the ground-state energy of an H2 molecule at several bond lengths with a variational quantum approach, and I'd like the same code to run on different vendors' backends by changing one line. Can you set that up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pennylane

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills pennylane
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `physical-sciences` category with `/plugin install physical-sciences@research-agent-skills`.

## Related

- [Skills for physics and astronomy](/fields/physics)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pennylane/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
