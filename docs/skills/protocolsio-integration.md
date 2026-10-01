---
title: "protocolsio-integration — AI agent skill for lab automation"
description: "Reads, validates, and exports protocols.io data using the documented REST v3/v4 endpoints and the official MCP endpoint, and builds non-executing mutation…"
---

# `protocolsio-integration`

> Reads, validates, and exports protocols.io data using the documented REST v3/v4 endpoints and the official MCP endpoint, and builds non-executing mutation plans. The bundled client makes bounded GET requests to official hosts only with --execute, and also validates saved protocol JSON offline for step order, version, DOI, and attribution metadata. Use when fetching a protocol, its steps, materials, or PDF from protocols.io by exact version. Use when validating a saved protocol snapshot for provenance before reuse. Use when planning a protocol create, update, publish, upload, or organization export without running it. Use when checking protocols.io rate limits, pagination, or authentication. Do not use for other protocol repositories or general literature search.

**Category:** [lab-automation](/skills#lab-automation) · **License:** MIT · **Version:** 1.2

## Install

```bash
npx research-agent-skills install protocolsio-integration
npx skills add KalarisLabs/research-agent-skills --skill protocolsio-integration
```

## When to use it

Reads, validates, and exports protocols.io data using the documented REST v3/v4 endpoints and the official MCP endpoint, and builds non-executing mutation plans. The bundled client makes bounded GET requests to official hosts only with --execute, and also validates saved protocol JSON offline for step order, version, DOI, and attribution metadata. Use when fetching a protocol, its steps, materials, or PDF from protocols.io by exact version. Use when validating a saved protocol snapshot for provenance before reuse. Use when planning a protocol create, update, publish, upload, or organization export without running it. Use when checking protocols.io rate limits, pagination, or authentication. Do not use for other protocol repositories or general literature search.

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/protocolsio-integration/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
