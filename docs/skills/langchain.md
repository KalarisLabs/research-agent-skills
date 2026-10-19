---
title: "langchain — AI agent skill for llm applications"
description: "Framework for building LLM-powered applications with agents, chains, and RAG."
keywords: ["Agents", "LangChain", "RAG", "Tool Calling", "ReAct", "Memory Management", "Vector Stores", "LLM Applications", "Chatbots", "Production"]
---

# `langchain`

**Category:** [llm-applications](/skills#llm-applications) · **License:** MIT · **Version:** 1.0.0 · **Includes scripts**

**Tags:** Agents, LangChain, RAG, Tool Calling, ReAct, Memory Management, Vector Stores, LLM Applications, Chatbots, Production

## When to use it

Framework for building LLM-powered applications with agents, chains, and RAG. Supports multiple providers (OpenAI, Anthropic, Google), 500+ integrations, ReAct agents, tool calling, memory management, and vector store retrieval. Use for building chatbots, question-answering systems, autonomous agents, or RAG applications. Best for rapid prototyping and production deployments.

## Example requests

Ask your agent in plain language, for example:

- *"How do I make a LangChain agent that can call a web search tool?"*
- *"I'm in my lab's repo with 40 PDFs of protocol papers in ./papers. I'm using langchain 0.3 with Chroma and an Anthropic model. When I query, retrieval returns chunks that cut sentences in half and the answers miss context. Can you fix my pipeline so it loads the PDFs, splits them sensibly, and answers questions with sources?"*
- *"I want a chatbot for my group's wiki that remembers what was said earlier in the conversation, and I want to be able to switch between OpenAI and Gemini without rewriting everything. What should I use and how do I set it up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill langchain

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills langchain
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `llm-applications` category with `/plugin install llm-applications@research-agent-skills`.

## Related

- [`autogpt-agents`](/skills/autogpt-agents)
- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/langchain/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
