# Listings and backlinks tracker (maintainers)

Where Research Agent Skills is listed, where it is pending, and ready-to-paste submission text.
Follow each list's rules exactly and submit one entry per list. Re-check this table monthly.

Audit date: 2026-10-19. Repository created 2026-07-07; 28 stars at audit time.

## Live

| Where | URL | Notes |
|---|---|---|
| GitHub | https://github.com/KalarisLabs/research-agent-skills | 20 topics set (GitHub's maximum) |
| Documentation (Mintlify) | https://docs.kalarislabs.com/research-agent-skills | Sitemap at `https://docs.kalarislabs.com/sitemap.xml`; per-page OG images are automatic |
| skills.sh | https://skills.sh/kalarislabs/research-agent-skills | 281 skills, about 2.9K installs. Groupings come from `skills.sh.json` |
| Skills Directory | https://www.skillsdirectory.com/authors/kalarislabs | 283 skill pages, security grade A (96/100), each links back to its `SKILL.md` |
| SkillsMP | https://skillsmp.com | Crawls public GitHub `SKILL.md` files automatically; no submission |
| Claude Code plugin marketplace | `/plugin marketplace add KalarisLabs/research-agent-skills` | Aggregators such as claudemarketplaces.com crawl `.claude-plugin/marketplace.json` |

## Pull requests (open from the maintainer account)

| List | Stars | Section | Rules | Status |
|---|---|---|---|---|
| [InternScience/Awesome-Scientific-Skills](https://github.com/InternScience/Awesome-Scientific-Skills) | 569 | Skill Sources → Science-Specific → Specialized Domain Tools | Table row; PR note on why it helps science | To open |
| [BehiSecc/awesome-claude-skills](https://github.com/BehiSecc/awesome-claude-skills) | 10K | Scientific & Research Tools | Fork, edit, PR | To open |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | 15K | Community Skills → Collections & Libraries | Fork, edit, PR | To open |
| [heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills) | 6K | Community Skills → Skill Collections | ≥20 stars, >14 days old, README.md only, one additive line, title `Add owner/repo to <Category>`, agents must disclose | To open |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 36K | Community Skills → AI and Data | One skill per entry, author prefix, ≤10-word description, needs real adoption | To open (`citation-verification` only) |

Entry text:

- InternScience: `| [KalarisLabs/research-agent-skills](https://github.com/KalarisLabs/research-agent-skills) | 28 | 280+ research skills: paper and thesis writing, journal formats, PRISMA reviews, citation verification, and ML, biology, chemistry, medicine and physics analysis |`
- BehiSecc: `- [research-agent-skills](https://github.com/KalarisLabs/research-agent-skills) - 280+ skills for academic writing, journal formatting, systematic reviews, citation verification and scientific data analysis.`
- travisvn: `- **[KalarisLabs/research-agent-skills](https://github.com/KalarisLabs/research-agent-skills)** - 280+ skills for academic research: paper writing, journal formats, PRISMA reviews, citation verification and field-specific analysis.`
- heilcheng: `- [KalarisLabs/research-agent-skills](https://github.com/KalarisLabs/research-agent-skills) - 280+ skills for academic writing, systematic reviews and scientific analysis`
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
