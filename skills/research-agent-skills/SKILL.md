---
name: research-agent-skills
description: Navigate and install the complete Research Agent Skills collection by Kalaris Labs for academia across AI, machine learning, biology, chemistry, medicine, physics, and academic writing. Use when a researcher wants the whole collection for Codex, Claude Code or Gemini CLI via skills.sh, needs to choose a field bundle, or asks which specialist SKILL.md files cover a cross-disciplinary research workflow. For a narrow task with a matching specialist skill already available, use that skill directly.
license: MIT
compatibility: The skill index works offline. Installing additional skills requires Node.js 18+ and access to the public GitHub repository.
metadata:
  version: '1.0'
  category: research-automation
  maintainer: Kalaris Labs
  tags: academia, research agents, scientific research, academic writing, skill collection, AI, machine learning, biology, chemistry, medicine, physics
---

# Research Agent Skills by Kalaris Labs

This is the collection entry for the specialist research skills in
`KalarisLabs/research-agent-skills`. It helps an agent choose the right skill for
a research task and provides the full collection installation path.

## Choose a skill

1. Identify the research deliverable and domain. Examples include a literature
   review in medicine, an ML experiment, a chemistry analysis, or a physics figure.
2. Read only the relevant section of [the bundled skill index](references/catalog.md).
   Select the smallest set of specialist skills that covers the task.
3. If those skills are already installed, read their `SKILL.md` files and follow
   their procedures. If they are not installed, give the researcher the exact
   install command or install them when they asked you to set up skills.
4. Keep claims and citations tied to checked sources. A skill's presence does
   not establish that an analysis or scientific claim is correct.

Use the specialist skill directly for ordinary single-domain work. This entry
is useful when the request spans skills or concerns collection setup.

Before installing, check:

- [ ] Which agent harness and scope (project or global) does the researcher want?
- [ ] Did they ask for the full collection or a focused field bundle?
- [ ] Are the selected specialist folders already installed?

## Install from skills.sh

To browse every individual skill without installing:

```sh
npx skills add KalarisLabs/research-agent-skills --list
```

To install one specialist into the current project for a chosen agent:

```sh
npx skills add KalarisLabs/research-agent-skills --skill citation-verification --agent codex --yes
```

To install the complete collection into the current project for one agent:

```sh
npx skills add KalarisLabs/research-agent-skills --skill '*' --agent codex --yes
```

Replace `codex` with the researcher's agent. Add `--global` for user-wide
installation. The full install places each specialist skill in its own folder;
this collection entry alone is an index and router, not a copy of every
specialist's scripts and references. A full install can add substantial context
to an agent, so choose it when the researcher wants the entire collection.

## Verify the handoff

After installation, verify the selected skill folders contain `SKILL.md` and
that the chosen agent can read them. For a full install, compare the installed
count with `npx skills add KalarisLabs/research-agent-skills --list` before
claiming the collection is complete. Never fabricate a successful install or
claim a directory page is live based only on CLI discovery.

The repository's own installer also provides focused audience bundles:
`research-essentials`, `ml-research`, `ai-research`, `biology-research`,
`chemistry-research`, `medicine-research`, and `physics-research`.

```sh
npx research-agent-skills install --bundle biology-research --project
```

See the [repository](https://github.com/KalarisLabs/research-agent-skills) for
current installation options and each skill's supporting files.
