---
title: "torch-geometric — AI agent skill for data science and ml"
description: "PyTorch Geometric (PyG) for graph neural networks — node/link/graph classification, message passing (GCN, GAT, GraphSAGE, GIN), heterogeneous graphs, neighbor…"
keywords: ["graph neural networks", "PyTorch Geometric", "GNN", "deep learning"]
---

# `torch-geometric`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** MIT · **Version:** 1.2

**Tags:** graph neural networks, PyTorch Geometric, GNN, deep learning

## When to use it

PyTorch Geometric (PyG) for graph neural networks — node/link/graph classification, message passing (GCN, GAT, GraphSAGE, GIN), heterogeneous graphs, neighbor sampling, and custom datasets. Use when working with torch_geometric, not for general NetworkX analytics or non-graph PyTorch models.

## Example requests

Ask your agent in plain language, for example:

- *"How do I build a 2-layer GCN for Cora in PyG?"*
- *"I'm training a GraphSAGE model on ogbn-products with NeighborLoader (num_neighbors=[15,10,5]) for a 2-layer model and my accuracy is bad and training is slow. In the loop I compute loss on out vs batch.y directly. Here's my loop: `for batch in loader: out = model(batch.x, batch.edge_index); loss = F.cross_entropy(out, batch.y)`. What's wrong?"*
- *"I have a CSV of users, a CSV of movies, and a CSV of ratings. I want to predict which movies a user will like, treating users and movies as different kinds of nodes with different relations between them. How should I set this up and train it?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill torch-geometric

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills torch-geometric
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [`networkx`](/skills/networkx)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/torch-geometric/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
