---
title: "ml-paper-writing — AI agent skill for research writing"
description: "Write publication-ready ML/AI papers for NeurIPS, ICML, ICLR, ACL, AAAI, COLM."
keywords: ["Academic Writing", "NeurIPS", "ICML", "ICLR", "ACL", "AAAI", "COLM", "LaTeX", "Paper Writing", "Citations", "Research"]
---

# `ml-paper-writing`

**Category:** [research-writing](/skills#research-writing) · **License:** MIT · **Version:** 1.2.0

**Tags:** Academic Writing, NeurIPS, ICML, ICLR, ACL, AAAI, COLM, LaTeX, Paper Writing, Citations, Research

## When to use it

Write publication-ready ML/AI papers for NeurIPS, ICML, ICLR, ACL, AAAI, COLM. Use when drafting papers from research repos, structuring arguments, verifying citations, or preparing camera-ready submissions. For systems venues (OSDI, NSDI, ASPLOS, SOSP), use systems-paper-writing instead.

## Example requests

Ask your agent in plain language, for example:

- *"Help me write up my paper for ICLR. I've got the code and results in a folder."*
- *"I have ~/proj/sae-steering with results/ablation_table.csv, wandb exports, and a README. We steer Llama-3-8B with sparse autoencoder features and it beats prompting on 4 benchmarks. Can you draft the abstract and intro for NeurIPS 2025? I need to stay inside 9 pages and fill in the checklist later."*
- *"My related work section has about 30 references that I pulled together with ChatGPT, and I'm worried some are fake. Can you check them and tidy up the section before I submit to ACL?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill ml-paper-writing

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills ml-paper-writing
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `research-writing` category with `/plugin install research-writing@research-agent-skills`.

## Related

- [`abstract-and-title`](/skills/abstract-and-title)
- [`academic-plotting`](/skills/academic-plotting)
- [`acm-sigconf`](/skills/acm-sigconf)
- [`arxiv-submission`](/skills/arxiv-submission)
- [`rebuttal-and-response-to-reviewers`](/skills/rebuttal-and-response-to-reviewers)
- [`reproducibility-statement`](/skills/reproducibility-statement)
- [`systems-paper-writing`](/skills/systems-paper-writing)
- [`unslop-academic-writing`](/skills/unslop-academic-writing)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/ml-paper-writing/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
