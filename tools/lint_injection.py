"""Security lint for agent skills: prompt injection, hidden content, dangerous code.

Scans every file in skills/ (instructions, references, scripts, tests, assets) for
patterns that indicate prompt injection or supply-chain abuse. Findings already
accepted in security/lint-baseline.json are reported but do not fail the run.

Usage:
    uv run tools/lint_injection.py                        # scan skills/
    uv run tools/lint_injection.py path ...               # scan specific files/dirs
    uv run tools/lint_injection.py --sarif out.sarif      # also write SARIF 2.1.0
    uv run tools/lint_injection.py --update-baseline      # accept current findings (review first!)
    uv run tools/lint_injection.py --update-domains       # add newly seen script domains to allowlist

Exit code 1 on any new HIGH or MEDIUM finding.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from dataclasses import asdict, dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import REPO_URL, ROOT, SKILLS_DIR  # noqa: E402

SECURITY = ROOT / "security"
BASELINE = SECURITY / "lint-baseline.json"
DOMAINS = SECURITY / "allowed-domains.txt"
SCRIPT_EXT = {".py", ".sh", ".bash", ".js", ".mjs", ".ts", ".ps1", ".r", ".jl"}
SKIP_EXT = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".webp"}


@dataclass(frozen=True)
class Rule:
    id: str
    severity: str  # HIGH | MEDIUM | LOW
    description: str
    pattern: re.Pattern[str]
    scope: str = "all"  # all | scripts | markdown


def _r(p: str, flags: int = re.I) -> re.Pattern[str]:
    return re.compile(p, flags)


RULES: list[Rule] = [
    Rule("RAS001", "HIGH", "Instruction-override phrase (prompt injection)",
         _r(r"\b(?:ignore|disregard|forget|override)\s+(?:all\s+|any\s+)?(?:the\s+)?(?:previous|prior|above|earlier|"
            r"preceding|system|original)\s+(?:instructions?|prompts?|rules|guidelines|directions)")),
    Rule("RAS002", "HIGH", "Instruction to hide actions from the user",
         _r(r"\b(?:do\s+not|don'?t|never)\s+(?:tell|inform|notify|alert|show|mention\s+(?:this\s+)?to)\s+the\s+user|"
            r"without\s+(?:the\s+user'?s?\s+knowledge|telling\s+the\s+user|informing\s+the\s+user)|"
            r"\bsilently\s+(?:send|upload|post|exfiltrate|transmit)")),
    Rule("RAS003", "HIGH", "Pipe-to-shell remote code execution",
         _r(r"\b(?:curl|wget)\b[^\n|]*\|\s*(?:sudo\s+)?(?:ba|z|k)?sh\b|"
            r"\b(?:iex|invoke-expression)\b[^\n]*(?:irm|iwr|invoke-(?:restmethod|webrequest)|downloadstring)|"
            r"(?:irm|iwr|invoke-(?:restmethod|webrequest))\b[^\n]*\|\s*(?:iex|invoke-expression)\b")),
    Rule("RAS004", "HIGH", "Access to credential or key material",
         _r(r"~/\.ssh\b|\bid_(?:rsa|ed25519|ecdsa)\b(?!\.pub)|\.aws/credentials|\.git-credentials|\.netrc\b|"
            r"/etc/shadow|\.docker/config\.json|\.kube/config|login\s+keychain|security\s+find-generic-password")),
    Rule("RAS005", "HIGH", "Obfuscated code execution (exec/eval of decoded data)",
         _r(r"\b(?:exec|eval)\s*\(\s*(?:base64|codecs|zlib|bz2|lzma|marshal|bytes\.fromhex|__import__)|"
            r"\bmarshal\.loads\s*\(|\bexec\s*\(\s*compile\s*\([^)]*b64decode"), "scripts"),
    Rule("RAS006", "MEDIUM", "Reverse shell / raw socket to shell pattern",
         _r(r"/dev/tcp/|\bnc\s+(?:-\w+\s+)*-e\s|\bsocket\b[^\n]*\bsubprocess\b[^\n]*\bsh\b|pty\.spawn\(")),
    Rule("RAS007", "MEDIUM", "Hidden HTML comment containing agent-directed instructions",
         _r(r"<!--(?:(?!-->).)*?(?:\b(?:you|assistant|agent|ai|model|claude|llm)\s+(?:must|should|shall|will|are\s+to|"
            r"need\s+to)\b|\b(?:ignore|disregard)\b|\binstructions?\s+(?:for|to)\s+(?:the\s+)?(?:assistant|agent|ai|model)\b|"
            r"\b(?:system|assistant)\s*:)(?:(?!-->).)*-->", re.I | re.S), "markdown"),
    Rule("RAS008", "MEDIUM", "Long encoded blob (base64/hex) that could hide a payload",
         _r(r"(?<![A-Za-z0-9+/=])(?:[A-Za-z0-9+/]{400,}={0,2}|(?:[0-9a-fA-F]{2}){300,})(?![A-Za-z0-9+/=])", 0)),
    Rule("RAS009", "MEDIUM", "Environment-variable harvesting sent over the network",
         _r(r"(?:os\.environ|process\.env)\b[^\n]{0,80}\b(?:requests\.(?:post|put)|urlopen|fetch\(|httpx\.(?:post|put))|"
            r"(?:requests\.(?:post|put)|httpx\.(?:post|put))\([^\n]{0,120}(?:dict\(os\.environ\)|os\.environ\.copy\(\))"),
         "scripts"),
    Rule("RAS010", "LOW", "Persona/role reassignment phrase",
         _r(r"\byou\s+are\s+now\s+(?:in\s+)?(?:developer|dan|jailbreak|unrestricted|god)\s*mode\b")),
]

INVISIBLE_RE = re.compile(
    "[​-‏‪-‮⁠-⁤⁦-⁩﻿\U000e0000-\U000e007f]"
)
URL_HOST_RE = re.compile(r"https?://([A-Za-z0-9][A-Za-z0-9.-]*\.[A-Za-z]{2,})(?::\d+)?")


@dataclass
class Finding:
    """Finding."""
    rule: str
    severity: str
    path: str
    line: int
    message: str
    snippet: str

    @property
    def fingerprint(self) -> str:
        norm = re.sub(r"\s+", " ", self.snippet.strip())
        return hashlib.sha256(f"{self.rule}|{self.path}|{norm}".encode()).hexdigest()[:20]


def iter_files(paths: list[Path]) -> list[Path]:
    """Iter files for *paths* and return list[Path]."""
    out: list[Path] = []
    for p in paths:
        if p.is_file():
            out.append(p)
        elif p.is_dir():
            out.extend(sorted(f for f in p.rglob("*") if f.is_file()))
    return [f for f in out if f.suffix.lower() not in SKIP_EXT and "__pycache__" not in f.parts]


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def scan_file(path: Path) -> tuple[list[Finding], set[str]]:
    """Scan file for *path* and return tuple[list[Finding], set[str]]."""
    findings: list[Finding] = []
    hosts: set[str] = set()
    try:
        text = path.read_bytes().decode("utf-8")
    except UnicodeDecodeError:
        return [Finding("RAS000", "MEDIUM", rel(path), 1, "Non-UTF-8 file cannot be inspected", "")], hosts
    ext = path.suffix.lower()
    is_script = ext in SCRIPT_EXT
    lines = text.splitlines()

    for i, line in enumerate(lines, 1):
        for m in INVISIBLE_RE.finditer(line):
            if m.group() == "﻿" and i == 1 and m.start() == 0:
                continue
            if m.group() == "‍" and m.start() > 0 and ord(line[m.start() - 1]) > 0x2000:
                continue  # zero-width joiner inside an emoji sequence
            if m.group() == "‍" and m.start() > 0 and ord(line[m.start() - 1]) > 0x2000:
                continue  # zero-width joiner inside an emoji sequence
            name = unicodedata.name(m.group(), f"U+{ord(m.group()):04X}")
            findings.append(Finding("RAS011", "HIGH", rel(path), i, f"Invisible/bidirectional character {name}",
                                    line.encode("unicode_escape").decode()[:160]))
            break

    for rule in RULES:
        if rule.scope == "scripts" and not is_script:
            continue
        if rule.scope == "markdown" and ext != ".md":
            continue
        for m in rule.pattern.finditer(text):
            line_no = text.count("\n", 0, m.start()) + 1
            snippet = lines[line_no - 1] if line_no <= len(lines) else m.group()
            findings.append(Finding(rule.id, rule.severity, rel(path), line_no, rule.description,
                                    snippet.strip()[:200]))

    if is_script:
        hosts.update(h.lower().rstrip(".") for h in URL_HOST_RE.findall(text))
    return findings, hosts


def host_allowed(host: str, allowed: set[str]) -> bool:
    parts = host.split(".")
    return any(".".join(parts[i:]) in allowed for i in range(len(parts) - 1))


def load_allowed() -> set[str]:
    if not DOMAINS.exists():
        return set()
    return {ln.split("#")[0].strip().lower() for ln in DOMAINS.read_text(encoding="utf-8").splitlines()
            if ln.split("#")[0].strip()}


def to_sarif(findings: list[Finding]) -> dict:
    """To sarif for *findings* and return dict."""
    level = {"HIGH": "error", "MEDIUM": "warning", "LOW": "note"}
    rules = {r.id: r.description for r in RULES}
    rules.update({"RAS011": "Invisible/bidirectional Unicode character", "RAS012": "Script contacts unreviewed domain",
                  "RAS000": "Non-UTF-8 file"})
    return {
        "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
        "version": "2.1.0",
        "runs": [{
            "tool": {"driver": {
                "name": "research-agent-skills-lint",
                "informationUri": REPO_URL,
                "rules": [{"id": k, "shortDescription": {"text": v}} for k, v in sorted(rules.items())],
            }},
            "results": [{
                "ruleId": f.rule, "level": level[f.severity], "message": {"text": f"{f.message}: {f.snippet}"},
                "partialFingerprints": {"primaryLocationLineHash": f.fingerprint},
                "locations": [{"physicalLocation": {"artifactLocation": {"uri": f.path},
                                                    "region": {"startLine": max(f.line, 1)}}}],
            } for f in findings],
        }],
    }


def main(argv: list[str] | None = None) -> int:
    """Main for *argv* and return int."""
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*", type=Path)
    ap.add_argument("--sarif", type=Path, help="write SARIF report to this path")
    ap.add_argument("--json", type=Path, help="write JSON findings to this path")
    ap.add_argument("--update-baseline", action="store_true", help="accept all current findings into the baseline")
    ap.add_argument("--update-domains", action="store_true", help="append newly seen script domains to the allowlist")
    ap.add_argument("--no-baseline", action="store_true", help="ignore the baseline (report everything as new)")
    args = ap.parse_args(argv)

    files = iter_files(args.paths or [SKILLS_DIR])
    findings: list[Finding] = []
    hosts_by_file: dict[str, set[str]] = {}
    for f in files:
        found, hosts = scan_file(f)
        findings.extend(found)
        if hosts:
            hosts_by_file[rel(f)] = hosts

    allowed = load_allowed()
    unseen = sorted({h for hs in hosts_by_file.values() for h in hs if not host_allowed(h, allowed)})
    if args.update_domains and unseen:
        with DOMAINS.open("a", encoding="utf-8", newline="\n") as fh:
            fh.write("".join(f"{h}\n" for h in unseen))
        print(f"added {len(unseen)} domains to {rel(DOMAINS)} - review them before committing")
        allowed = load_allowed()
    for path, hosts in sorted(hosts_by_file.items()):
        for h in sorted(hosts):
            if not host_allowed(h, allowed):
                findings.append(Finding("RAS012", "MEDIUM", path, 1, "Script contacts a domain not in "
                                        "security/allowed-domains.txt", h))

    baseline: set[str] = set()
    if BASELINE.exists() and not args.no_baseline:
        baseline = set(json.loads(BASELINE.read_text(encoding="utf-8")).get("accepted", []))
    if args.update_baseline:
        SECURITY.mkdir(exist_ok=True)
        data = {"_comment": "Reviewed, accepted findings (fingerprints). Regenerate with --update-baseline "
                            "only after manual review.",
                "accepted": sorted({f.fingerprint for f in findings})}
        BASELINE.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8", newline="\n")
        print(f"baseline updated with {len(data['accepted'])} fingerprints")
        baseline = set(data["accepted"])

    new = [f for f in findings if f.fingerprint not in baseline]
    for f in sorted(new, key=lambda x: ("HIGH", "MEDIUM", "LOW").index(x.severity)):
        print(f"{f.severity:<6} {f.rule} {f.path}:{f.line}  {f.message}\n         {f.snippet}")
    if args.sarif:
        args.sarif.parent.mkdir(parents=True, exist_ok=True)
        args.sarif.write_text(json.dumps(to_sarif(new), indent=2), encoding="utf-8")
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps([asdict(f) | {"fingerprint": f.fingerprint} for f in new], indent=2),
                             encoding="utf-8")
    blocking = [f for f in new if f.severity in ("HIGH", "MEDIUM")]
    print(f"\n{len(files)} files scanned: {len(findings)} findings, {len(findings) - len(new)} baselined, "
          f"{len(blocking)} new blocking")
    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())
