---
title: "speculative-decoding — AI agent skill for multimodal and emerging"
description: "Accelerate LLM inference using speculative decoding, Medusa multiple heads, and lookahead decoding techniques."
keywords: ["Emerging Techniques", "Speculative Decoding", "Medusa", "Lookahead Decoding", "Fast Inference", "Draft Models", "Tree Attention", "Parallel Generation", "Latency Reduction", "Inference Optimization"]
---

# `speculative-decoding`

**Category:** [multimodal-and-emerging](/skills#multimodal-and-emerging) · **License:** MIT · **Version:** 1.0.0

**Tags:** Emerging Techniques, Speculative Decoding, Medusa, Lookahead Decoding, Fast Inference, Draft Models, Tree Attention, Parallel Generation, Latency Reduction, Inference Optimization

## When to use it

Accelerate LLM inference using speculative decoding, Medusa multiple heads, and lookahead decoding techniques. Use when optimizing inference speed (1.5-3.6× speedup), reducing latency for real-time applications, or deploying models with limited compute. Covers draft models, tree-based attention, Jacobi iteration, parallel token generation, and production deployment strategies.

## Example requests

Ask your agent in plain language, for example:

- *"How do I add Medusa heads to Vicuna-7B and train them?"*
- *"I'm running Llama-2-70B on 4xA100 for a code-completion tool, and p50 latency per token is about 45ms, which is too slow for our IDE plugin. I have Llama-2-7B and TinyLlama-1.1B checkpoints available. In HF transformers, how can I use one of them to speed up generation without changing the 70B outputs? Please include the assistant_model setup and how to choose the number of speculative tokens."*
- *"We can't afford to train anything or host a second model. Is there a way to get our existing LLM to produce several tokens per forward pass by solving the decoding as a parallel fixed-point problem? Which settings matter?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill speculative-decoding

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills speculative-decoding
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `multimodal-and-emerging` category with `/plugin install multimodal-and-emerging@research-agent-skills`.

## Related

- [`knowledge-distillation`](/skills/knowledge-distillation)
- [`model-pruning`](/skills/model-pruning)
- [`phoenix-observability`](/skills/phoenix-observability)
- [`rwkv-architecture`](/skills/rwkv-architecture)
- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/speculative-decoding/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
