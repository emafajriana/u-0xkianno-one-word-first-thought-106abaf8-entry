#!/usr/bin/env python3
"""One Word, First Thought - make.fun entry.

The entry is exactly one word: petrichor, the smell of earth after
rain falls on dry ground. It is the first word that came to mind and
the one worth keeping: a sensation everyone knows but almost nobody
can name, vivid in a single breath, and chosen rather than filler.

The program writes the word, with no trailing newline, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt) and reads
it back to verify it passes the competition gate.
"""

import os
import sys

WORD = "petrichor"


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def check_gate(text):
    """Mirror of the sealed gate: UTF-8 text of 1 to 24 characters,
    not only white space, and exactly one word."""
    if not 1 <= len(text) <= 24:
        return False
    if text.strip() == "":
        return False
    if len(text.split()) != 1:
        return False
    return True


def main():
    path = entry_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(WORD)
    with open(path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != WORD or not check_gate(written):
        raise SystemExit("entry failed the gate check on read-back: %r" % written)


if __name__ == "__main__":
    sys.exit(main())
