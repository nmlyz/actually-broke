#!/usr/bin/env python3
"""actually-broke: write one one-line error message to /output/entry.txt.

The error message says what actually broke: a typo in the config file
took the site down. One letter, total darkness. It is fixed, and the
letter is on probation now. One line, 117 characters, inside the 1-200
character gate, so it goes before the judge exactly as written.

Standard library only, no network. Deterministic: the same bytes on every run.
"""

import os
import sys

ENTRY = (
    "A typo in our config file took the site down. One letter, "
    "total darkness. It's fixed; the letter is on probation now."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    if not (1 <= len(text) <= 200):
        print(f"entry is {len(text)} code points, must be 1-200", file=sys.stderr)
        return 1
    if text != text.strip() or "\n" in text or not text.strip():
        print("entry must be a single non-blank line", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # chmod is best-effort: in the grading sandbox /output is a root-owned
    # mount and the program runs as uid 65534, so chmod there raises EPERM.
    # The entry file itself is what matters; a failed chmod must not fail
    # the run. (The output directory itself is never chmodded or removed.)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
