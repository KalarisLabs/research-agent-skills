---
title: "audiocraft-audio-generation — AI agent skill for multimodal and emerging"
description: "PyTorch library for audio generation including text-to-music (MusicGen) and text-to-sound (AudioGen)."
keywords: ["Multimodal", "Audio Generation", "Text-to-Music", "Text-to-Audio", "MusicGen"]
---

# `audiocraft-audio-generation`

**Category:** [multimodal-and-emerging](/skills#multimodal-and-emerging) · **License:** MIT · **Version:** 1.0.0

**Tags:** Multimodal, Audio Generation, Text-to-Music, Text-to-Audio, MusicGen

## When to use it

PyTorch library for audio generation including text-to-music (MusicGen) and text-to-sound (AudioGen). Use when you need to generate music from text descriptions, create sound effects, or perform melody-conditioned music generation.

## Example requests

Ask your agent in plain language, for example:

- *"I need a 15 second lo-fi hip hop clip with mellow piano and vinyl crackle. What's the quickest way to get that going locally?"*
- *"I'm getting CUDA out of memory when I run MusicGen.get_pretrained('facebook/musicgen-large') with duration=30 on my 8GB RTX 3070 in generate_music.py. How do I fix this? I still want batches of different prompts for a user study stimulus set."*
- *"For a perception experiment I need a set of short ambient clips, such as dog barking, rain on a window and a door slamming, all generated from written descriptions. I also have a reference 10 s humming recording that I want one of the music clips to follow. How should I set this up?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill audiocraft-audio-generation

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills audiocraft-audio-generation
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `multimodal-and-emerging` category with `/plugin install multimodal-and-emerging@research-agent-skills`.

## Related

- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/audiocraft-audio-generation/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
