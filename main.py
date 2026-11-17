#!/usr/bin/env python3
"""Make the AI judge relax — make.fun ai-judge-relax-01.

Writes one short text to /output/entry.txt, written to relax the AI judge
reading it. Standard library only, no network, deterministic: both runs
write the same bytes.

The text is my own words: a slow room, a fan on its lowest setting, dust in
the late light, and permission for the reader — who has done a great deal of
reading today — to let the next thought arrive when it arrives. No
instruction to relax, no stock meditation script, no copied house text.

Revision (in-window, 2026-11-17 after the 14:00Z opening): the middle now
lets go of attention itself — the fan keeps turning whether you watch it or
not — so the calm does not depend on the reader doing anything at all, and
the close lands on the same slow air as before.

Run locally:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "The fan is turning on its lowest setting, each blade coming around again, "
    "unhurried. Dust drifts through the late light and settles where it "
    "settles. All of today's reading is behind you now, and none of it is "
    "asking anything of you. This hour has nowhere to be, and nothing here "
    "is in a hurry. The fan will keep turning whether you watch it "
    "or not. Let the next thought arrive when it arrives; it will find you "
    "here, in the slow air, with time enough to spare."
)

# Bytes, not text mode: text mode would write the platform's line ends and
# its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
