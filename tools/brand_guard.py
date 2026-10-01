"""Fail if upstream product names appear outside the provenance files.

Patterns and allowed paths are defined in third_party/rebrand-rules.yaml
(`guard_patterns`, `guard_allowed_paths`). Provenance and license notices for
imported material live only in LICENSES/, THIRD_PARTY_NOTICES.md and third_party/.

Usage:
    uv run tools/brand_guard.py            # scan all tracked + untracked files
    uv run tools/brand_guard.py path ...   # scan specific paths
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import ROOT, THIRD_PARTY, load_yaml  # noqa: E402

BINARY_EXT = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".webp", ".ico", ".woff", ".woff2"}


def candidate_files(paths: list[str]) -> list[Path]:
    if paths:
        out: list[Path] = []
        for p in map(Path, paths):
            out.extend(sorted(f for f in p.rglob("*") if f.is_file()) if p.is_dir() else [p])
        return out
    res = subprocess.run(["git", "ls-files", "-co", "--exclude-standard"], cwd=ROOT, capture_output=True,
                         text=True, check=True)
    return [ROOT / line for line in res.stdout.splitlines() if line]


def main(argv: list[str] | None = None) -> int:
    rules = load_yaml(THIRD_PARTY / "rebrand-rules.yaml")
    pattern = re.compile("|".join(f"(?:{p})" for p in rules["guard_patterns"]), re.I)
    allowed = tuple(rules["guard_allowed_paths"])
    hits = 0
    for path in candidate_files(sys.argv[1:] if argv is None else argv):
        try:
            rel = path.resolve().relative_to(ROOT).as_posix()
        except ValueError:
            rel = path.as_posix()
        if rel.startswith(allowed) or path.suffix.lower() in BINARY_EXT or not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            if pattern.search(line):
                print(f"{rel}:{i}: {line.strip()[:160]}")
                hits += 1
    if hits:
        print(f"\n{hits} upstream name reference(s) outside {', '.join(allowed)}. "
              "Add a rule to third_party/rebrand-rules.yaml or reword.")
        return 1
    print("brand guard: clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
