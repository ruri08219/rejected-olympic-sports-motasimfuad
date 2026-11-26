"""Rejected Olympic Sports — one funny single-line sport the Olympics turned down.

Writes the entry line to /output/entry.txt (UTF-8, 1-200 characters).
Standard library only; fully deterministic.
"""

import os
from pathlib import Path

def entry_line() -> str:
    """The single entry line: concrete scene, reversal, landing final line."""
    return (
        "The 100m sprint, but every runner carries a full cup of tea: "
        "spill a drop, lose a second \u2014 gold goes to whoever finishes driest."
    )


ENTRY = entry_line()

# Gate guard: the entry must be 1-200 UTF-8 characters, one line, not blank.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY and ENTRY.strip(), "entry must be a single non-blank line"


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(entry_line(), encoding="utf-8")


if __name__ == "__main__":
    main()
