---
title: "relsa-severity-assessment — AI agent skill for ideation and design"
description: "Multivariate severity assessment and humane endpoint prediction for laboratory animal studies using the RELSA (RELative Severity Assessment) score and…"
keywords: ["animal welfare", "laboratory animals", "humane endpoints", "severity assessment"]
---

# `relsa-severity-assessment`

**Category:** [ideation-and-design](/skills#ideation-and-design) · **License:** MIT · **Version:** 1.1 · **Includes scripts**

**Tags:** animal welfare, laboratory animals, humane endpoints, severity assessment

## When to use it

Multivariate severity assessment and humane endpoint prediction for laboratory animal studies using the RELSA (RELative Severity Assessment) score and ARIMA-based foRcast forecasting. Use when combining welfare readouts — body weight or weight loss, body temperature, clinical or nesting scores, biomarkers, activity, heart rate, burrowing, wheel running — into one severity score per animal per day, when asking which animals are at risk of reaching a humane endpoint or when one will be reached, when defining attention/danger zones or thresholds on a severity scale by kernel density estimation, or when reporting severity for a 3Rs, refinement, animal-welfare, or EU Directive 2010/63/EU severity-assessment context. Covers directionality ("turned" variables), baseline normalization, reference sets, RELSA weights, ARIMA prediction intervals, and RMSE/PICP/MPIW evaluation.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get one severity number per mouse per day from weight, temp and a clinical score?"*
- *"I have telemetry from a mouse endotoxaemia study in telemetry_hourly.csv (columns id, treatment, hour, temp, hr, activity, weight). Hourly values are in there. I want to score each animal and see which ones are about to hit endpoint. Temperature drops in this model. Where do I start?"*
- *"We're writing up a refinement analysis for our ethics committee and want to find data-driven cut-offs that separate the sick animals from the ones that recovered on a combined welfare scale. How should we define and report them?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill relsa-severity-assessment

# Kalaris Labs installer with checksum verification
npx research-agent-skills install relsa-severity-assessment
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ideation-and-design` category with `/plugin install ideation-and-design@research-agent-skills`.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/relsa-severity-assessment/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
