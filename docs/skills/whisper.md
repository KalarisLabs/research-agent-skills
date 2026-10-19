---
title: "whisper — AI agent skill for multimodal and emerging"
description: "Transcribes and translates audio with OpenAI's Whisper (openai-whisper Python package and whisper CLI), covering model sizes from tiny to large plus turbo…"
keywords: ["Whisper", "Speech Recognition", "ASR", "Multimodal", "Multilingual", "OpenAI", "Speech-To-Text", "Transcription", "Translation", "Audio Processing"]
---

# `whisper`

**Category:** [multimodal-and-emerging](/skills#multimodal-and-emerging) · **License:** MIT · **Version:** 1.0.0

**Tags:** Whisper, Speech Recognition, ASR, Multimodal, Multilingual, OpenAI, Speech-To-Text, Transcription, Translation, Audio Processing

## When to use it

Transcribes and translates audio with OpenAI's Whisper (openai-whisper Python package and whisper CLI), covering model sizes from tiny to large plus turbo, language specification, initial prompts, word and segment timestamps, temperature fallback, batch processing, and subtitle generation. Use when transcribing speech, podcasts, meetings, or video audio to text. Use when translating non-English speech to English. Use when working with noisy or multilingual audio in any of 99 languages. Use when choosing a Whisper model size for available VRAM. Use when generating subtitles from audio. Not for speaker diarization or live captioning; use AssemblyAI or Deepgram instead.

## Example requests

Ask your agent in plain language, for example:

- *"What's the quickest way to transcribe an mp3 to text with Whisper on my laptop?"*
- *"I have 40 lecture recordings in ./lectures/*.m4a, mostly Spanish with some English code-switching, and a 8 GB GPU. I ran `whisper lec01.m4a --model large` and got CUDA out of memory. How should I process the whole folder and get .srt subtitles for each?"*
- *"I recorded about 20 field interviews in Swahili and Tagalog on a noisy phone recorder. I need English text versions I can quote in my paper. What should I do, and what should I watch out for?"*

## Install

```bash
# skills.sh (Claude Code, Codex, Cursor, Gemini CLI, Copilot and more)
npx skills add KalarisLabs/research-agent-skills --skill whisper

# GitHub CLI
gh skill install KalarisLabs/research-agent-skills whisper
```

In Claude Code you can also add the marketplace with `/plugin marketplace add KalarisLabs/research-agent-skills` and install the whole `multimodal-and-emerging` category with `/plugin install multimodal-and-emerging@research-agent-skills`.

## Related

- [Skills for AI research](/fields/artificial-intelligence)

## Full playbook

Read [SKILL.md](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/whisper/SKILL.md) for the complete workflow, references and any scripts. The agent installer copies the full skill folder.
