#!/usr/bin/env python3
"""data/build.json 에 빌드 시각 박음. 푸터에서 표시."""
import json
import os
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))
OUT = os.path.join(os.path.dirname(__file__), "..", "data", "build.json")


def main():
    now = datetime.now(KST)
    payload = {
        "built_at": now.strftime("%Y-%m-%d %H:%M KST"),
        "builder": "github-actions/daily.yml",
        "note": "매일 04:00 KST 자동 갱신.",
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
