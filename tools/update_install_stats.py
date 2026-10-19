"""Refresh per-skill install counts from skills.sh into catalog/installs.json and the README.

skills.sh publishes a repository-level badge but no per-skill API, so this reads the
counts from the public repository page. The README table between
<!-- installs:start --> and <!-- installs:end --> shows the most-installed skills.

Usage:
    uv run tools/update_install_stats.py            # fetch and write
    uv run tools/update_install_stats.py --top 15   # longer leaderboard
    uv run tools/update_install_stats.py --html page.html  # parse a saved page (offline)

Exit codes: 0 updated or unchanged, 1 page fetched but no counts found, 2 network or input error.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import REPO_SLUG, ROOT, write_text  # noqa: E402

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

SLUG = REPO_SLUG.lower()
PAGE_URL = f"https://www.skills.sh/{SLUG}"
BADGE_URL = f"https://skills.sh/api/badge/{SLUG}"
UA = f"research-agent-skills-install-stats/1.0 (https://github.com/{REPO_SLUG})"
INSTALLS_START, INSTALLS_END = "<!-- installs:start -->", "<!-- installs:end -->"
# The collection index skill is not a specialist skill, so it is left out of the leaderboard.
EXCLUDE = {"research-agent-skills"}
CARD_RE = re.compile(
    rf'href="/{re.escape(SLUG)}/([a-z0-9][a-z0-9-]*)".*?<h3[^>]*>[^<]*</h3>.*?<span[^>]*>\s*([\d,]+)\s*</span>',
    re.S,
)


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:  # noqa: S310 (fixed https URL)
        return r.read().decode("utf-8")


def parse_counts(html: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for name, n in CARD_RE.findall(html):
        counts.setdefault(name, int(n.replace(",", "")))
    return counts


def render_table(counts: dict[str, int], total: str, top: int, date: str) -> str:
    known = {p.name for p in (ROOT / "skills").iterdir() if (p / "SKILL.md").is_file()}
    ranked = sorted(((n, c) for n, c in counts.items() if n in known and n not in EXCLUDE), key=lambda x: (-x[1], x[0]))
    rows = [
        f"| {i} | [`{name}`](skills/{name}/SKILL.md) | {c:,} | "
        f"`npx skills add {REPO_SLUG} --skill {name}` |"
        for i, (name, c) in enumerate(ranked[:top], 1)
    ]
    return "\n".join([
        "",
        f"Live from [skills.sh]({PAGE_URL}) · **{total}** installs across the collection · updated {date}",
        "",
        "| # | Skill | Installs | Install just this skill |",
        "|---|---|---|---|",
        *rows,
        "",
    ])


def update_readme(readme: str, table: str) -> str:
    if INSTALLS_START not in readme or INSTALLS_END not in readme:
        raise ValueError(f"README.md has no {INSTALLS_START} ... {INSTALLS_END} block")
    pre, rest = readme.split(INSTALLS_START, 1)
    _, post = rest.split(INSTALLS_END, 1)
    return pre + INSTALLS_START + table + INSTALLS_END + post


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--top", type=int, default=10, help="rows in the README leaderboard (default 10)")
    ap.add_argument("--html", type=Path, help="parse a saved skills.sh page instead of fetching it")
    args = ap.parse_args(argv)
    try:
        html = args.html.read_text(encoding="utf-8") if args.html else fetch(PAGE_URL)
    except (OSError, urllib.error.URLError, UnicodeDecodeError) as exc:
        print(f"error: cannot read skills.sh page: {exc}", file=sys.stderr)
        return 2
    counts = parse_counts(html)
    if not counts:
        print("error: no install counts found; the skills.sh page layout may have changed", file=sys.stderr)
        return 1
    total = f"{sum(counts.values()):,}"
    if not args.html:
        try:
            total = json.loads(fetch(BADGE_URL)).get("message") or total
        except (OSError, urllib.error.URLError, ValueError):
            pass  # fall back to the sum of per-skill counts
    date = dt.date.today().isoformat()
    out = ROOT / "catalog" / "installs.json"
    data = {"source": PAGE_URL, "updated": date, "total": total,
            "skills": dict(sorted(counts.items(), key=lambda x: (-x[1], x[0])))}
    old = json.loads(out.read_text(encoding="utf-8")) if out.exists() else {}
    if old.get("skills") == data["skills"] and old.get("total") == total:
        print(f"unchanged: {len(counts)} skills, {total} installs")
        return 0
    write_text(out, json.dumps(data, indent=2) + "\n")
    readme_path = ROOT / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    write_text(readme_path, update_readme(readme, render_table(counts, total, args.top, date)))
    print(f"updated: {len(counts)} skills, {total} installs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
