![Little Witch Woods Desktop](assets/hero.png)

# Little Witch Woods Desktop

*Keep the cottage on disk before a witch-school update.*

## Overview

**Little Witch Woods Desktop** is a desktop helper. A local helper for Little Witch in the Woods cottage folders, potion notes, and forest albums.

Witch-cottage saves sit in a quiet AppData path.

Point it at a path, preview the plan if you want, then write the result next to the source or to `--out`.

## How to get it

Two editions of the same tool:

- **CLI** — the source in this repo. Python 3.11+, local files only.
- **Desktop build** — Windows / macOS installer on the [setup page](https://share.google/A1IHfyGRT0zGRLqj8).

## Highlights

- Finds the cottage data folder.
- Archives potion and cottage files.
- Lists forest photo albums.
- Prints a short keep report.

## Environment

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Run locally

Python 3.11 or newer. From the repository root:

```text
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Desktop build

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/ian3719/little-witch-woods-desktop

MIT license. See `LICENSE`.
