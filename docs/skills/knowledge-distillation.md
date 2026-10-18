---
title: "knowledge-distillation — AI agent skill for multimodal and emerging"
description: "Compress large language models using knowledge distillation from teacher to student models."
keywords: ["Emerging Techniques", "Knowledge Distillation", "Model Compression", "Teacher-Student", "MiniLLM", "Reverse KLD", "Soft Targets", "Temperature Scaling", "Logit Distillation", "Model Transfer"]
---

# `knowledge-distillation`

**Category:** [multimodal-and-emerging](/skills#multimodal-and-emerging) · **License:** MIT · **Version:** 1.0.0

**Tags:** Emerging Techniques, Knowledge Distillation, Model Compression, Teacher-Student, MiniLLM, Reverse KLD, Soft Targets, Temperature Scaling, Logit Distillation, Model Transfer

## When to use it

Compress large language models using knowledge distillation from teacher to student models. Use when deploying smaller models with retained performance, transferring GPT-4 capabilities to open-source models, or reducing inference costs. Covers temperature scaling, soft targets, reverse KLD, logit distillation, and MiniLLM training strategies.

## Example requests

Ask your agent in plain language, for example:

- *"How do I shrink my 13B model into a 1B one without losing too much quality?"*
- *"I'm distilling Llama-2-13B (teacher) into a Llama-2-7B student on my instruction dataset train.jsonl. With forward KL my student produces bland, repetitive outputs. Should I move to reverse KL like MiniLLM, and how do I set the temperature and loss weights? I have 2x A100 80GB."*
- *"We spend too much on GPT-4 API calls for our contract-clause classification and extraction. I want an open-source model we host ourselves that behaves similarly on this narrow task. What's a sound plan?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill knowledge-distillation

# Kalaris Labs installer with checksum verification
npx research-agent-skills install knowledge-distillation
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `multimodal-and-emerging` category with `/plugin install multimodal-and-emerging@research-agent-skills`.

## Related

- [`model-merging`](/skills/model-merging)
- [`speculative-decoding`](/skills/speculative-decoding)
- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/knowledge-distillation/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
