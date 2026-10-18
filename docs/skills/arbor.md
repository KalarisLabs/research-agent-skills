---
title: "arbor — AI agent skill for research automation"
description: "Autonomously improve a real artifact (code, training recipe, agent harness, data pipeline, prompt) against an objective and an evaluator, using Hypothesis…"
keywords: ["autonomous optimization", "hypothesis tree", "research automation", "AI agents", "experiments"]
---

# `arbor`

**Category:** [research-automation](/skills#research-automation) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** autonomous optimization, hypothesis tree, research automation, AI agents, experiments

## When to use it

Autonomously improve a real artifact (code, training recipe, agent harness, data pipeline, prompt) against an objective and an evaluator, using Hypothesis Tree Refinement (HTR) from the Arbor paper. Use this whenever someone wants to iteratively optimize something over many experiments without overfitting — e.g. "get my model's eval score up", "improve this agent/harness", "tune this pipeline", "beat the baseline on this benchmark", "run a search over approaches and keep the best", "do an MLE-bench / Kaggle-style optimization", or any long-horizon "make this artifact better and don't just memorize the dev set" task. Trigger it even when the user doesn't say "Arbor" or "hypothesis tree" but describes repeated experiment-and-evaluate loops, branching exploration of competing ideas, or worries about a dev/test gap. Runs Claude itself as the coordinator with subagent executors in isolated git worktrees; for the standalone `arbor` CLI tool see references/arbor-upstream.md.

## Example requests

Ask your agent in plain language, for example:

- *"I have a training script for a small transformer and I want to push validation perplexity down as far as possible. Can you run a long autonomous search over optimizer and architecture tweaks and keep only what really generalizes?"*
- *"improve my agent harness pass rate"*
- *"My repo at ./mle_tabular is a Kaggle-style tabular competition solution (LightGBM, features in features.py, 5-fold CV in cv.py, MAE currently 0.412). I'd like to try many different approaches in parallel, record what each one taught us, drop the dead ends, and make sure the final winner isn't just overfit to the CV folds. Budget is about 20 rounds."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill arbor

# Kalaris Labs installer with checksum verification
npx research-agent-skills install arbor
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `research-automation` category with `/plugin install research-automation@research-agent-skills`.

## Related

- [`hypothesis-generation`](/skills/hypothesis-generation)
- [`research-skill-creator`](/skills/research-skill-creator)
- [`scientific-brainstorming`](/skills/scientific-brainstorming)
- [`statistical-analysis`](/skills/statistical-analysis)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/arbor/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
