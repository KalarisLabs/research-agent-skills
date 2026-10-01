---
title: "ara-rigor-reviewer — AI agent skill for research automation"
description: "Performs ARA Seal Level 2 semantic epistemic review of an Agent-Native Research Artifact directory, reading PAPER.md, logic/claims.md, logic/experiments.m…"
---

# `ara-rigor-reviewer`

> Performs ARA Seal Level 2 semantic epistemic review of an Agent-Native Research Artifact directory, reading PAPER.md, logic/claims.md, logic/experiments.md, and trace/exploration_tree.yaml. Scores six dimensions (evidence relevance, falsifiability, scope calibration, argument coherence, exploration integrity, methodological rigor) from 1 to 5 and writes a severity-ranked level2_report.json with a Strong Accept to Reject grade. Use when Level 1 structural validation has passed and an ARA needs a critique before release. Use when checking whether claims are supported by their cited experiments. Use when auditing falsification criteria or scope over-claiming. Use when judging whether an exploration tree documents real dead ends. Not for structural or reference validation, which is Level 1.

**Category:** [research-automation](/skills#research-automation) · **License:** MIT · **Version:** 3.0.0

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill ara-rigor-reviewer
```

## When to use it

Performs ARA Seal Level 2 semantic epistemic review of an Agent-Native Research Artifact directory, reading PAPER.md, logic/claims.md, logic/experiments.md, and trace/exploration_tree.yaml. Scores six dimensions (evidence relevance, falsifiability, scope calibration, argument coherence, exploration integrity, methodological rigor) from 1 to 5 and writes a severity-ranked level2_report.json with a Strong Accept to Reject grade. Use when Level 1 structural validation has passed and an ARA needs a critique before release. Use when checking whether claims are supported by their cited experiments. Use when auditing falsification criteria or scope over-claiming. Use when judging whether an exploration tree documents real dead ends. Not for structural or reference validation, which is Level 1.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/ara-rigor-reviewer/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
