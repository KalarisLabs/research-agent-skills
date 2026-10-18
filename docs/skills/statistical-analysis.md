---
title: "statistical-analysis — AI agent skill for data science and ml"
description: "Guided statistical analysis for research data - test selection, assumption checking, effect sizes, power analysis, Bayesian alternatives, and APA-formatted…"
keywords: ["statistics", "hypothesis testing", "effect sizes", "power analysis", "APA reporting"]
---

# `statistical-analysis`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** statistics, hypothesis testing, effect sizes, power analysis, APA reporting

## When to use it

Guided statistical analysis for research data - test selection, assumption checking, effect sizes, power analysis, Bayesian alternatives, and APA-formatted reporting. Use whenever a user wants to compare groups, test a hypothesis, analyze experimental or survey data, check statistical assumptions, compute required sample sizes, or write up results - even if they never name a specific test. Covers t-tests, ANOVA, chi-square, correlation, regression, non-parametric and Bayesian methods. For low-level model APIs, see the statsmodels and pymc skills.

## Example requests

Ask your agent in plain language, for example:

- *"Do a t-test on my two groups?"*
- *"I have survey_responses.csv with a 'condition' column (control, mindfulness, exercise) and a 'stress_score' outcome from 187 undergrads. Scores look right-skewed and the exercise group has only 41 people vs 73 in the others. I'm submitting to a psych journal and need the analysis and the results paragraph."*
- *"We're testing whether a new tutoring program improves exam scores. Students were measured before and after the program, and I'm not sure whether I can just say it worked. How should I approach this and what should I report so reviewers are satisfied?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill statistical-analysis

# Kalaris Labs installer with checksum verification
npx research-agent-skills install statistical-analysis
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [`apa7`](/skills/apa7)
- [`arbor`](/skills/arbor)
- [`bgpt-paper-search`](/skills/bgpt-paper-search)
- [`bulk-rnaseq`](/skills/bulk-rnaseq)
- [`cell-press`](/skills/cell-press)
- [`nature-portfolio`](/skills/nature-portfolio)
- [`pathway-enrichment`](/skills/pathway-enrichment)
- [`plos`](/skills/plos)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/statistical-analysis/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
