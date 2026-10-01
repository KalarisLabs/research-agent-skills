---
title: "statistical-power — AI agent skill for ideation and design"
description: "Sample-size and statistical power calculations for planning studies."
---

# `statistical-power`

> Sample-size and statistical power calculations for planning studies. Use whenever someone asks "how many subjects/samples/replicates do I need", wants an a priori power analysis, a minimum detectable effect (MDE), a power curve, or needs to justify a sample size for a grant, IRB protocol, or pre-registration. Covers closed-form power for t-tests, ANOVA, proportions, correlations, chi-square, and regression, plus simulation-based (Monte Carlo) power for designs with no formula — logistic/Poisson regression, mixed models, cluster-randomized trials, survival, and interactions. Use this skill even when the request only mentions an effect size, alpha, or "80% power" without saying "power analysis" explicitly. For laying out the study (randomization, blocking, factorial/DOE, crossover, sequential designs) use experimental-design; for analyzing data already collected and reporting it use statistical-analysis.

**Category:** [ideation-and-design](/skills#ideation-and-design) · **License:** MIT · **Version:** 1.1

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill statistical-power
```

## When to use it

Sample-size and statistical power calculations for planning studies. Use whenever someone asks "how many subjects/samples/replicates do I need", wants an a priori power analysis, a minimum detectable effect (MDE), a power curve, or needs to justify a sample size for a grant, IRB protocol, or pre-registration. Covers closed-form power for t-tests, ANOVA, proportions, correlations, chi-square, and regression, plus simulation-based (Monte Carlo) power for designs with no formula — logistic/Poisson regression, mixed models, cluster-randomized trials, survival, and interactions. Use this skill even when the request only mentions an effect size, alpha, or "80% power" without saying "power analysis" explicitly. For laying out the study (randomization, blocking, factorial/DOE, crossover, sequential designs) use experimental-design; for analyzing data already collected and reporting it use statistical-analysis.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/statistical-power/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
