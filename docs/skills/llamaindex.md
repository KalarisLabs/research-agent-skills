---
title: "llamaindex — AI agent skill for llm applications"
description: "Data framework for building LLM applications with RAG. Specializes in document ingestion (300+ connectors), indexing, and querying."
keywords: ["Agents", "LlamaIndex", "RAG", "Document Ingestion", "Vector Indices", "Query Engines", "Knowledge Retrieval", "Data Framework", "Multimodal", "Private Data", "Connectors"]
---

# `llamaindex`

**Category:** [llm-applications](/skills#llm-applications) · **License:** MIT · **Version:** 1.0.0

**Tags:** Agents, LlamaIndex, RAG, Document Ingestion, Vector Indices, Query Engines, Knowledge Retrieval, Data Framework, Multimodal, Private Data, Connectors

## When to use it

Data framework for building LLM applications with RAG. Specializes in document ingestion (300+ connectors), indexing, and querying. Features vector indices, query engines, agents, and multi-modal support. Use for document Q&A, chatbots, knowledge retrieval, or building RAG pipelines. Best for data-centric LLM applications.

## Example requests

Ask your agent in plain language, for example:

- *"How do I build a quick RAG over a folder of PDFs?"*
- *"I have about 400 PDFs of oncology papers in ./papers and a Postgres table with trial metadata (nct_id, phase, status). I want to ask questions over the papers and filter retrieval by phase and status. Using llama-index 0.14 with Chroma as the store. How should I set this up, and how do I stop it from re-embedding everything every time I restart?"*
- *"My lab has years of internal protocols, meeting notes and Notion pages. I'd like a chatbot that lets students ask questions about them and remembers earlier turns in the conversation, answering from our own documents. What's a sensible way to build it?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill llamaindex

# Kalaris Labs installer with checksum verification
npx research-agent-skills install llamaindex
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `llm-applications` category with `/plugin install llm-applications@research-agent-skills`.

## Related

- [`langsmith-observability`](/skills/langsmith-observability)
- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/llamaindex/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
