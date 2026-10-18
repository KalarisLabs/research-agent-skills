---
title: "constitutional-ai — AI agent skill for ml evaluation and safety"
description: "Anthropic's method for training harmless AI through self-improvement."
keywords: ["Safety Alignment", "Constitutional AI", "RLAIF", "Self-Critique", "Harmlessness", "Anthropic", "AI Safety", "RL From AI Feedback", "Claude"]
---

# `constitutional-ai`

**Category:** [ml-evaluation-and-safety](/skills#ml-evaluation-and-safety) · **License:** MIT · **Version:** 1.0.0

**Tags:** Safety Alignment, Constitutional AI, RLAIF, Self-Critique, Harmlessness, Anthropic, AI Safety, RL From AI Feedback, Claude

## When to use it

Anthropic's method for training harmless AI through self-improvement. Two-phase approach - supervised learning with self-critique/revision, then RLAIF (RL from AI Feedback). Use for safety alignment, reducing harmful outputs without human labels. Powers Claude's safety system.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get a model to critique and revise its own harmful answers?"*
- *"I'm training a 7B Llama model with TRL and want to cut harmful outputs without paying for human red-team labels. I've got a 16-principle constitution in constitution.yaml and red-team prompts in redteam.jsonl. Set up the pipeline, including the preference stage, and tell me what GPUs I need. My AI-generated preference labels look noisy between runs."*
- *"We want our assistant to follow a written set of ethical principles, and to stop giving evasive non-answers to borderline questions, with an AI model rather than crowd workers providing the training signal. What approach should we use and how do we tune it?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill constitutional-ai

# Kalaris Labs installer with checksum verification
npx research-agent-skills install constitutional-ai
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-evaluation-and-safety` category with `/plugin install ml-evaluation-and-safety@research-agent-skills`.

## Related

- [`fine-tuning-with-trl`](/skills/fine-tuning-with-trl)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/constitutional-ai/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
