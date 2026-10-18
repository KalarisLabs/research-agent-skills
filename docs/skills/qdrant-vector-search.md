---
title: "qdrant-vector-search — AI agent skill for knowledge and rag"
description: "High-performance vector similarity search engine for RAG and semantic search."
keywords: ["RAG", "Vector Search", "Qdrant", "Semantic Search", "Embeddings", "Similarity Search", "HNSW", "Production", "Distributed"]
---

# `qdrant-vector-search`

**Category:** [knowledge-and-rag](/skills#knowledge-and-rag) · **License:** MIT · **Version:** 1.0.0

**Tags:** RAG, Vector Search, Qdrant, Semantic Search, Embeddings, Similarity Search, HNSW, Production, Distributed

## When to use it

High-performance vector similarity search engine for RAG and semantic search. Use when building production RAG systems requiring fast nearest neighbor search, hybrid search with filtering, or scalable vector storage with Rust-powered performance.

## Example requests

Ask your agent in plain language, for example:

- *"How do I set up Qdrant with payload filtering for my paper abstracts?"*
- *"I have 2.3M PubMed abstracts embedded with BAAI/bge-base-en-v1.5 (768-d) in embeddings.parquet, with fields year, journal and mesh_terms. I need to load them into a self-hosted Docker instance and query for nearest neighbors restricted to year >= 2020 and a given journal. My filtered queries are taking several seconds. What should I do?"*
- *"We're building an internal literature QA system for our lab. Each chunk needs both a dense embedding and a BM25-style sparse representation, and we want to combine them with metadata filters like publication year. Data must stay on our own servers and be able to scale to tens of millions of chunks. Which vector store and architecture would you use, and how do I implement it?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill qdrant-vector-search

# Kalaris Labs installer with checksum verification
npx research-agent-skills install qdrant-vector-search
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `knowledge-and-rag` category with `/plugin install knowledge-and-rag@research-agent-skills`.

## Related

- [`chroma`](/skills/chroma)
- [`faiss`](/skills/faiss)
- [`lamindb`](/skills/lamindb)
- [`matchms`](/skills/matchms)
- [`paper-corpus-rag`](/skills/paper-corpus-rag)
- [`pinecone`](/skills/pinecone)
- [`sentence-transformers`](/skills/sentence-transformers)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/qdrant-vector-search/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
