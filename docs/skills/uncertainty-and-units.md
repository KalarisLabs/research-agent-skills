---
title: "uncertainty-and-units — AI agent skill for ideation and design"
description: "Track physical units and propagate measurement uncertainty in scientific calculations using pint and uncertainties."
keywords: ["measurement uncertainty", "units", "GUM", "metrology", "physics"]
---

# `uncertainty-and-units`

**Category:** [ideation-and-design](/skills#ideation-and-design) · **License:** MIT · **Version:** 1.1 · **Includes scripts**

**Tags:** measurement uncertainty, units, GUM, metrology, physics

## When to use it

Track physical units and propagate measurement uncertainty in scientific calculations using pint and uncertainties. Use for unit conversion and dimensional checking, GUM uncertainty budgets, Type A and Type B evaluation, coverage factors and expanded uncertainty, Monte Carlo propagation, significant-figure and plus-minus reporting, error propagation through curve fits, CODATA constants, auditing Python code for stripped units or broken uncertainty propagation, and order-of-magnitude plausibility checks using dimensionless groups (Reynolds, Peclet, Damkohler, Knudsen, Biot, Womersley), characteristic scales such as diffusion time or Debye length, and observed magnitude ranges. Trigger on "is this number physically reasonable", "sanity check these units", "what regime is this flow in", or a result that looks off by orders of magnitude.

## Example requests

Ask your agent in plain language, for example:

- *"my pipe flow Re comes out as 4e7 in a 200 micron capillary, is that even physically reasonable?"*
- *"I'm fitting calibration.csv (voltage vs. temperature, with per-point standard uncertainties from the DMM certificate) using scipy curve_fit in fit_cal.py, then computing the temperature at 3.2 V from the slope and intercept. The reported error bar seems too small and doesn't change when I change sigma. How should I get the correct uncertainty on the predicted value?"*
- *"I weighed a sample on a balance with a calibration certificate saying U = 0.2 mg at k = 2, plus the balance resolution is 0.1 mg, and I have 8 repeat readings. How do I combine these and report the final mass so reviewers know what the ± means?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill uncertainty-and-units

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills uncertainty-and-units
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ideation-and-design` category with `/plugin install ideation-and-design@research-agent-skills`.

## Related

- [`astropy`](/skills/astropy)
- [`experimental-design`](/skills/experimental-design)
- [`statistical-analysis`](/skills/statistical-analysis)
- [`statistical-power`](/skills/statistical-power)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/uncertainty-and-units/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
