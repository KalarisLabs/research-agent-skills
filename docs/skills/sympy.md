---
title: "sympy — AI agent skill for data science and ml"
description: "Use when you need exact symbolic math in Python — algebra, calculus, equation solving, symbolic linear algebra, or code generation via lambdify/LaTeX."
keywords: ["symbolic math", "computer algebra", "calculus", "mathematics", "Python"]
---

# `sympy`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** https://github.com/sympy/sympy/blob/master/LICENSE · **Version:** 1.3

**Tags:** symbolic math, computer algebra, calculus, mathematics, Python

## When to use it

Use when you need exact symbolic math in Python — algebra, calculus, equation solving, symbolic linear algebra, or code generation via lambdify/LaTeX. Prefer NumPy or SciPy when floating-point approximations are sufficient.

## Example requests

Ask your agent in plain language, for example:

- *"what's the closed-form integral of x**2 * exp(-x) from 0 to infinity? want the exact answer, not a decimal"*
- *"I'm getting `NameError: name 'theta' is not defined` in my script derive_pendulum.py where I'm trying to take the Jacobian of a Lagrangian with sympy and then print it as LaTeX for my paper's appendix. Can you fix it and give me the LaTeX for the 2x2 Jacobian?"*
- *"I have a 3x3 matrix with an unknown parameter a in it, and I need to know for which values of a the matrix becomes singular, plus the eigenvalues as functions of a, all in exact form so I can put them in my derivation."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill sympy

# Kalaris Labs installer with checksum verification
npx research-agent-skills install sympy
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/sympy/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
