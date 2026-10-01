from tools.snyk_agent_scan_gate import check


def test_snyk_gate_requires_full_coverage_and_blocks_high_risks(tmp_path):
    root = tmp_path / "skills"
    for name in ("safe", "risky"):
        directory = root / name
        directory.mkdir(parents=True)
        (directory / "SKILL.md").write_text(f"# {name}\n", encoding="utf-8")

    report = {"scan_path_responses": [{"path": "skills", "server_risks": [], "skill_risks": [
        {"name": "safe", "risk_indexes": {"third_party_content_exposure": {"score": 300}}},
        {"name": "risky", "risk_indexes": {"malicious_code": {"score": 600}}},
    ]}]}
    errors, warnings = check(report, root)
    assert any("malicious_code" in finding for finding in errors)
    assert any("third_party_content_exposure" in finding for finding in warnings)

    report["scan_path_responses"][0]["skill_risks"].pop()
    errors, _ = check(report, root)
    assert any("Unscanned skills: risky" in finding for finding in errors)
