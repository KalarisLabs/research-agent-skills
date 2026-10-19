---
title: "mlflow — AI agent skill for ml inference and ops"
description: "Tracks machine learning experiments and manages model lifecycles with MLflow, covering mlflow.log_param, log_metric and log_artifact, autologging for…"
keywords: ["MLOps", "MLflow", "Experiment Tracking", "Model Registry", "ML Lifecycle", "Deployment", "Model Versioning", "PyTorch", "TensorFlow", "Scikit-Learn", "HuggingFace"]
---

# `mlflow`

**Category:** [ml-inference-and-ops](/skills#ml-inference-and-ops) · **License:** MIT · **Version:** 1.0.0

**Tags:** MLOps, MLflow, Experiment Tracking, Model Registry, ML Lifecycle, Deployment, Model Versioning, PyTorch, TensorFlow, Scikit-Learn, HuggingFace

## When to use it

Tracks machine learning experiments and manages model lifecycles with MLflow, covering mlflow.log_param, log_metric and log_artifact, autologging for scikit-learn, PyTorch Lightning, XGBoost and HuggingFace Transformers, the Model Registry with versions and stage transitions, run searching, and local or cloud model serving. Use when logging parameters, metrics and artifacts for training runs, comparing runs across experiments, registering and promoting model versions from Staging to Production, serving a logged model for inference, or reproducing an experiment from an MLflow project. Not for hyperparameter-sweep dashboards or general data versioning; use a dedicated tool for those.

## Example requests

Ask your agent in plain language, for example:

- *"How do I log my sklearn model's accuracy to MLflow?"*
- *"I'm training an XGBoost classifier on train.csv for churn prediction and have a tracking server at http://localhost:5000. I ran 12 configs with different max_depth and learning_rate, and now want to pull the run with the best val_auc, register that model as 'churn-xgb', and move it to Production. Getting 'RestException: RESOURCE_DOES_NOT_EXIST' when I call transition_model_version_stage. What should I do?"*
- *"I fine-tuned a BERT classifier last month and can't remember which learning rate and epoch count gave my best F1. I'd like each training run automatically recorded with its settings, scores and saved weights so I can compare them side by side later and ask a teammate to rerun the exact best one on their machine. How should I set that up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill mlflow

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills mlflow
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-inference-and-ops` category with `/plugin install ml-inference-and-ops@research-agent-skills`.

## Related

- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/mlflow/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
