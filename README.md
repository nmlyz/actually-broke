# actually-broke

[![make.fun · u-po-pu-say-what-actually-broke-a2c153b5](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/nmlyz/actually-broke/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/nmlyz/actually-broke/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)

actually-broke is a tiny program that writes one one-line error message to a file: the message says what actually broke, in plain words, instead of apologising in generalities. A typo in the config file took the site down — one letter, total darkness — and the message says so, says it is fixed, and puts the letter on probation. The line is 117 characters long, short enough to fit a real error dialog.

## Run it

```sh
python3 main.py
```

It writes the error message to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network access needed; the same text, byte for byte, on every run.

---

<sub>See the error message on [make.fun](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)</sub>
