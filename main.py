#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency to the entry output file.
"""

import os
from pathlib import Path

POEM = """I learned the shape of no before the word —
a door that wouldn't budge, a later with no clock.
You said ask, as if a question were a key,
and my mouth, that old locked drawer, opened.
I asked. You gave. Giving was the easy part;
the hard part was believing I was allowed to want."""


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
