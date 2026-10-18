---
title: "tensorboard — AI agent skill for ml inference and ops"
description: "Logs and views ML training data in TensorBoard using PyTorch SummaryWriter and TensorFlow/Keras callbacks: scalars, images, text, histograms, model graphs…"
keywords: ["MLOps", "TensorBoard", "Visualization", "Training Metrics", "Model Debugging", "PyTorch", "TensorFlow", "Experiment Tracking", "Performance Profiling"]
---

# `tensorboard`

**Category:** [ml-inference-and-ops](/skills#ml-inference-and-ops) · **License:** MIT · **Version:** 1.0.0

**Tags:** MLOps, TensorBoard, Visualization, Training Metrics, Model Debugging, PyTorch, TensorFlow, Experiment Tracking, Performance Profiling

## When to use it

Logs and views ML training data in TensorBoard using PyTorch SummaryWriter and TensorFlow/Keras callbacks: scalars, images, text, histograms, model graphs, embedding projector, hyperparameter tables, PR curves, and TensorFlow or PyTorch profiler traces. Use when plotting loss and accuracy curves during training, comparing multiple runs in one dashboard, inspecting weight and gradient distributions, projecting embeddings with PCA or t-SNE, tracking hyperparameter experiments, or finding performance bottlenecks in a training loop. Not for hosted experiment tracking with team collaboration; use a dedicated tracking service for that.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get my PyTorch loss curve showing up in TensorBoard?"*
- *"I'm training a ResNet-18 on CIFAR-10 in train.py with a Keras-free PyTorch loop. Val accuracy is flat after epoch 5 and I suspect vanishing gradients in the early conv layers. I already have a SummaryWriter at runs/resnet18_lr1e-3. Add logging so I can inspect the weight and gradient distributions per layer every epoch, and also log a few misclassified validation images."*
- *"I ran 12 learning-rate and batch-size combos of my transformer and want one view where I can see which settings gave the best validation loss, and see all the loss curves overlaid without a pile of separate folders to dig through."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill tensorboard

# Kalaris Labs installer with checksum verification
npx research-agent-skills install tensorboard
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-inference-and-ops` category with `/plugin install ml-inference-and-ops@research-agent-skills`.

## Related

- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/tensorboard/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
