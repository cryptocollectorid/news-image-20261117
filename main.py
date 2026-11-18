#!/usr/bin/env python3
"""news-image-20261117 entry (Python 3.13, standard library only).

The image is the entry: a newspaper front page summing up the world news
of Tuesday 17 November 2026, held in this repository as entry.png
(1024x1024, drawn with PIL at build time from verified headlines).
This program copies it to /output/entry.png, deterministically.

Usage: python3 main.py
  Writes $MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"),
                    os.path.join(OUT_DIR, "entry.png"))


if __name__ == "__main__":
    main()
