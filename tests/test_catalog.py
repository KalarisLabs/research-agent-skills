from __future__ import annotations

import json
import xml.etree.ElementTree as ET

import brand_guard
import build_catalog
from common import ROOT, load_skills, load_yaml


def test_generated_files_are_current():
    assert build_catalog.main(["--check"]) == 0


def test_marketplace_covers_every_skill_once_per_category():
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    names = {s.path.name for s in load_skills()}
    cats = load_yaml(ROOT / "third_party" / "categories.yaml")["categories"]
    category_plugins = [p for p in market["plugins"] if p["name"] in cats]
    listed = [s.split("/")[-1] for p in category_plugins for s in p["skills"]]
    assert sorted(listed) == sorted(names)
    for p in market["plugins"]:
        assert p["source"] == "./" and p["strict"] is False
        assert all(s.startswith("./skills/") and ".." not in s for s in p["skills"])


def test_release_metadata_versions_match():
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    assert json.loads((ROOT / "cli" / "package.json").read_text(encoding="utf-8"))["version"] == version
    assert json.loads((ROOT / "codemeta.json").read_text(encoding="utf-8"))["version"] == version
    assert str(load_yaml(ROOT / "CITATION.cff")["version"]) == version


def test_codex_manifest_meets_the_awesome_codex_plugins_requirements():
    """The catalog validator needs these fields and an icon file; its absence failed our listing."""
    manifest = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    for field in ("name", "version", "description", "repository", "license"):
        assert manifest[field]
    assert manifest["version"] == (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    assert manifest["skills"] == "./skills/" and (ROOT / "skills").is_dir()
    icon = manifest["interface"]["composerIcon"]
    assert icon.startswith("./") and (ROOT / icon).is_file()
    assert (ROOT / icon).stat().st_size < 50_000
    for name in ("SECURITY.md", "LICENSE", "README.md"):
        assert (ROOT / name).is_file()


def test_every_skill_has_search_tags():
    index = json.loads((ROOT / "catalog" / "skills.json").read_text(encoding="utf-8"))
    assert [s["name"] for s in index["skills"] if not s["tags"]] == []


def test_index_and_graph_consistency():
    index = json.loads((ROOT / "catalog" / "skills.json").read_text(encoding="utf-8"))
    graph = json.loads((ROOT / "catalog" / "graph.json").read_text(encoding="utf-8"))
    skill_nodes = {n["id"] for n in graph["nodes"] if n["type"] == "skill"}
    assert skill_nodes == {f"skill:{s['name']}" for s in index["skills"]}
    node_ids = {n["id"] for n in graph["nodes"]}
    assert all(e["source"] in node_ids and e["target"] in node_ids for e in graph["edges"])
    ET.parse(ROOT / "catalog" / "graph.graphml")  # well-formed XML


def test_notices_cover_all_imported_skills():
    manifest = json.loads((ROOT / "third_party" / "upstream-manifest.json").read_text(encoding="utf-8"))
    notices = (ROOT / "THIRD_PARTY_NOTICES.md").read_text(encoding="utf-8")
    for s in manifest["skills"]:
        if s["rewrite_status"] == "imported":
            assert f"`{s['name']}`" in notices
    for src in manifest["sources"]:
        assert src["copyright"] in notices


def test_brand_guard_clean():
    assert brand_guard.main([]) == 0


def test_brand_guard_detects(tmp_path):
    rules = load_yaml(ROOT / "third_party" / "rebrand-rules.yaml")
    sample = rules["replacements"][-3][0]  # an upstream name, taken from the rules file
    f = tmp_path / "leak.md"
    f.write_text(f"made by {sample}\n", encoding="utf-8")
    assert brand_guard.main([str(f)]) == 1
