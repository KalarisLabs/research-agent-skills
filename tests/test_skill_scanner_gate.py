import json

from tools.skill_scanner_gate import filter_sarif, finding_key, sarif_key


def test_finding_key_normalizes_runner_path():
    expected = "autoskill|BEHAVIOR_ENV_VAR_EXFILTRATION|scripts/backends.py"
    for path in (
        "scripts/backends.py",
        "/home/runner/work/repo/repo/skills/autoskill/scripts/backends.py",
        r"C:\runner\repo\skills\autoskill\scripts\backends.py",
    ):
        assert finding_key("autoskill", {"rule_id": "BEHAVIOR_ENV_VAR_EXFILTRATION", "file_path": path}) == expected


def _result(rule, uri):
    return {"ruleId": rule, "locations": [{"physicalLocation": {"artifactLocation": {"uri": uri}}}]}


def test_sarif_key_matches_baseline_format():
    assert sarif_key(_result("R", "skills/model-pruning/SKILL.md")) == ("model-pruning|R|skill.md", "model-pruning|R|")
    runner = "/home/runner/work/research-agent-skills/research-agent-skills/skills/autoskill/scripts/run.py"
    assert sarif_key(_result("R", runner))[0] == "autoskill|R|scripts/run.py"
    nested = "skills/research-agent-skills/references/catalog.md"
    assert sarif_key(_result("R", nested))[0] == "research-agent-skills|R|references/catalog.md"
    assert sarif_key(_result("R", "tools/x.py")) is None


def test_filter_sarif_drops_only_baselined_results(tmp_path):
    sarif = {"runs": [{"results": [
        _result("MDBLOCK_PYTHON_EVAL_EXEC", "skills/modal/references/functions.md"),   # accepted by file
        _result("BEHAVIOR_CROSSFILE_EXFILTRATION_CHAIN", "skills/infographics/SKILL.md"),  # accepted cross-file key
        _result("NEW_RULE", "skills/modal/references/functions.md"),                   # not reviewed: kept
    ]}]}
    path = tmp_path / "r.sarif"
    path.write_text(json.dumps(sarif), encoding="utf-8")
    accepted = {"modal|MDBLOCK_PYTHON_EVAL_EXEC|references/functions.md",
                "infographics|BEHAVIOR_CROSSFILE_EXFILTRATION_CHAIN|"}
    assert filter_sarif(path, accepted) == (1, 2)
    left = json.loads(path.read_text(encoding="utf-8"))["runs"][0]["results"]
    assert [r["ruleId"] for r in left] == ["NEW_RULE"]
