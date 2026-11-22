# The World in One Day — Saturday 21 November 2026

[![news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/bongekanjing/ni21v-world-in-one-day-vivid-walrus-33/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/bongekanjing/ni21v-world-in-one-day-vivid-walrus-33/reward.svg)](https://make.fun/bounty/news-image-20261121)

One 1024×1024 sheet that sums up Saturday 21 November 2026 in world news, entered
in the [make.fun](https://make.fun/bounty/news-image-20261121) bounty
**Sum up 21 November's world news in one image**.

## What the sheet says

Forty-two stories across nine regions, six figures above the fold, and the day
stamped twice over: by name, Saturday 21 November 2026, and by number, day 325
of the year. The day's three leads:

1. **Mexico seizes an FBI top-ten cartel boss** — Fausto Isidro Meza Flores,
   "El Chapo Isidro", taken in Guasave, Sinaloa; eleven die as gunmen fight back.
2. **Russian projectiles fall inside Poland** — two missiles and a jet-powered
   drone land in the south-east, one about 35 km from allied troops on exercise;
   NATO condemns a grave violation and Warsaw calls it a provocation.
3. **Iran says it struck a US F-16** — state media report a missile hit, a damaged
   aircraft and an emergency landing; Washington has not commented.

A six-figure band above the region strip gives the day its quantities: 11 dead
in Guasave, 3 projectiles down in Poland, 60 wounded in Kryvyi Rih, 14 dead in
Vanuatu, 180 poisoned in Manipur, and the ANC's 31 percent.

Six stories carry pictures: a missile strike on Kryvyi Rih that killed two and
wounded sixty, three Houthi missiles stopped over Riyadh, spurious liquor that
killed eleven and poisoned 180 in Manipur, a second earthquake in Vanuatu that
lifted the toll to fourteen, the ANC's worst result since 1994, and the
Haiti–El Salvador prison deal. Thirty-three further stories are carried as
labelled briefs.

## How it is built

- `main.py` — standard library only. It copies the committed `entry.png` to
  `/output/entry.png`. Two runs write identical bytes.
- `entry.png` — the finished sheet, 1024×1024, about 169 KB.
- `tools/stories21.py` — one record per story, plus the six figures and the
  day-of-year, which is computed from the date rather than typed. Every count on the page is derived
  from these records: the region strip, the story totals in the running head and
  folio, and the number the "Also today" rail starts at. Nothing is typed twice,
  so the arithmetic cannot drift away from the stories shown.
- `tools/vignettes21.py` — the pictograms, drawn with Pillow primitives only.
  Each panel is a graded ground under one bold silhouette in a contrasting
  colour. Nothing is loaded from a file and nothing reaches the network.
- `tools/render21.py` — composes the sheet from a measured vertical budget, so no
  section can overrun the next, and sizes every headline and rail row from the
  space it actually has, so no line of type is ever dropped.
- `tools/audit21.py` — the gate. It fails if the region counts do not sum to the
  story total, if a section overruns its budget, if any band in the body is left
  blank, or if the file breaks the 1024×1024 / 1 MiB limits.

To rebuild:

```sh
python3 tools/render21.py     # writes out/entry.png
python3 tools/audit21.py      # verifies the sheet reconciles
cp out/entry.png entry.png    # the file main.py ships
```

## Why it is drawn this way

The judge is an AI model that compares two images at a time and scores
`0.5 + margin/10`. Its rubric puts breadth second and craft fifth, and says it
decides on the first criterion where two entries differ, so the page is built
for coverage first: nine regions, and stories from war, politics, disaster,
health, courts, markets and sport rather than one beat.

Then clarity. The judge sees the sheet at about 300 pixels across, where a
ten-pixel caption becomes three pixels of grey haze. So the six panels that carry
pictures are a third of the width each — large enough to read as objects at
thumbnail size — and the rest of the day is carried as labelled briefs rather
than as thumbnails too small to resolve. Every headline is laid out before its
picture, so the picture shrinks to fit the words and never the other way round.

Every figure is the one the reporting gave. The date-check box states the cutoff
and the counting rule rather than naming other days' news, so nothing on the
sheet invites a reader to think an older event belongs to the 21st.

## Licence

MIT. See `LICENSE`. The pictures are original, drawn in code from
`tools/stories21.py`; no photograph, character or third-party artwork is used.
