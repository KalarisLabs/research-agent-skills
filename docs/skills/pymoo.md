---
title: "pymoo — AI agent skill for data science and ml"
description: "Solves single- and multi-objective optimization problems in Python with pymoo, using NSGA-II, NSGA-III, MOEA/D, SPEA2, RVEA, GA, DE and PSO."
keywords: ["multi-objective optimization", "evolutionary algorithms", "NSGA-II", "optimization"]
---

# `pymoo`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** Apache-2.0 license · **Version:** 1.4 · **Includes scripts**

**Tags:** multi-objective optimization, evolutionary algorithms, NSGA-II, optimization

## When to use it

Solves single- and multi-objective optimization problems in Python with pymoo, using NSGA-II, NSGA-III, MOEA/D, SPEA2, RVEA, GA, DE and PSO. Covers custom problems (Problem, ElementwiseProblem, FunctionalProblem), constraint handling, mixed-variable problems, ZDT/DTLZ/WFG benchmarks, genetic operators, parallel evaluation, Pareto front visualization and multi-criteria decision making. Use when finding Pareto-optimal trade-offs between conflicting objectives. Use when defining a constrained or mixed-variable problem and choosing an evolutionary algorithm. Use when benchmarking algorithms on standard test problems. Use when customizing crossover or mutation operators. Use when picking one solution from a Pareto front. Not for gradient-based or convex solvers.

## Example requests

Ask your agent in plain language, for example:

- *"How do I get the Pareto front for two conflicting objectives in Python?"*
- *"I'm designing a truss in truss_opt.py. It has 3 variables: a continuous beam thickness, an integer number of struts, and a categorical material (steel, aluminum, titanium). I'm minimizing mass and deflection. Stress must stay under 250 MPa and the deflection limit is a hard constraint. My NSGA-II run keeps crashing with 'ValueError: could not convert string to float' when the material gets sampled. How should I set this up?"*
- *"I have a simulation of a bioreactor with 5 competing goals: yield, cost, energy use, waste and run time. I want a spread of good trade-off designs. Then I need to pick a single recipe to run in the lab, and I care most about yield. How should I go about this?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill pymoo

# Kalaris Labs installer with checksum verification
npx research-agent-skills install pymoo
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/pymoo/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
