---
title: "creative-thinking-for-research — AI agent skill for ideation and design"
description: "Applies cognitive science frameworks for creative thinking to CS and AI research ideation."
keywords: ["Creative Thinking", "Research Ideation", "Analogical Reasoning", "Problem Reformulation", "Cognitive Science"]
---

# `creative-thinking-for-research`

**Category:** [ideation-and-design](/skills#ideation-and-design) · **License:** MIT · **Version:** 1.0.0

**Tags:** Creative Thinking, Research Ideation, Analogical Reasoning, Problem Reformulation, Cognitive Science

## When to use it

Applies cognitive science frameworks for creative thinking to CS and AI research ideation. Use when seeking genuinely novel research directions by leveraging combinatorial creativity, analogical reasoning, constraint manipulation, and other empirically grounded creative strategies.

## Example requests

Ask your agent in plain language, for example:

- *"Help me come up with a really new research angle on LLM test-time compute. I keep going in circles on the same ideas."*
- *"I'm working on KV-cache eviction for long-context transformers (my notes are in kv_cache_notes.md). Everything I find is a tweak on H2O or SnapKV. Can you help me find a structurally different idea by borrowing from another field, like immunology or database systems, and tell me how to tell whether the analogy is deep or just a surface metaphor?"*
- *"I'm prepping for a lab retreat. I want to list every hidden assumption in how we train vision-language models, including labeled pairs, fixed resolution and benchmark-driven evaluation. Then I want to work out which ones we could drop to open up a new kind of research."*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill creative-thinking-for-research

# Kalaris Labs installer with checksum verification
npx research-agent-skills install creative-thinking-for-research
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `ideation-and-design` category with `/plugin install ideation-and-design@research-agent-skills`.

## Related

- [`autoresearch`](/skills/autoresearch)
- [`brainstorming-research-ideas`](/skills/brainstorming-research-ideas)
- [`dhdna-profiler`](/skills/dhdna-profiler)
- [`science-aaas`](/skills/science-aaas)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/creative-thinking-for-research/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
