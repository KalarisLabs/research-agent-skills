---
title: Quickstart | Install your first research agent skill
description: Install one Kalaris Labs skill with skills.sh, try a citation-checking task, then find skills for your academic field.
keywords: [quickstart, install agent skills, citation verification, academic research]
---

# Quickstart: use your first research skill

Start with one task and one skill. You can add more after you see how your agent uses it.

<Steps>
  <Step title="Install citation verification">
    In a project with a bibliography, run:

    ```bash
    npx skills add KalarisLabs/research-agent-skills --skill citation-verification
    ```

    The skills.sh installer lets you select an agent harness. It installs into this project by default;
    use `--global` if you want the skill available across projects. Restart your agent if it was open
    during installation.
  </Step>
  <Step title="Try a real research task">
    Open your agent in the project and ask:

    > Verify every reference in `refs.bib`. Separate confirmed, mismatched and unverified entries,
    > and show the scholarly record used for each decision.

    Replace `refs.bib` with your own reference file. Check the cited records before using the
    result in a manuscript; a missing match is not proof that a paper does not exist.
  </Step>
  <Step title="Add skills for your field">
    List every available skill, then pick another one that matches your next task:

    ```bash
    npx skills add KalarisLabs/research-agent-skills --list
    ```

    See [skills by discipline](/guides/by-field) for starting points in ML, AI, biology, chemistry,
    medicine and physics, or [browse all 281 skills](/skills).
  </Step>
</Steps>

## More first tasks

| Your next task | Skill to install | Example request |
|---|---|---|
| Revise academic prose | [`unslop-academic-writing`](/skills/unslop-academic-writing) | “Revise this introduction in my voice without changing its claims.” |
| Draft from results | [`scientific-writing`](/skills/scientific-writing) | “Draft Results from `results/` and the figures in `figs/`; mark any missing evidence.” |
| Plan a systematic review | [`systematic-review-prisma`](/skills/systematic-review-prisma) | “Draft a PRISMA 2020 protocol and screening plan for this question.” |
| Prepare a preprint | [`arxiv-submission`](/skills/arxiv-submission) | “Check this LaTeX folder for arXiv submission problems.” |

The agent normally selects a skill from your task. You can name the skill when you want to be explicit.
For installation scope, harness support and other methods, see the [installation guide](/getting-started/installation).
