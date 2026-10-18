---
title: "pyvene-interventions — AI agent skill for ml evaluation and safety"
description: "Provides guidance for performing causal interventions on PyTorch models using pyvene's declarative intervention framework."
keywords: ["Causal Intervention", "pyvene", "Activation Patching", "Causal Tracing", "Interpretability"]
---

# `pyvene-interventions`

**Category:** [ml-evaluation-and-safety](/skills#ml-evaluation-and-safety) · **License:** MIT · **Version:** 1.0.0

**Tags:** Causal Intervention, pyvene, Activation Patching, Causal Tracing, Interpretability

## When to use it

Provides guidance for performing causal interventions on PyTorch models using pyvene's declarative intervention framework. Use when conducting causal tracing, activation patching, interchange intervention training, or testing causal hypotheses about model behavior.

## Example requests

Ask your agent in plain language, for example:

- *"How do I do activation patching with pyvene on GPT-2?"*
- *"I'm replicating ROME-style causal tracing on gpt2-xl for the prompt 'The Space Needle is located in the city of'. I corrupted the subject tokens with Gaussian noise, and now I want to restore the clean hidden state at each (layer, token position) and plot a heatmap of the recovered probability for ' Seattle'. I'm using pyvene and getting a dimension mismatch error when I set the intervention location. How should I set this up and fix it?"*
- *"I think a model represents whether a number is greater than a threshold in a low-dimensional linear subspace of one layer's residual stream. I want to learn that subspace by training with counterfactual pairs and then test if swapping it flips the model's output. What approach and library setup would you recommend?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pyvene-interventions

# Kalaris Labs installer with checksum verification
npx research-agent-skills install pyvene-interventions
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-evaluation-and-safety` category with `/plugin install ml-evaluation-and-safety@research-agent-skills`.

## Related

- [`hypothesis-generation`](/skills/hypothesis-generation)
- [`langsmith-observability`](/skills/langsmith-observability)
- [`transformer-lens-interpretability`](/skills/transformer-lens-interpretability)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pyvene-interventions/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
