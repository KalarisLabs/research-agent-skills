---
title: "huggingface-accelerate — AI agent skill for ml training"
description: "Wraps existing PyTorch training scripts with HuggingFace Accelerate (Accelerator class, accelerate config, accelerate launch) so the same code runs on CPU…"
keywords: ["Distributed Training", "HuggingFace", "Accelerate", "DeepSpeed", "FSDP", "Mixed Precision", "PyTorch", "DDP", "Unified API", "Simple"]
---

# `huggingface-accelerate`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Distributed Training, HuggingFace, Accelerate, DeepSpeed, FSDP, Mixed Precision, PyTorch, DDP, Unified API, Simple

## When to use it

Wraps existing PyTorch training scripts with HuggingFace Accelerate (Accelerator class, accelerate config, accelerate launch) so the same code runs on CPU, single GPU, multi-GPU, multi-node, TPU, or Apple MPS. Covers device placement, FP16/BF16/FP8 mixed precision, gradient accumulation, distributed checkpointing, and switching between DDP, DeepSpeed ZeRO, FSDP, and Megatron backends. Use when converting a single-GPU script to multi-GPU, enabling mixed precision, configuring DeepSpeed ZeRO or FSDP, or setting up gradient accumulation. Use when one script must run on different hardware. Not for callback-heavy training loops (use PyTorch Lightning) or multi-node orchestration with hyperparameter tuning (use Ray Train).

## Example requests

Ask your agent in plain language, for example:

- *"How do I make my train.py run on 4 GPUs without rewriting it?"*
- *"I have a ResNet-50 fine-tuning script, finetune_cifar.py, with a plain loop: model.cuda(), loss.backward(), and a DataLoader with batch_size=64. Moving it to 2 A100s gives me 'RuntimeError: Expected all tensors to be on the same device' after I started using DDP. I also want bf16 and an effective batch size of 256. Can you fix it?"*
- *"My 7B model doesn't fit in memory on a single 24GB card, and I want the same training code to also run on my colleague's MacBook for debugging. What's the most painless way to set this up so I don't maintain two scripts?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill huggingface-accelerate

# Kalaris Labs installer with checksum verification
npx research-agent-skills install huggingface-accelerate
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`deepspeed`](/skills/deepspeed)
- [`pytorch-lightning`](/skills/pytorch-lightning)
- [`pytorch-lightning-distributed`](/skills/pytorch-lightning-distributed)
- [`nanogpt`](/skills/nanogpt)
- [`pytorch-fsdp2`](/skills/pytorch-fsdp2)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/huggingface-accelerate/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
