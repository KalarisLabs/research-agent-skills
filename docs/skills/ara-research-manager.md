---
title: "ara-research-manager — AI agent skill for research automation"
description: "Records research provenance at the end of a coding or research session by scanning the conversation and writing decisions, experiments, dead ends, pivots,…"
---

# `ara-research-manager`

> Records research provenance at the end of a coding or research session by scanning the conversation and writing decisions, experiments, dead ends, pivots, claims, and heuristics into the ara/ directory (exploration_tree.yaml, claims.md, heuristics.md, observations.yaml, session records), each tagged user, ai-suggested, ai-executed, or user-revised. Use when a task is finished and you want a session epilogue. Use when you need an auditable trace of how a project evolved. Use when decisions and dead ends need logging with provenance. Use when initializing an ara/ directory. Do not use during task execution, since it must run only after the request is complete.

**Category:** [research-automation](/skills#research-automation) · **License:** MIT · **Version:** 1.0.0

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill ara-research-manager
```

## When to use it

Records research provenance at the end of a coding or research session by scanning the conversation and writing decisions, experiments, dead ends, pivots, claims, and heuristics into the ara/ directory (exploration_tree.yaml, claims.md, heuristics.md, observations.yaml, session records), each tagged user, ai-suggested, ai-executed, or user-revised. Use when a task is finished and you want a session epilogue. Use when you need an auditable trace of how a project evolved. Use when decisions and dead ends need logging with provenance. Use when initializing an ara/ directory. Do not use during task execution, since it must run only after the request is complete.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/ara-research-manager/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
