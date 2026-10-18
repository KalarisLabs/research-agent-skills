---
title: "huggingface-tokenizers — AI agent skill for ml training"
description: "Provides the HuggingFace Tokenizers library (Rust core with Python and Node.js bindings) for training and using BPE, WordPiece, and Unigram tokenizers."
keywords: ["Tokenization", "HuggingFace", "BPE", "WordPiece", "Unigram", "Fast Tokenization", "Rust", "Custom Tokenizer", "Alignment Tracking", "Production"]
---

# `huggingface-tokenizers`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Tokenization, HuggingFace, BPE, WordPiece, Unigram, Fast Tokenization, Rust, Custom Tokenizer, Alignment Tracking, Production

## When to use it

Provides the HuggingFace Tokenizers library (Rust core with Python and Node.js bindings) for training and using BPE, WordPiece, and Unigram tokenizers. Covers the pipeline of normalizers, pre-tokenizers, models, post-processors and decoders, padding and truncation, batch encoding, alignment tracking, and conversion to transformers PreTrainedTokenizerFast. Use when training a custom tokenizer or vocabulary on a new corpus, tokenizing large text corpora quickly, mapping tokens back to character offsets for NER or question answering, or configuring normalization and special tokens. Use when wrapping a custom tokenizer for transformers. For SentencePiece models or tiktoken, use those tools instead; for loading a pretrained tokenizer only, AutoTokenizer is enough.

## Example requests

Ask your agent in plain language, for example:

- *"How do I train a BPE tokenizer on my own text files?"*
- *"I'm fine-tuning a token classification model for biomedical NER on ~/data/pubmed_abstracts.jsonl (about 4 GB). My labels are character spans, and after tokenizing with a custom tokenizer I can't line them up with the tokens. How do I get each token's start/end character positions and assign labels, including handling truncation at 512 tokens with overflowing sequences?"*
- *"I have a corpus of Python source code and legal contracts, and I need a vocabulary of about 32k subword units tailored to it, then I want to plug it into a Hugging Face model using the standard from_pretrained workflow and Trainer. What's the best way to build that?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill huggingface-tokenizers

# Kalaris Labs installer with checksum verification
npx research-agent-skills install huggingface-tokenizers
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`sentencepiece`](/skills/sentencepiece)
- [`transformers`](/skills/transformers)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/huggingface-tokenizers/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
