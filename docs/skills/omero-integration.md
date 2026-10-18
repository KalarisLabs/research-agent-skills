---
title: "omero-integration — AI agent skill for lab automation"
description: "Securely inspect and automate microscopy data workflows against OMERO.server with omero-py, BlitzGateway, OMERO CLI, tables, annotations, ROIs, rendering, and…"
keywords: ["microscopy", "image data management", "OMERO", "bioimaging"]
---

# `omero-integration`

**Category:** [lab-automation](/skills#lab-automation) · **License:** MIT · **Version:** 1.4 · **Includes scripts**

**Tags:** microscopy, image data management, OMERO, bioimaging

## When to use it

Securely inspect and automate microscopy data workflows against OMERO.server with omero-py, BlitzGateway, OMERO CLI, tables, annotations, ROIs, rendering, and documented OMERO.web APIs. Use for scoped OMERO inventory, metadata export, import/export planning, or reviewed write workflows.

## Example requests

Ask your agent in plain language, for example:

- *"List the datasets in my OMERO project 4512 and tell me how many images each has."*
- *"I need the key-value map annotations and ROI shapes for images 88101, 88102 and 88107 on omero.ourlab.edu (group 'Kessler_Lab') exported to JSON for a figure legend. My script keeps failing with 'Ice.ConnectionRefusedException' when I use port 4064. The server is 5.6.x and I'm on Python 3.13."*
- *"Our microscopy core stores a few hundred confocal stacks on a shared imaging server, and I want to move one finished screening plate's worth of images to a collaborator as OME-TIFFs without pulling in the rest of the group's unpublished data. How should I go about it?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill omero-integration

# Kalaris Labs installer with checksum verification
npx research-agent-skills install omero-integration
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `lab-automation` category with `/plugin install lab-automation@research-agent-skills`.

## Related

- [`labarchive-integration`](/skills/labarchive-integration)
- [Skills for biology and bioinformatics](/fields/biology)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/omero-integration/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
