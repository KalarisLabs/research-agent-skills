"""Catalog loader, search and selection helpers for research-agent-skills."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

_SKILLS_JSON = "skills.json"


@dataclass
class SkillEntry:
    """Skill entry."""
    name: str
    description: str
    category: str
    version: str
    license: str
    compatibility: str
    tags: list[str] = field(default_factory=list)
    path: str = ""
    has_scripts: bool = False
    origin: str = "adapted"


@dataclass
class Category:
    """Category."""
    id: str
    description: str
    count: int


@dataclass
class Bundle:
    """Bundle."""
    description: str
    categories: list[str] = field(default_factory=list)
    skills: list[str] = field(default_factory=list)


class Catalog:
    """Catalog."""
    def __init__(self, data: dict[str, Any]):
        """Initialise the instance."""
        self.name: str = data.get("name", "research-agent-skills")
        self.version: str = data.get("version", "1.1.0")
        self.repository: str = data.get("repository", "https://github.com/KalarisLabs/research-agent-skills")
        self.categories: list[Category] = [
            Category(id=c["id"], description=c.get("description", ""), count=c.get("count", 0))
            for c in data.get("categories", [])
        ]
        self.bundles: dict[str, Bundle] = {
            k: Bundle(
                description=v.get("description", ""),
                categories=v.get("categories", []),
                skills=v.get("skills", []),
            )
            for k, v in data.get("bundles", {}).items()
        }
        self.skills: list[SkillEntry] = [
            SkillEntry(
                name=s["name"],
                description=s.get("description", ""),
                category=s.get("category", ""),
                version=s.get("version", "1.0"),
                license=s.get("license", "MIT"),
                compatibility=s.get("compatibility", ""),
                tags=s.get("tags", []),
                path=s.get("path", f"skills/{s['name']}"),
                has_scripts=s.get("has_scripts", False),
                origin=s.get("origin", "adapted"),
            )
            for s in data.get("skills", [])
        ]
        self._by_name: dict[str, SkillEntry] = {s.name: s for s in self.skills}

    def get_skill(self, name: str) -> SkillEntry | None:
        """Get skill."""
        return self._by_name.get(name)

    def search(self, query: str) -> list[SkillEntry]:
        """Search."""
        q = query.lower().strip()
        if not q:
            return self.skills
        results: list[tuple[int, SkillEntry]] = []
        for s in self.skills:
            score = 0
            if q == s.name:
                score += 100
            elif q in s.name:
                score += 40
            if q in s.category:
                score += 20
            if any(q in t.lower() for t in s.tags):
                score += 15
            if q in s.description.lower():
                score += 10
            if score > 0:
                results.append((score, s))
        results.sort(key=lambda x: (-x[0], x[1].name))
        return [s for _, s in results]

    def select(
        self,
        names: list[str] | None = None,
        categories: list[str] | None = None,
        bundles: list[str] | None = None,
        all_skills: bool = False,
    ) -> list[SkillEntry]:
        """Select."""
        if all_skills:
            return list(self.skills)

        chosen: dict[str, SkillEntry] = {}
        for n in names or []:
            s = self.get_skill(n)
            if not s:
                raise ValueError(f"unknown skill '{n}' (try: research-agent-skills search {n})")
            chosen[n] = s

        cats = set(categories or [])
        for b in bundles or []:
            bundle = self.bundles.get(b)
            if not bundle:
                known = ", ".join(self.bundles.keys())
                raise ValueError(f"unknown bundle '{b}'. Known: {known}")
            cats.update(bundle.categories)
            for skill_name in bundle.skills:
                s = self.get_skill(skill_name)
                if not s:
                    raise ValueError(f"bundle '{b}' references unknown skill '{skill_name}'")
                chosen[s.name] = s

        for c in cats:
            if not any(cat.id == c for cat in self.categories):
                known_cats = ", ".join(c_obj.id for c_obj in self.categories)
                raise ValueError(f"unknown category '{c}'. Known: {known_cats}")
            for s in self.skills:
                if s.category == c:
                    chosen[s.name] = s

        return sorted(chosen.values(), key=lambda s: s.name)


def load_catalog(custom_path: Path | None = None) -> Catalog:
    """Load catalog from bundled data, custom path, or repository root."""
    paths_to_try: list[Path] = []
    if custom_path:
        paths_to_try.append(custom_path)

    # 1. Look inside package data directory
    pkg_dir = Path(__file__).resolve().parent
    paths_to_try.append(pkg_dir / "data" / _SKILLS_JSON)
    paths_to_try.append(pkg_dir / _SKILLS_JSON)

    # 2. Look in repository root if working inside checkout
    root = pkg_dir.parents[1]
    paths_to_try.append(root / "catalog" / _SKILLS_JSON)

    for p in paths_to_try:
        if p.is_file():
            try:
                data = json.loads(p.read_text(encoding="utf-8"))
                return Catalog(data)
            except (json.JSONDecodeError, OSError):
                pass

    # Minimal fallback catalog
    return Catalog({"name": "research-agent-skills", "version": "1.1.0", "skills": [], "categories": []})
