#!/usr/bin/env python3
"""Say What Actually Broke: one line of error copy that tells the user
the brutal truth about what went wrong, and makes them laugh.

The entry is a single-line error message (at most 200 characters) for a
billing failure: the customer was charged in the wrong currency, so a
coffee cost as much as a car in yen. It names the real failure in plain
words, says what happens next (the refund is on its way), and closes
with the one true thing left standing: the coffee was real.

Run: python3 main.py
Writes: /output/entry.txt (exactly one line, no trailing newline)
Standard library only.
"""

import os

ENTRY = (
    "We charged you in the wrong currency, so your coffee cost "
    "the price of a car in yen. The refund is on its way; "
    "the coffee was real."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text):
    """Check the entry against the competition gate before writing it:
    UTF-8 text of 1 to 200 characters, a single line, not only
    whitespace. Raises ValueError with the failing rule when it does
    not hold, so a bad entry never reaches /output silently."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(text) > 200:
        raise ValueError("entry is {} characters, over the 200 limit".format(len(text)))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return True


def write_entry(path=OUTPUT_PATH):
    """Write the entry line to path, creating the directory if needed."""
    validate_entry(ENTRY)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    write_entry()
    print("wrote {} ({} characters)".format(OUTPUT_PATH, len(ENTRY)))
