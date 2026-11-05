---
title: "mamba-architecture — AI agent skill for ml training"
description: "Explains how to use Mamba selective state-space models (state-spaces/mamba package, Mamba-1 with d_state=16 and Mamba-2 with multi-head structure and…"
keywords: ["Model Architecture", "Mamba", "State Space Models", "SSM", "Linear Complexity", "Long Context", "Efficient Inference", "Hardware-Aware", "Alternative To Transformers"]
---

# `mamba-architecture`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Model Architecture, Mamba, State Space Models, SSM, Linear Complexity, Long Context, Efficient Inference, Hardware-Aware, Alternative To Transformers

## When to use it

Explains how to use Mamba selective state-space models (state-spaces/mamba package, Mamba-1 with d_state=16 and Mamba-2 with multi-head structure and d_state=128) for linear-time sequence modeling. Covers installation, the Mamba block, building a language model with MambaLMHeadModel, loading pretrained state-spaces checkpoints (130M to 2.8B) from HuggingFace, and benchmarking against Transformers. Use when implementing or loading Mamba models, processing very long sequences without a KV cache, building streaming applications, choosing between Mamba-1 and Mamba-2, or fixing install and CUDA memory problems. Requires Linux and an NVIDIA GPU. Do not use for standard Transformer models, or for RWKV, RetNet, or Hyena architectures.

## Example requests

Ask your agent in plain language, for example:

- *"How do I install mamba-ssm on my Linux box with an A100?"*
- *"I'm trying to load state-spaces/mamba-1.4b in my script eval_lm.py with AutoModelForCausalLM.from_pretrained and it throws an error about an unrecognized model config. I'm on a 24GB RTX 4090 and want to generate text from a prompt. What should I change?"*
- *"I need to run a language model over 500K-token genomic sequences, and a standard Transformer's KV cache blows up my GPU memory. I want something with linear-time scaling that can also stream. What architecture and setup would you suggest?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill mamba-architecture

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills mamba-architecture
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`optimizing-attention-flash`](/skills/optimizing-attention-flash)
- [`rwkv-architecture`](/skills/rwkv-architecture)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/mamba-architecture/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
