---
title: "flowio — AI agent skill for life sciences"
description: "Read, inspect, and write Flow Cytometry Standard (FCS) 2.0, 3.0, and 3.1 files with FlowIO."
keywords: ["flow cytometry", "FCS files", "cytometry", "immunology", "bioinformatics"]
---

# `flowio`

**Category:** [life-sciences](/skills#life-sciences) · **License:** BSD-3-Clause license · **Version:** 2.1 · **Includes scripts**

**Tags:** flow cytometry, FCS files, cytometry, immunology, bioinformatics

## When to use it

Read, inspect, and write Flow Cytometry Standard (FCS) 2.0, 3.0, and 3.1 files with FlowIO. Use for low-level FCS metadata and channel inspection, NumPy event extraction, multi-dataset files, table export, and FCS 3.1 creation; use FlowKit for compensation, cytometry transforms, gating, or FlowJo workspaces.

## Example requests

Ask your agent in plain language, for example:

- *"How do I pull the events out of an .fcs file into a numpy array?"*
- *"I have a legacy file 'plate3_legacy.fcs' that I think has several datasets stacked in it, and when I try flowio.FlowData('plate3_legacy.fcs') I only get the first one. Also my script does flow.text['$DATE'] and raises KeyError. Can you fix this and list the channel PnN/PnS names for each dataset?"*
- *"I exported a bunch of per-cell measurements from my own analysis as a NumPy matrix (50,000 cells x 8 markers) and need to hand them to a collaborator as a standard flow cytometry file their software can open. What's the right way to do it?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill flowio

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills flowio
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/flowio/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
