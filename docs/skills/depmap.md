---
title: "depmap — AI agent skill for scientific databases"
description: "Query the Cancer Dependency Map (DepMap) for cancer cell line gene dependency scores (CRISPR Chronos), drug sensitivity data, and gene effect profiles."
keywords: ["cancer research", "gene dependency", "CRISPR screens", "drug sensitivity", "oncology"]
---

# `depmap`

**Category:** [scientific-databases](/skills#scientific-databases) · **License:** CC-BY-4.0 · **Version:** 1.0

**Tags:** cancer research, gene dependency, CRISPR screens, drug sensitivity, oncology

## When to use it

Query the Cancer Dependency Map (DepMap) for cancer cell line gene dependency scores (CRISPR Chronos), drug sensitivity data, and gene effect profiles. Use for identifying cancer-specific vulnerabilities, synthetic lethal interactions, and validating oncology drug targets.

## Example requests

Ask your agent in plain language, for example:

- *"Is KRAS a selective dependency in pancreatic lines? Need it from DepMap."*
- *"I downloaded CRISPRGeneEffect.csv and OmicsSomaticMutationsMatrixDamaging.csv from the 24Q4 release. I want to find genes that are more essential in TP53-mutant lines than in wild-type lines, and I get a KeyError on 'ACH-000012' when I join with sample_info.csv. Can you write the analysis and fix the join?"*
- *"We have a candidate oncology target and want to know whether knocking it out kills only certain tumour cell lines, or whether it would hit essentially every cell and cause toxicity. We also want to know which genomic features predict response. What public data can we use and how should we analyse it?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill depmap

# Kalaris Labs installer with checksum verification
npx research-agent-skills install depmap
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `scientific-databases` category with `/plugin install scientific-databases@research-agent-skills`.

## Related

- [`imaging-data-commons`](/skills/imaging-data-commons)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/depmap/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
