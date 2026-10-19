---
title: "matlab — AI agent skill for data science and ml"
description: "Designs, reviews, and migrates MATLAB R2026a and GNU Octave numerical code, covering functions with arguments blocks, arrays and indexing, tables and…"
keywords: ["MATLAB", "GNU Octave", "numerical computing", "scientific computing"]
---

# `matlab`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** MIT · **Version:** 1.2 · **Includes scripts**

**Tags:** MATLAB, GNU Octave, numerical computing, scientific computing

## When to use it

Designs, reviews, and migrates MATLAB R2026a and GNU Octave numerical code, covering functions with arguments blocks, arrays and indexing, tables and timetables, matlab.unittest tests, MATLAB Projects, exportgraphics figures, MAT file inventory, and MATLAB-Python interoperability. Includes static helper scripts that scan .m files, plan argv commands, and hash artifacts without executing anything. Use when writing or reviewing .m code, migrating code between MATLAB releases or to Octave, setting up reproducible tests and projects, inspecting an untrusted MAT or .mlx file safely, or checking Python Engine compatibility. Do not use for pure Python numerical work with NumPy or SciPy.

## Example requests

Ask your agent in plain language, for example:

- *"Can you review this .m function before I send it to my lab? It uses inv(A)*b and a for loop that grows an array."*
- *"I'm porting our lab's spectral analysis from MATLAB R2022b to run on GNU Octave 11 on a Linux cluster. The code uses `arguments` blocks, a `timetable` of sensor readings loaded from sensors.csv with readtable, and `exportgraphics` for figures. Running it gives 'parse error near line 12'. What will break and how do I fix it?"*
- *"A collaborator emailed me a results.mat file from an unknown source and I need to see what variables are inside. I'd rather not just double-click it in MATLAB. How should I go about it?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill matlab

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills matlab
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/matlab/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
