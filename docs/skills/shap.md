---
title: "shap — AI agent skill for data science and ml"
description: "Explain and audit machine-learning predictions with SHAP."
keywords: ["explainable AI", "SHAP", "feature attribution", "model interpretability", "machine learning"]
---

# `shap`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** MIT · **Version:** 2.1 · **Includes scripts**

**Tags:** explainable AI, SHAP, feature attribution, model interpretability, machine learning

## When to use it

Explain and audit machine-learning predictions with SHAP. Use for selecting SHAP explainers and maskers, computing and validating feature attributions, handling multi-output explanations, and producing local or global SHAP visualizations.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get SHAP values for my XGBoost classifier and make a beeswarm plot?"*
- *"I'm working on a LightGBM model predicting 30-day readmission from train.parquet (about 40 features, many correlated like creatinine and eGFR). I ran shap.TreeExplainer(model).shap_values(X_test) and got a list of two arrays, then plotting with values[1] fails with a shape error on the newer shap version. Also I get an additivity check error when I switch to model_output='probability'. How do I fix this?"*
- *"I trained a gradient boosted model on patient lab data and a reviewer asked us to show why the model flagged certain patients as high risk and which inputs drive predictions overall. How should I go about producing that for the paper, including making sure the explanations are trustworthy?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill shap

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills shap
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/shap/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
