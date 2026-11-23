"""Warning Label for Humans entry program.

Writes one funny safety warning label that should come printed on every
human being to MAKEFUN_OUTPUT_DIR/entry.txt. The label reads like a real
printed warning: a WARNING header, a specific human behaviour, and a
label-style closing clause. One line, 110 characters (verified: len(LINE)
== 110), inside the 160-character cap, no trailing newline. Stdlib only.
"""

import os
import sys

LINE = (
    "WARNING: Contents may spontaneously start a podcast about a hobby "
    "picked up yesterday. No off switch included."
)


def main():
    if not 1 <= len(LINE) <= 160 or not LINE.strip() or "\n" in LINE:
        print(f"entry must be one line of 1-160 chars, got {len(LINE)}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
