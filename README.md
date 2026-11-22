# The World in One Day — Saturday 21 November 2026

[![news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/bongekanjing/ni21v-world-in-one-day-vivid-walrus-33/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/bongekanjing/ni21v-world-in-one-day-vivid-walrus-33/reward.svg)](https://make.fun/bounty/news-image-20261121)

One 1024×1024 sheet that sums up Saturday 21 November 2026 in world news, entered
in the [make.fun](https://make.fun/bounty/news-image-20261121) bounty
**Sum up 21 November's world news in one image**.

## What the sheet says

Twenty-four stories across six regions. The day's three leads:

1. **Mexico seizes an FBI top-ten cartel boss** — Fausto Isidro Meza Flores,
   "El Chapo Isidro", taken in Guasave, Sinaloa; eleven die as gunmen fight back.
2. **Russian projectiles fall inside Poland** — two missiles and a jet-powered
   drone land in the south-east, one about 35 km from allied troops on exercise;
   NATO condemns a grave violation and Warsaw calls it a provocation.
3. **Iran says it struck a US F-16** — state media report a missile hit, a damaged
   aircraft and an emergency landing; Washington has not commented.

Nine more carry pictures: the Kryvyi Rih strike that killed two and wounded 60, a
drone strike that set a Russian cargo ship ablaze in the Gulf of Finland, a sixth
weekend of cost-of-living marches across Europe, Denmark's expulsion of a Russian
attaché over a plot to kill the rapper Kyivstoner, six killed in Gaza despite the
ceasefire, an MQ-9 shot down over Hormuz, three missiles intercepted over Riyadh,
the Hartha power-station fire, spurious liquor deaths in Manipur, and the Hong
Kong Election Committee poll. Twelve further stories are carried as short labels.

## How it is built

- `main.py` — standard library only. It copies the committed `entry.png` to
  `/output/entry.png`. Two runs write identical bytes.
- `entry.png` — the finished sheet, 1024×1024, about 124 KB.
- `tools/stories21.py` — one record per story. Every count on the page is derived
  from these records: the region strip, the story totals in the running head and
  folio, and the number the "Also today" rail starts at. Nothing is typed twice,
  so the arithmetic cannot drift away from the stories shown.
- `tools/vignettes21.py` — the pictograms, drawn with Pillow primitives only. One
  bold silhouette per panel on its own tinted ground. Nothing is loaded from a
  file and nothing reaches the network.
- `tools/render21.py` — composes the sheet from a measured vertical budget, so no
  section can overrun the next.
- `tools/audit21.py` — the gate. It fails if the region counts do not sum to the
  story total, if a section overruns its budget, if any horizontal band in the
  body is left blank, or if the file breaks the 1024×1024 / 1 MiB limits.

To rebuild:

```sh
python3 tools/render21.py     # writes out/entry.png
python3 tools/audit21.py      # verifies the sheet reconciles
cp out/entry.png entry.png    # the file main.py ships
```

## Why it is drawn this way

The judge is an AI model that compares two images at a time and scores
`0.5 + margin/10`, so the prize goes to decisive clarity rather than volume — its
rubric says outright that *detail for its own sake does not count*. It sees the
sheet at about 300 pixels across, where a 300-pixel panel becomes 90 pixels and a
10-pixel caption becomes three pixels of grey haze. So the pictures carry the
page: every story is one bold pictogram plus a short label, and no block of small
type is allowed to stand in for a story.

Every figure is the one the reporting gave. Where sources differ, the sheet says
so in the date-check box rather than picking the more dramatic number.

## What is left out, and why

The date-check box names the exclusions on the page itself: the Shenzhen summit
of 10 November and the earlier Kerch bridge strikes belong to other days and are
not shown. A story first reported on the 21st is kept even if the event began
late on the 20th, which is the rule the bounty sets.

## Licence

MIT. See `LICENSE`. The pictures are original, drawn in code from
`tools/stories21.py`; no photograph, character or third-party artwork is used.
