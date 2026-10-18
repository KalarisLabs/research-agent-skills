---
title: "adaptyv — AI agent skill for chemistry and drug discovery"
description: "How to use the Adaptyv Bio Foundry API and Python SDK for protein experiment design, submission, and results retrieval."
keywords: ["protein engineering", "binding assays", "protein screening", "lab automation", "drug discovery"]
---

# `adaptyv`

**Category:** [chemistry-and-drug-discovery](/skills#chemistry-and-drug-discovery) · **License:** MIT · **Version:** 1.3

**Tags:** protein engineering, binding assays, protein screening, lab automation, drug discovery

## When to use it

How to use the Adaptyv Bio Foundry API and Python SDK for protein experiment design, submission, and results retrieval. Use this skill whenever the user mentions Adaptyv, Foundry API, protein binding assays, protein screening experiments, BLI/SPR assays, thermostability assays, or wants to submit protein sequences for experimental characterization. Also trigger when code imports `adaptyv`, `adaptyv_sdk`, or `FoundryClient`, or references `foundry-api-public.adaptyvbio.com`.

## Example requests

Ask your agent in plain language, for example:

- *"How do I submit a few sequences to a cloud lab to see if they bind my target? I'm using the Python SDK."*
- *"I have binders.fasta with 48 designed nanobody sequences. I want KD values against my target using SPR, and I want the quote auto-accepted so nothing waits on me. My script has `from adaptyv_sdk import FoundryClient` and it's returning a 401. Can you fix the script and set up a webhook so I get notified on status changes?"*
- *"I've designed 200 miniprotein binders computationally and want real wet-lab data on which ones actually express and how stable they are. Is there an automated lab service with an API where I can send the sequences and get melting temperatures and yields back, and how would I script that and poll for results?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill adaptyv

# Kalaris Labs installer with checksum verification
npx research-agent-skills install adaptyv
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `chemistry-and-drug-discovery` category with `/plugin install chemistry-and-drug-discovery@research-agent-skills`.

## Related

- [`ginkgo-cloud-lab`](/skills/ginkgo-cloud-lab)
- [Skills for chemistry and drug discovery](/fields/chemistry)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/adaptyv/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
