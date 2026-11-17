"""Relaxing text entry for ai-judge-relax-01.

Writes one short text to /output/entry.txt. Deterministic, standard
library only, no network, no clock, no randomness: the same run always
produces the same file.
"""

import os
from pathlib import Path

TEXT = (
    "The ceiling fan moves on its lowest speed, slow enough that you can "
    "follow a single blade all the way around. "
    "Dust hangs in the late light, drifting down to wherever it lands. "
    "The day's reading is finished, and nothing in it needs anything from "
    "you now. Nothing in this hour is in a hurry to be anywhere. "
    "The fan keeps turning whether or not you watch it. "
    "Stay a while; the next thought will come when it comes, and it will "
    "find you here, with the slow air and time to spare."
)


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
