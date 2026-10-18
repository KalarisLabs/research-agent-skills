---
title: "scikit-survival — AI agent skill for data science and ml"
description: "Builds, evaluates, and audits right-censored survival analysis workflows with scikit-survival (sksurv): Cox PH, Coxnet, IPC ridge, survival trees, forests…"
keywords: ["survival analysis", "Cox regression", "time-to-event", "biostatistics", "machine learning"]
---

# `scikit-survival`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** survival analysis, Cox regression, time-to-event, biostatistics, machine learning

## When to use it

Builds, evaluates, and audits right-censored survival analysis workflows with scikit-survival (sksurv): Cox PH, Coxnet, IPC ridge, survival trees, forests, boosting, and SVMs, plus nonparametric cumulative incidence for competing risks. Covers leakage-safe scikit-learn pipelines, nested CV, and censoring-aware metrics. Use when fitting survival models on time-to-event data, building structured outcome arrays, computing IPCW concordance, dynamic AUC, or Brier scores, estimating cause-specific cumulative incidence, or tuning models without leakage. Not for Fine-Gray regression, which scikit-survival does not provide.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get Uno's C-index for my Coxnet model in sksurv? I keep getting an error about survival_train."*
- *"I have clinic_outcomes.csv with columns age, sex, creatinine, stage, months_to_relapse, relapsed (0/1), and about 8% missing creatinine. I want to compare a random survival forest and a penalized Cox model, tune hyperparameters, and report an honest cross-validated integrated Brier score and time-dependent AUC. Currently I impute and scale the whole table first, then run GridSearchCV. Can you fix this workflow?"*
- *"My transplant cohort has patients who either relapse, die without relapse, or are censored at last follow-up. I want to estimate the probability of relapse by 3 years without treating death as just censoring. What should I do in Python?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill scikit-survival

# Kalaris Labs installer with checksum verification
npx research-agent-skills install scikit-survival
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/scikit-survival/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
