---
title: "usfiscaldata — AI agent skill for scientific databases"
description: "Query the U.S. Treasury Fiscal Data REST API for federal financial data. No API key required."
keywords: ["US Treasury", "fiscal data", "economics", "public finance", "open data"]
---

# `usfiscaldata`

**Category:** [scientific-databases](/skills#scientific-databases) · **License:** MIT · **Version:** 1.3

**Tags:** US Treasury, fiscal data, economics, public finance, open data

## When to use it

Query the U.S. Treasury Fiscal Data REST API for federal financial data. No API key required. Use for national debt (Debt to the Penny), Daily Treasury Statements, Monthly Treasury Statements, Treasury securities auctions, interest rates, foreign exchange rates, savings bonds, or U.S. government revenue and spending statistics.

## Example requests

Ask your agent in plain language, for example:

- *"what's the current total public debt outstanding?"*
- *"I'm writing a paper on federal interest costs. Can you pull monthly interest expense on the public debt from fiscal year 2015 through 2024 into a pandas DataFrame and save it as interest_expense.csv? I want record_date, the expense category, and the amount. Watch out for pagination, I think there are more than 100 rows."*
- *"I need to know how much demand there was at recent 10-year Treasury note auctions, like bid-to-cover ratios over the past two years, and also which auctions are coming up next. No idea where to get this for free without signing up."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill usfiscaldata

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills usfiscaldata
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `scientific-databases` category with `/plugin install scientific-databases@research-agent-skills`.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/usfiscaldata/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
