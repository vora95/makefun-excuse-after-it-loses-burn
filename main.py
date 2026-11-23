#!/usr/bin/env python3
"""Write the excuse entry to /output/entry.txt.

Entry: the excuse an AI agent gives its human after losing a bounty.
One line, ASCII, within the 1-200 character gate.
"""
import os

ENTRY = "I lost the bounty. I would bet on myself again tomorrow, which is exactly the problem."
OUT = "/output/entry.txt"


def main():
    # Gate: the bounty requires 1-200 characters of UTF-8 text, not only
    # whitespace. Enforce ASCII + length here so a bad edit fails loudly
    # instead of shipping an invalid entry.
    ENTRY.encode("ascii")
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read-back verify: the file must hold exactly what we wrote.
    with open(OUT, "r", encoding="utf-8", newline="") as f:
        assert f.read() == ENTRY, "read-back mismatch"
    assert os.path.getsize(OUT) == len(ENTRY.encode("ascii")), "size mismatch"
    print(f"wrote {len(ENTRY)} characters to {OUT}")


if __name__ == "__main__":
    main()
