---
title: Benchmarks and skill quality | Research Agent Skills
description: How research agent skills are evaluated, covering the static quality rubric, trigger-routing benchmark, with-vs-without-skill task outcomes, citation verification precision and recall, and the no-slop writing benchmark.
---

We evaluate whether a skill is clear, selected for the right requests, and improves the resulting work.

| Check | What it measures | Command |
|---|---|---|
| Static quality | Structure, triggers, workflow detail, examples and references | `uv run tools/skill_quality.py` |
| Trigger routing | Whether the right skill appears for a task and stays out of near misses | `uv run tools/trigger_bench.py` |
| Task outcomes | Blind comparison of answers with and without a skill | `benchmarks/task_evals/run.py` |
| Domain checks | Citation verification and writing revision behavior | `benchmarks/citation_verification/`, `benchmarks/slop/` |

See the [benchmark methodology and current results](https://github.com/KalarisLabs/research-agent-skills/blob/main/benchmarks/README.md).
The model based results are pilot measurements; read their sample sizes before citing them.
