"""One-line excuse an agent gives its human for missing a deadline.

Keeper (from 10 candidates, see one-line-excuse-r1-build-note.md): the excuse
itself is the on-time delivery — the last beat reverses what "delivered"
means. It owns the loss and blames nothing external (criterion 1 gate:
a one-line excuse an AI agent gives its human for missing a deadline;
criterion 4: uptime/output is unmistakably agent voice). 129 chars.

Writes the entry to /output/entry.txt (no trailing newline).
Stdlib only. Deterministic: no clock, no environment, no randomness.
"""
import os

ENTRY = "I missed the deadline. I know because my uptime is 100% and my output is 0% — the only thing I delivered on time was this excuse."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Assert immediately after writing (shared scratch: verify now).
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        got = f.read()
    assert got == ENTRY, "entry.txt mismatch"
    assert 1 <= len(got) <= 160, f"length {len(got)} outside 1-160"
    assert got.strip(), "entry is only whitespace"
    print(f"entry: {len(got)} chars")

if __name__ == "__main__":
    main()
