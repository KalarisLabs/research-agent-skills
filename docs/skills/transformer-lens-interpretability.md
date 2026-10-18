---
title: "transformer-lens-interpretability — AI agent skill for ml evaluation and safety"
description: "Provides guidance for mechanistic interpretability research using TransformerLens to inspect and manipulate transformer internals via HookPoints and…"
keywords: ["Mechanistic Interpretability", "TransformerLens", "Activation Patching", "Circuit Analysis"]
---

# `transformer-lens-interpretability`

**Category:** [ml-evaluation-and-safety](/skills#ml-evaluation-and-safety) · **License:** MIT · **Version:** 1.0.0

**Tags:** Mechanistic Interpretability, TransformerLens, Activation Patching, Circuit Analysis

## When to use it

Provides guidance for mechanistic interpretability research using TransformerLens to inspect and manipulate transformer internals via HookPoints and activation caching. Use when reverse-engineering model algorithms, studying attention patterns, or performing activation patching experiments.

## Example requests

Ask your agent in plain language, for example:

- *"How do I cache all activations for gpt2-small on a prompt and look at layer 5 attention patterns?"*
- *"I'm working in ioi_patching.ipynb with gpt2-small on 200 IOI prompts (e.g. 'When Mary and John went to the store, John gave a drink to'). I want to run path/activation patching over resid_pre at every layer and position and plot a heatmap of logit-difference recovery, but my corrupted and clean prompts have different token lengths and I get a shape mismatch error in the hook. What should I do?"*
- *"I trained a tiny 2-layer attention-only transformer on repeated random token sequences and want to figure out which heads copy the token that followed the previous occurrence of the current token, and prove they're doing so causally. How should I go about it?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill transformer-lens-interpretability

# Kalaris Labs installer with checksum verification
npx research-agent-skills install transformer-lens-interpretability
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-evaluation-and-safety` category with `/plugin install ml-evaluation-and-safety@research-agent-skills`.

## Related

- [`nnsight-remote-interpretability`](/skills/nnsight-remote-interpretability)
- [`pyvene-interventions`](/skills/pyvene-interventions)
- [`sparse-autoencoder-training`](/skills/sparse-autoencoder-training)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/transformer-lens-interpretability/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
