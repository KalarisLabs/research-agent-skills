---
title: "chroma — AI agent skill for knowledge and rag"
description: "Open-source embedding database for AI applications. Store embeddings and metadata, perform vector and full-text search, filter by metadata."
keywords: ["RAG", "Chroma", "Vector Database", "Embeddings", "Semantic Search", "Open Source", "Self-Hosted", "Document Retrieval", "Metadata Filtering"]
---

# `chroma`

**Category:** [knowledge-and-rag](/skills#knowledge-and-rag) · **License:** MIT · **Version:** 1.0.0

**Tags:** RAG, Chroma, Vector Database, Embeddings, Semantic Search, Open Source, Self-Hosted, Document Retrieval, Metadata Filtering

## When to use it

Open-source embedding database for AI applications. Store embeddings and metadata, perform vector and full-text search, filter by metadata. Simple 4-function API. Scales from notebooks to production clusters. Use for semantic search, RAG applications, or document retrieval. Best for local development and open-source projects.

## Example requests

Ask your agent in plain language, for example:

- *"How do I set up a local Chroma DB for my paper embeddings?"*
- *"I'm building a RAG pipeline over 4,000 PDF methods sections saved in ./papers/. I chunked them into ~500-token pieces and call collection.add(documents=chunks, ids=ids) with chromadb 1.3.3, but I get 'DuplicateIDError' halfway through and my notebook loses everything on restart. How do I fix both?"*
- *"I have about 20k abstracts from our lab's literature collection and want to find the ones related to a question I type in plain English. I'd like it to run on my laptop, be free and open source, let me restrict results to papers after 2020, and not need a cloud account. What should I use and how should I set it up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill chroma

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills chroma
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `knowledge-and-rag` category with `/plugin install knowledge-and-rag@research-agent-skills`.

## Related

- [`qdrant-vector-search`](/skills/qdrant-vector-search)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/chroma/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
