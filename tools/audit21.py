"""Structural gate: the sheet must reconcile with its own story records.

Run after render. Fails loudly rather than shipping a page whose numbers argue
with each other, and checks every section stays inside the vertical budget it was
given, so no block can silently overlap the next.
"""

import sys

sys.path.insert(0, "tools")

from PIL import Image, ImageDraw  # noqa: E402

import render21 as R  # noqa: E402
import stories21 as S  # noqa: E402

problems = []


def check(cond, msg):
    if not cond:
        problems.append(msg)


# --- arithmetic ------------------------------------------------------------- #
counts = S.region_counts()
total = S.total_stories()
check(sum(counts.values()) == total,
      f"region counts sum to {sum(counts.values())} but total_stories() is {total}")
check(len(S.REGIONS) == len(counts), "a region has no records or vice versa")
check(S.rail_start() == len(S.LEADS) + len(S.CARDS) + 1,
      "rail numbering does not continue from the cards")

# every story names a region the strip knows about
for story in S.all_stories():
    check(story["region"] in dict(S.REGIONS),
          f"unknown region {story['region']!r}")

# the leads and cards carry the icons they name
import vignettes21 as V  # noqa: E402
for item in list(S.LEADS) + list(S.CARDS):
    check(item["icon"] in V.PANELS, f"no pictogram named {item['icon']!r}")

# --- vertical budget -------------------------------------------------------- #
img = Image.new("RGB", (R.W, R.H), R.PAPER)
d = ImageDraw.Draw(img)
y = 10
y_head = R.head_block(d, y)
y_fig = R.figures_block(d, y_head)
y_reg = R.region_block(d, y_fig)
check(y_head <= 145, f"head block ends at {y_head}, over budget")
check(y_fig <= 235, f"figures band ends at {y_fig}, over budget")
check(y_reg <= 295, f"region strip ends at {y_reg}, over budget")

footer_h = 80
bottom = R.H - 8 - footer_h
flex = bottom - y_reg
lead_h = int(flex * 0.31)
cards_h = int(flex * 0.46)
rail_h = flex - lead_h - cards_h - 18

check(lead_h > 205, f"lead row only {lead_h}px: the pictures would be too small")
check(cards_h > 250, f"card grid only {cards_h}px")
check(rail_h > 110, f"rail only {rail_h}px")

ends = y_reg + lead_h + 8 + cards_h + 10 + rail_h
check(ends <= bottom + 1, f"body ends at {ends}, past the footer at {bottom}")

# --- the rendered file ------------------------------------------------------ #
path = "out/entry.png"
with Image.open(path) as im:
    check(im.size == (1024, 1024), f"image is {im.size}, not 1024x1024")
    nbytes = len(open(path, "rb").read())
    check(nbytes <= 1048576, f"image is {nbytes} bytes, over 1 MiB")

# no near-blank horizontal band left in the body: every 32px row must carry ink
im = Image.open(path).convert("RGB")
px = im.load()
blank = []
for y0 in range(y_reg, bottom, 32):
    hits = 0
    for yy in range(y0, min(y0 + 32, bottom), 4):
        for xx in range(0, R.W, 8):
            p = px[xx, yy]
            if abs(p[0] - 250) > 12 or abs(p[1] - 248) > 12 or abs(p[2] - 242) > 12:
                hits += 1
    if hits == 0:
        blank.append(y0)
check(not blank, f"fully blank horizontal bands in the body at {blank}")

if problems:
    print("FAIL")
    for p in problems:
        print("  -", p)
    sys.exit(1)

print("OK")
print(f"  stories {total} across {len(S.REGIONS)} regions: {counts}")
print(f"  sections: head<={y_head} figs<={y_fig} region<={y_reg} lead={lead_h} "
      f"cards={cards_h} rail={rail_h} end={ends} footer={bottom}")
print(f"  image 1024x1024, {nbytes} bytes")
