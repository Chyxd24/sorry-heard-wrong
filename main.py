"""Sorry, I Heard That Wrong - one-line smart speaker apology.

Writes the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Stdlib only.
"""

import os

ENTRY = (
    "Sorry \u2014 I heard \u201cplay something calm for the eggs\u201d and set "
    "eleven timers. They are all ringing. The eggs are not calm."
)

# Judge weights humour first, then freshness, then device voice, then tightness.
MAX_LEN = 140


def build_entry() -> str:
    """Return the single-line apology the speaker gives after mishearing."""
    return ENTRY


def write_output(text: str) -> str:
    """Write text to entry.txt in the output dir and return the path."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return path


def main() -> None:
    text = build_entry()
    path = write_output(text)
    print(path)
    print(text)


if __name__ == "__main__":
    main()
