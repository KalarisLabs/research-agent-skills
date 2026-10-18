---
title: "sentence-transformers — AI agent skill for knowledge and rag"
description: "Generates sentence, text, and image embeddings locally with the Python sentence-transformers (SBERT) library, using pre-trained Hugging Face models such as…"
keywords: ["Sentence Transformers", "Embeddings", "Semantic Similarity", "RAG", "Multilingual", "Multimodal", "Pre-Trained Models", "Clustering", "Semantic Search", "Production"]
---

# `sentence-transformers`

**Category:** [knowledge-and-rag](/skills#knowledge-and-rag) · **License:** MIT · **Version:** 1.0.0

**Tags:** Sentence Transformers, Embeddings, Semantic Similarity, RAG, Multilingual, Multimodal, Pre-Trained Models, Clustering, Semantic Search, Production

## When to use it

Generates sentence, text, and image embeddings locally with the Python sentence-transformers (SBERT) library, using pre-trained Hugging Face models such as all-MiniLM-L6-v2, all-mpnet-base-v2, and multilingual variants. Covers encoding, cosine similarity, semantic search, batch encoding, fine-tuning, and LangChain/LlamaIndex integration. Use when building embeddings for RAG, running semantic search or similarity scoring, clustering or classifying text, embedding multilingual text without an API, or fine-tuning an embedding model on domain data. For API-based or managed embeddings, use OpenAI or Cohere Embed instead.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get embeddings for a list of sentences without calling an API?"*
- *"I have abstracts.csv with about 40k paper abstracts in a 'abstract' column. I want to build a semantic search so I can type a query and get the top 10 most similar abstracts. I'm on a laptop with no GPU. Can you set that up with all-mpnet-base-v2 and tell me how long it will take?"*
- *"I have about 3,000 customer support tickets in German, French and English. I want to group them into topics automatically, and I can't send the text to any external service because of privacy rules. What should I do?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill sentence-transformers

# Kalaris Labs installer with checksum verification
npx research-agent-skills install sentence-transformers
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `knowledge-and-rag` category with `/plugin install knowledge-and-rag@research-agent-skills`.

## Related

- [`autoskill`](/skills/autoskill)
- [`esm`](/skills/esm)
- [`paper-corpus-rag`](/skills/paper-corpus-rag)
- [`qdrant-vector-search`](/skills/qdrant-vector-search)
- [`umap-learn`](/skills/umap-learn)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/sentence-transformers/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
