# Listings and backlinks tracker (maintainers)

Where Research Agent Skills is listed, where it is pending, and ready-to-paste submission text.
Follow each list's rules exactly and submit one entry per list. Re-check this table monthly.

Audit date: 2026-10-19. Repository created 2026-07-07; 28 stars at audit time.

## Live

| Where | URL | Notes |
|---|---|---|
| GitHub | https://github.com/KalarisLabs/research-agent-skills | 20 topics set (GitHub's maximum) |
| Documentation (Mintlify) | https://docs.kalarislabs.com/research-agent-skills | Sitemap at `https://docs.kalarislabs.com/sitemap.xml`; per-page OG images are automatic |
| skills.sh | https://skills.sh/kalarislabs/research-agent-skills | 281 skills, 3.5K installs (2026-10-19). Per-skill counts: `catalog/installs.json`. Groupings come from `skills.sh.json` |
| Skills Directory | https://www.skillsdirectory.com/authors/kalarislabs | 283 skill pages, security grade A (96/100), each links back to its `SKILL.md` |
| SkillsMP | https://skillsmp.com | Crawls public GitHub `SKILL.md` files automatically; no submission |
| Claude Code plugin marketplace | `/plugin marketplace add KalarisLabs/research-agent-skills` | Aggregators such as claudemarketplaces.com crawl `.claude-plugin/marketplace.json` |

## Pull requests (open from the maintainer account)

