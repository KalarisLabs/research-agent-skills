---
title: "ara-rigor-reviewer — AI agent skill for research automation"
description: "Performs ARA Seal Level 2 semantic epistemic review of an Agent-Native Research Artifact directory, reading PAPER.md, logic/claims.md, logic/experiments.md…"
keywords: ["ARA", "Epistemic Review", "Research Rigor", "Peer Review", "Scoring", "Audit", "Falsifiability", "Research Tooling"]
---

# `ara-rigor-reviewer`

**Category:** [research-automation](/skills#research-automation) · **License:** MIT · **Version:** 3.0.0

**Tags:** ARA, Epistemic Review, Research Rigor, Peer Review, Scoring, Audit, Falsifiability, Research Tooling

## When to use it

Performs ARA Seal Level 2 semantic epistemic review of an Agent-Native Research Artifact directory, reading PAPER.md, logic/claims.md, logic/experiments.md, and trace/exploration_tree.yaml. Scores six dimensions (evidence relevance, falsifiability, scope calibration, argument coherence, exploration integrity, methodological rigor) from 1 to 5 and writes a severity-ranked level2_report.json with a Strong Accept to Reject grade. Use when Level 1 structural validation has passed and an ARA needs a critique before release. Use when checking whether claims are supported by their cited experiments. Use when auditing falsification criteria or scope over-claiming. Use when judging whether an exploration tree documents real dead ends. Not for structural or reference validation, which is Level 1.

## Example requests

Ask your agent in plain language, for example:

- *"Can you give my ARA a rigor review before I publish it? It's in ./artifacts/lora-merge-ara"*
- *"Level 1 passed on ara_out/protein-fold-bench. Claim C03 says our retrieval reranker 'generalizes across all protein families' but it only cites E02, which is run on 4 CATH superfamilies. Also the falsification criterion for C03 just says 'if it doesn't work'. Can you critique whether these claims actually hold up and write up the findings?"*
- *"I've got this research artifact folder with claims, experiments and a log of what we tried. Structure checks are done. I want an honest second opinion on whether the dead ends in our log are real or just tidied up for show, and whether our argument hangs together."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill ara-rigor-reviewer

# Kalaris Labs installer with checksum verification
npx research-agent-skills install ara-rigor-reviewer
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `research-automation` category with `/plugin install research-automation@research-agent-skills`.

## Related

- [`ara-compiler`](/skills/ara-compiler)
- [`ara-research-manager`](/skills/ara-research-manager)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/ara-rigor-reviewer/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
