---
title: "experimental-design — AI agent skill for ideation and design"
description: "Design experiments and studies BEFORE data is collected — choosing a design, randomizing, blocking, and laying out treatment combinations so results are…"
keywords: ["experimental design", "randomization", "blocking", "study design", "statistics"]
---

# `experimental-design`

**Category:** [ideation-and-design](/skills#ideation-and-design) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** experimental design, randomization, blocking, study design, statistics

## When to use it

Design experiments and studies BEFORE data is collected — choosing a design, randomizing, blocking, and laying out treatment combinations so results are interpretable. Use whenever someone is planning a study, asks how to assign subjects/samples to groups, mentions randomization, blocking, stratification, controls, factorial or fractional-factorial designs, design of experiments (DOE), screening many factors, response-surface optimization, crossover or repeated-measures or split-plot designs, cluster/group randomization, Latin squares, plate layouts, batch/run-order effects, replication vs. pseudoreplication, or sequential/adaptive/group-sequential designs. Trigger even for informal phrasings like "how should I set up this experiment", "how do I avoid confounding", "what's the best way to test these 6 factors", or "assign these mice to conditions". For computing the sample size or power once the design is chosen, use statistical-power; for analyzing data already collected, use statistical-analysis.

## Example requests

Ask your agent in plain language, for example:

- *"how do I assign 24 mice to 4 drug conditions without bias?"*
- *"I'm running a qPCR study on 48 liver samples (24 treated, 24 control) in 96-well plates, and the plate_layout.csv I drafted has all the controls in columns 1-2 and treated samples in the rest. Two technicians will split the work across two days. Can you help me redo the layout so I don't get plate or day artifacts?"*
- *"We have 7 process parameters for a fermentation (temperature, pH, feed rate, agitation, inoculum size, and so on) and each run costs about $2k, so we can afford maybe 16 runs. We want to find which ones matter and then tune the important ones to maximize titer. What's a sensible plan?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill experimental-design

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills experimental-design
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ideation-and-design` category with `/plugin install ideation-and-design@research-agent-skills`.

## Related

- [`scientific-brainstorming`](/skills/scientific-brainstorming)
- [`uncertainty-and-units`](/skills/uncertainty-and-units)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/experimental-design/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
