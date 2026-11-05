---
title: "protocolsio-integration — AI agent skill for lab automation"
description: "Reads, validates, and exports protocols.io data using the documented REST v3/v4 endpoints and the official MCP endpoint, and builds non-executing mutation…"
keywords: ["protocols.io", "lab protocols", "reproducibility", "methods"]
---

# `protocolsio-integration`

**Category:** [lab-automation](/skills#lab-automation) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** protocols.io, lab protocols, reproducibility, methods

## When to use it

Reads, validates, and exports protocols.io data using the documented REST v3/v4 endpoints and the official MCP endpoint, and builds non-executing mutation plans. The bundled client makes bounded GET requests to official hosts only with --execute, and also validates saved protocol JSON offline for step order, version, DOI, and attribution metadata. Use when fetching a protocol, its steps, materials, or PDF from protocols.io by exact version. Use when validating a saved protocol snapshot for provenance before reuse. Use when planning a protocol create, update, publish, upload, or organization export without running it. Use when checking protocols.io rate limits, pagination, or authentication. Do not use for other protocol repositories or general literature search.

## Example requests

Ask your agent in plain language, for example:

- *"Pull protocol 12345 from protocols.io, version 3, and give me the steps."*
- *"I saved a protocol export as snapshots/rna_extraction_v2.json from our lab's protocols.io page and want to reuse it in a methods section. Before I do, can you check that the step order is intact and the DOI, version and authors are all there? It's offline, don't hit the network."*
- *"We finished optimizing our cell-lysis method and I'd like it to go live with a citable identifier on the site we host it on. Can you just do that for me with my token?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill protocolsio-integration

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills protocolsio-integration
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `lab-automation` category with `/plugin install lab-automation@research-agent-skills`.

## Related

- [`cell-press`](/skills/cell-press)
- [`database-lookup`](/skills/database-lookup)
- [`opentrons-integration`](/skills/opentrons-integration)
- [`pymatgen`](/skills/pymatgen)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/protocolsio-integration/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
