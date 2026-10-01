from tools.skill_scanner_gate import finding_key


def test_finding_key_normalizes_runner_path():
    expected = "autoskill|BEHAVIOR_ENV_VAR_EXFILTRATION|scripts/backends.py"
    for path in (
        "scripts/backends.py",
        "/home/runner/work/repo/repo/skills/autoskill/scripts/backends.py",
        r"C:\runner\repo\skills\autoskill\scripts\backends.py",
    ):
        assert finding_key("autoskill", {"rule_id": "BEHAVIOR_ENV_VAR_EXFILTRATION", "file_path": path}) == expected
