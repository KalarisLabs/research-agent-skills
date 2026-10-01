"""Generate every derived artifact from skills/ and third_party/.

Outputs (all committed except docs pages):
    .claude-plugin/marketplace.json   Claude Code plugin marketplace (one plugin per category + bundles)
    plugin.json                       Agent Plugins 1.0 manifest (Codex, Cursor, Copilot, gh skill)
    catalog/skills.json               machine-readable index used by the CLI and docs
    catalog/graph.json                skills/categories knowledge graph (nodes + edges)
    catalog/graph.graphml             same graph as GraphML (Gephi, yEd, NetworkX, graph tools)
    skills.sh.json                    skills.sh repository page groupings
    skills/research-agent-skills/references/catalog.md  bundled offline skill index
    THIRD_PARTY_NOTICES.md            upstream copyright + license notices for imported skills
    README.md                         skill catalog tables between <!-- catalog:start/end --> markers
    docs/skills/*.md                  (with --docs) one page per skill for the documentation site

Usage:
    uv run tools/build_catalog.py           # write outputs
    uv run tools/build_catalog.py --check   # exit 1 if any committed output is stale (CI)
    uv run tools/build_catalog.py --docs    # also generate docs/skills pages
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (  # noqa: E402
    BRAND,
    DOCS_URL,
    PROJECT_NAME,
    REPO_SLUG,
    REPO_URL,
    ROOT,
    THIRD_PARTY,
    Skill,
    load_skills,
    load_yaml,
    write_text,
)

VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
MARKETPLACE_NAME = "research-agent-skills"
KEYWORDS = [
    "agent-skills", "claude-code", "codex", "cursor", "gemini-cli", "research", "scientific-writing",
    "research-paper", "literature-review", "citations", "latex", "academic-writing", "peer-review",
    "bioinformatics", "cheminformatics", "machine-learning", "llm", "ai-agents",
]
BUNDLES = {
    "research-essentials": ("Everything for writing and publishing research: paper writing, journal formats, "
                            "literature review, citations, ideation and figures.",
                            ["research-writing", "journal-formats", "literature-review", "ideation-and-design",
                             "visualization-and-presentation"]),
}
CURATED_BUNDLES = {
    "ml-research": ("Machine learning experiments, training, evaluation and reproducible papers.", [
        "ml-paper-writing", "exploratory-data-analysis", "scikit-learn", "pytorch-lightning",
        "transformers", "ml-training-recipes", "huggingface-accelerate", "evaluating-llms-harness",
        "shap", "statistical-analysis", "reproducibility-statement", "academic-plotting",
    ]),
    "ai-research": ("AI agents, language models, retrieval, evaluation and research papers.", [
        "ml-paper-writing", "dspy", "instructor", "llamaindex", "paper-corpus-rag",
        "research-knowledge-graph", "research-skill-creator", "autoresearch",
        "evaluating-llms-harness", "transformer-lens-interpretability", "citation-verification",
        "reproducibility-statement",
    ]),
    "biology-research": ("Genomics and bioinformatics, from data analysis to publication.", [
        "anndata", "biopython", "scanpy", "scvi-tools", "pydeseq2", "pathway-enrichment",
        "nextflow", "database-lookup", "statistical-analysis", "scientific-visualization",
        "citation-verification", "scientific-writing",
    ]),
    "chemistry-research": ("Cheminformatics, molecular modelling and research reporting.", [
        "rdkit", "datamol", "deepchem", "medchem", "molecular-dynamics", "pymatgen",
        "statistical-analysis", "scientific-visualization", "citation-verification", "scientific-writing",
    ]),
    "medicine-research": ("Clinical and biomedical evidence, imaging, systematic reviews and writing.", [
        "clinical-reports", "pydicom", "pathml", "pyhealth", "systematic-review-prisma",
        "statistical-analysis", "citation-verification", "literature-review", "scientific-writing",
        "reproducibility-statement",
    ]),
    "physics-research": ("Physics, astronomy, quantum computing, materials and reproducible figures.", [
        "astropy", "qiskit", "qutip", "pymatgen", "sympy", "matlab",
        "scientific-visualization", "statistical-analysis", "reproducibility-statement",
        "citation-verification", "scientific-writing",
    ]),
}

DIRECTORY_GROUPS = [
    ("Academic writing", "Papers, theses, citations, literature reviews and journal formats.",
     ["research-writing", "journal-formats", "literature-review"]),
    ("Research methods", "Research design, data sources, knowledge retrieval and automation.",
     ["ideation-and-design", "knowledge-and-rag", "scientific-databases", "research-automation"]),
    ("Machine learning", "Data science, model training, evaluation and deployment.",
     ["data-science-and-ml", "ml-training", "ml-evaluation-and-safety", "ml-inference-and-ops"]),
    ("Artificial intelligence", "Language models, agents and multimodal research.",
     ["llm-applications", "multimodal-and-emerging"]),
    ("Biology", "Bioinformatics, life sciences and lab automation.",
     ["life-sciences", "lab-automation"]),
    ("Chemistry", "Cheminformatics, drug discovery and molecular research.",
     ["chemistry-and-drug-discovery"]),
    ("Medicine", "Clinical, biomedical and health research.",
     ["clinical-and-health"]),
    ("Physics", "Physics, astronomy, quantum and materials science.",
     ["physical-sciences"]),
    ("Figures and slides", "Scientific visualization, schematics and presentations.",
     ["visualization-and-presentation"]),
]


def bundle_definitions(skills: list[Skill]) -> dict[str, dict]:
    known = {s.name for s in skills}
    out = {name: {"description": description, "categories": categories, "skills": []}
           for name, (description, categories) in BUNDLES.items()}
    for name, (description, names) in CURATED_BUNDLES.items():
        missing = set(names) - known
        if missing:
            raise ValueError(f"{name} references missing skills: {', '.join(sorted(missing))}")
        out[name] = {"description": description, "categories": [], "skills": names}
    return out


def bundle_skill_names(bundle: dict, index: dict) -> list[str]:
    cats = set(bundle["categories"])
    return sorted(set(bundle["skills"]) | {e["name"] for e in index["skills"] if e["category"] in cats})
CATALOG_START, CATALOG_END = "<!-- catalog:start -->", "<!-- catalog:end -->"
COUNT_RE = re.compile(r"<!-- count -->\d+\+?<!-- /count -->")


def _json(data: object) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def _first_sentence(text: str, limit: int = 160) -> str:
    text = " ".join(text.split())
    m = re.match(r"(.+?[.!?])(\s|$)", text)
    s = m.group(1) if m else text
    return s if len(s) <= limit else s[: limit - 1].rstrip() + "…"


def build_index(skills: list[Skill], cats: dict, manifest: dict) -> dict:
    origin = {s["name"]: s["rewrite_status"] for s in manifest.get("skills", [])}
    entries = []
    for s in skills:
        md = s.metadata
        entries.append({
            "name": s.name,
            "description": " ".join(str(s.meta.get("description", "")).split()),
            "category": s.category,
            "version": md.get("version", ""),
            "license": s.meta.get("license", ""),
            "compatibility": s.meta.get("compatibility", ""),
            "tags": [t.strip() for t in str(md.get("tags", "")).split(",") if t.strip()],
            "path": f"skills/{s.path.name}",
            "has_scripts": (s.path / "scripts").is_dir(),
            "origin": "original" if origin.get(s.name, "original") == "original" else "adapted",
        })
    return {
        "name": MARKETPLACE_NAME,
        "version": VERSION,
        "repository": REPO_URL,
        "categories": [{"id": k, "description": v, "count": sum(e["category"] == k for e in entries)}
                       for k, v in cats["categories"].items()],
        "bundles": bundle_definitions(skills),
        "skills": entries,
    }


def build_marketplace(index: dict) -> dict:
    by_cat: dict[str, list[str]] = defaultdict(list)
    for e in index["skills"]:
        by_cat[e["category"]].append(f"./{e['path']}")
    plugins = []
    for bundle, definition in index["bundles"].items():
        plugins.append({"name": bundle, "description": definition["description"], "source": "./", "strict": False,
                        "skills": [f"./skills/{name}" for name in bundle_skill_names(definition, index)]})
    for cat in index["categories"]:
        if by_cat.get(cat["id"]):
            plugins.append({"name": cat["id"], "description": f"{cat['description']}.", "source": "./",
                            "strict": False, "skills": sorted(by_cat[cat["id"]])})
    return {
        "name": MARKETPLACE_NAME,
        "owner": {"name": BRAND, "url": REPO_URL},
        "metadata": {"description": f"{PROJECT_NAME}: {len(index['skills'])} agent skills for scientific research, "
                                    "paper writing, literature review and domain science.",
                     "version": VERSION},
        "plugins": plugins,
    }


def build_plugin_manifest(index: dict) -> dict:
    return {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "name": MARKETPLACE_NAME,
        "version": VERSION,
        "description": (f"{len(index['skills'])} Agent Skills for researchers: scientific and research paper writing, "
                        "journal formats, literature review, citations, data science, ML research and domain science."),
        "author": {"name": BRAND, "url": REPO_URL},
        "homepage": REPO_URL,
        "repository": REPO_URL,
        "license": "MIT",
        "keywords": KEYWORDS,
    }


def build_skills_sh_config(index: dict) -> dict:
    category_ids = {c["id"] for c in index["categories"]}
    grouped_ids = {category for _, _, categories in DIRECTORY_GROUPS for category in categories}
    if category_ids != grouped_ids:
        raise ValueError(f"skills.sh category mapping differs: {category_ids ^ grouped_ids}")
    featured = "research-agent-skills"
    if featured not in {entry["name"] for entry in index["skills"]}:
        raise ValueError(f"missing collection skill: {featured}")
    groups = [{"title": "Full collection", "description": "Research Agent Skills by Kalaris Labs.",
               "skills": [featured]}]
    seen = {featured}
    for title, description, categories in DIRECTORY_GROUPS:
        names = [entry["name"] for entry in index["skills"]
                 if entry["category"] in categories and entry["name"] not in seen]
        seen.update(names)
        groups.append({"title": title, "description": description, "skills": names})
    missing = {entry["name"] for entry in index["skills"]} - seen
    if missing:
        raise ValueError(f"skills.sh grouping omits: {', '.join(sorted(missing))}")
    return {"$schema": "https://skills.sh/schemas/skills.sh.schema.json",
            "notGrouped": "bottom", "groupings": groups}


def build_collection_reference(index: dict) -> str:
    lines = ["# Research Agent Skills index", "",
             f"{len(index['skills']) - 1} specialist skills in this Kalaris Labs collection.",
             "Select a specialist by the research task; install the full collection only when requested.", ""]
    for title, _, categories in DIRECTORY_GROUPS:
        lines += [f"## {title}", ""]
        lines += [f"- `{entry['name']}` — {_first_sentence(entry['description'])}"
                  for entry in index["skills"]
                  if entry["category"] in categories and entry["name"] != "research-agent-skills"]
        lines.append("")
    return "\n".join(lines)


SKILL_REF_RE = re.compile(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`")


def build_graph(skills: list[Skill], index: dict) -> dict:
    names = {s.name for s in skills}
    nodes = [{"id": f"category:{c['id']}", "type": "category", "label": c["id"], "description": c["description"]}
             for c in index["categories"]]
    edges = []
    for s, e in zip(skills, index["skills"], strict=True):
        nodes.append({"id": f"skill:{s.name}", "type": "skill", "label": s.name, "description": e["description"],
                      "category": e["category"], "path": e["path"]})
        edges.append({"source": f"skill:{s.name}", "target": f"category:{e['category']}", "type": "in_category"})
        refs = {m for m in SKILL_REF_RE.findall(s.body) if m in names and m != s.name}
        edges.extend({"source": f"skill:{s.name}", "target": f"skill:{r}", "type": "references"} for r in sorted(refs))
    return {"directed": True, "generator": f"{MARKETPLACE_NAME} {VERSION}", "nodes": nodes, "edges": edges}


def graph_to_graphml(graph: dict) -> str:
    keys = [("type", "node"), ("label", "node"), ("description", "node"), ("category", "node"), ("path", "node"),
            ("type", "edge")]
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<graphml xmlns="http://graphml.graphdrawing.org/xmlns">']
    for i, (k, scope) in enumerate(keys):
        out.append(f'  <key id="{scope[0]}{i}" for="{scope}" attr.name="{k}" attr.type="string"/>')
    out.append('  <graph id="research-agent-skills" edgedefault="directed">')
    for n in graph["nodes"]:
        out.append(f'    <node id="{escape(n["id"], {chr(34): "&quot;"})}">')
        for i, (k, scope) in enumerate(keys):
            if scope == "node" and n.get(k):
                out.append(f'      <data key="n{i}">{escape(str(n[k]))}</data>')
        out.append("    </node>")
    for j, e in enumerate(graph["edges"]):
        out.append(f'    <edge id="e{j}" source="{escape(e["source"])}" target="{escape(e["target"])}">'
                   f'<data key="e5">{e["type"]}</data></edge>')
    out += ["  </graph>", "</graphml>", ""]
    return "\n".join(out)


def build_notices(manifest: dict) -> str:
    by_source: dict[str, list[str]] = defaultdict(list)
    for s in manifest.get("skills", []):
        if s["rewrite_status"] == "imported":
            by_source[s["source"]].append(s["name"])
    lines = [
        "# Third-Party Notices",
        "",
        f"{PROJECT_NAME} is © {BRAND} and distributed under the MIT License (see `LICENSE`).",
        "",
        "Some skills in `skills/` are adapted from third-party projects licensed under the MIT License. "
        "As that license requires, their copyright and permission notices are reproduced below and in `LICENSES/`. "
        "Per-skill provenance (source path and pinned revision) is recorded in `third_party/upstream-manifest.json`.",
        "",
        "Individual skills may also describe or bundle material under its own license (for example LaTeX "
        "templates from publishers, or the `license:` field in a skill's frontmatter naming the license of the "
        "software it documents). Those terms apply to that material.",
        "",
    ]
    for src in manifest.get("sources", []):
        names = sorted(by_source.get(src["id"], []))
        if not names:
            continue
        lic = (ROOT / src["license_file"]).read_text(encoding="utf-8").strip()
        lines += [f"## {src['repo'].removesuffix('.git').split('github.com/')[-1]}", "",
                  f"- Source: {src['repo'].removesuffix('.git')} (revision `{src['ref'][:12]}`)",
                  f"- {src['copyright']}",
                  f"- Skills ({len(names)}): {', '.join(f'`{n}`' for n in names)}", "",
                  "```text", lic, "```", ""]
    return "\n".join(lines).rstrip() + "\n"


def build_readme_catalog(index: dict) -> str:
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for e in index["skills"]:
        by_cat[e["category"]].append(e)
    parts = [CATALOG_START, ""]
    for cat in index["categories"]:
        items = by_cat.get(cat["id"])
        if not items:
            continue
        parts += [f"<details><summary><b>{cat['id']}</b> ({len(items)}) · {cat['description']}</summary>", "",
                  "| Skill | What it does |", "|---|---|"]
        parts += [f"| [`{e['name']}`]({e['path']}/SKILL.md) | {_first_sentence(e['description']).replace('|', '/')} |"
                  for e in items]
        parts += ["", "</details>", ""]
    parts.append(CATALOG_END)
    return "\n".join(parts)


def build_llms_txt(index: dict) -> str:
    """llms.txt (https://llmstxt.org): a Markdown index that AI search engines and agents can read."""
    raw = f"https://raw.githubusercontent.com/{REPO_SLUG}/main"
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for e in index["skills"]:
        by_cat[e["category"]].append(e)
    out = [f"# {PROJECT_NAME}", "",
           f"> {len(index['skills'])} open-source Agent Skills (SKILL.md) for academic research by {BRAND}: "
           "research paper and thesis writing without AI slop, journal formatting (Nature, Science, Cell, IEEE, "
           "ACM, Elsevier, Springer LNCS, PLOS, APA 7, arXiv), literature and systematic reviews (PRISMA 2020), "
           "citation verification, and 100+ scientific databases and analysis packages. "
           "Install: `npx research-agent-skills`.",
           "", "## Docs", "",
           f"- [README]({raw}/README.md): overview, installation for Claude Code, Codex, Cursor, Gemini CLI, Copilot",
           f"- [Documentation site]({DOCS_URL}): guides for papers, theses, systematic reviews",
           f"- [Machine-readable catalog]({raw}/catalog/skills.json): every skill with category and description",
           f"- [Benchmarks]({raw}/benchmarks/README.md): how skills are evaluated", ""]
    for cat in index["categories"]:
        items = by_cat.get(cat["id"])
        if not items:
            continue
        out += [f"## {cat['id']}", ""]
        out += [f"- [{e['name']}]({raw}/{e['path']}/SKILL.md): {_first_sentence(e['description'], 200)}" for e in items]
        out.append("")
    return "\n".join(out)


def update_readme(readme: str, index: dict) -> str:
    if CATALOG_START in readme and CATALOG_END in readme:
        pre, rest = readme.split(CATALOG_START, 1)
        _, post = rest.split(CATALOG_END, 1)
        readme = pre + build_readme_catalog(index) + post
    count = len(index["skills"]) // 10 * 10
    return COUNT_RE.sub(f"<!-- count -->{count}+<!-- /count -->", readme)


def build_docs(skills: list[Skill], index: dict) -> dict[Path, str]:
    pages: dict[Path, str] = {}
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for s, e in zip(skills, index["skills"], strict=True):
        by_cat[e["category"]].append(e)
        pages[ROOT / "docs" / "skills" / f"{s.name}.md"] = "\n".join([
            "---",
            f"title: \"{s.name} — AI agent skill for {e['category'].replace('-', ' ')}\"",
            f"description: {json.dumps(_first_sentence(e['description'], 155), ensure_ascii=False)}",
            "---", "",
            f"# `{s.name}`", "",
            f"> {e['description']}", "",
            f"**Category:** [{e['category']}](/skills#{e['category']}) · **License:** {e['license'] or 'MIT'} · "
            f"**Version:** {e['version']}", "",
            "## Install", "",
            "```bash",
            f"npx research-agent-skills install {s.name}",
            f"npx skills add {REPO_SLUG} --skill {s.name}",
            "```", "",
            "## When to use it", "",
            e["description"], "",
            "## Full playbook", "",
            f"Read [SKILL.md]({REPO_URL}/blob/main/{e['path']}/SKILL.md) for the complete workflow, "
            "references and any scripts. The agent installer copies the full skill folder.",
            "",
        ])
    idx = ["---", "title: Skill catalog", f"description: All {len(skills)} research agent skills by category.",
           "---", "", "# Skill catalog", ""]
    for cat in index["categories"]:
        if by_cat.get(cat["id"]):
            idx += [f"## {cat['id']}", "", f"{cat['description']}.", ""]
            idx += [f"- [`{e['name']}`](/skills/{e['name']}) — {_first_sentence(e['description'])}"
                    for e in by_cat[cat["id"]]]
            idx.append("")
    pages[ROOT / "docs" / "skills" / "index.md"] = "\n".join(idx)
    return pages


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="fail if committed outputs are out of date")
    ap.add_argument("--docs", action="store_true", help="also generate docs/skills pages")
    args = ap.parse_args(argv)

    skills = load_skills()
    cats = load_yaml(THIRD_PARTY / "categories.yaml")
    manifest_path = THIRD_PARTY / "upstream-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    index = build_index(skills, cats, manifest)
    graph = build_graph(skills, index)
    readme_path = ROOT / "README.md"

    outputs: dict[Path, str] = {
        ROOT / ".claude-plugin" / "marketplace.json": _json(build_marketplace(index)),
        ROOT / "plugin.json": _json(build_plugin_manifest(index)),
        ROOT / "catalog" / "skills.json": _json(index),
        ROOT / "catalog" / "graph.json": _json(graph),
        ROOT / "catalog" / "graph.graphml": graph_to_graphml(graph),
        ROOT / "skills.sh.json": _json(build_skills_sh_config(index)),
        ROOT / "skills" / "research-agent-skills" / "references" / "catalog.md": build_collection_reference(index),
        ROOT / "THIRD_PARTY_NOTICES.md": build_notices(manifest),
        ROOT / "llms.txt": build_llms_txt(index),
        ROOT / "docs" / "llms.txt": build_llms_txt(index),
    }
    # Plain-text skill lists for the shell installers' no-Node fallback.
    for cat in index["categories"]:
        names = [e["name"] for e in index["skills"] if e["category"] == cat["id"]]
        outputs[ROOT / "catalog" / "lists" / f"{cat['id']}.txt"] = "".join(f"{n}\n" for n in names)
    for bundle, definition in index["bundles"].items():
        names = bundle_skill_names(definition, index)
        outputs[ROOT / "catalog" / "lists" / f"{bundle}.txt"] = "".join(f"{n}\n" for n in names)
    outputs[ROOT / "catalog" / "lists" / "all.txt"] = "".join(f"{e['name']}\n" for e in index["skills"])
    if readme_path.exists():
        outputs[readme_path] = update_readme(readme_path.read_text(encoding="utf-8"), index)

    if args.check:
        stale = [p.relative_to(ROOT).as_posix() for p, text in outputs.items()
                 if not p.exists() or p.read_text(encoding="utf-8") != text]
        if stale:
            print("stale generated files (run `uv run tools/build_catalog.py`):\n  " + "\n  ".join(stale))
            return 1
        print(f"generated files up to date ({len(skills)} skills)")
        return 0

    if args.docs:
        outputs.update(build_docs(skills, index))
    changed = [p.relative_to(ROOT).as_posix() for p, text in outputs.items() if write_text(p, text)]
    detail = (":\n  " + "\n  ".join(changed[:20])) if changed else ""
    print(f"{len(skills)} skills; {len(changed)} files updated{detail}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
