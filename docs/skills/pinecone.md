---
title: "pinecone — AI agent skill for knowledge and rag"
description: "Guides use of Pinecone, a managed serverless vector database, through its Python client and the LangChain and LlamaIndex integrations."
keywords: ["RAG", "Pinecone", "Vector Database", "Managed Service", "Serverless", "Hybrid Search", "Production", "Auto-Scaling", "Low Latency", "Recommendations"]
---

# `pinecone`

**Category:** [knowledge-and-rag](/skills#knowledge-and-rag) · **License:** MIT · **Version:** 1.0.0

**Tags:** RAG, Pinecone, Vector Database, Managed Service, Serverless, Hybrid Search, Production, Auto-Scaling, Low Latency, Recommendations

## When to use it

Guides use of Pinecone, a managed serverless vector database, through its Python client and the LangChain and LlamaIndex integrations. Covers creating indexes, upserting and querying vectors, metadata filtering, namespaces, hybrid dense and sparse search, index management, and deleting vectors. Use when building a production RAG system on a hosted vector store, adding semantic search or recommendations without running infrastructure, isolating per-user or per-tenant data with namespaces, combining dense and sparse vectors in one query, or filtering results by metadata. Do not use for self-hosted or local stores (Chroma, Weaviate) or offline similarity search (FAISS).

## Example requests

Ask your agent in plain language, for example:

- *"How do I upsert embeddings into a Pinecone index?"*
- *"I have 40k chunked abstracts from our lab's PubMed pull in abstracts.jsonl, embedded with text-embedding-3-small (1536 dims). I need to load them into Pinecone so each postdoc gets their own isolated space, and then query only records where year >= 2020 and journal == 'Cell'. Getting 'Vector dimension 768 does not match the dimension of the index 1536' on upsert. Can you fix and set it up?"*
- *"We're building a literature search tool for our group and want it hosted so we don't run any servers. Queries mix exact gene names like 'BRCA2 c.5946delT' with fuzzy conceptual phrasing, and keyword-only or embedding-only search each miss things. What's the best way to combine both in a single query against a managed vector store?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pinecone

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills pinecone
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `knowledge-and-rag` category with `/plugin install knowledge-and-rag@research-agent-skills`.

## Related

- [`qdrant-vector-search`](/skills/qdrant-vector-search)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pinecone/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
