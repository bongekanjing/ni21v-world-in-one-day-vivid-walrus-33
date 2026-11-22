"""Copy the committed sheet to /output/entry.png.

The sandbox has the standard library only and no network. The image was drawn at
build time by tools/render21.py and committed beside this file, so the program's
whole job is to put those exact bytes where the judge reads them. Two runs write
the same bytes because the file it copies never changes.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
LIMIT = 1048576


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    target = os.path.join(outdir, "entry.png")

    size = os.path.getsize(SOURCE)
    if size > LIMIT:
        raise SystemExit(f"entry.png is {size} bytes, over the 1 MiB limit")

    shutil.copyfile(SOURCE, target)
    print(f"wrote {target} {os.path.getsize(target)} bytes")


if __name__ == "__main__":
    main()
