---
title: "statistical-power — AI agent skill for ideation and design"
description: "Sample-size and statistical power calculations for planning studies."
keywords: ["power analysis", "sample size", "study design", "statistics"]
---

# `statistical-power`

**Category:** [ideation-and-design](/skills#ideation-and-design) · **License:** MIT · **Version:** 1.1 · **Includes scripts**

**Tags:** power analysis, sample size, study design, statistics

## When to use it

Sample-size and statistical power calculations for planning studies. Use whenever someone asks "how many subjects/samples/replicates do I need", wants an a priori power analysis, a minimum detectable effect (MDE), a power curve, or needs to justify a sample size for a grant, IRB protocol, or pre-registration. Covers closed-form power for t-tests, ANOVA, proportions, correlations, chi-square, and regression, plus simulation-based (Monte Carlo) power for designs with no formula — logistic/Poisson regression, mixed models, cluster-randomized trials, survival, and interactions. Use this skill even when the request only mentions an effect size, alpha, or "80% power" without saying "power analysis" explicitly. For laying out the study (randomization, blocking, factorial/DOE, crossover, sequential designs) use experimental-design; for analyzing data already collected and reporting it use statistical-analysis.

## Example requests

Ask your agent in plain language, for example:

- *"how many mice per group for d=0.8, 90% power?"*
- *"I'm writing an R01 aim where we randomize 24 clinics (about 30 patients each) to a new intake protocol vs usual care, and the outcome is 6-month remission (binary, baseline around 35%). Our ICC from a pilot is 0.05. I need a sample size justification paragraph for the grant. Can you work out how many clinics we need to see a 10 percentage point improvement and tell me if 24 is enough?"*
- *"We only have budget for 12 animals per arm in our two-arm tail-suspension study, with SD around 25 seconds immobility. Before I commit to this, what's the smallest difference between groups we could realistically pick up, and can you show how that changes if a couple of animals die?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill statistical-power

# Kalaris Labs installer with checksum verification
npx research-agent-skills install statistical-power
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ideation-and-design` category with `/plugin install ideation-and-design@research-agent-skills`.

## Related

- [`scientific-brainstorming`](/skills/scientific-brainstorming)
- [`statistical-analysis`](/skills/statistical-analysis)
- [`uncertainty-and-units`](/skills/uncertainty-and-units)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/statistical-power/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
