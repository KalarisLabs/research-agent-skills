---
title: "pymc — AI agent skill for data science and ml"
description: "Builds, fits, checks, and compares Bayesian models in Python with PyMC and ArviZ."
keywords: ["Bayesian statistics", "MCMC", "probabilistic programming", "hierarchical models", "statistics"]
---

# `pymc`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** Apache License, Version 2.0 · **Version:** 1.4 · **Includes scripts**

**Tags:** Bayesian statistics, MCMC, probabilistic programming, hierarchical models, statistics

## When to use it

Builds, fits, checks, and compares Bayesian models in Python with PyMC and ArviZ. Covers hierarchical (multilevel) models, NUTS MCMC sampling, variational inference (ADVI), prior and posterior predictive checks, convergence diagnostics (R-hat, ESS, divergences), and LOO/WAIC model comparison. Use when writing a PyMC model for regression, count, or binary data. Use when fitting a hierarchical model with partial pooling. Use when diagnosing divergences, low ESS, or high R-hat. Use when comparing candidate models with LOO. Use when choosing priors or running prior predictive checks. Not for non-Bayesian regression; use statsmodels or scikit-learn instead.

## Example requests

Ask your agent in plain language, for example:

- *"Can you help me fit a hierarchical logistic model for patient response across 12 hospitals? I want partial pooling."*
- *"My PyMC model on trial_counts.csv (Poisson likelihood, site random effects) gives 'There were 214 divergences after tuning' and r_hat of 1.07 for tau. Raising target_accept to 0.99 didn't help. What should I do?"*
- *"I have two candidate models for reaction times in a psychology experiment, one with a per-subject slope and one without. How do I decide which one predicts new subjects better, with uncertainty on the difference, in a Bayesian framework?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pymc

# Kalaris Labs installer with checksum verification
npx research-agent-skills install pymc
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [`statistical-analysis`](/skills/statistical-analysis)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pymc/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