| List | Stars | Section | Rules | Status |
|---|---|---|---|---|
| [InternScience/Awesome-Scientific-Skills](https://github.com/InternScience/Awesome-Scientific-Skills) | 569 | Skill Sources → Science-Specific → Specialized Domain Tools | Table row; PR note on why it helps science | [PR #20](https://github.com/InternScience/Awesome-Scientific-Skills/pull/20) open (2026-10-19) |
| [BehiSecc/awesome-claude-skills](https://github.com/BehiSecc/awesome-claude-skills) | 10K | Scientific & Research Tools | Fork, edit, PR | [PR #986](https://github.com/BehiSecc/awesome-claude-skills/pull/986) open (2026-10-19) |
| [heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills) | 6K | Community Skills → Skill Collections | ≥20 stars, >14 days old, README.md only, one additive line, title `Add owner/repo to <Category>`, agents must disclose | [PR #603](https://github.com/heilcheng/awesome-agent-skills/pull/603) open (2026-10-19); merged in weekly batches |
| [gmh5225/awesome-skills](https://github.com/gmh5225/awesome-skills) | 94 | Community Skills → Scientific & Research | Table row; merges several PRs a week | Branch `add-research-agent-skills` pushed to the fork; PR not opened yet |
| [junminhong/awesome-agent-skills](https://github.com/junminhong/awesome-agent-skills) | 18 | Skill Collections | Links only; edit `README.md` and `README_ZH.md` together; no counts in descriptions; every commit Verified; disclose affiliation | Ready to submit (entry text below) |
| [karanb192/awesome-claude-skills](https://github.com/karanb192/awesome-claude-skills) | 553 | Writing & Research | One skill per PR, alphabetical, under 150 characters, PR template, title `Add [skill] to [category]` | Ready to submit (`citation-verification`) |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 77K | Data & Analysis | Alphabetical, `*By [@owner]*` suffix; large review backlog | Ready to submit (`citation-verification`) |
| [JackyST0/awesome-agent-skills](https://github.com/JackyST0/awesome-agent-skills) | 650 | Skills Collections | Community entries need 64+ stars | Wait for 64 stars |
| [BioTender-max/awesome-bio-agent-skills](https://github.com/BioTender-max/awesome-bio-agent-skills) | 200 | Sources | Aggregated index, no pushes since 2026-07 | Skip unless it becomes active again |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 36K | Community Skills → AI and Data | One skill per entry, author prefix, ≤10-word description, needs "community-adopted, proven" skills | Deferred until `citation-verification` has clear adoption |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | 15K | Community Skills → Collections & Libraries | ≥10 stars; **PRs must not be AI-generated or AI-submitted** | Human-only: write and submit the PR yourself |

Entry text:

- InternScience: `| [KalarisLabs/research-agent-skills](https://github.com/KalarisLabs/research-agent-skills) | 28 | 280+ research skills: paper and thesis writing, journal formats, PRISMA reviews, citation verification, and ML, biology, chemistry, medicine and physics analysis |`
- BehiSecc: `- [research-agent-skills](https://github.com/KalarisLabs/research-agent-skills) - 280+ skills for academic writing, journal formatting, systematic reviews, citation verification and scientific data analysis.`
- travisvn: `- **[KalarisLabs/research-agent-skills](https://github.com/KalarisLabs/research-agent-skills)** - 280+ skills for academic research: paper writing, journal formats, PRISMA reviews, citation verification and field-specific analysis.`
- heilcheng: `- [KalarisLabs/research-agent-skills](https://github.com/KalarisLabs/research-agent-skills) - 280+ skills for academic writing, systematic reviews and scientific analysis`
- gmh5225: `| [research-agent-skills](https://github.com/KalarisLabs/research-agent-skills) | 280+ research skills: paper writing, journal formats, PRISMA reviews, citation checks against Crossref/OpenAlex/arXiv, and biology, chemistry, physics and ML analysis |`
- junminhong (EN): `` - [Research Agent Skills](https://github.com/KalarisLabs/research-agent-skills) — Guides agents through academic writing, journal formatting, systematic reviews, reference checks against Crossref, OpenAlex and arXiv, and field-specific scientific data analysis. `Type: Collection` · `Platforms: Cross-platform` ``
- junminhong (ZH, `README_ZH.md`): `` - [Research Agent Skills](https://github.com/KalarisLabs/research-agent-skills) — 引導 Agent 執行學術寫作、期刊格式排版、系統性文獻回顧、以 Crossref、OpenAlex 與 arXiv 核對參考文獻，以及各領域的科學資料分析。 `Type: Collection` · `Platforms: Cross-platform` ``
- karanb192: `| [citation-verification](https://github.com/KalarisLabs/research-agent-skills/tree/main/skills/citation-verification) | Check every reference in a .bib file against Crossref, OpenAlex and arXiv and flag fabricated or mismatched citations. |`
- ComposioHQ: `- [citation-verification](https://github.com/KalarisLabs/research-agent-skills/tree/main/skills/citation-verification) - Checks every reference in a manuscript or .bib file against Crossref, OpenAlex and arXiv, flagging fabricated citations, DOIs that point to the wrong paper, and wrong years or authors. *By [@KalarisLabs](https://github.com/KalarisLabs)*`
- VoltAgent: `- **[kalarislabs/citation-verification](https://github.com/KalarisLabs/research-agent-skills/tree/main/skills/citation-verification)** - Checks references against Crossref, OpenAlex and arXiv`

## Human-only submissions (maintainer, in a browser)

### hesreallyhim/awesome-claude-code (56K stars)

Recommendations must be made by a person through the repository's web issue form. PRs and `gh` submissions are
rejected. Open https://github.com/hesreallyhim/awesome-claude-code/issues/new/choose and pick the resource
recommendation form. Suggested answers:

- **Name:** Research Agent Skills
- **Link:** https://github.com/KalarisLabs/research-agent-skills
- **Category:** Agent Skills
- **Description:** 280+ Agent Skills for academic research in Claude Code. Highlights: `citation-verification`
  checks every reference against Crossref, OpenAlex and arXiv; `unslop-academic-writing` lints and rewrites
  AI-sounding prose; journal skills read current author guidelines before formatting. Installs as a Claude Code
  plugin marketplace with field bundles (`/plugin install research-essentials@research-agent-skills`).

### Web directories

| Directory | Submit at | What to enter |
|---|---|---|
| claudeskills.info | https://claudeskills.info/submit/ | Repo URL; short description below; category Research |
| MCP Market (skills) | https://mcpmarket.com/submit | Repo URL; short description below |
| LobeHub skills | https://market.lobehub.com/s/skills | Repo URL |
| agentskill.work | site submit page | Repo URL |
| Research Software Directory | https://research-software-directory.org | After the Zenodo DOI exists |

Short description (≤160 characters):
`Open-source AI agent skills for academic writing, systematic reviews, citation verification and scientific data analysis. Claude Code, Codex, Cursor, Gemini CLI.`

## Academic indexing

- [ ] Zenodo: sign in with GitHub at https://zenodo.org/account/settings/github/, switch on
  `KalarisLabs/research-agent-skills`, then publish the next release. `.zenodo.json` supplies the metadata.
  Add the DOI to `CITATION.cff` (`identifiers`) and a DOI badge to the README.
- [ ] Google Search Console: verify `docs.kalarislabs.com` and submit `https://docs.kalarislabs.com/sitemap.xml`.
- [ ] JOSS: once benchmarks are run at scale (needs `paper.md`).

## Launch posts (post from personal accounts)

Lead with the measurable result, not adjectives. Follow each community's self-promotion rules.

**Show HN title:** `Show HN: Agent skills that check every citation against Crossref before you submit`

**Show HN text:**
> AI assistants are good at drafting papers and bad at references. We built 280+ open-source Agent Skills for
> research work. The one we use most, citation-verification, checks each entry in a .bib file against Crossref,
> OpenAlex and arXiv and flags fabricated or mismatched references; on our labeled benchmark it caught every
> fabricated and corrupted reference and passed every correct one. Other skills cover PRISMA systematic reviews,
> journal formatting from current author guidelines, and analysis packages for biology, chemistry, medicine,
> physics and ML. MIT licensed; works in Claude Code, Codex, Cursor and Gemini CLI.
> https://github.com/KalarisLabs/research-agent-skills

**Reddit (r/PhD, r/AskAcademia, r/GradSchool, r/LaTeX, r/bioinformatics, r/ClaudeAI):** adapt the Show HN text,
lead with the subreddit's problem (for example fake references for r/AskAcademia, PRISMA for r/medicine-adjacent
subs), and disclose that you maintain the project.

**Bluesky / Mastodon / LinkedIn / X:** a 30-second clip of `citation-verification` flagging a fabricated
reference, then the install command and repository link.
