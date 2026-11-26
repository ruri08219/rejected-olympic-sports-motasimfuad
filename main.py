"""Rejected Olympic Sports — one funny single-line sport the Olympics turned down.

Writes the entry line to /output/entry.txt (UTF-8, 1-200 characters).
Standard library only; fully deterministic.
"""

import os
from pathlib import Path

ENTRY = (
    "The 100m sprint, but every runner carries a full cup of tea: "
    "spill a drop, lose a second \u2014 gold goes to whoever finishes driest."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
