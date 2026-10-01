---
title: "pinecone — AI agent skill for knowledge and rag"
description: "Guides use of Pinecone, a managed serverless vector database, through its Python client and the LangChain and LlamaIndex integrations."
---

# `pinecone`

> Guides use of Pinecone, a managed serverless vector database, through its Python client and the LangChain and LlamaIndex integrations. Covers creating indexes, upserting and querying vectors, metadata filtering, namespaces, hybrid dense and sparse search, index management, and deleting vectors. Use when building a production RAG system on a hosted vector store, adding semantic search or recommendations without running infrastructure, isolating per-user or per-tenant data with namespaces, combining dense and sparse vectors in one query, or filtering results by metadata. Do not use for self-hosted or local stores (Chroma, Weaviate) or offline similarity search (FAISS).

**Category:** [knowledge-and-rag](/skills#knowledge-and-rag) · **License:** MIT · **Version:** 1.0.0

## Install

```bash
npx skills add KalarisLabs/research-agent-skills --skill pinecone
```

## When to use it

Guides use of Pinecone, a managed serverless vector database, through its Python client and the LangChain and LlamaIndex integrations. Covers creating indexes, upserting and querying vectors, metadata filtering, namespaces, hybrid dense and sparse search, index management, and deleting vectors. Use when building a production RAG system on a hosted vector store, adding semantic search or recommendations without running infrastructure, isolating per-user or per-tenant data with namespaces, combining dense and sparse vectors in one query, or filtering results by metadata. Do not use for self-hosted or local stores (Chroma, Weaviate) or offline similarity search (FAISS).

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pinecone/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
