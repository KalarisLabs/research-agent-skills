---
title: "simpy — AI agent skill for data science and ml"
description: "Builds, tests, and analyzes bounded process-based discrete-event simulations in Python with SimPy 4.1.2: Environment, Timeout, Process, AnyOf/AllOf…"
keywords: ["discrete-event simulation", "simulation", "queueing", "operations research"]
---

# `simpy`

**Category:** [data-science-and-ml](/skills#data-science-and-ml) · **License:** MIT · **Version:** 1.4 · **Includes scripts**

**Tags:** discrete-event simulation, simulation, queueing, operations research

## When to use it

Builds, tests, and analyzes bounded process-based discrete-event simulations in Python with SimPy 4.1.2: Environment, Timeout, Process, AnyOf/AllOf conditions, interrupts, Resource, PriorityResource, PreemptiveResource, Container, Store, time-weighted monitoring, and replication-based output analysis, plus bundled safe CLIs. Use when modeling queues, production lines, logistics, or service operations with generator processes; when contending entities need shared resources or preemption; when instrumenting queue length or utilization correctly; when running independent replications with seeds and confidence intervals; when debugging event ordering or run(until=) boundaries. Not for continuous-time ODE or agent-based modeling frameworks.

## Example requests

Ask your agent in plain language, for example:

- *"How do I make a SimPy process wait for either a timeout or a resource request, whichever comes first?"*
- *"My clinic model in clinic_sim.py has 3 nurses as a simpy.Resource and I log len(res.queue) each time a patient arrives, then take the mean. The mean queue length comes out far lower than the M/M/3 formula gives. I also run it with env.run(until=480). What's wrong, and how do I measure it properly? I'd like a CI over 30 seeds too."*
- *"I'm studying a two-stage production line where machines break down and a repair technician has to stop whatever job is running. I need to estimate throughput and how long parts spend in the system, and I want to be able to trust the numbers. How should I build and analyze this?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill simpy

# Kalaris Labs installer with checksum verification
npx research-agent-skills install simpy
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `data-science-and-ml` category with `/plugin install data-science-and-ml@research-agent-skills`.

## Related

- [Skills for machine learning research](/fields/machine-learning)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/simpy/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
