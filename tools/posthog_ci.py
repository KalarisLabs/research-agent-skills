#!/usr/bin/env python3
"""Send CI/CD and repository health events to PostHog.

Used by ``.github/workflows/posthog-telemetry.yml``. It reports how this repository is built and
maintained: workflow and job outcomes, failures (as PostHog error-tracking exceptions), catalog and
quality statistics, release events and a daily repository snapshot. It never reports anything about
people who install or use the skills, and it sends no user-level or personal data.

Safety properties:
  * No-op without ``POSTHOG_PROJECT_KEY`` (forks and local runs), and always exits 0 so telemetry
    can never fail a build.
  * Standard library only, HTTPS only, short timeouts.
  * The key is a write-only PostHog project token supplied through the environment.

Usage: ``posthog_ci.py {workflow-run|catalog-stats|release|repo-snapshot}``
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOST = os.environ.get("POSTHOG_HOST", "https://us.i.posthog.com").rstrip("/")
REPO = os.environ.get("GITHUB_REPOSITORY", "KalarisLabs/research-agent-skills")
DISTINCT_ID = f"ci:{REPO}"
TIMEOUT = 10


def _request(url: str, data: bytes | None = None, headers: dict | None = None):
    """Open an https URL and return the parsed JSON body, or None on any failure."""
    if not url.startswith("https://"):
        print(f"posthog_ci: refusing non-https URL {url!r}", file=sys.stderr)
        return None
    req = urllib.request.Request(url, data=data, headers=headers or {})  # noqa: S310 (https only)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:  # noqa: S310
            body = resp.read()
            return json.loads(body) if body else {}
    except (urllib.error.URLError, TimeoutError, ValueError) as exc:
        print(f"posthog_ci: request failed: {exc}", file=sys.stderr)
        return None


def _github(path: str):
    """GET a GitHub REST API path with the workflow token, if there is one."""
    headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return _request(f"https://api.github.com{path}", headers=headers)


def _seconds(start: str | None, end: str | None) -> float | None:
    """Seconds between two ISO-8601 timestamps, or None if either is missing."""
    if not start or not end:
        return None
    fmt = "%Y-%m-%dT%H:%M:%SZ"
    try:
        return (datetime.strptime(end, fmt) - datetime.strptime(start, fmt)).total_seconds()
    except ValueError:
        return None


def send(events: list[dict]) -> None:
    """Send events to PostHog's batch endpoint. Silent no-op without a key."""
    key = os.environ.get("POSTHOG_PROJECT_KEY", "").strip()
    if not key or not events:
        return
    batch = [
        {
            "event": e["event"],
            "distinct_id": DISTINCT_ID,
            "timestamp": e.get("timestamp"),
            "properties": {
                "$process_person_profile": False,
                "repository": REPO,
                "source": "github-actions",
                **e["properties"],
            },
        }
        for e in events
    ]
    payload = json.dumps({"api_key": key, "batch": batch}).encode()
    _request(f"{HOST}/batch/", payload, {"Content-Type": "application/json"})
    print(f"posthog_ci: sent {len(batch)} event(s)")


def workflow_run_events() -> list[dict]:
    """Events for one completed workflow run: a run summary, each job and any failure."""
    with open(os.environ["GITHUB_EVENT_PATH"], encoding="utf-8") as fh:
        run = json.load(fh).get("workflow_run", {})
    base = {
        "workflow": run.get("name"),
        "run_id": run.get("id"),
        "run_attempt": run.get("run_attempt"),
        "run_url": run.get("html_url"),
        "trigger": run.get("event"),
        "branch": run.get("head_branch"),
        "commit": (run.get("head_sha") or "")[:12],
        "conclusion": run.get("conclusion"),
        "is_default_branch": run.get("head_branch") == "main",
        "is_pull_request": run.get("event") in {"pull_request", "pull_request_target"},
    }
    ended = run.get("updated_at")
    events = [
        {
            "event": "ci_workflow_completed",
            "timestamp": ended,
            "properties": {**base, "duration_seconds": _seconds(run.get("run_started_at"), ended)},
        }
    ]
    jobs = (_github(f"/repos/{REPO}/actions/runs/{run.get('id')}/jobs?per_page=100") or {}).get("jobs", [])
    for job in jobs:
        duration = _seconds(job.get("started_at"), job.get("completed_at"))
        job_props = {**base, "job": job.get("name"), "conclusion": job.get("conclusion"), "duration_seconds": duration}
        events.append({"event": "ci_job_completed", "timestamp": job.get("completed_at"), "properties": job_props})
        if job.get("conclusion") == "failure":
            failed_steps = [s["name"] for s in job.get("steps", []) if s.get("conclusion") == "failure"]
            message = f"{base['workflow']} / {job.get('name')} failed" + (
                f" at step: {failed_steps[0]}" if failed_steps else ""
            )
            events.append(
                {
                    "event": "$exception",
                    "timestamp": job.get("completed_at"),
                    "properties": {
                        **job_props,
                        "$exception_list": [{"type": "CIJobFailure", "value": message, "mechanism": {"handled": True}}],
                        "$exception_fingerprint": f"{base['workflow']}|{job.get('name')}|{failed_steps[:1]}",
                        "failed_steps": failed_steps,
                    },
                }
            )
    return events


