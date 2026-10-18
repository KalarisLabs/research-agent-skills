---
title: "scikit-learn — AI agent skill for data science and ml"
description: "Covers classical machine learning in Python with scikit-learn (sklearn): classification and regression estimators, clustering and dimensionality reduction…"
keywords: ["machine learning", "scikit-learn", "classification", "regression", "cross-validation"]
---

# `scikit-learn`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** BSD-3-Clause license · **Version:** 1.3 · **Includes scripts**

**Tags:** machine learning, scikit-learn, classification, regression, cross-validation

## When to use it

Covers classical machine learning in Python with scikit-learn (sklearn): classification and regression estimators, clustering and dimensionality reduction, preprocessing, Pipeline and ColumnTransformer, cross-validation, metrics, and GridSearchCV hyperparameter tuning. Use when training or comparing classifiers and regressors on tabular or text data, clustering data and choosing the cluster count, building leakage-free preprocessing pipelines, evaluating models with cross-validation and metrics, or tuning hyperparameters. Not for deep learning; use a dedicated neural network framework instead.

## Example requests

Ask your agent in plain language, for example:

- *"random forest vs gradient boosting on my csv, which is better? use cross-val"*
- *"I have patients.csv with columns age, bmi, sex, smoker, region and a binary target 'readmitted' (about 8% positive). I'm doing StandardScaler on everything and then train_test_split, then LogisticRegression, and I get a ConvergenceWarning plus suspiciously high AUC. Can you fix this and set up a proper evaluation?"*
- *"I've got a table of 5,000 customers with about 20 numeric behavior measurements and no labels. I want to find natural groups and work out how many groups there really are, then show them in 2D."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill scikit-learn

# Kalaris Labs installer with checksum verification
npx research-agent-skills install scikit-learn
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [`aeon`](/skills/aeon)
- [`arboreto`](/skills/arboreto)
- [`datamol`](/skills/datamol)
- [`weights-and-biases`](/skills/weights-and-biases)
- [`timesfm-forecasting`](/skills/timesfm-forecasting)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/scikit-learn/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
