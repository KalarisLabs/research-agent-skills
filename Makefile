# Developer entry points. Every target is a thin wrapper around `uv run` / `npm`,
# so the same commands work without make (see CONTRIBUTING.md).
.DEFAULT_GOAL := help
.PHONY: help setup check validate lint security test cli catalog quality bench-triggers bench-citations \
        bench-slop bench-tasks docs docs-serve import clean

help: ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "} {printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2}'

setup: ## Install Python tooling and CLI dependencies
	uv sync --group docs
	cd cli && npm ci

check: validate security catalog quality test ## Everything CI runs on a pull request (fast, offline)

validate: ## Agent Skills spec + repository policy
	uv run tools/validate.py --quiet

lint: ## Ruff for tooling, tests and benchmarks
	uv run ruff check tools tests benchmarks

security: ## Prompt-injection lint and provenance guard
	uv run tools/lint_injection.py
	uv run tools/brand_guard.py

test: lint ## Python tests (tooling + skill scripts)
	uv run python -m pytest -q

cli: ## Build and test the npm installer
	cd cli && npm test

catalog: ## Regenerate marketplace, plugin manifest, catalog, notices and README tables
	uv run tools/build_catalog.py

quality: ## Static quality rubric for all skills (report) and original skills (gate)
	uv run tools/skill_quality.py --json benchmarks/results/skill-quality.json --markdown benchmarks/results/skill-quality.md
	uv run tools/skill_quality.py --origin original --min-score 80

bench-triggers: ## Trigger-routing benchmark (BM25, free)
	uv run tools/trigger_bench.py --json benchmarks/results/trigger-bm25.json

bench-citations: ## Citation-verification precision/recall (network)
	uv run benchmarks/citation_verification/run.py --json benchmarks/results/citation-verification.json

bench-slop: ## Slop benchmark: fetch human abstracts, generate with/without skill (paid), score
	uv run benchmarks/slop/run.py fetch --n 60
	uv run benchmarks/slop/run.py generate --limit 30
	uv run benchmarks/slop/run.py score --json benchmarks/results/slop.json

bench-tasks: ## With-vs-without-skill task outcomes, blind LLM judge (paid)
	uv run benchmarks/task_evals/run.py --all-original --json benchmarks/results/task-evals.json

docs: ## Validate Mintlify documentation pages and links
	uv run tools/build_catalog.py --docs
	cd docs && npx -y mint@4.2.963 broken-links

docs-serve: ## Live-preview the Mintlify documentation site
	uv run tools/build_catalog.py --docs
	cd docs && npx -y mint@4.2.963 dev

import: ## Re-import adapted skills from pinned upstream revisions
	uv run tools/import_upstream.py
	uv run tools/build_catalog.py

clean: ## Remove caches and build output
	rm -rf .cache site cli/dist .pytest_cache .ruff_cache docs/skills