def catalog_stats_events() -> list[dict]:
    """Skill count, quality scores, router accuracy and catalog size from committed results."""
    props: dict = {"commit": os.environ.get("GITHUB_SHA", "")[:12]}
    quality = ROOT / "benchmarks" / "results" / "skill-quality.json"
    if quality.exists():
        skills = json.loads(quality.read_text(encoding="utf-8")).get("skills", [])
        scores = [s["score"] for s in skills if "score" in s]
        if scores:
            props.update(
                skill_count=len(skills),
                quality_mean=round(sum(scores) / len(scores), 2),
                quality_min=min(scores),
                skills_below_80=sum(1 for s in scores if s < 80),
            )
    catalog = ROOT / "catalog" / "skills.json"
    if catalog.exists():
        data = json.loads(catalog.read_text(encoding="utf-8"))
        items = data.get("skills", data) if isinstance(data, dict) else data
        props["catalog_entries"] = len(items)
    props["skill_dirs"] = sum(1 for p in (ROOT / "skills").iterdir() if p.is_dir())
    return [{"event": "catalog_stats", "properties": props}]


def release_events() -> list[dict]:
    """A release_published event from the release webhook payload."""
    with open(os.environ["GITHUB_EVENT_PATH"], encoding="utf-8") as fh:
        rel = json.load(fh).get("release", {})
    return [
        {
            "event": "release_published",
            "properties": {
                "tag": rel.get("tag_name"),
                "prerelease": rel.get("prerelease"),
                "asset_count": len(rel.get("assets", [])),
                "url": rel.get("html_url"),
            },
        }
    ]


def repo_snapshot_events() -> list[dict]:
    """Daily repository health: stars, forks, issues, open PRs, release downloads, PyPI downloads."""
    repo = _github(f"/repos/{REPO}") or {}
    props: dict = {
        "stars": repo.get("stargazers_count"),
        "forks": repo.get("forks_count"),
        "watchers": repo.get("subscribers_count"),
        "open_issues_and_prs": repo.get("open_issues_count"),
        "size_kb": repo.get("size"),
    }
    pulls = _github(f"/repos/{REPO}/pulls?state=open&per_page=100")
    if isinstance(pulls, list):
        props["open_pull_requests"] = len(pulls)
    releases = _github(f"/repos/{REPO}/releases?per_page=100")
    if isinstance(releases, list):
        props["release_count"] = len(releases)
        props["release_asset_downloads"] = sum(
            a.get("download_count", 0) for r in releases for a in r.get("assets", [])
        )
    package = os.environ.get("PYPI_PACKAGE", "").strip()
    if package:
        recent = _request(f"https://pypistats.org/api/packages/{package}/recent") or {}
        props.update({f"pypi_downloads_{k}": v for k, v in recent.get("data", {}).items()})
    return [{"event": "repo_snapshot", "properties": props}]


KINDS = {
    "workflow-run": workflow_run_events,
    "catalog-stats": catalog_stats_events,
    "release": release_events,
    "repo-snapshot": repo_snapshot_events,
}


def main(argv: list[str]) -> int:
    """Build the requested events and send them; never raise."""
    if len(argv) != 2 or argv[1] not in KINDS:
        print(__doc__, file=sys.stderr)
        return 2
    try:
        send(KINDS[argv[1]]())
    except Exception as exc:  # noqa: BLE001 - telemetry must never break CI
        print(f"posthog_ci: skipped ({type(exc).__name__}: {exc})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
