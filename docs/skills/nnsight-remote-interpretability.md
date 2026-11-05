---
title: "nnsight-remote-interpretability — AI agent skill for ml evaluation and safety"
description: "Provides guidance for interpreting and manipulating neural network internals using nnsight with optional NDIF remote execution."
keywords: ["nnsight", "NDIF", "Remote Execution", "Mechanistic Interpretability", "Model Internals"]
---

# `nnsight-remote-interpretability`

**Category:** [ml-evaluation-and-safety](/skills#ml-evaluation-and-safety) · **License:** MIT · **Version:** 1.0.0

**Tags:** nnsight, NDIF, Remote Execution, Mechanistic Interpretability, Model Internals

## When to use it

Provides guidance for interpreting and manipulating neural network internals using nnsight with optional NDIF remote execution. Use when needing to run interpretability experiments on massive models (70B+) without local GPU resources, or when working with any PyTorch architecture.

## Example requests

Ask your agent in plain language, for example:

- *"How do I grab the layer 20 residual stream from Llama-3.1-70B when I don't have a GPU?"*
- *"I'm running activation patching on Llama-3.1-8B for my IOI-style prompts in ioi_patch.py. Locally it works, but when I set remote=True my loop over layers keeps timing out, and sometimes I get an error that my saved tensor is a Proxy object outside the with block. How do I fix it?"*
- *"I want to see what a Mamba state space model represents internally at each block, and copy the hidden state from one prompt into another prompt's forward pass. I'd rather not rewrite the model in some interpretability library. What approach works?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill nnsight-remote-interpretability

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills nnsight-remote-interpretability
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-evaluation-and-safety` category with `/plugin install ml-evaluation-and-safety@research-agent-skills`.

## Related

- [`slime-rl-training`](/skills/slime-rl-training)
- [`sparse-autoencoder-training`](/skills/sparse-autoencoder-training)
- [`transformer-lens-interpretability`](/skills/transformer-lens-interpretability)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/nnsight-remote-interpretability/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
