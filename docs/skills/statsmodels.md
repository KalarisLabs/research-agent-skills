---
title: "statsmodels — AI agent skill for data science and ml"
description: "Statistical models library for Python."
keywords: ["statistical models", "regression", "time series", "econometrics", "statistics"]
---

# `statsmodels`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** BSD-3-Clause license · **Version:** 1.3

**Tags:** statistical models, regression, time series, econometrics, statistics

## When to use it

Statistical models library for Python. Use when you need specific model classes (OLS, GLM, mixed models, ARIMA) with detailed diagnostics, residuals, and inference. Best for econometrics, time series, rigorous inference with coefficient tables. For guided statistical test selection with APA reporting use statistical-analysis.

## Example requests

Ask your agent in plain language, for example:

- *"How do I fit a negative binomial model in statsmodels and check whether my Poisson fit is overdispersed?"*
- *"I have panel.csv with columns firm_id, year, log_wage, tenure, educ. I ran smf.ols('log_wage ~ tenure + educ', data=df).fit() and the Breusch-Pagan test rejects. Observations within firm are clearly correlated. How should I get defensible standard errors and show them in a table for my econometrics paper?"*
- *"I have 15 years of monthly retail sales numbers with an obvious holiday bump each December. I want a forecast for the next 12 months with uncertainty bands and some confidence that the model is reasonable."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill statsmodels

# Kalaris Labs installer with checksum verification
npx research-agent-skills install statsmodels
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [`statistical-analysis`](/skills/statistical-analysis)
- [`timesfm-forecasting`](/skills/timesfm-forecasting)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/statsmodels/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
