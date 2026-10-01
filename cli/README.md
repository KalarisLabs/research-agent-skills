# research-agent-skills

One-command installer for **[Research Agent Skills](https://github.com/KalarisLabs/research-agent-skills)**:
280+ agent skills for academia, scientific research, research paper writing, journal formatting and literature review,
for Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot, OpenCode and Windsurf.

```bash
npx research-agent-skills                       # interactive
npx research-agent-skills install               # research-essentials bundle for detected agents
npx research-agent-skills install citation-verification nature-portfolio
npx research-agent-skills install --category literature-review --harness claude-code,codex --project
npx research-agent-skills install --bundle medicine-research --project
npx research-agent-skills list --categories
npx research-agent-skills search "systematic review"
npx research-agent-skills installed | update | uninstall <skills|--all> | doctor
```

Installation defaults to global user directories. Add `--project` for the current project.
The interactive command lets you select skills and harnesses. Curated bundles cover ML, AI, biology,
chemistry, medicine and physics in addition to cross-disciplinary research essentials.

- Downloads a pinned GitHub release and verifies its SHA-256 against the release `SHA256SUMS` before extracting.
- Safe extraction: rejects links, absolute paths and `..`. Never deletes folders it did not install.
- Records per-file hashes; `doctor` reports modified or missing files.
- Zero runtime dependencies. No telemetry. Node.js 18.17+.

Created by Sayan Chowdhury · Kalaris Labs · MIT License
