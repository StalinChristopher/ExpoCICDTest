#!/usr/bin/env python3
"""Parse JSON from `eas build:download --json` (stdout captured to a file) and print the artifact path."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def parse_json_file(path: Path) -> object | None:
    raw = path.read_text(encoding="utf-8").strip()
    if not raw:
        print("eas_extract_download_path: empty JSON file", file=sys.stderr)
        return None
    for chunk in (raw, *reversed(raw.splitlines())):
        chunk = chunk.strip()
        if not chunk:
            continue
        try:
            return json.loads(chunk)
        except json.JSONDecodeError:
            continue
    print("eas_extract_download_path: could not parse JSON from file", file=sys.stderr)
    return None


def main() -> int:
    if len(sys.argv) != 3:
        print(
            "usage: eas_extract_download_path.py <path-to-json-file> <android|ios>",
            file=sys.stderr,
        )
        return 2
    path_json = Path(sys.argv[1])
    platform = sys.argv[2].lower().strip()
    if platform not in ("android", "ios"):
        print("eas_extract_download_path: platform must be android or ios", file=sys.stderr)
        return 2
    if not path_json.is_file():
        print(f"eas_extract_download_path: missing file {path_json}", file=sys.stderr)
        return 1
    data = parse_json_file(path_json)
    if data is None:
        return 1
    if not isinstance(data, dict):
        print("eas_extract_download_path: JSON root must be an object", file=sys.stderr)
        return 1
    path_value = data.get("path")
    if not isinstance(path_value, str) or not path_value.strip():
        print("eas_extract_download_path: missing or invalid 'path' in JSON", file=sys.stderr)
        print(path_json.read_text(encoding="utf-8"), file=sys.stderr)
        return 1
    artifact = Path(path_value).expanduser()
    if not artifact.is_file():
        print(f"eas_extract_download_path: path is not a file: {artifact}", file=sys.stderr)
        return 1
    suffix = artifact.suffix.lower()
    if platform == "android" and suffix != ".apk":
        print(
            f"eas_extract_download_path: expected .apk for android, got {suffix}",
            file=sys.stderr,
        )
        return 1
    if platform == "ios" and suffix != ".ipa":
        print(
            f"eas_extract_download_path: expected .ipa for ios, got {suffix}",
            file=sys.stderr,
        )
        return 1
    print(str(artifact.resolve()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
