---
title: "paper-corpus-rag — AI agent skill for knowledge and rag"
description: "Build grounded question answering and retrieval-augmented generation (RAG) over your own collection of research papers, with answers that cite the exact paper…"
keywords: ["RAG", "retrieval", "vector database", "pgvector", "Chroma", "Qdrant", "FAISS", "SQLite", "full-text search", "literature synthesis"]
---

# `paper-corpus-rag`

**Category:** [knowledge-and-rag](/skills#knowledge-and-rag) · **License:** MIT · **Version:** 1.0 · **Includes scripts**

**Tags:** RAG, retrieval, vector database, pgvector, Chroma, Qdrant, FAISS, SQLite, full-text search, literature synthesis

## When to use it

Build grounded question answering and retrieval-augmented generation (RAG) over your own collection of research papers, with answers that cite the exact paper and passage. Use when a user wants to "chat with" or search a folder of PDFs, synthesize evidence across a literature corpus, find which paper says X, or build a vector/hybrid index with SQLite FTS5, pgvector (Postgres), Chroma, Qdrant or FAISS. Includes a zero-dependency local full-text index with citable hits.

## Example requests

Ask your agent in plain language, for example:

- *"I have 300 PDFs of papers. Let me ask questions and get answers with citations to the exact passages."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill paper-corpus-rag

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills paper-corpus-rag
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `knowledge-and-rag` category with `/plugin install knowledge-and-rag@research-agent-skills`.

## Related

- [`firecrawl-research-index`](/skills/firecrawl-research-index)
- [`literature-review`](/skills/literature-review)
- [`open-notebook`](/skills/open-notebook)
- [`qdrant-vector-search`](/skills/qdrant-vector-search)
- [`research-knowledge-graph`](/skills/research-knowledge-graph)
- [`sentence-transformers`](/skills/sentence-transformers)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/paper-corpus-rag/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
