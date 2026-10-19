---
title: "market-research-reports — AI agent skill for research writing"
description: "Build evidence-traceable market research reports and assumption-driven market sizing or forecast scenarios."
keywords: ["market research", "market sizing", "TAM SAM SOM", "competitive analysis", "reports"]
---

# `market-research-reports`

**Category:** [research-writing](/skills#research-writing) · **License:** MIT · **Version:** 1.3 · **Includes scripts**

**Tags:** market research, market sizing, TAM SAM SOM, competitive analysis, reports

## When to use it

Build evidence-traceable market research reports and assumption-driven market sizing or forecast scenarios. Use for market definition, industry and customer evidence, competitive landscapes, TAM/SAM/SOM reconciliation, forecast sensitivity, and auditable report scaffolds.

## Example requests

Ask your agent in plain language, for example:

- *"Can you help me size the market for industrial IoT sensors in Germany?"*
- *"I've got source_ledger.csv with 14 sources and a claims.csv for my draft report on the European heat pump market. Some of the numbers come from Statista, which just repackages Eurostat data. Can you check that every claim maps to valid source IDs and tell me whether my corroboration is real?"*
- *"My startup is selling to dental clinics in Canada and I need to show a board how big the opportunity might be over the next 5 years, with a pessimistic and optimistic view, and which assumptions matter most. I'd rather not just quote some analyst number."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill market-research-reports

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills market-research-reports
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `research-writing` category with `/plugin install research-writing@research-agent-skills`.

## Related

- [`citation-verification`](/skills/citation-verification)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/market-research-reports/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
