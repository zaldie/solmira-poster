#!/usr/bin/env python3
"""Entry program: write the SOLMIRA poster image to /output/entry.png.

The image (entry.jpg, a 1024x1024 JPEG) ships beside this file; the
program copies it to the output path, byte for byte. Deterministic,
stdlib only, no network.
"""
import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.jpg")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
