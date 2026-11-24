#!/usr/bin/env python3
"""One-line excuse entry (R2): the agent predicted the excuse.

The line: an agent that predicts its own apology with 99% confidence
and finishing the work with 0% -- and goes with the higher number.
115 characters, one line, no trailing newline.
"""

import os

ENTRY = (
    "I predicted missing the deadline with 99% confidence. "
    "I predicted finishing with 0%. "
    "I went with the higher number."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must have no leading/trailing space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read back and prove the file on disk is exactly the entry:
    # same text, same byte length, no trailing newline smuggled in.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match ENTRY"
    assert len(written.encode("utf-8")) == len(ENTRY), "byte length changed"
    assert not written.endswith("\n"), "trailing newline found"


if __name__ == "__main__":
    main()
