---
title: "long-context — AI agent skill for multimodal and emerging"
description: "Extend context windows of transformer models using RoPE, YaRN, ALiBi, and position interpolation techniques."
keywords: ["Emerging Techniques", "Long Context", "RoPE", "YaRN", "ALiBi", "Position Interpolation", "Extended Context", "Rotary Embeddings", "Attention Bias", "Context Extension", "Positional Encoding"]
---

# `long-context`

**Category:** [multimodal-and-emerging](/skills#multimodal-and-emerging) · **License:** MIT · **Version:** 1.0.0

**Tags:** Emerging Techniques, Long Context, RoPE, YaRN, ALiBi, Position Interpolation, Extended Context, Rotary Embeddings, Attention Bias, Context Extension, Positional Encoding

## When to use it

Extend context windows of transformer models using RoPE, YaRN, ALiBi, and position interpolation techniques. Use when processing long documents (32k-128k+ tokens), extending pre-trained models beyond original context limits, or implementing efficient positional encodings. Covers rotary embeddings, attention biases, interpolation methods, and extrapolation strategies for LLMs.

## Example requests

Ask your agent in plain language, for example:

- *"How do I stretch Mistral 7B to handle 64k tokens?"*
- *"I loaded meta-llama/Llama-2-7b-hf in transformers and set rope_scaling=\{'type':'linear','factor':8.0\}, aiming for 32k. Perplexity on my 30k-token legal contracts in contracts_eval.jsonl is much worse than at 4k, and I get an OOM at 24k tokens on a 40GB A100. What should I change, and do I need to fine-tune?"*
- *"I'm pretraining a small language model from scratch and want it to be trained on 1k-token sequences but still work reasonably when tested on 2k+ tokens. It would be nice if it also used less memory. Which way of encoding token positions should I use, and why?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill long-context

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills long-context
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `multimodal-and-emerging` category with `/plugin install multimodal-and-emerging@research-agent-skills`.

## Related

- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/long-context/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
