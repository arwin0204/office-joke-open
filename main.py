"""Office Joke Open entry: writes one line of office comedy to /output/entry.txt.

Deterministic: no randomness, no time, no network. The same text every run.
"""

import os
from pathlib import Path

ENTRY = (
    "I replied-all to the meeting that should've been an email, "
    "cc'ing the printer \u2014 it jammed, which is still the clearest "
    "feedback this company has ever given."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
