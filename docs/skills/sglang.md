---
title: "sglang — AI agent skill for ml inference and ops"
description: "Fast structured generation and serving for LLMs with RadixAttention prefix caching."
keywords: ["Inference Serving", "SGLang", "Structured Generation", "RadixAttention", "Prefix Caching", "Constrained Decoding", "Agents", "JSON Output", "Fast Inference", "Production Scale"]
---

# `sglang`

**Category:** [ml-inference-and-ops](/skills#ml-inference-and-ops) · **License:** MIT · **Version:** 1.0.0

**Tags:** Inference Serving, SGLang, Structured Generation, RadixAttention, Prefix Caching, Constrained Decoding, Agents, JSON Output, Fast Inference, Production Scale

## When to use it

Fast structured generation and serving for LLMs with RadixAttention prefix caching. Use for JSON/regex outputs, constrained decoding, agentic workflows with tool calls, or when you need 5× faster inference than vLLM with prefix sharing. Powers 300,000+ GPUs at xAI, AMD, NVIDIA, and LinkedIn.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get SGLang to only output valid JSON matching my schema?"*
- *"I'm running Llama-3.1-8B-Instruct on a single A100 to annotate 20k abstracts in abstracts.jsonl. Every request starts with the same ~1,200-token system prompt plus 8 few-shot examples, and throughput is awful with my current vLLM setup. I'm now getting 'CUDA out of memory' when I raise concurrency. Can you set up SGLang for this and tell me what to tune?"*
- *"I'm building a lab assistant agent that calls tools (plate reader lookup, protocol search) in multi-step loops, and each step resends a long shared context. I want to self-host an open model so the repeated context isn't recomputed every turn and the tool call arguments always parse correctly. What serving stack and setup should I use?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill sglang

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills sglang
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-inference-and-ops` category with `/plugin install ml-inference-and-ops@research-agent-skills`.

## Related

- [`llama-cpp`](/skills/llama-cpp)
- [`tensorrt-llm`](/skills/tensorrt-llm)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/sglang/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
