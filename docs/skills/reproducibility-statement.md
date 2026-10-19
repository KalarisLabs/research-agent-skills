---
title: "reproducibility-statement — AI agent skill for research writing"
description: "Prepare the reproducibility, transparency and open-science parts of a paper, including data and code availability statements, reproducibility checklists…"
keywords: ["reproducibility", "data availability", "code availability", "open science", "FAIR", "checklist", "CRediT", "Zenodo", "ethics statement"]
---

# `reproducibility-statement`

**Category:** [research-writing](/skills#research-writing) · **License:** MIT · **Version:** 1.0

**Tags:** reproducibility, data availability, code availability, open science, FAIR, checklist, CRediT, Zenodo, ethics statement

## When to use it

Prepare the reproducibility, transparency and open-science parts of a paper, including data and code availability statements, reproducibility checklists (NeurIPS, ICML, ICLR, ACL Responsible NLP, Nature reporting summaries), research artifact packaging (Zenodo DOI, CITATION.cff, environment lockfiles, seeds), ethics/broader-impact statements, CRediT author contributions, competing interests and AI-use disclosures. Use when a venue requires any of these statements or checklists, or when preparing code/data for release alongside a paper.

## Example requests

Ask your agent in plain language, for example:

- *"Fill in the NeurIPS checklist and write our data and code availability statements."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill reproducibility-statement

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills reproducibility-statement
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `research-writing` category with `/plugin install research-writing@research-agent-skills`.

## Related

- [`arxiv-submission`](/skills/arxiv-submission)
- [`cell-press`](/skills/cell-press)
- [`cover-letter-to-editor`](/skills/cover-letter-to-editor)
- [`elsevier-cas`](/skills/elsevier-cas)
- [`ml-paper-writing`](/skills/ml-paper-writing)
- [`nature-portfolio`](/skills/nature-portfolio)
- [`peer-review`](/skills/peer-review)
- [`plos`](/skills/plos)
- [Write a research paper with AI](/guides/write-a-research-paper)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/reproducibility-statement/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
