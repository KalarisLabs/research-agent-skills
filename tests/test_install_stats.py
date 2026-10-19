from __future__ import annotations

import pytest

import update_install_stats as stats

CARD = ('<a class="group grid" href="/kalarislabs/research-agent-skills/{name}"><div class="min-w-0">'
        '<h3 class="font-semibold">{name}</h3></div><div class="text-right">'
        '<span class="font-mono text-sm">{n}</span></div></a>')


def page(**counts: str) -> str:
    return "<main>" + "".join(CARD.format(name=k.replace("_", "-"), n=v) for k, v in counts.items()) + "</main>"


def test_parse_counts_reads_each_card():
    html = page(citation_verification="30", apa7="1,204", scanpy="11")
    assert stats.parse_counts(html) == {"citation-verification": 30, "apa7": 1204, "scanpy": 11}


def test_parse_counts_ignores_other_repositories():
    html = page(apa7="16").replace("kalarislabs/research-agent-skills", "someone/else")
    assert stats.parse_counts(html) == {}


def test_render_table_ranks_known_skills_and_skips_collection():
    counts = {"research-agent-skills": 99, "apa7": 16, "citation-verification": 30, "not-a-skill": 50}
    table = stats.render_table(counts, "3.5K", top=10, date="2026-10-19")
    rows = [line for line in table.splitlines() if line.startswith("| ") and line[2].isdigit()]
    assert [r.split("`")[1] for r in rows] == ["citation-verification", "apa7"]
    assert "--skill citation-verification" in rows[0]
    assert "**3.5K**" in table


def test_update_readme_replaces_only_the_block():
    readme = f"top\n{stats.INSTALLS_START}\nold\n{stats.INSTALLS_END}\nbottom\n"
    out = stats.update_readme(readme, "\nnew\n")
    assert out == f"top\n{stats.INSTALLS_START}\nnew\n{stats.INSTALLS_END}\nbottom\n"
    with pytest.raises(ValueError):
        stats.update_readme("no markers", "x")
