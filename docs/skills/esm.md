---
title: "esm — AI agent skill for life sciences"
description: "Covers the EvolutionaryScale/Biohub `esm` Python SDK: ESM3 generative protein design (sequence, structure and function tracks, chain-of-thought), ESMC…"
keywords: ["protein language models", "protein design", "structure prediction", "protein embeddings"]
---

# `esm`

**Category:** [life-sciences](/skills#life-sciences) · **License:** MIT · **Version:** 1.2

**Tags:** protein language models, protein design, structure prediction, protein embeddings

## When to use it

Covers the EvolutionaryScale/Biohub `esm` Python SDK: ESM3 generative protein design (sequence, structure and function tracks, chain-of-thought), ESMC embeddings, inverse folding, ESMFold2 structure prediction, and hosted Forge/Biohub inference with ESM_API_KEY. Use when generating or completing proteins with ESM3, extracting ESMC embeddings for classification or similarity, folding a sequence or designing sequences from a structure, or choosing between esm3-open, esmc_300m and Forge-hosted models. Use when batching async Forge or Biohub API calls. Not for other protein models such as AlphaFold or generic Hugging Face transformers usage.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get per-residue embeddings for a protein sequence with ESMC locally?"*
- *"I have a 3,000-sequence file, kinases.fasta, and I'm trying to classify them as active/inactive with logistic regression. I tried esm.sdk.client('esmc-600m-2024-12') in a loop and keep hitting rate-limit errors (429) after a few hundred calls. How should I restructure this so it finishes reliably?"*
- *"I have a crystal structure of a de novo binder backbone (binder.pdb) and I want new amino acid sequences that would fold into it. Is there a language-model route for that, and how would I check the designs afterward?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill esm

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills esm
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `life-sciences` category with `/plugin install life-sciences@research-agent-skills`.

## Related

- [`sentence-transformers`](/skills/sentence-transformers)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/esm/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
