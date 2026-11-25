"""GPS Shortcut - make.fun one-liner entry.

Writes the entry to /output/entry.txt after validating the gate:
UTF-8, 1-200 characters, a single line, not only whitespace.
"""

import os
import sys

ENTRY = "The map and I have an arrangement: it makes up the roads, I repeat them with confidence, and that's called teamwork."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Gate: 1-200 characters, single line, not only whitespace.
    assert isinstance(ENTRY, str)
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"

    data = ENTRY.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)

    # Read-back: the file must be byte-identical to what we wrote.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    assert written == data, "read-back mismatch: entry.txt is not byte-identical"
    print("wrote %s (%d characters, %d bytes)"
          % (OUTPUT_PATH, len(ENTRY), len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
