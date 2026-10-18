---
title: "axolotl — AI agent skill for ml training"
description: "Provides guidance for fine-tuning large language models with Axolotl, covering YAML training configs, LoRA and QLoRA, preference training with DPO, KTO, ORPO…"
keywords: ["Fine-Tuning", "Axolotl", "LLM", "LoRA", "QLoRA", "DPO", "KTO", "ORPO", "GRPO", "YAML", "HuggingFace", "DeepSpeed", "Multimodal"]
---

# `axolotl`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Fine-Tuning, Axolotl, LLM, LoRA, QLoRA, DPO, KTO, ORPO, GRPO, YAML, HuggingFace, DeepSpeed, Multimodal

## When to use it

Provides guidance for fine-tuning large language models with Axolotl, covering YAML training configs, LoRA and QLoRA, preference training with DPO, KTO, ORPO and GRPO, multimodal models, FSDP and multi-GPU setups, sequence (context) parallelism, NCCL bandwidth tests, dataset formats, compressed model saving for vLLM and llmcompressor, and custom integrations. Use when writing or debugging an Axolotl YAML config, choosing a dataset format for a fine-tuning run, setting up FSDP or context_parallel_size across GPUs, or running DPO, KTO, ORPO or GRPO training. Use when saving a compressed model for vLLM inference, or when writing a custom Axolotl plugin or integration. Not for inference serving or general Hugging Face Trainer scripts outside Axolotl.

## Example requests

Ask your agent in plain language, for example:

- *"my axolotl run dies with OOM on 2x A100 40GB when I turn on 8k context. how do I split sequences across the two GPUs?"*
- *"I'm fine-tuning Llama-3.1-8B with QLoRA in Axolotl on a JSONL file of \{"prompt", "chosen", "rejected"\} rows at data/prefs.jsonl. Can you write me a config for DPO and tell me which dataset type to set? I get 'KeyError: messages' right now."*
- *"I trained a model and want to ship a smaller checkpoint to serve with vLLM, and maybe quantize it further later with llmcompressor. How can I save it so the files take less disk space while still loading in those tools?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill axolotl

# Kalaris Labs installer with checksum verification
npx research-agent-skills install axolotl
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`llama-factory`](/skills/llama-factory)
- [`peft-fine-tuning`](/skills/peft-fine-tuning)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/axolotl/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
