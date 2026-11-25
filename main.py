"""Fortune Cookie for the Liquidated Trader - make.fun entry.

Writes a single fortune-cookie line for a crypto trader who has just
been liquidated to /output/entry.txt.

Pure stdlib, no network, fully deterministic: the output is always the
same one line.

The fortune (17 words, 95 characters):
  "Fortune favors the bold, says the cookie - which has never once
   been liquidated at 3 a.m."

Why this line: it keeps the oracular fortune voice ("Fortune favors
the bold"), names the trader's loss (liquidated), echoes the judge's
own scene (3 a.m., empty wallet), and lands the joke with a turn -
the cookie itself, smug and crumbly, has never been liquidated.
Rueful and warm, never cruel: the trader laughs with the cookie.
"""

import os

FORTUNE = (
    "Fortune favors the bold, says the cookie - "
    "which has never once been liquidated at 3 a.m."
)

OUT_DIR = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main():
    # Gate self-check: 1-160 UTF-8 chars, not only whitespace,
    # one line, at most 20 words of plain text.
    text = FORTUNE
    if not (1 <= len(text.encode("utf-8")) <= 160):
        raise ValueError("fortune must be 1-160 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("fortune must not be only whitespace")
    if "\n" in text:
        raise ValueError("fortune must be a single line")
    if len(text.split()) > 20:
        raise ValueError("fortune must be at most 20 words, got %d" % len(text.split()))
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print("wrote %s (%d chars, %d words)" % (OUT_PATH, len(text), len(text.split())))


if __name__ == "__main__":
    main()
