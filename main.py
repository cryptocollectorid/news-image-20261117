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
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_DIMENSION = 1024
MAX_SIZE = 1024 * 1024


def validate_png(path):
    """Check the copied file is a valid PNG within the entry limits.

    Verifies the PNG magic bytes, parses the IHDR width/height, and
    enforces width <= 1024, height <= 1024 and file size <= 1 MiB.
    Raises ValueError with a clear message on any failure.
    """
    size = os.path.getsize(path)
    if size > MAX_SIZE:
        raise ValueError(
            "entry.png is %d bytes, over the 1 MiB limit" % size)
    with open(path, "rb") as f:
        header = f.read(33)
    if header[:8] != PNG_MAGIC:
        raise ValueError("entry.png is not a PNG (bad magic bytes)")
    if len(header) < 33 or header[12:16] != b"IHDR":
        raise ValueError("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", header[16:24])
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        raise ValueError(
            "entry.png is %dx%d, over the 1024x1024 limit"
            % (width, height))
    return width, height, size


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, "entry.png")
    shutil.copyfile(os.path.join(HERE, "entry.png"), out_path)
    width, height, size = validate_png(out_path)
    print("wrote %s (%dx%d, %d bytes)" % (out_path, width, height, size))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as exc:
        print("error: %s" % exc, file=sys.stderr)
        sys.exit(1)
