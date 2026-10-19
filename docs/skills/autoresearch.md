---
title: "autoresearch — AI agent skill for research automation"
description: "Orchestrates end-to-end autonomous AI research projects using a two-loop architecture."
keywords: ["Autonomous Research", "Two-Loop Architecture", "Experiment Orchestration", "Research Synthesis", "Project Management"]
---

# `autoresearch`

**Category:** [research-automation](/skills#research-automation) · **License:** MIT · **Version:** 1.0.0

**Tags:** Autonomous Research, Two-Loop Architecture, Experiment Orchestration, Research Synthesis, Project Management

## When to use it

Orchestrates end-to-end autonomous AI research projects using a two-loop architecture. The inner loop runs rapid experiment iterations with clear optimization targets. The outer loop synthesizes results, identifies patterns, and steers research direction. Routes to domain-specific skills for execution, supports continuous agent operation via Claude Code /loop and OpenClaw heartbeat, and produces research presentations and papers. Use when starting a research project, running autonomous experiments, or managing a multi-hypothesis research effort.

## Example requests

Ask your agent in plain language, for example:

- *"I want to spin up an autonomous research project on whether sparse attention hurts long-context retrieval. Set it up and just start running."*
- *"I have a research-state.yaml and findings.md in ~/proj/grokking-wd from last week. Weight decay sweeps on modular addition (H1 supported, H2 inconclusive) and about 12 runs logged in data/trajectory_H1_runs001-012.csv. Pick up where we left off."*
- *"I'm going to be offline for a few days. Can you keep investigating why my small transformer's loss spikes early in training, running experiments on your own, testing ideas, and then writing up what you find with a summary deck I can look at when I'm back?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill autoresearch

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills autoresearch
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `research-automation` category with `/plugin install research-automation@research-agent-skills`.

## Related

- [`autogpt-agents`](/skills/autogpt-agents)
- [`brainstorming-research-ideas`](/skills/brainstorming-research-ideas)
- [`creative-thinking-for-research`](/skills/creative-thinking-for-research)
- [`research-skill-creator`](/skills/research-skill-creator)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/autoresearch/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
