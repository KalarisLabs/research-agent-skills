"""Check that what a skill says about its own scripts is true.

A SKILL.md is a promise to the agent and the user: "run this script with this flag", "it queries these
services", "it reports these statuses". The static quality rubric only rewards the *words* (verify, check),
so a skill can name an API its script never calls and still score well. This audit reads the claim and looks in
the code:

  missing-script   a `scripts/<file>` named in SKILL.md does not exist
  missing-flag     a `--flag` used on a line that runs a bundled script is not defined by that script
  missing-host     a host named in `compatibility` is never contacted by the skill's scripts
  missing-service  a service named in a "Queries/Searches/Resolves ..." description sentence is never contacted
  missing-status   a value in a "Status" column of a table never appears in the skill's scripts

Scope: original skills (those not imported from upstream), where the maintainers own both text and code.
Findings that are intentional go in `security/claim-audit-ignore.txt` as `<skill>:<kind>:<token>  # reason`.

Usage:
    uv run tools/claim_audit.py                    # all original skills
    uv run tools/claim_audit.py --all              # imported skills too (noisy, advisory)
    uv run tools/claim_audit.py skills/foo ...     # specific skills
    uv run tools/claim_audit.py --json report.json

Exit code 1 if any finding survives the ignore list.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import ROOT, SKILLS_DIR, THIRD_PARTY, split_frontmatter  # noqa: E402

IGNORE_FILE = ROOT / "security" / "claim-audit-ignore.txt"
HOST_RE = re.compile(r"\b((?:[a-z0-9-]+\.)+(?:org|com|gov|io|net|edu|ac\.uk|eu))\b", re.I)
SCRIPT_REF_RE = re.compile(r"(?<![\w/.-])scripts/([A-Za-z0-9_.-]+\.(?:py|sh|js|R|r))")
FLAG_RE = re.compile(r"(?<![\w-])(--[a-z][a-z0-9-]*)")
SERVICES = {  # service name in a description -> host a script must contact to honestly claim it
    "crossref": "crossref.org", "openalex": "openalex.org", "arxiv": "arxiv.org", "datacite": "datacite.org",
    "pubmed": "ncbi.nlm.nih.gov", "unpaywall": "unpaywall.org", "semantic scholar": "semanticscholar.org",
    "europe pmc": "europepmc.org", "zenodo": "zenodo.org", "orcid": "orcid.org", "ror": "ror.org",
}
QUERY_SENTENCE_RE = re.compile(r"(?:^|(?<=[.;]\s))(?:Queries|Searches|Resolves|Fetches|Calls|Reads from)\b[^.;]*", re.I)
GENERIC_HOSTS = {"github.com", "example.org", "example.com", "youruni.edu", "university.edu", "uni.edu"}


def original_skills() -> set[str]:
    """Skill names not imported from upstream."""
    manifest = json.loads((THIRD_PARTY / "upstream-manifest.json").read_text(encoding="utf-8"))
    entries = manifest.get("skills", [])
    imported = {e["name"] for e in entries if isinstance(e, dict) and "name" in e}
    return {p.name for p in SKILLS_DIR.iterdir() if (p / "SKILL.md").exists()} - imported


def load_ignores() -> set[str]:
    """Return the `skill:kind:token` entries to skip."""
    if not IGNORE_FILE.exists():
        return set()
    out = set()
    for line in IGNORE_FILE.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            out.add(line)
    return out


def script_sources(skill: Path) -> dict[str, str]:
    """Map script filename to its source for every file under scripts/."""
    d = skill / "scripts"
    return {p.name: p.read_text(encoding="utf-8", errors="replace") for p in sorted(d.rglob("*")) if p.is_file()
            and p.suffix in {".py", ".sh", ".js", ".R", ".r"}} if d.is_dir() else {}


def status_tokens(body: str) -> set[str]:
    """Backticked first-column values of every Markdown table whose header cell is exactly `Status`."""
    tokens: set[str] = set()
    lines = body.splitlines()
    for i, line in enumerate(lines):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if line.strip().startswith("|") and cells and cells[0].lower() == "status":
            for row in lines[i + 2:]:
                if not row.strip().startswith("|"):
                    break
                first = row.strip().strip("|").split("|")[0].strip()
                tokens.update(re.findall(r"`([a-z][a-z0-9_-]+)`", first))
    return tokens


def audit_skill(skill: Path) -> list[dict]:
    """Return findings for one skill."""
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    meta, body = split_frontmatter(text)
    sources = script_sources(skill)
    blob = "\n".join(sources.values())
    findings: list[dict] = []

    def add(kind: str, token: str, detail: str) -> None:
        findings.append({"skill": skill.name, "kind": kind, "token": token, "detail": detail})

    for ref in sorted(set(SCRIPT_REF_RE.findall(text))):
        if ref not in sources:
            add("missing-script", ref, f"SKILL.md names scripts/{ref}, which does not exist")
    for line in body.splitlines():
        for script in SCRIPT_REF_RE.findall(line):
            src = sources.get(script)
            if src is None:
                continue
            for flag in FLAG_RE.findall(line):
                if flag not in {"--help", "--version"} and f'"{flag}"' not in src and f"'{flag}'" not in src:
                    add("missing-flag", flag, f"`{script}` is run with {flag}, which the script does not define")
    if sources:
        hosts = {h.lower() for h in HOST_RE.findall(str(meta.get("compatibility", "")))} - GENERIC_HOSTS
        for host in sorted(hosts):
            if host not in blob.lower():
                add("missing-host", host, f"`compatibility` names {host}, but no script contacts it")
        for sentence in QUERY_SENTENCE_RE.findall(str(meta.get("description", ""))):
            for name, host in SERVICES.items():
                if re.search(rf"\b{re.escape(name)}\b", sentence, re.I) and host not in blob.lower():
                    add("missing-service", name, f"the description says it queries {name}; no script contacts {host}")
        for status in sorted(status_tokens(body)):
            if f'"{status}"' not in blob and f"'{status}'" not in blob:
                add("missing-status", status, f"the Status table lists `{status}`, which no script can produce")
    return findings


def main(argv: list[str] | None = None) -> int:
    """Run the command-line interface."""
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("skills", nargs="*", help="skill folders (default: all original skills)")
    ap.add_argument("--all", action="store_true", help="include imported skills")
    ap.add_argument("--json", metavar="PATH")
    args = ap.parse_args(argv)
    if args.skills:
        paths = [Path(s) for s in args.skills]
    else:
        names = {p.name for p in SKILLS_DIR.iterdir() if (p / "SKILL.md").exists()}
        paths = [SKILLS_DIR / n for n in sorted(names if args.all else original_skills())]
    ignores = load_ignores()
    findings = []
    for p in paths:
        for f in audit_skill(p):
            if f"{f['skill']}:{f['kind']}:{f['token']}" not in ignores:
                findings.append(f)
    for f in findings:
        print(f"{f['skill']}: {f['kind']} {f['token']}: {f['detail']}")
    if args.json:
        Path(args.json).write_text(json.dumps(findings, indent=2) + "\n", encoding="utf-8")
    print(f"{len(paths)} skills audited, {len(findings)} claim(s) the code does not support")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
