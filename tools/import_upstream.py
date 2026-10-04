"""Import MIT-licensed upstream skills into skills/ at pinned revisions.

Usage:
    uv run tools/import_upstream.py                 # clone pinned refs into .cache/upstream
    uv run tools/import_upstream.py --source-dir D  # use existing checkouts D/<source-id>

Idempotent: re-running with the same pins produces no diff. Skills marked
`rewrite_status: original` in the manifest are never overwritten.
Outputs: skills/<name>/, third_party/upstream-manifest.json.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import enrich  # noqa: E402
from common import (  # noqa: E402
    ROOT,
    SKILLS_DIR,
    THIRD_PARTY,
    load_skill,
    load_skills,
    load_yaml,
    split_frontmatter,
    write_text,
)
from rebrand import rebrand_skill  # noqa: E402
from skill_quality import tfidf_overlap  # noqa: E402

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
IGNORE = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store", ".gitkeep", "Thumbs.db", ".ipynb_checkpoints")
MANIFEST = THIRD_PARTY / "upstream-manifest.json"
PATCHES = THIRD_PARTY / "patches"
CACHE = ROOT / ".cache" / "upstream"


def git(*args: str, cwd: Path | None = None) -> str:
    return subprocess.run(["git", "-c", "core.longpaths=true", "-c", "core.autocrlf=false", *args], cwd=cwd, check=True,
                          capture_output=True, text=True).stdout.strip()


def checkout(source: dict, source_dir: Path | None) -> Path:
    """Checkout for *source*, *source_dir* and return Path."""
    if source_dir:
        path = source_dir / source["id"]
        if not path.exists():
            sys.exit(f"missing checkout: {path}")
        head = git("rev-parse", "HEAD", cwd=path)
        if head != source["ref"]:
            sys.exit(f"{path} is at {head}, expected pinned {source['ref']}")
        return path
    path = CACHE / source["id"]
    if not (path / ".git").exists():
        path.mkdir(parents=True, exist_ok=True)
        git("init", "-q", cwd=path)
        git("remote", "add", "origin", source["repo"], cwd=path)
    git("fetch", "-q", "--depth", "1", "origin", source["ref"], cwd=path)
    git("checkout", "-q", "--force", source["ref"], cwd=path)
    return path


def discover(source: dict, checkout_dir: Path) -> list[tuple[str, Path]]:
    """Return [(relative source path, skill dir)] for one source."""
    root = checkout_dir / source.get("root", ".")
    found = []
    for skill_md in sorted(root.rglob("SKILL.md")):
        rel = skill_md.parent.relative_to(root).as_posix()
        if ".git" in rel.split("/"):
            continue
        glob = source.get("include_glob")
        if glob and not fnmatch.fnmatch(rel.split("/")[0], glob):
            continue
        found.append((rel, skill_md.parent))
    return found


def final_name(source: dict, rel: str, skill_dir: Path) -> str:
    if rel in source.get("renames", {}):
        return source["renames"][rel]
    if source["layout"] == "flat":
        return rel
    meta, _ = split_frontmatter((skill_dir / "SKILL.md").read_text(encoding="utf-8"))
    return str(meta.get("name") or Path(rel).name)


def category_for(name: str, rel: str, cats: dict) -> str:
    """Category for and return str."""
    for category, names in cats["assign"].items():
        if name in names:
            return category
    prefix = rel.split("/")[0]
    if prefix in cats["by_prefix"]:
        return cats["by_prefix"][prefix]
    sys.exit(f"no category for skill '{name}' ({rel}); add it to third_party/categories.yaml")


def apply_patches(*, after_enrichment: bool = False) -> None:
    for patch in sorted(PATCHES.glob("*.patch")) if PATCHES.exists() else []:
        if patch.name.startswith("post-") != after_enrichment:
            continue
        subprocess.run(["git", "apply", "--whitespace=nowarn", str(patch)], cwd=ROOT, check=True)
        print(f"applied {patch.name}")


def enrich_imported(names: list[str]) -> None:
    """SOP enrichment after patches: dead links, oversize split, operating procedure, related skills."""
    skills = {s.name: s for s in load_skills()}
    stats = {"links": 0, "split": 0, "procedure": 0, "related": 0}
    for name in names:
        s = skills[name]
        stats["links"] += enrich.unlink_dead_links(s.path)
        meta, body = split_frontmatter((s.path / "SKILL.md").read_text(encoding="utf-8"))
        extra = enrich.procedure_lines(s.category) if enrich.needs_procedure(body) else 10
        stats["split"] += bool(enrich.split_oversized(s.path, enrich.MAX_LINES - extra))
        stats["procedure"] += enrich.add_procedure(load_skill(s.path))
    skills = {s.name: s for s in load_skills()}
    neighbours: dict[str, list[tuple[float, str]]] = {}
    # The collection router is an index, not a specialist recommendation.
    specialists = [s for s in skills.values() if s.name != "research-agent-skills"]
    for a, b, sim in tfidf_overlap(specialists, 0.08):
        neighbours.setdefault(a, []).append((sim, b))
        neighbours.setdefault(b, []).append((sim, a))
    for name in names:
        top = sorted(neighbours.get(name, []), reverse=True)[:3]
        related = [(b, _first_sentence(str(skills[b].meta.get("description", "")))) for _, b in top]
        stats["related"] += enrich.add_related(skills[name], related)
    print("enriched: " + ", ".join(f"{k}={v}" for k, v in stats.items()))


def _first_sentence(text: str, limit: int = 140) -> str:
    text = " ".join(text.split())
    m = re.match(r"(.+?[.!?])(\s|$)", text)
    s = m.group(1) if m else text
    return s if len(s) <= limit else s[: limit - 1].rstrip() + "…"


def main() -> None:
    """Main."""
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source-dir", type=Path, help="directory with pre-cloned checkouts named by source id")
    args = ap.parse_args()

    config = load_yaml(THIRD_PARTY / "sources.yaml")
    cats = load_yaml(THIRD_PARTY / "categories.yaml")
    old = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {"skills": []}
    protected = {s["name"] for s in old["skills"] if s.get("rewrite_status") == "original"}
    previously_imported = {s["name"] for s in old["skills"]} - protected

    entries, seen = [], {}
    for source in config["sources"]:
        src_dir = checkout(source, args.source_dir)
        for rel, skill_dir in discover(source, src_dir):
            top = rel.split("/")[-1] if source["layout"] == "flat" else rel
            if top in source.get("exclude", {}) or rel in source.get("exclude", {}):
                continue
            name = final_name(source, rel, skill_dir)
            if not NAME_RE.match(name) or len(name) > 64:
                sys.exit(f"invalid skill name '{name}' from {source['id']}:{rel}; add a rename")
            if name in seen:
                sys.exit(f"name collision '{name}': {seen[name]} vs {source['id']}:{rel}; add a rename")
            seen[name] = f"{source['id']}:{rel}"
            category = category_for(name, rel, cats)
            entry = {"name": name, "source": source["id"], "path": f"{source.get('root', '.')}/{rel}".lstrip("./"),
                     "category": category, "rewrite_status": "imported"}
            if name in protected:
                entry["rewrite_status"] = "original"
                entries.append(entry)
                continue
            dest = SKILLS_DIR / name
            if dest.exists() and old["skills"] and name not in previously_imported:
                sys.exit(f"'{name}' already exists as an original skill; add a rename for {source['id']}:{rel}")
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(skill_dir, dest, ignore=IGNORE)
            for pattern in source.get("exclude_files", []):
                for victim in SKILLS_DIR.glob(pattern):
                    if victim.is_relative_to(dest) and victim.is_file():
                        victim.unlink()
            rebrand_skill(dest, name, category)
            meta, _ = split_frontmatter((dest / "SKILL.md").read_text(encoding="utf-8"))
            entry["license"] = str(meta.get("license", ""))
            entries.append(entry)

    # Remove skills that were imported before but are now excluded upstream.
    for stale in sorted(previously_imported - set(seen)):
        shutil.rmtree(SKILLS_DIR / stale, ignore_errors=True)
        print(f"removed stale skill {stale}")

    apply_patches()
    enrich_imported([e["name"] for e in entries if e["rewrite_status"] == "imported"])
    apply_patches(after_enrichment=True)

    manifest = {
        "_comment": "Generated by tools/import_upstream.py. Provenance for THIRD_PARTY_NOTICES.md.",
        "sources": [{k: s[k] for k in ("id", "repo", "ref", "copyright", "license_file")} for s in config["sources"]],
        "skills": sorted(entries, key=lambda e: e["name"]),
    }
    write_text(MANIFEST, json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    print(f"imported {sum(e['rewrite_status'] == 'imported' for e in entries)} skills "
          f"({len(protected)} protected originals)")


if __name__ == "__main__":
    main()
