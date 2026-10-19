---
title: "exploratory-data-analysis — AI agent skill for data science and ml"
description: "Perform bounded, local exploratory analysis of explicitly supported scientific files."
keywords: ["exploratory data analysis", "data profiling", "data quality", "scientific data"]
---

# `exploratory-data-analysis`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** exploratory data analysis, data profiling, data quality, scientific data

## When to use it

Perform bounded, local exploratory analysis of explicitly supported scientific files. Use for redacted CSV/TSV/JSON profiles; optional NumPy, HDF5, FASTA/FASTQ, and basic image metadata inspection; missingness/leakage audits; outlier and transformation sensitivity; and rigorous EDA report scaffolds. Other domain formats are reference-only and unknown formats fail closed.

## Example requests

Ask your agent in plain language, for example:

- *"Can you do a quick EDA on assay_results.csv before I start modeling?"*
- *"I have plasma_cytokines_v3.tsv from a 3-site cohort study, with repeated visits per participant and columns subject_id, site, visit, IL6, TNFa, split. I'm worried the train/test split leaks and that missing IL6 values aren't random. Can you audit this before I fit a random forest? Some IL6 values are below the LOQ and coded as 0."*
- *"My measurements are heavily right-skewed and a few points look extreme. Before I decide whether to log-transform or drop them, I'd like to see how much those points drive the mean and spread in my exported table."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill exploratory-data-analysis

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills exploratory-data-analysis
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [`timesfm-forecasting`](/skills/timesfm-forecasting)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/exploratory-data-analysis/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
