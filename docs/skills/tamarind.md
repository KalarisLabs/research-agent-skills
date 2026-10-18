---
title: "tamarind — AI agent skill for chemistry and drug discovery"
description: "Access a collection of open-source molecular design and structural biology tools on the Tamarind Bio platform, via its REST API or MCP server — no local GPUs…"
keywords: ["protein structure prediction", "molecular design", "structural biology", "drug discovery"]
---

# `tamarind`

**Category:** [chemistry-and-drug-discovery](/skills#chemistry-and-drug-discovery) · **License:** MIT · **Version:** 1.1

**Tags:** protein structure prediction, molecular design, structural biology, drug discovery

## When to use it

Access a collection of open-source molecular design and structural biology tools on the Tamarind Bio platform, via its REST API or MCP server — no local GPUs required. Tamarind bundles popular open-source models for structure prediction (AlphaFold, Boltz, Chai, ESMFold), protein, binder, and de novo design (RFdiffusion, ProteinMPNN, BoltzGen), antibody and nanobody design and developability, protein-ligand docking (DiffDock, Autodock Vina), binding-affinity prediction, MSA generation, and molecular dynamics. Use when the user mentions Tamarind or tamarind.bio, wants to run any of these open-source tools in the cloud, references app.tamarind.bio/api or the x-api-key header, or needs to submit batches of sequences for structural or biophysical characterization.

## Example requests

Ask your agent in plain language, for example:

- *"How do I run Boltz-2 on Tamarind for a protein-ligand complex?"*
- *"I have 240 candidate binder sequences in designs.csv, column 'seq', and I need to fold them all against my target and get confidence scores. I'm on a laptop with no GPU. I'm using the app.tamarind.bio API and got a 403 on my first submit-job call. What should I do?"*
- *"I want to design a small protein that binds my target's epitope, then check that the designs fold as intended. I don't have any GPUs. What's a practical cloud pipeline for this?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill tamarind

# Kalaris Labs installer with checksum verification
npx research-agent-skills install tamarind
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `chemistry-and-drug-discovery` category with `/plugin install chemistry-and-drug-discovery@research-agent-skills`.

## Related

- [Skills for chemistry and drug discovery](/fields/chemistry)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/tamarind/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
