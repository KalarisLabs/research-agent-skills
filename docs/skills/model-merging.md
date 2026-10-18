---
title: "model-merging — AI agent skill for multimodal and emerging"
description: "Merge multiple fine-tuned models using mergekit to combine capabilities without retraining."
keywords: ["Emerging Techniques", "Model Merging", "Mergekit", "SLERP", "TIES", "DARE", "Task Arithmetic", "Model Fusion", "No Retraining", "Multi-Capability", "Arcee AI"]
---

# `model-merging`

**Category:** [multimodal-and-emerging](/skills#multimodal-and-emerging) · **License:** MIT · **Version:** 1.0.0

**Tags:** Emerging Techniques, Model Merging, Mergekit, SLERP, TIES, DARE, Task Arithmetic, Model Fusion, No Retraining, Multi-Capability, Arcee AI

## When to use it

Merge multiple fine-tuned models using mergekit to combine capabilities without retraining. Use when creating specialized models by blending domain-specific expertise (math + coding + chat), improving performance beyond single models, or experimenting rapidly with model variants. Covers SLERP, TIES-Merging, DARE, Task Arithmetic, linear merging, and production deployment strategies.

## Example requests

Ask your agent in plain language, for example:

- *"How do I merge two Mistral-7B fine-tunes with SLERP?"*
- *"I have three Llama-2-7B fine-tunes on my disk: ./models/math-ft, ./models/code-ft and ./models/chat-ft, all from the same base meta-llama/Llama-2-7b-hf. I tried a linear merge and the output is garbled and worse than any single model. Can you write me a mergekit config that uses TIES with density 0.5 and weights, and explain how to run it on CPU?"*
- *"I have a few open-weight models, each fine-tuned for a different skill. I have no GPU budget for more training. Can I produce one model that is decent at all of those skills by combining their weights, and how would I pick the mixing coefficients without labeled data?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill model-merging

# Kalaris Labs installer with checksum verification
npx research-agent-skills install model-merging
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `multimodal-and-emerging` category with `/plugin install multimodal-and-emerging@research-agent-skills`.

## Related

- [`knowledge-distillation`](/skills/knowledge-distillation)
- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/model-merging/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
