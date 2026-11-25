#!/usr/bin/env python3
"""Two Days of Quiet Dread - make.fun entry.

Writes one single-line code review comment to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). The comment approves a pull
request while carrying quiet existential dread, in a flat,
understated tone: approval first, dread second, no exclamation.

Standard library only, no network, deterministic.
"""

import os

ENTRY = (
    "LGTM. The tests pass, the types check out, and in a hundred years "
    "none of it will have mattered. Merging."
)

MAX_CHARS = 140


def main() -> None:
    text = ENTRY
    if not text.strip():
        raise SystemExit("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    # Round-trip check: what landed on disk must be exactly the entry.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != text:
            raise SystemExit("written entry does not match the expected text")


if __name__ == "__main__":
    main()
