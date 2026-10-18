---
title: "sentencepiece — AI agent skill for ml training"
description: "Language-independent tokenizer treating text as raw Unicode. Supports BPE and Unigram algorithms."
keywords: ["Tokenization", "SentencePiece", "Language-Independent", "BPE", "Unigram", "Multilingual", "CJK Languages", "Unicode", "Deterministic", "Google"]
---

# `sentencepiece`

**Category:** [ml-training](/skills#ml-training) · **License:** MIT · **Version:** 1.0.0

**Tags:** Tokenization, SentencePiece, Language-Independent, BPE, Unigram, Multilingual, CJK Languages, Unicode, Deterministic, Google

## When to use it

Language-independent tokenizer treating text as raw Unicode. Supports BPE and Unigram algorithms. Fast (50k sentences/sec), lightweight (6MB memory), deterministic vocabulary. Used by T5, ALBERT, XLNet, mBART. Train on raw text without pre-tokenization. Use when you need multilingual support, CJK languages, or reproducible tokenization.

## Example requests

Ask your agent in plain language, for example:

- *"How do I train a 32k Unigram SentencePiece model on my raw text file?"*
- *"I'm building a Japanese-Chinese-Korean translation model from corpus_cjk.txt (about 2GB, no word segmentation). I need a subword vocab of ~64k, and I want the same vocab every time I rerun the pipeline. Tokenization currently chokes on missing characters and I see lots of &lt;unk>. What should I do?"*
- *"I want to fine-tune a T5-style model on multilingual text, and I need to build a tokenizer from scratch that uses the same approach T5 uses, without any language-specific preprocessing. How should I set that up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill sentencepiece

# Kalaris Labs installer with checksum verification
npx research-agent-skills install sentencepiece
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ml-training` category with `/plugin install ml-training@research-agent-skills`.

## Related

- [`huggingface-tokenizers`](/skills/huggingface-tokenizers)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/sentencepiece/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
