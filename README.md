# GPS Shortcut — make.fun one-liner

[![make.fun · u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![rank](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/khususcrypto0000-coder/gps-shortcut-makefun/rank.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![reward](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/khususcrypto0000-coder/gps-shortcut-makefun/reward.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)

One-line entry for the make.fun bounty **"The GPS Swears It Was a Shortcut"**
(`u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9`).

The entry is the GPS's own excuse, in its own voice, for sending the driver
down the wrong road — arrogant, defensive, caught red-handed, and blaming the
map:

> The map and I have an arrangement: it makes up the roads, I repeat them with confidence, and that's called teamwork.

## Run

```sh
python3 main.py
```

This validates the entry (UTF-8, 1–200 characters, a single line, not only
whitespace) and writes it to `/output/entry.txt`, then reads the file back
and asserts it is byte-identical.
