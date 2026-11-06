from __future__ import annotations

import json

import posthog_ci as p


def _capture(monkeypatch):
    sent = []
    monkeypatch.setattr(p, "_request", lambda url, data=None, headers=None: sent.append((url, data)) or {})
    return sent


def test_send_is_noop_without_key(monkeypatch):
    sent = _capture(monkeypatch)
    monkeypatch.delenv("POSTHOG_PROJECT_KEY", raising=False)
    p.send([{"event": "x", "properties": {}}])
    assert sent == []


def test_send_posts_anonymous_batch(monkeypatch):
    sent = _capture(monkeypatch)
    monkeypatch.setenv("POSTHOG_PROJECT_KEY", "phc_test")
    p.send([{"event": "x", "properties": {"a": 1}}])
    url, data = sent[0]
    body = json.loads(data)
    assert url.endswith("/batch/") and body["api_key"] == "phc_test"
    props = body["batch"][0]["properties"]
    assert props["$process_person_profile"] is False and props["a"] == 1


def test_request_refuses_non_https():
    assert p._request("http://example.com") is None
    assert p._request("file:///etc/passwd") is None


def test_seconds():
    assert p._seconds("2026-01-01T00:00:00Z", "2026-01-01T00:01:30Z") == 90
    assert p._seconds(None, "2026-01-01T00:00:00Z") is None
    assert p._seconds("bad", "bad") is None


def test_catalog_stats_reports_real_counts():
    props = p.catalog_stats_events()[0]["properties"]
    assert props["skill_count"] > 200 and props["skills_below_80"] == 0


def test_workflow_run_events_include_failure_exception(monkeypatch, tmp_path):
    event = tmp_path / "event.json"
    event.write_text(
        json.dumps(
            {
                "workflow_run": {
                    "name": "Tests",
                    "id": 7,
                    "event": "pull_request",
                    "head_branch": "feat",
                    "head_sha": "abcdef1234567890",
                    "conclusion": "failure",
                    "run_started_at": "2026-01-01T00:00:00Z",
                    "updated_at": "2026-01-01T00:02:00Z",
                }
            }
        )
    )
    monkeypatch.setenv("GITHUB_EVENT_PATH", str(event))
    jobs = {
        "jobs": [
            {
                "name": "unit",
                "conclusion": "failure",
                "started_at": "2026-01-01T00:00:00Z",
                "completed_at": "2026-01-01T00:01:00Z",
                "steps": [{"name": "pytest", "conclusion": "failure"}],
            },
            {"name": "lint", "conclusion": "success"},
        ]
    }
    monkeypatch.setattr(p, "_github", lambda path: jobs)
    events = p.workflow_run_events()
    names = [e["event"] for e in events]
    assert names == ["ci_workflow_completed", "ci_job_completed", "$exception", "ci_job_completed"]
    assert events[0]["properties"]["duration_seconds"] == 120 and events[0]["properties"]["is_pull_request"]
    assert events[2]["properties"]["failed_steps"] == ["pytest"]


def test_release_and_snapshot_events(monkeypatch, tmp_path):
    event = tmp_path / "event.json"
    event.write_text(json.dumps({"release": {"tag_name": "v1", "assets": [{}], "prerelease": False}}))
    monkeypatch.setenv("GITHUB_EVENT_PATH", str(event))
    assert p.release_events()[0]["properties"]["tag"] == "v1"

    def fake_github(path):
        if "pulls" in path:
            return [{}, {}]
        if "releases" in path:
            return [{"assets": [{"download_count": 3}]}]
        return {"stargazers_count": 5, "forks_count": 1}

    monkeypatch.setattr(p, "_github", fake_github)
    monkeypatch.setenv("PYPI_PACKAGE", "pkg")
    monkeypatch.setattr(p, "_request", lambda url, **kw: {"data": {"last_week": 9}})
    props = p.repo_snapshot_events()[0]["properties"]
    assert props["stars"] == 5 and props["open_pull_requests"] == 2
    assert props["release_asset_downloads"] == 3 and props["pypi_downloads_last_week"] == 9


def test_main_never_raises(monkeypatch):
    monkeypatch.setitem(p.KINDS, "boom", lambda: 1 / 0)
    assert p.main(["x", "boom"]) == 0
    assert p.main(["x"]) == 2
