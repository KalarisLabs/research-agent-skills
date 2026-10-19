---
title: "sparse-autoencoder-training — AI agent skill for ml evaluation and safety"
description: "Provides guidance for training and analyzing Sparse Autoencoders (SAEs) using SAELens to decompose neural network activations into interpretable features."
keywords: ["Sparse Autoencoders", "SAE", "Mechanistic Interpretability", "Feature Discovery", "Superposition"]
---

# `sparse-autoencoder-training`

**Category:** [ml-evaluation-and-safety](/skills#ml-evaluation-and-safety) · **License:** MIT · **Version:** 1.0.0

**Tags:** Sparse Autoencoders, SAE, Mechanistic Interpretability, Feature Discovery, Superposition

## When to use it

Provides guidance for training and analyzing Sparse Autoencoders (SAEs) using SAELens to decompose neural network activations into interpretable features. Use when discovering interpretable features, analyzing superposition, or studying monosemantic representations in language models.

## Example requests

Ask your agent in plain language, for example:

- *"How do I load a pretrained SAE for GPT-2 small and see which features fire on a sentence?"*
- *"I'm training an SAE on layer 8 residual stream of Gemma 2B with SAELens (d_model 2048, d_sae 16384). After 20k steps, about 40% of my features are dead and the L0 is ~600. Here's my config: l1_coefficient=2e-4, lr=5e-4, l1_warm_up_steps=0. What should I change and what metrics should I check?"*
- *"I want to break apart a language model's internal activations into human-understandable concepts, because I think individual neurons are encoding multiple unrelated things at once. How should I go about it, and how do I check the concepts are really meaningful?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill sparse-autoencoder-training

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills sparse-autoencoder-training
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-evaluation-and-safety` category with `/plugin install ml-evaluation-and-safety@research-agent-skills`.

## Related

- [`nnsight-remote-interpretability`](/skills/nnsight-remote-interpretability)
- [`transformer-lens-interpretability`](/skills/transformer-lens-interpretability)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/sparse-autoencoder-training/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
