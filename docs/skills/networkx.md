---
title: "networkx — AI agent skill for data science and ml"
description: "Create, analyze, and visualize complex networks and graphs in Python with NetworkX."
keywords: ["network analysis", "graph theory", "graphs", "community detection", "Python"]
---

# `networkx`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** 3-clause BSD license · **Version:** 1.2

**Tags:** network analysis, graph theory, graphs, community detection, Python

## When to use it

Create, analyze, and visualize complex networks and graphs in Python with NetworkX. Use when working with network/graph data structures, computing graph algorithms (shortest paths, centrality, clustering), detecting communities, generating synthetic networks (random, scale-free, small-world), reading/writing graph file formats, or drawing network topologies. Common applications include social, biological, transportation, and citation networks.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get the top 10 nodes by betweenness in my graph?"*
- *"I have an edge list in interactions.tsv (columns: protein_a, protein_b, score) from STRING for human PPI. I loaded it with nx.read_edgelist and now get 'TypeError: Failed to convert edge data' on the score column. Fix this, then find the connected components, report the size of the largest one, and run Louvain community detection with a fixed seed."*
- *"I'm modeling how a rumor spreads through a school. I want to simulate a few hundred students where most are in tight friend clusters but a few have friends across clusters, then see how many hops it takes on average for any two students to connect. How should I set this up in Python?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill networkx

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills networkx
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [`research-knowledge-graph`](/skills/research-knowledge-graph)
- [`torch-geometric`](/skills/torch-geometric)
- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/networkx/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
