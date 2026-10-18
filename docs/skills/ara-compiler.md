---
title: "ara-compiler — AI agent skill for research automation"
description: "Compiles any research input — PDF papers, GitHub repositories, experiment logs, code directories, or raw notes — into a complete Agent-Native Research…"
keywords: ["ARA", "Research Artifacts", "Knowledge Extraction", "Paper Ingestion", "Exploration Graph", "Provenance", "Research Tooling", "Epistemic Compilation"]
---

# `ara-compiler`

**Category:** [research-automation](/skills#research-automation) · **License:** MIT · **Version:** 1.0.0

**Tags:** ARA, Research Artifacts, Knowledge Extraction, Paper Ingestion, Exploration Graph, Provenance, Research Tooling, Epistemic Compilation

## When to use it

Compiles any research input — PDF papers, GitHub repositories, experiment logs, code directories, or raw notes — into a complete Agent-Native Research Artifact (ARA) with cognitive layer (claims, concepts, heuristics), physical layer (configs, code stubs), exploration graph, and grounded evidence. Use when ingesting a paper or codebase into a structured, machine-executable knowledge package, building an ARA from scratch, or converting research outputs into a falsifiable, agent-traversable form.

## Example requests

Ask your agent in plain language, for example:

- *"Turn this paper into an ARA: ~/papers/lora_scaling.pdf"*
- *"I've got the repo at ./diffusion-protein-design (README, train.py, configs/sweep_v3.yaml) plus a folder of wandb logs from our runs and a Slack export where we argued about why we dropped the contact-map loss. Compile all of it into a structured, agent-traversable knowledge package in ./ara/protein, and make the dead ends explicit."*
- *"My advisor wants our single-cell atlas project written up in a machine-readable form that an AI agent could follow and check, with every claim falsifiable and tied to evidence. I only have messy notes in notes.md and a few result CSVs. How do I get there?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill ara-compiler

# Kalaris Labs installer with checksum verification
npx research-agent-skills install ara-compiler
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `research-automation` category with `/plugin install research-automation@research-agent-skills`.

## Related

- [`ara-research-manager`](/skills/ara-research-manager)
- [`ara-rigor-reviewer`](/skills/ara-rigor-reviewer)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/ara-compiler/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
