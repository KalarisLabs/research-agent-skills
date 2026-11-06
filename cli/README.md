# research-agent-skills

[![GitHub stars](https://img.shields.io/github/stars/KalarisLabs/research-agent-skills?style=social)](https://github.com/KalarisLabs/research-agent-skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/KalarisLabs/research-agent-skills/blob/main/LICENSE)

One-command installer for **[Research Agent Skills](https://github.com/KalarisLabs/research-agent-skills)**:
280+ agent skills for academia, scientific research, research paper writing, journal formatting and literature review,
with auto-detection and zero-configuration support for Claude Science, Open Science, T3 Code, Google Antigravity, Claude Code, Cursor, Codex, OpenHands, Aider, Goose, Windsurf and 10+ more harnesses.

> **Not published to npm.** Install the skills with skills.sh instead:
> `npx skills add KalarisLabs/research-agent-skills` (see the
> [main README](https://github.com/KalarisLabs/research-agent-skills#install)).
> To use this installer, build it from source: `cd cli && npm ci && npm run build && node dist/bin.js --help`.
> The commands below assume a future npm release.

```bash
npx research-agent-skills                        # interactive
npx research-agent-skills install                # research-essentials bundle for detected agents
npx research-agent-skills install --configure    # install and auto-configure instruction anchors
npx research-agent-skills configure              # auto-configure anchors (AGENTS.md, CLAUDE.md, etc.)
npx research-agent-skills install citation-verification nature-portfolio
npx research-agent-skills install --category literature-review --harness claude-science,t3-code --project
npx research-agent-skills install --bundle medicine-research --project
npx research-agent-skills list --categories
npx research-agent-skills search "systematic review"
npx research-agent-skills installed | update | uninstall <skills|--all> | doctor
```

Installation defaults to global user directories. Add `--project` for the current project.
The interactive command lets you select skills and harnesses. Curated bundles cover ML, AI, biology,
chemistry, medicine and physics in addition to cross-disciplinary research essentials.

## What researchers use it for

| Task | Skills |
|---|---|
| Catch hallucinated references before submission | `citation-verification` (Crossref, OpenAlex, arXiv) |
| Remove AI-sounding prose from a manuscript | `unslop-academic-writing` |
| Draft and format a paper for a journal or venue | `scientific-writing`, `ml-paper-writing`, `nature-portfolio`, `apa7` |
| Run a PRISMA systematic review | `systematic-review-prisma`, `literature-review` |
| Answer reviewers | `rebuttal-and-response-to-reviewers`, `cover-letter-to-editor` |
| Analyze data in your field | `scanpy`, `rdkit`, `astropy`, `pydeseq2`, `pymatgen` and 200+ more |

Browse every skill in the [documentation](https://docs.kalarislabs.com/research-agent-skills) or on
[skills.sh](https://skills.sh/kalarislabs/research-agent-skills).

## Security

- Downloads a pinned GitHub release and verifies its SHA-256 against the release `SHA256SUMS` before extracting.
- Safe extraction: rejects links, absolute paths and `..`. Never deletes folders it did not install.
- Records per-file hashes; `doctor` reports modified or missing files.
- Zero runtime dependencies. No telemetry. Node.js 18.17+.

Created by Sayan Chowdhury · [Kalaris Labs](https://kalarislabs.com) · MIT License
