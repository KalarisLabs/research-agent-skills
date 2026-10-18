---
title: "polars — AI agent skill for data science and ml"
description: "High-performance DataFrame library for Python ETL, analytics, and pandas migration."
keywords: ["DataFrames", "data engineering", "ETL", "data analysis", "Python"]
---

# `polars`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** https://github.com/pola-rs/polars/blob/main/LICENSE · **Version:** 1.2

**Tags:** DataFrames, data engineering, ETL, data analysis, Python

## When to use it

High-performance DataFrame library for Python ETL, analytics, and pandas migration. Use for expression-based data manipulation with lazy query optimization, parallel execution, streaming out-of-core processing, Arrow interoperability, and optional GPU execution.

## Example requests

Ask your agent in plain language, for example:

- *"my pandas groupby is painfully slow, how do I convert it to polars?"*
- *"I have 40 GB of Parquet files in data/trips/*.parquet (columns: trip_id, vendor, pickup_ts, fare, distance_km). I need average fare per km by vendor and by hour of day, and the script keeps getting killed with a MemoryError when I use pd.read_parquet. Can you rewrite it?"*
- *"I've got sensor logs from several lab instruments in separate CSVs. I want to join them on timestamp, compute a rolling 5-minute mean per instrument without a Python loop, and write one compact columnar file I can reload quickly later. What's a fast, clean way to do this?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill polars

# Kalaris Labs installer with checksum verification
npx research-agent-skills install polars
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [`ray-data`](/skills/ray-data)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/polars/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
