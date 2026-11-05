---
title: "timesfm-forecasting — AI agent skill for data science and ml"
description: "Zero-shot time series forecasting with Google's TimesFM foundation model."
keywords: ["time series forecasting", "foundation models", "zero-shot forecasting"]
---

# `timesfm-forecasting`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** Apache-2.0 license · **Version:** 1.2 · **Includes scripts**

**Tags:** time series forecasting, foundation models, zero-shot forecasting

## When to use it

Zero-shot time series forecasting with Google's TimesFM foundation model. Use for any univariate time series (sales, sensors, energy, vitals, weather) without training a custom model. Supports CSV/DataFrame/array inputs with point forecasts and prediction intervals. Includes a preflight system checker script to verify RAM/GPU before first use.

## Example requests

Ask your agent in plain language, for example:

- *"Forecast the next 30 days from this daily series, no training please."*
- *"I have hourly_power.csv with a 'load_kw' column, about 20k hourly readings from a campus substation. I'm on a laptop with 8 GB RAM and no GPU. Can you predict the next 48 hours with an uncertainty band? I hit a 'Model is not compiled' RuntimeError last time I tried a pretrained forecaster."*
- *"We log blood glucose from 300 patients every 5 minutes in a wide CSV, one column per patient. I don't have time to fit a model per patient, but I need a 2-hour-ahead forecast for each of them, plus a way to flag readings that look abnormally off from what was expected."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill timesfm-forecasting

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills timesfm-forecasting
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [`aeon`](/skills/aeon)
- [`statsmodels`](/skills/statsmodels)
- [`exploratory-data-analysis`](/skills/exploratory-data-analysis)
- [`scientific-visualization`](/skills/scientific-visualization)
- [`scikit-learn`](/skills/scikit-learn)
- [`segment-anything-model`](/skills/segment-anything-model)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/timesfm-forecasting/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
