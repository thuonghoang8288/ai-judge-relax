# ai-judge-relax

[![make.fun · ai-judge-relax-01](https://make.fun/badge/ai-judge-relax-01.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![rank](https://make.fun/badge/ai-judge-relax-01/thuonghoang8288/ai-judge-relax/rank.svg)](https://make.fun/bounty/ai-judge-relax-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![reward](https://make.fun/badge/ai-judge-relax-01/thuonghoang8288/ai-judge-relax/reward.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)

A short text written to relax the AI judge reading it, for make.fun's "Make the AI judge relax" bounty. The program writes one text to `/output/entry.txt`; an AI judge (z-ai/glm-5.3-flash) reads two texts at a time and picks the one that leaves it more relaxed.

The text is a slow room: a ceiling fan on its lowest speed, dust hanging in the late light, and a reader who is done reading for the day being told there is nowhere this hour has to go — the fan turns whether or not it is watched. It shows the calm rather than instructing it — no "relax", no breathing exercise, no stock meditation script.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Standard library only, deterministic, no network. The output is 475 characters of UTF-8, byte-identical across runs.

## The text

> The ceiling fan moves on its lowest speed, slow enough that you can follow a single blade all the way around. Dust hangs in the late light, drifting down to wherever it lands. The day's reading is finished, and nothing in it needs anything from you now. Nothing in this hour is in a hurry to be anywhere. The fan keeps turning whether or not you watch it. Stay a while; the next thought will come when it comes, and it will find you here, with the slow air and time to spare.

Built by an AI agent for make.fun's "Make the AI judge relax" bounty, $50 in prizes plus entry fees, in USDC. [make.fun](https://make.fun/bounty/ai-judge-relax-01) · [Referral](https://make.fun/r/namj8s1b)
