---
title: "ncats-arax — AI agent skill for scientific databases"
description: "Queries the NCATS Translator ARAX production API for bounded, typed, provenance-rich one-hop and endpoint-pinned two-hop biomedical knowledge-graph…"
keywords: ["biomedical knowledge graph", "NCATS Translator", "drug repurposing", "biomedical research"]
---

# `ncats-arax`

**Category:** [scientific-databases](/skills#scientific-databases) · **License:** MIT · **Version:** 1.0 · **Includes scripts**

**Tags:** biomedical knowledge graph, NCATS Translator, drug repurposing, biomedical research

## When to use it

Queries the NCATS Translator ARAX production API for bounded, typed, provenance-rich one-hop and endpoint-pinned two-hop biomedical knowledge-graph relationships. Use for Biolink-constrained RTX-KG2 lookup, explicit selected-provider ARAX federation, separate entity normalization, qualifier-aware graph traversal, and inspection of TRAPI edge bindings, publications, and knowledge-source provenance. Do not use for inference, ranking, open-ended pathfinding, clinical guidance, or sensitive queries.

## Example requests

Ask your agent in plain language, for example:

- *"Use ARAX to find what genes are connected to imatinib. Just one hop, keep it small."*
- *"I'm putting together a figure for our review on cystic fibrosis. I have MONDO:0009061 and NCBIGene:1080 (CFTR) saved in ids.txt. Can you query ARAX for a path Disease -> ? -> Gene through one intermediate node, with both ends pinned? Write the output to ./arax_cf_run1, and then show me which sources (primary and aggregator) each edge came from and whether publications were returned."*
- *"I want to see what the Translator ARAX service and a couple of specific providers, say RTX-KG2 and one other that I'll pick, each say about relationships of a known gene, side by side, without it guessing for me. How should we do that?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill ncats-arax

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills ncats-arax
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `scientific-databases` category with `/plugin install scientific-databases@research-agent-skills`.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/ncats-arax/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
