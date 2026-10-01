---
title: "axolotl — AI agent skill for ml training"
description: "Provides guidance for fine-tuning large language models with Axolotl, covering YAML training configs, LoRA and QLoRA, preference training with DPO, KTO, O…"
---

# `axolotl`

> Provides guidance for fine-tuning large language models with Axolotl, covering YAML training configs, LoRA and QLoRA, preference training with DPO, KTO, ORPO and GRPO, multimodal models, FSDP and multi-GPU setups, sequence (context) parallelism, NCCL bandwidth tests, dataset formats, compressed model saving for vLLM and llmcompressor, and custom integrations. Use when writing or debugging an Axolotl YAML config, choosing a dataset format for a fine-tuning run, setting up FSDP or context_parallel_size across GPUs, or running DPO, KTO, ORPO or GRPO training. Use when saving a compressed model for vLLM inference, or when writing a custom Axolotl plugin or integration. Not for inference serving or general Hugging Face Trainer scripts outside Axolotl.

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

## Install

```bash
npx research-agent-skills install axolotl
npx skills add KalarisLabs/research-agent-skills --skill axolotl
```

## When to use it

Provides guidance for fine-tuning large language models with Axolotl, covering YAML training configs, LoRA and QLoRA, preference training with DPO, KTO, ORPO and GRPO, multimodal models, FSDP and multi-GPU setups, sequence (context) parallelism, NCCL bandwidth tests, dataset formats, compressed model saving for vLLM and llmcompressor, and custom integrations. Use when writing or debugging an Axolotl YAML config, choosing a dataset format for a fine-tuning run, setting up FSDP or context_parallel_size across GPUs, or running DPO, KTO, ORPO or GRPO training. Use when saving a compressed model for vLLM inference, or when writing a custom Axolotl plugin or integration. Not for inference serving or general Hugging Face Trainer scripts outside Axolotl.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/axolotl/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
