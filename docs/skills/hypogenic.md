---
title: "hypogenic — AI agent skill for ideation and design"
description: "Plans and audits use of ChicagoHAI HypoGeniC/HypoRefine for LLM-assisted hypothesis generation from labeled text datasets."
keywords: ["hypothesis generation", "LLM", "text datasets", "research automation"]
---

# `hypogenic`

**Category:** [ideation-and-design](/skills#ideation-and-design) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** hypothesis generation, LLM, text datasets, research automation

## When to use it

Plans and audits use of ChicagoHAI HypoGeniC/HypoRefine for LLM-assisted hypothesis generation from labeled text datasets. Use for the `hypogenic` package, its task configs, hypothesis banks, or HypoBench datasets—not for manual hypothesis formulation or scientific validation.

## Example requests

Ask your agent in plain language, for example:

- *"I want to try hypogenic on my review-classification data. Where do I start?"*
- *"I've got a hypogenic task config at configs/deceptive_reviews.yaml and the HypoBench deceptive-review train/val/test JSONs. Before I spend anything on OpenAI, can you check the splits for leakage and estimate the worst-case cost for 20 iterations with gpt-4o-mini?"*
- *"I have a few thousand labeled tweets about whether people are sarcastic. I'd like an LLM to automatically propose textual patterns that predict the label, keep the ones that score well on held-out data, and then give me the ranked list as JSON. Is there an existing open-source tool for that, and how do I run it reproducibly?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill hypogenic

# Kalaris Labs installer with checksum verification
npx research-agent-skills install hypogenic
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ideation-and-design` category with `/plugin install ideation-and-design@research-agent-skills`.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/hypogenic/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
