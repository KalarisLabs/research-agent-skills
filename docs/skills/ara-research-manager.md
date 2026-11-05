---
title: "ara-research-manager — AI agent skill for research automation"
description: "Records research provenance at the end of a coding or research session by scanning the conversation and writing decisions, experiments, dead ends, pivots…"
keywords: ["ARA", "Research Recording", "Provenance", "Session Logging", "Knowledge Management", "Exploration Tree", "Research Tooling"]
---

# `ara-research-manager`

**Category:** [research-automation](/skills#research-automation) · **License:** MIT · **Version:** 1.0.0

**Tags:** ARA, Research Recording, Provenance, Session Logging, Knowledge Management, Exploration Tree, Research Tooling

## When to use it

Records research provenance at the end of a coding or research session by scanning the conversation and writing decisions, experiments, dead ends, pivots, claims, and heuristics into the ara/ directory (exploration_tree.yaml, claims.md, heuristics.md, observations.yaml, session records), each tagged user, ai-suggested, ai-executed, or user-revised. Use when a task is finished and you want a session epilogue. Use when you need an auditable trace of how a project evolved. Use when decisions and dead ends need logging with provenance. Use when initializing an ara/ directory. Do not use during task execution, since it must run only after the request is complete.

## Example requests

Ask your agent in plain language, for example:

- *"ok we're done for today, log the session"*
- *"That finishes the ablation on my CIFAR-10 ResNet-18 run. We tried cosine vs step LR (cosine hit 94.1% vs 92.7%), dropped mixup after it hurt accuracy, and I decided to keep label smoothing 0.1. Now that everything's finished, can you record all of this in ara/trace/exploration_tree.yaml and ara/logic/claims.md so there's a record of who decided what, and add a session file?"*
- *"My project just wrapped up its first phase and I need a durable, auditable trail of how our direction changed over the past few weeks of chats, including which ideas were mine and which came from the assistant. There's no folder for this yet. Can you set that up and fill it in?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill ara-research-manager

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills ara-research-manager
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `research-automation` category with `/plugin install research-automation@research-agent-skills`.

## Related

- [`ara-compiler`](/skills/ara-compiler)
- [`ara-rigor-reviewer`](/skills/ara-rigor-reviewer)
- [`treatment-plans`](/skills/treatment-plans)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/ara-research-manager/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
