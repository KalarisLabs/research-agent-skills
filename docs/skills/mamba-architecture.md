---
title: "mamba-architecture — AI agent skill for ml training"
description: "Explains how to use Mamba selective state-space models (state-spaces/mamba package, Mamba-1 with d_state=16 and Mamba-2 with multi-head structure and d_st…"
---

# `mamba-architecture`

> Explains how to use Mamba selective state-space models (state-spaces/mamba package, Mamba-1 with d_state=16 and Mamba-2 with multi-head structure and d_state=128) for linear-time sequence modeling. Covers installation, the Mamba block, building a language model with MambaLMHeadModel, loading pretrained state-spaces checkpoints (130M to 2.8B) from HuggingFace, and benchmarking against Transformers. Use when implementing or loading Mamba models, processing very long sequences without a KV cache, building streaming applications, choosing between Mamba-1 and Mamba-2, or fixing install and CUDA memory problems. Requires Linux and an NVIDIA GPU. Do not use for standard Transformer models, or for RWKV, RetNet, or Hyena architectures.

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

## Install

```bash
npx research-agent-skills install mamba-architecture
npx skills add KalarisLabs/research-agent-skills --skill mamba-architecture
```

## When to use it

Explains how to use Mamba selective state-space models (state-spaces/mamba package, Mamba-1 with d_state=16 and Mamba-2 with multi-head structure and d_state=128) for linear-time sequence modeling. Covers installation, the Mamba block, building a language model with MambaLMHeadModel, loading pretrained state-spaces checkpoints (130M to 2.8B) from HuggingFace, and benchmarking against Transformers. Use when implementing or loading Mamba models, processing very long sequences without a KV cache, building streaming applications, choosing between Mamba-1 and Mamba-2, or fixing install and CUDA memory problems. Requires Linux and an NVIDIA GPU. Do not use for standard Transformer models, or for RWKV, RetNet, or Hyena architectures.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/mamba-architecture/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
