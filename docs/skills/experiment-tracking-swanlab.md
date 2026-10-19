---
title: "experiment-tracking-swanlab — AI agent skill for ml inference and ops"
description: "Tracks ML experiments with SwanLab, an open-source tool covering swanlab.init, config and metric logging, scalar charts, and media logging (images, audio…"
keywords: ["MLOps", "SwanLab", "Experiment Tracking", "Open Source", "Visualization", "PyTorch", "Transformers", "PyTorch Lightning", "Fastai", "Self-Hosted"]
---

# `experiment-tracking-swanlab`

**Category:** [ml-inference-and-ops](/skills#ml-inference-and-ops) · **License:** MIT · **Version:** 1.0.0

**Tags:** MLOps, SwanLab, Experiment Tracking, Open Source, Visualization, PyTorch, Transformers, PyTorch Lightning, Fastai, Self-Hosted

## When to use it

Tracks ML experiments with SwanLab, an open-source tool covering swanlab.init, config and metric logging, scalar charts, and media logging (images, audio, text, GIFs, point clouds, molecules), in cloud, local (mode="local" with swanlab[dashboard]), or self-hosted setups. Includes integrations for PyTorch, Transformers, PyTorch Lightning, and Fastai. Use when logging metrics and hyperparameters for training runs, comparing runs across seeds, checkpoints, or hyperparameters, running an offline or self-hosted dashboard instead of managed SaaS, logging media alongside scalars, or adding tracking callbacks to a Transformers, Lightning, or Fastai training loop. Not for other trackers such as Weights & Biases or MLflow.

## Example requests

Ask your agent in plain language, for example:

- *"How do I log loss and accuracy per epoch to SwanLab?"*
- *"I'm fine-tuning bert-base-uncased on SST-2 with a HuggingFace Trainer in train_sst2.py. I want the loss curves and my learning rate / batch size / seed recorded so I can compare three seeds side by side. The cluster has no internet, so it has to work offline. How should I set this up?"*
- *"My lab doesn't want training data going to a third-party SaaS. I need something open-source that I can host on our own server to see training curves and also look at the generated images and audio samples from my GAN next to the loss plots. What should I use and how do I wire it into my PyTorch loop?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill experiment-tracking-swanlab

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills experiment-tracking-swanlab
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-inference-and-ops` category with `/plugin install ml-inference-and-ops@research-agent-skills`.

## Related

- [`pytorch-lightning`](/skills/pytorch-lightning)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/experiment-tracking-swanlab/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
