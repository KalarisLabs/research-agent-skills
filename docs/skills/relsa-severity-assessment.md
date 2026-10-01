---
title: "relsa-severity-assessment — AI agent skill for ideation and design"
description: "Multivariate severity assessment and humane endpoint prediction for laboratory animal studies using the RELSA (RELative Severity Assessment) score and ARI…"
---

# `relsa-severity-assessment`

> Multivariate severity assessment and humane endpoint prediction for laboratory animal studies using the RELSA (RELative Severity Assessment) score and ARIMA-based foRcast forecasting. Use when combining welfare readouts — body weight or weight loss, body temperature, clinical or nesting scores, biomarkers, activity, heart rate, burrowing, wheel running — into one severity score per animal per day, when asking which animals are at risk of reaching a humane endpoint or when one will be reached, when defining attention/danger zones or thresholds on a severity scale by kernel density estimation, or when reporting severity for a 3Rs, refinement, animal-welfare, or EU Directive 2010/63/EU severity-assessment context. Covers directionality ("turned" variables), baseline normalization, reference sets, RELSA weights, ARIMA prediction intervals, and RMSE/PICP/MPIW evaluation.

**Category:** [ideation-and-design](/skills#ideation-and-design) · **License:** MIT · **Version:** 1.1

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill relsa-severity-assessment
```

## When to use it

Multivariate severity assessment and humane endpoint prediction for laboratory animal studies using the RELSA (RELative Severity Assessment) score and ARIMA-based foRcast forecasting. Use when combining welfare readouts — body weight or weight loss, body temperature, clinical or nesting scores, biomarkers, activity, heart rate, burrowing, wheel running — into one severity score per animal per day, when asking which animals are at risk of reaching a humane endpoint or when one will be reached, when defining attention/danger zones or thresholds on a severity scale by kernel density estimation, or when reporting severity for a 3Rs, refinement, animal-welfare, or EU Directive 2010/63/EU severity-assessment context. Covers directionality ("turned" variables), baseline normalization, reference sets, RELSA weights, ARIMA prediction intervals, and RMSE/PICP/MPIW evaluation.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/relsa-severity-assessment/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
