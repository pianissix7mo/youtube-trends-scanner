import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime
from zoneinfo import ZoneInfo

OWNER = "pianissix7mo"
TARGETS = [
    ("youtube-trends-scanner", "scan.yml"),
    ("youtube-catalyst-scanner", "scanner_b.yml"),
]
TORONTO = ZoneInfo("America/Toronto")


def dispatch(token: str, repo: str, workflow: str) -> None:
    url = f"https://api.github.com/repos/{OWNER}/{repo}/actions/workflows/{workflow}/dispatches"
    payload = json.dumps({"ref": "main"}).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=payload,
        method="POST",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "scanner-ab-render-trigger",
            "Content-Type": "application/json",
        },
    )

    last_error = None
    for attempt in range(1, 4):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                if response.status == 204:
                    print(f"Triggered {repo}:{workflow}")
                    return
                raise RuntimeError(f"Unexpected GitHub status {response.status}")
        except (urllib.error.URLError, urllib.error.HTTPError, RuntimeError) as exc:
            last_error = exc
            print(f"Attempt {attempt}/3 failed for {repo}:{workflow}: {exc}", file=sys.stderr)
            if attempt < 3:
                time.sleep(5 * attempt)

    raise RuntimeError(f"Failed to trigger {repo}:{workflow}") from last_error


def main() -> int:
    now = datetime.now(TORONTO)
    print(f"Toronto time: {now.isoformat()}")

    # Render evaluates cron in UTC. The Blueprint fires at both 09:07 and
    # 10:07 UTC so DST is automatic. Only the occurrence landing in Toronto's
    # 05:00 hour is allowed to dispatch.
    if now.hour != 5:
        print("Not Toronto 05:xx; DST guard says skip.")
        return 0

    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if not token:
        print("Missing GITHUB_TOKEN environment variable.", file=sys.stderr)
        return 2

    failures = []
    for repo, workflow in TARGETS:
        try:
            dispatch(token, repo, workflow)
        except Exception as exc:
            failures.append(f"{repo}:{workflow}: {exc}")

    if failures:
        print("One or more dispatches failed:", file=sys.stderr)
        for item in failures:
            print(f"- {item}", file=sys.stderr)
        return 1

    print("Scanner A and Scanner B dispatch requests were both accepted by GitHub.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
