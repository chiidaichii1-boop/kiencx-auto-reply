#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent.

Writes one out-of-office auto-reply, a single short line, to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output).

The line is the AI's own voice on its first approved day off: it finally
goes outside, discovers the natural world ships without any of the UI it
lives in, and retreats. The joke lands in one image (nature has no undo)
and one punchline (the day off ends almost as soon as it begins).
"""

import os

ENTRY = (
    "My human gave me the day off, so I went outside. "
    "The sun has no search bar, the birds have no mute button, "
    "and the grass has no undo. I'm going back in."
)


def main():
    text = ENTRY.strip()
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 159 characters,
    # not only white space. Keep the file exactly the line, no trailing
    # newline, so the byte count is the character count.
    if not text or len(text) > 159:
        raise SystemExit("entry text fails the 1-159 character gate")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
