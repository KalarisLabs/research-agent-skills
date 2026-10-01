# Launch and discoverability checklist (maintainers)

Organic growth only. Never buy stars or use star-exchange rings or bots: they violate GitHub's terms
and can get the repository delisted. Usefulness, visibility in academic channels, and trust drive adoption.

## Repository settings (GitHub → About)

- **Description:** `AI agent skills for academic writing & scientific research: papers, theses, systematic reviews (PRISMA), journal formatting, citation verification, no AI slop. Claude Code, Codex, Cursor, Gemini CLI.`
- **Website:** https://docs.kalarislabs.com/research-agent-skills (live Mintlify project page).
- **Topics (max 20):** `agent-skills` `claude-code` `codex` `ai-agents` `academic-writing` `scientific-writing` `research-paper` `thesis` `literature-review` `systematic-review` `prisma` `citation` `latex` `zotero` `peer-review` `bioinformatics` `open-science` `research-tools` `llm` `claude-skills`
- Social preview image (1280×640): project name, "AI skills for academic writing & research", agent logos.
- Keep Discussions, private vulnerability reporting, secret scanning and push protection enabled. Protect `main`
  with a pull request, an independent approval, required CI checks and linear history.
- Mintlify: connect the GitHub repository with `docs/` as the documentation root. `docs.yml` validates generated pages and links; Mintlify deploys from the connected repository.
- Domain: `docs.kalarislabs.com` serves the Mintlify documentation over HTTPS. Verify the sitemap after each deployment.
- Environments: `npm` (trusted publishing) and `benchmarks` (holds `ANTHROPIC_API_KEY` for manual benchmark runs).

## Vendor security and npm release setup

1. Add GitHub repository secrets `SNYK_TOKEN` and `SOCKET_CLI_API_TOKEN` in
   **Settings → Secrets and variables → Actions**. Do not paste tokens into an
   issue or chat. The Socket token needs `full-scans:create`, `full-scans:list`,
   and `security-policy:read` permissions. Set the repository variable
   `VENDOR_SCANS_ENABLED=true` after both are present. The vendor workflow then
   scans main and runs weekly, and becomes an additional release gate. Without
   those credentials, releases still run local validation, prompt-injection
   lint, Cisco AI Defense scanning and tests.
2. The first `research-agent-skills` npm version must be published by an npm
   account owner from `cli/` using `npm login` and `npm publish --access public`.
   Confirm the package name and tarball contents first with `npm pack --dry-run`.
   Do not create the release tag until this bootstrap publish is visible on npm.
3. In npm package settings, add a trusted GitHub Actions publisher: organization
   `KalarisLabs`, repository `research-agent-skills`, workflow `release.yml`,
   environment `npm`, and **Allow npm publish**. Future tag releases use OIDC
   and provenance without a long-lived npm publishing token. The release job
   recognizes a version already published during bootstrap.

## Citable research software (academics search and cite here)

- [ ] Connect the repository to **Zenodo** so each release mints a DOI, then add the DOI badge to the README and `CITATION.cff`.
- [ ] Submit to the **Journal of Open Source Software (JOSS)** once benchmarks are run at scale. It gives a peer-reviewed, citable paper.
- [ ] List on **Research Software Directory** instances, **pyOpenSci/rOpenSci** forums (as appropriate), and **Papers with Code**-style tool lists.
- [ ] Register the docs site in Google Search Console and submit `sitemap.xml`.

## Launch week

- [ ] skills.sh listing (first `npx skills add` installs register it).
- [ ] PRs to awesome lists: agent skills, Claude Code, research tools, academic writing, LaTeX, open science.
- [ ] Show HN: problem (slop + fake citations) → demo → benchmarks → security.
- [ ] Reddit: r/PhD, r/AskAcademia, r/GradSchool, r/LaTeX, r/bioinformatics, r/MachineLearning ([P] thread), r/ClaudeAI. Follow each sub's self-promotion rules.
- [ ] Academic social: Bluesky and Mastodon science communities, LinkedIn, and X threads with short clips (citation check, unslop before/after, PRISMA diagram).
- [ ] Offer workshops or demos to university research-computing groups, libraries and graduate schools.

## Ongoing

- [ ] Triage issues within 48 h, merge good community skills quickly, and write a changelog entry per release.
- [ ] Monthly: rerun model benchmarks with current models and publish the results in `benchmarks/results/`.
- [ ] Track installs (npm, skills.sh), stars, docs traffic and top search queries, and turn them into new skills and guides.
- [ ] Rewrite the lowest-scoring adapted skills (see `benchmarks/results/skill-quality.md`) as originals.
