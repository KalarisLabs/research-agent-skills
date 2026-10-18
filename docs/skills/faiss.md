---
title: "faiss — AI agent skill for knowledge and rag"
description: "Facebook's library for efficient similarity search and clustering of dense vectors."
keywords: ["RAG", "FAISS", "Similarity Search", "Vector Search", "Facebook AI", "GPU Acceleration", "Billion-Scale", "K-NN", "HNSW", "High Performance", "Large Scale"]
---

# `faiss`

**Category:** [knowledge-and-rag](/skills#knowledge-and-rag) · **License:** MIT · **Version:** 1.0.0

**Tags:** RAG, FAISS, Similarity Search, Vector Search, Facebook AI, GPU Acceleration, Billion-Scale, K-NN, HNSW, High Performance, Large Scale

## When to use it

Facebook's library for efficient similarity search and clustering of dense vectors. Supports billions of vectors, GPU acceleration, and various index types (Flat, IVF, HNSW). Use for fast k-NN search, large-scale vector retrieval, or when you need pure similarity search without metadata. Best for high-performance applications.

## Example requests

Ask your agent in plain language, for example:

- *"How do I build a FAISS index for 2M embeddings?"*
- *"I have 5M 768-dim sentence-transformer embeddings of PubMed abstracts saved in pubmed_emb.npy (float32). Using faiss.IndexIVFFlat with nlist=4096 I get 'RuntimeError: Error in faiss::IndexIVFFlat::add_core ... index not trained' when I call index.add(). Search is also slow on CPU. How do I fix this and speed it up?"*
- *"I've got about 300 million image feature vectors from a microscopy screen, 512-dim, and I need to find the 50 nearest neighbors for each of 10,000 query images as fast as possible. There's no metadata filtering, it's a one-off offline batch job on a machine with a few GPUs. What approach should I use?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill faiss

# Kalaris Labs installer with checksum verification
npx research-agent-skills install faiss
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `knowledge-and-rag` category with `/plugin install knowledge-and-rag@research-agent-skills`.

## Related

- [`qdrant-vector-search`](/skills/qdrant-vector-search)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/faiss/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
