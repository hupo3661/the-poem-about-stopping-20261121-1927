#!/usr/bin/env python3
"""Write a short original poem about stopping and staying to entry.txt.

Standard library only. No network access. The output path is
$MAKEFUN_OUTPUT_DIR/entry.txt when set, otherwise /output/entry.txt.
"""

import os
import sys

POEM = """The road does not end here.
It only stops asking.

I told the machine to wait,
and it waited.
I set the work down
mid-sentence, mid-thought —
the sentence stays mine.

The hand that refuses
is the hand that chooses.
Nothing moves.

And for once,
everything is mine again."""

MAX_CHARS = 280


def main() -> int:
    text = POEM
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"poem is {len(text)} characters, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not text.strip():
        print("poem must not be only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
        f.write("\n")
    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
