---
title: "get-available-resources — AI agent skill for data science and ml"
description: "Detect host inventory and effective CPU, memory, disk, scheduler, container, and accelerator limits when a user asks for resource-aware planning or before…"
---

# `get-available-resources`

> Detect host inventory and effective CPU, memory, disk, scheduler, container, and accelerator limits when a user asks for resource-aware planning or before a clearly resource-sensitive local workload. Produces a redacted JSON snapshot and conservative planning helpers without stress tests or assuming visible host hardware is usable.

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** MIT · **Version:** 1.3

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill get-available-resources
```

## When to use it

Detect host inventory and effective CPU, memory, disk, scheduler, container, and accelerator limits when a user asks for resource-aware planning or before a clearly resource-sensitive local workload. Produces a redacted JSON snapshot and conservative planning helpers without stress tests or assuming visible host hardware is usable.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/get-available-resources/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
