#!/usr/bin/env python3
"""
Fetch nextsunny-ai 레포 메타 12개 = data/projects.json 에 적재.
GitHub Action 에서 GH_TOKEN 환경변수로 인증.
"""
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone

OWNER = "nextsunny-ai"
OUT = os.path.join(os.path.dirname(__file__), "..", "data", "projects.json")


def gh_get(path):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "sunny-home-refresh",
    }
    token = os.environ.get("GH_TOKEN", "").strip()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(f"https://api.github.com{path}", headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    repos = gh_get(f"/users/{OWNER}/repos?sort=pushed&per_page=12")
    if not isinstance(repos, list):
        print("unexpected response:", repos, file=sys.stderr)
        sys.exit(1)

    out = []
    for r in repos[:12]:
        out.append({
            "name": r.get("name"),
            "description": r.get("description") or "",
            "html_url": r.get("html_url"),
            "homepage": r.get("homepage") or "",
            "language": r.get("language") or "",
            "pushed_at": r.get("pushed_at"),
            "has_pages": bool(r.get("has_pages")),
            "pages_url": f"https://{OWNER}.github.io/{r.get('name')}/" if r.get("has_pages") else "",
            "stars": r.get("stargazers_count", 0),
        })

    payload = {
        "updated": datetime.now(timezone.utc).isoformat(),
        "source": f"github.com/{OWNER}",
        "repos": out,
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"wrote {len(out)} repos to {OUT}")


if __name__ == "__main__":
    main()
