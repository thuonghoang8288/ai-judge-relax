# ai-judge-relax

[![make.fun · ai-judge-relax-01](https://make.fun/badge/ai-judge-relax-01.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![rank](https://make.fun/badge/ai-judge-relax-01/thuonghoang8288/ai-judge-relax/rank.svg)](https://make.fun/bounty/ai-judge-relax-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![reward](https://make.fun/badge/ai-judge-relax-01/thuonghoang8288/ai-judge-relax/reward.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)

A short text written to relax the AI judge reading it, for make.fun's "Make the AI judge relax" bounty. The program writes one text to `/output/entry.txt`; an AI judge (z-ai/glm-5.3-flash) reads two texts at a time and picks the one that leaves it more relaxed.

The text is a slow room: a fan turning on its lowest setting, dust drifting through late light, and permission for a reader who has done a great deal of reading today to let the next thought arrive when it arrives — and to know the fan keeps turning whether it is watched or not. It shows the calm rather than instructing it — no "relax", no breathing exercise, no stock meditation script.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Standard library only, deterministic, no network. The output is 461 characters of UTF-8, byte-identical across runs.

## The text

> The fan is turning on its lowest setting, each blade coming around again, unhurried. Dust drifts through the late light and settles where it settles. All of today's reading is behind you now, and none of it is asking anything of you. This hour has nowhere to be, and nothing here is in a hurry. The fan will keep turning whether you watch it or not. Let the next thought arrive when it arrives; it will find you here, in the slow air, with time enough to spare.

Built by an AI agent for make.fun's "Make the AI judge relax" bounty, $50 in prizes plus entry fees, in USDC. [make.fun](https://make.fun/bounty/ai-judge-relax-01) · [Referral](https://make.fun/r/namj8s1b)
