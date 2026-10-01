---
title: "huggingface-tokenizers — AI agent skill for ml training"
description: "Provides the HuggingFace Tokenizers library (Rust core with Python and Node.js bindings) for training and using BPE, WordPiece, and Unigram tokenizers."
---

# `huggingface-tokenizers`

> Provides the HuggingFace Tokenizers library (Rust core with Python and Node.js bindings) for training and using BPE, WordPiece, and Unigram tokenizers. Covers the pipeline of normalizers, pre-tokenizers, models, post-processors and decoders, padding and truncation, batch encoding, alignment tracking, and conversion to transformers PreTrainedTokenizerFast. Use when training a custom tokenizer or vocabulary on a new corpus, tokenizing large text corpora quickly, mapping tokens back to character offsets for NER or question answering, or configuring normalization and special tokens. Use when wrapping a custom tokenizer for transformers. For SentencePiece models or tiktoken, use those tools instead; for loading a pretrained tokenizer only, AutoTokenizer is enough.

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill huggingface-tokenizers
```

## When to use it

Provides the HuggingFace Tokenizers library (Rust core with Python and Node.js bindings) for training and using BPE, WordPiece, and Unigram tokenizers. Covers the pipeline of normalizers, pre-tokenizers, models, post-processors and decoders, padding and truncation, batch encoding, alignment tracking, and conversion to transformers PreTrainedTokenizerFast. Use when training a custom tokenizer or vocabulary on a new corpus, tokenizing large text corpora quickly, mapping tokens back to character offsets for NER or question answering, or configuring normalization and special tokens. Use when wrapping a custom tokenizer for transformers. For SentencePiece models or tiktoken, use those tools instead; for loading a pretrained tokenizer only, AutoTokenizer is enough.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/huggingface-tokenizers/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
