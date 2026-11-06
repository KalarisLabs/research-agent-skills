"""Skill installation, locking and verification logic for Python CLI."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import tarfile
import urllib.request
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from .catalog import Catalog, SkillEntry

LOCK_NAME = ".research-agent-skills.lock.json"
REPO_SLUG = "KalarisLabs/research-agent-skills"


def compute_sha256(path: Path) -> str:
    """Compute sha256."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def read_lock(skills_dir: Path) -> dict[str, Any] | None:
    """Read lock."""
    lock_file = skills_dir / LOCK_NAME
    if lock_file.is_file():
        try:
            return json.loads(lock_file.read_text(encoding="utf-8"))
        except Exception:
            return None
    return None


def write_lock(skills_dir: Path, lock: dict[str, Any]) -> None:
    """Write lock."""
    lock["updatedAt"] = datetime.now(UTC).isoformat()
    lock_file = skills_dir / LOCK_NAME
    lock_file.write_text(json.dumps(lock, indent=2) + "\n", encoding="utf-8")


def locate_local_skills_root() -> Path | None:
    """Find local checkout skills/ directory if running inside git clone."""
    cur = Path(__file__).resolve().parent
    for parent in [cur, *cur.parents]:
        skills_candidate = parent / "skills"
        if skills_candidate.is_dir() and (skills_candidate / "citation-verification" / "SKILL.md").is_file():
            return skills_candidate
    return None


def download_release_tarball(version: str, cache_dir: Path) -> Path:
    """Download and cache GitHub release tarball for standalone use."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    tar_path = cache_dir / f"research-agent-skills-{version}.tar.gz"
    if tar_path.is_file():
        return tar_path

    url = f"https://github.com/{REPO_SLUG}/releases/download/v{version}/research-agent-skills-{version}.tar.gz"
    # Fallback to main branch archive if release tag not yet created
    fallback_url = f"https://github.com/{REPO_SLUG}/archive/refs/heads/main.tar.gz"

    for u in (url, fallback_url):
        try:
            req = urllib.request.Request(u, headers={"User-Agent": "research-agent-skills-python"})
            with urllib.request.urlopen(req, timeout=30) as resp, open(tar_path, "wb") as out:
                shutil.copyfileobj(resp, out)
            return tar_path
        except Exception:
            if tar_path.exists():
                tar_path.unlink()
            continue

    raise RuntimeError(f"failed to download skills release archive from {url} or {fallback_url}")


def extract_skill_from_tar(tar_path: Path, skill_name: str, dest_dir: Path) -> None:
    """Extract a specific skill folder from the tarball into dest_dir."""
    with tarfile.open(tar_path, "r:*") as tar:
        # Find prefix (e.g., research-agent-skills-1.1.0/skills/skill-name/...)
        prefix = None
        for member in tar.getmembers():
            parts = Path(member.name).parts
            if "skills" in parts:
                idx = parts.index("skills")
                if len(parts) > idx + 1 and parts[idx + 1] == skill_name:
                    prefix = "/".join(parts[: idx + 2])
                    break

        if not prefix:
            raise RuntimeError(f"skill '{skill_name}' not found in archive {tar_path}")

        dest_dir.mkdir(parents=True, exist_ok=True)
        for member in tar.getmembers():
            if member.name.startswith(prefix):
                rel_path = member.name[len(prefix) :].lstrip("/\\")
                if not rel_path:
                    continue
                target_path = dest_dir / rel_path
                if member.isdir():
                    target_path.mkdir(parents=True, exist_ok=True)
                elif member.isreg():
                    target_path.parent.mkdir(parents=True, exist_ok=True)
                    with tar.extractfile(member) as src, open(target_path, "wb") as dst:
                        if src:
                            shutil.copyfileobj(src, dst)


def install_skills_to_dir(
    skills: list[SkillEntry],
    target_dir: Path,
    catalog: Catalog,
    mode: str = "copy",
    force: bool = False,
    dry_run: bool = False,
) -> list[str]:
    """Install skills to target directory and update lockfile."""
    installed: list[str] = []
    if dry_run:
        return [s.name for s in skills]

    target_dir.mkdir(parents=True, exist_ok=True)
    lock = read_lock(target_dir) or {
        "tool": "research-agent-skills",
        "version": catalog.version,
        "origin": catalog.repository,
        "skills": {},
    }

    local_root = locate_local_skills_root()
    cache_dir = Path.home() / ".cache" / "research-agent-skills"

    tar_path: Path | None = None
    if not local_root:
        tar_path = download_release_tarball(catalog.version, cache_dir)

    for s in skills:
        dest_skill_dir = target_dir / s.name
        if dest_skill_dir.exists():
            if not force and s.name not in lock.get("skills", {}):
                print(f"Skipping existing skill '{s.name}' (not installed by this tool; use --force)")
                continue
            if dest_skill_dir.is_symlink() or dest_skill_dir.is_file():
                dest_skill_dir.unlink()
            else:
                shutil.rmtree(dest_skill_dir)

        if local_root:
            src_skill_dir = local_root / s.name
            if not src_skill_dir.is_dir():
                print(f"Warning: local skill folder '{src_skill_dir}' not found")
                continue
            if mode == "symlink":
                try:
                    os.symlink(src_skill_dir, dest_skill_dir, target_is_directory=True)
                except OSError:
                    shutil.copytree(src_skill_dir, dest_skill_dir)
            else:
                shutil.copytree(src_skill_dir, dest_skill_dir)
        else:
            if tar_path:
                extract_skill_from_tar(tar_path, s.name, dest_skill_dir)

        # Record file hashes in lock
        file_hashes: dict[str, str] = {}
        if dest_skill_dir.is_dir() and not dest_skill_dir.is_symlink():
            for f in dest_skill_dir.rglob("*"):
                if f.is_file():
                    rel = str(f.relative_to(dest_skill_dir)).replace("\\", "/")
                    file_hashes[rel] = compute_sha256(f)

        lock["skills"][s.name] = {
            "version": s.version,
            "mode": mode if not dest_skill_dir.is_symlink() else "symlink",
            "files": file_hashes,
        }
        installed.append(s.name)

    write_lock(target_dir, lock)
    return installed
