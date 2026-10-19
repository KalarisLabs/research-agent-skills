---
title: "weights-and-biases — AI agent skill for ml inference and ops"
description: "Logs and tracks machine learning experiments with Weights & Biases (W&B, wandb): metrics, hyperparameters, checkpoints, sweeps, artifacts with lineage, model…"
keywords: ["MLOps", "Weights And Biases", "WandB", "Experiment Tracking", "Hyperparameter Tuning", "Model Registry", "Collaboration", "Real-Time Visualization", "PyTorch", "TensorFlow", "HuggingFace"]
---

# `weights-and-biases`

**Category:** [ml-inference-and-ops](/skills#ml-inference-and-ops) · **License:** MIT · **Version:** 1.0.0

**Tags:** MLOps, Weights And Biases, WandB, Experiment Tracking, Hyperparameter Tuning, Model Registry, Collaboration, Real-Time Visualization, PyTorch, TensorFlow, HuggingFace

## When to use it

Logs and tracks machine learning experiments with Weights & Biases (W&B, wandb): metrics, hyperparameters, checkpoints, sweeps, artifacts with lineage, model registry, custom charts and shareable reports. Includes integrations for PyTorch, HuggingFace Transformers, PyTorch Lightning and Keras/TensorFlow. Use when logging training runs and comparing them across configurations, running automated hyperparameter sweeps, versioning datasets and models as artifacts, registering model versions, or sharing results with a team workspace. Use when setting up wandb.init for offline or unstable-connection training. Not for general data versioning outside ML runs.

## Example requests

Ask your agent in plain language, for example:

- *"How do I log my loss curves to wandb?"*
- *"I'm fine-tuning bert-base-uncased with HuggingFace Trainer in train_glue.py on a cluster with a flaky network, and my run keeps crashing with 'wandb: ERROR Error communicating with wandb process' and 'CommError: Run initialization has timed out'. I want to keep the metrics and upload them later. How should I set this up?"*
- *"I've trained 40 ResNet variants with different learning rates, batch sizes and weight decays. I want the search over those settings automated so I can see which combination gives the best validation accuracy, and then share a summary with my labmates. What should I do?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill weights-and-biases

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills weights-and-biases
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-inference-and-ops` category with `/plugin install ml-inference-and-ops@research-agent-skills`.

## Related

- [`ray-train`](/skills/ray-train)
- [`scikit-learn`](/skills/scikit-learn)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/weights-and-biases/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
