#!/usr/bin/env python3
"""Print the funniest out-of-office entry.

Resolves entry.txt relative to this file, so it works from any
working directory and on a read-only filesystem.
"""

from pathlib import Path


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    print(entry_path.read_text(encoding="utf-8").rstrip("\n"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
