# CLAUDE.md

See [AGENTS.md](AGENTS.md) for repository layout, commands and rules. The same instructions apply to Claude Code.

This repository is also a Claude Code plugin marketplace: `/plugin marketplace add ./` loads it locally for testing.

## graphify

This project uses a local knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- When graphify-out/graph.json exists, run `graphify query "<question>"` before your first grep, search or source-file read for a codebase question, and put this rule in every subagent prompt that explores code. Read raw files only for lines the graph or an earlier read already located. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
- graphify-out/ and the graphify project skill are git-ignored. Set up once per clone: `uv tool install graphifyy && graphify install --project && graphify update .` (about a minute, AST-only, no API cost).
