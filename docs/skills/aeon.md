---
title: "aeon — AI agent skill for data science and ml"
description: "This skill should be used for time series machine learning tasks including classification, regression, clustering, forecasting, anomaly detection…"
keywords: ["time series", "classification", "forecasting", "anomaly detection", "machine learning"]
---

# `aeon`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** BSD-3-Clause license · **Version:** 1.1

**Tags:** time series, classification, forecasting, anomaly detection, machine learning

## When to use it

This skill should be used for time series machine learning tasks including classification, regression, clustering, forecasting, anomaly detection, segmentation, and similarity search. Use when working with temporal data, sequential patterns, or time-indexed observations requiring specialized algorithms beyond standard ML approaches. Particularly suited for univariate and multivariate time series analysis with scikit-learn compatible APIs.

## Example requests

Ask your agent in plain language, for example:

- *"How do I train a fast classifier on my accelerometer windows? Shape is (500, 3, 128)."*
- *"I have ECG recordings in ecg_train.csv, with 1 row per beat, 140 columns for the samples and a final column for the label (normal or abnormal). I tried sklearn's RandomForest on the raw values and got about 70% accuracy. I'd like to try elastic-distance methods, and I got `ImportError: cannot import name 'ROCKETClassifier' from 'aeon.classification.convolution_based'`. Can you fix the import and compare 1-NN with DTW against a ROCKET-family model, using cross-validation?"*
- *"I have a year of minute-level vibration readings from a turbine. I need to flag the odd stretches and also work out where the machine switched operating regimes. There are no labels. What approach would you take?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill aeon

# Kalaris Labs installer with checksum verification
npx research-agent-skills install aeon
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [`crewai-multi-agent`](/skills/crewai-multi-agent)
- [`scikit-learn`](/skills/scikit-learn)
- [`timesfm-forecasting`](/skills/timesfm-forecasting)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/aeon/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
