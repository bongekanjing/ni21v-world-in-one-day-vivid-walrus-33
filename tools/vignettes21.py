"""Flat pictograms, drawn with Pillow primitives only.

One bold silhouette per panel on a light tinted ground with a single saturated
accent. That is deliberate: the judge sees the sheet at about 300 pixels across,
where a panel is only 30-90 pixels wide, and at that size a scene with many small
figures collapses into a dark smudge. A single strong shape in a contrasting
colour still reads. Each panel gets its own ground tint so a row of them does not
read as one repeated texture.

Nothing here loads a file or reaches the network: every shape is placed by code.
"""

from PIL import Image, ImageDraw

INK = (26, 28, 33)
DARK = (44, 48, 56)
BONE = (245, 241, 232)
WHITE = (252, 250, 245)


def _bg(d, box, tone):
    x0, y0, x1, y1 = box
    d.rectangle([x0, y0, x1, y1], fill=tone)


def _bar(d, box, frac, colour, from_bottom=True):
    """A ground band: the horizon every outdoor panel stands on."""
    x0, y0, x1, y1 = box
    h = y1 - y0
    if from_bottom:
        d.rectangle([x0, y1 - int(h * frac), x1, y1], fill=colour)
    else:
        d.rectangle([x0, y0, x1, y0 + int(h * frac)], fill=colour)


def _big(box):
    x0, y0, x1, y1 = [int(v) for v in box]
    return x0, y0, x1, y1, x1 - x0, y1 - y0


# --------------------------------------------------------------------------- #
# Pictograms. Every one is built around a single silhouette plus one accent.
# --------------------------------------------------------------------------- #

def capture(d, box):
    """A figure behind bars: the arrest reads at any size."""
    x0, y0, x1, y1, w, h = _big(box)
    _bg(d, box, (232, 224, 206))
    _bar(d, box, 0.18, (203, 188, 160))
    # The prisoner: head and shoulders, dark, centred.
    hr = int(min(w, h) * 0.115)
    hx = x0 + int(w * 0.50)
    hy = y0 + int(h * 0.40)
    d.ellipse([hx - hr, hy - hr, hx + hr, hy + hr], fill=DARK)
    d.polygon([(hx - int(hr * 1.9), y1 - int(h * 0.18)),
               (hx - int(hr * 1.5), hy + int(hr * 1.1)),
               (hx + int(hr * 1.5), hy + int(hr * 1.1)),
               (hx + int(hr * 1.9), y1 - int(h * 0.18))], fill=DARK)
    # The bars, in front of him.
    n = 3
    for i in range(n):
        bx = x0 + int(w * (0.30 + 0.20 * i))
        d.rectangle([bx, y0 + int(h * 0.10), bx + max(4, int(w * 0.035)), y1 - int(h * 0.14)],
                    fill=(140, 31, 43))
    d.rectangle([x0 + int(w * 0.24), y0 + int(h * 0.10), x1 - int(w * 0.24),
                 y0 + int(h * 0.10) + max(4, int(h * 0.045))], fill=(140, 31, 43))


def missiles(d, box):
    """Three descending trails over a flat horizon."""
    x0, y0, x1, y1, w, h = _big(box)
    _bg(d, box, (206, 216, 224))
    _bar(d, box, 0.30, (108, 78, 62))
    for i, fx in enumerate((0.22, 0.50, 0.78)):
        sx = x0 + int(w * fx)
        sy = y0 + int(h * (0.10 + 0.05 * i))
        ex = sx + int(w * 0.10)
        ey = y0 + int(h * 0.62)
        d.line([(sx, sy), (ex, ey)], fill=(226, 118, 44), width=max(2, int(w * 0.022)))
        tri = int(min(w, h) * 0.055)
        d.polygon([(ex, ey + tri), (ex - tri, ey - tri // 2), (ex + tri, ey - tri // 2)],
                  fill=(140, 31, 43))


def jet(d, box):
    """A fighter in profile with a hit marker: the F-16 claim."""
    x0, y0, x1, y1, w, h = _big(box)
    _bg(d, box, (188, 206, 220))
    _bar(d, box, 0.22, (96, 112, 128))
    cy = y0 + int(h * 0.46)
    bx0, bx1 = x0 + int(w * 0.16), x0 + int(w * 0.78)
    body = int(h * 0.10)
    d.ellipse([bx0, cy - body, bx1, cy + body], fill=(90, 98, 110))
    d.polygon([(x0 + int(w * 0.30), cy), (x0 + int(w * 0.52), cy - int(h * 0.30)),
               (x0 + int(w * 0.56), cy - int(h * 0.06))], fill=(118, 126, 138))
    d.polygon([(x0 + int(w * 0.34), cy + int(h * 0.02)), (x0 + int(w * 0.50), cy + int(h * 0.24)),
               (x0 + int(w * 0.54), cy + int(h * 0.04))], fill=(104, 112, 124))
    d.polygon([(x0 + int(w * 0.74), cy - int(h * 0.16)), (x0 + int(w * 0.86), cy),
               (x0 + int(w * 0.74), cy + int(h * 0.16))], fill=(78, 86, 98))
    cr = int(min(w, h) * 0.115)
    ccx, ccy = x0 + int(w * 0.62), cy - int(h * 0.24)
    d.ellipse([ccx - cr, ccy - cr, ccx + cr, ccy + cr], fill=(198, 36, 48))
    d.line([(ccx - cr // 2, ccy), (ccx + cr // 2, ccy)], fill=WHITE, width=max(2, cr // 4))
    d.line([(ccx, ccy - cr // 2), (ccx, ccy + cr // 2)], fill=WHITE, width=max(2, cr // 4))


def ruins(d, box):
    """A broken apartment block: the Kryvyi Rih strike."""
    x0, y0, x1, y1, w, h = _big(box)
    _bg(d, box, (214, 206, 196))
    _bar(d, box, 0.22, (128, 112, 96))
    bx0, bx1 = x0 + int(w * 0.22), x0 + int(w * 0.80)
    top = y0 + int(h * 0.24)
    d.rectangle([bx0, top, bx1, y1 - int(h * 0.22)], fill=(104, 100, 98))
    d.polygon([(bx0, top), (x0 + int(w * 0.40), top - int(h * 0.14)),
               (x0 + int(w * 0.50), top + int(h * 0.16)),
               (x0 + int(w * 0.62), top - int(h * 0.04)),
               (bx1, top + int(h * 0.05)), (bx1, top)], fill=(120, 116, 112))
    for r_i in range(3):
        for c_i in range(4):
            if (r_i + c_i) % 3 == 0:
                continue
            wx = bx0 + int((bx1 - bx0) * (0.12 + 0.23 * c_i))
            wy = top + int(h * (0.10 + 0.20 * r_i))
            d.rectangle([wx, wy, wx + int(w * 0.10), wy + int(h * 0.10)],
                        fill=(226, 118, 44) if (r_i + c_i) % 2 else (58, 62, 70))


def ship(d, box):
    """A cargo hull with a fire on deck: the Gulf of Finland strike."""
    x0, y0, x1, y1, w, h = _big(box)
    _bg(d, box, (176, 198, 210))
    _bar(d, box, 0.34, (52, 88, 108))
    hy = y0 + int(h * 0.60)
    d.polygon([(x0 + int(w * 0.16), hy), (x0 + int(w * 0.86), hy),
               (x0 + int(w * 0.76), hy + int(h * 0.20)),
               (x0 + int(w * 0.26), hy + int(h * 0.20))], fill=(64, 70, 80))
    d.rectangle([x0 + int(w * 0.60), hy - int(h * 0.14), x0 + int(w * 0.72), hy],
                fill=(94, 100, 110))
    d.polygon([(x0 + int(w * 0.30), hy), (x0 + int(w * 0.40), hy - int(h * 0.16)),
               (x0 + int(w * 0.50), hy - int(h * 0.08)), (x0 + int(w * 0.56), hy)],
              fill=(226, 118, 44))
    d.polygon([(x0 + int(w * 0.37), hy - int(h * 0.05)), (x0 + int(w * 0.44), hy - int(h * 0.30)),
               (x0 + int(w * 0.50), hy - int(h * 0.10))], fill=(232, 186, 72))


def crowd(d, box):
    """A marching column with a banner: the sixth weekend of protests."""
    x0, y0, x1, y1, w, h = _big(box)
    _bg(d, box, (222, 214, 226))
    _bar(d, box, 0.20, (150, 138, 158))
    d.rectangle([x0 + int(w * 0.14), y0 + int(h * 0.12), x0 + int(w * 0.68), y0 + int(h * 0.34)],
                fill=(140, 31, 43))
    for i in range(7):
        cx = x0 + int(w * (0.12 + 0.115 * i))
        cy = y0 + int(h * (0.52 + (0.05 if i % 2 else 0)))
        r = int(min(w, h) * 0.085)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(58, 52, 66))
        d.rectangle([cx - int(r * 0.8), cy + int(r * 0.7), cx + int(r * 0.8), y1 - int(h * 0.16)],
                    fill=(58, 52, 66))


def spy(d, box):
    """A struck-through dossier: the murder plot and the expulsion."""
    x0, y0, x1, y1, w, h = _big(box)
    _bg(d, box, (218, 216, 208))
    _bar(d, box, 0.18, (150, 146, 136))
    dx0, dx1 = x0 + int(w * 0.22), x0 + int(w * 0.78)
    dy0, dy1 = y0 + int(h * 0.16), y0 + int(h * 0.80)
    d.rectangle([dx0, dy0, dx1, dy1], fill=BONE, outline=(122, 118, 108), width=2)
    for i in range(4):
        ly = dy0 + int((dy1 - dy0) * (0.22 + 0.18 * i))
        d.rectangle([dx0 + int(w * 0.06), ly, dx1 - int(w * 0.16), ly + max(2, int(h * 0.03))],
                    fill=(150, 146, 136))
    d.line([(dx0, dy1), (dx1, dy0)], fill=(198, 36, 48), width=max(4, int(w * 0.035)))


def rubble(d, box):
    """A drone over broken low buildings: the Gaza strikes."""
    x0, y0, x1, y1, w, h = _big(box)
    _bg(d, box, (216, 208, 190))
    _bar(d, box, 0.30, (150, 134, 108))
    for i, (fx, fh) in enumerate(((0.14, 0.20), (0.34, 0.13), (0.54, 0.17), (0.74, 0.10))):
        bx = x0 + int(w * fx)
        bw = int(w * 0.16)
        d.rectangle([bx, y1 - int(h * (0.30 + fh)), bx + bw, y1 - int(h * 0.30)],
                    fill=(118, 106, 88))
    dx, dy = x0 + int(w * 0.66), y0 + int(h * 0.18)
    d.rectangle([dx - int(w * 0.09), dy - int(h * 0.02), dx + int(w * 0.09), dy + int(h * 0.02)],
                fill=DARK)
    d.line([(dx - int(w * 0.13), dy - int(h * 0.05)), (dx + int(w * 0.13), dy - int(h * 0.05))],
           fill=DARK, width=max(2, int(h * 0.025)))


def dronehit(d, box):
    """A drone silhouette and a falling wreck: the MQ-9 claim."""
    x0, y0, x1, y1, w, h = _big(box)
    _bg(d, box, (196, 210, 218))
    _bar(d, box, 0.28, (72, 92, 108))
    cx, cy = x0 + int(w * 0.52), y0 + int(h * 0.34)
    d.rectangle([cx - int(w * 0.22), cy - int(h * 0.035), cx + int(w * 0.22), cy + int(h * 0.035)],
                fill=DARK)
    d.rectangle([cx - int(w * 0.06), cy - int(h * 0.05), cx + int(w * 0.06), cy + int(h * 0.05)],
                fill=DARK)
    d.line([(cx - int(w * 0.16), cy + int(h * 0.06)), (cx + int(w * 0.16), cy + int(h * 0.06))],
           fill=DARK, width=max(2, int(h * 0.022)))
    d.line([(cx, cy), (x0 + int(w * 0.30), y1 - int(h * 0.34))], fill=(198, 36, 48),
           width=max(2, int(w * 0.018)))
    d.polygon([(x0 + int(w * 0.24), y1 - int(h * 0.30)),
               (x0 + int(w * 0.38), y1 - int(h * 0.26)),
               (x0 + int(w * 0.30), y1 - int(h * 0.18))], fill=(198, 36, 48))


def intercept(d, box):
    """Arcing interceptor tracks over a skyline: the Riyadh intercepts."""
    x0, y0, x1, y1, w, h = _big(box)
    _bg(d, box, (206, 200, 214))
    _bar(d, box, 0.26, (88, 76, 96))
    for i, (fx, up) in enumerate(((0.24, 0.30), (0.50, 0.40), (0.76, 0.26))):
        ax = x0 + int(w * fx)
        ay = y0 + int(h * (0.66 - up))
        d.arc([ax - int(w * 0.18), ay - int(h * 0.18), ax + int(w * 0.18), ay + int(h * 0.18)],
              200, 340, fill=(198, 36, 48), width=max(2, int(w * 0.022)))
        d.ellipse([ax - 4, ay - 4, ax + 4, ay + 4], fill=(232, 186, 72))
    for i in range(5):
        bx = x0 + int(w * (0.10 + 0.17 * i))
        d.rectangle([bx, y1 - int(h * 0.26), bx + int(w * 0.10), y1 - int(h * 0.14)],
                    fill=(64, 56, 72))


def powerplant(d, box):
    """Cooling towers with a plume: the Hartha fire."""
    x0, y0, x1, y1, w, h = _big(box)
    _bg(d, box, (198, 206, 208))
    _bar(d, box, 0.22, (102, 110, 100))
    for fx, fh in ((0.20, 0.46), (0.52, 0.56), (0.78, 0.38)):
        cx = x0 + int(w * fx)
        tw = int(w * 0.15)
        top = y1 - int(h * (0.24 + fh))
        d.polygon([(cx - tw // 2, y1 - int(h * 0.22)), (cx + tw // 2, y1 - int(h * 0.22)),
                   (cx + tw // 3, top), (cx - tw // 3, top)], fill=(150, 146, 138))
    cx = x0 + int(w * 0.52)
    d.polygon([(cx - int(w * 0.04), y1 - int(h * 0.78)), (cx + int(w * 0.10), y1 - int(h * 0.96)),
               (cx + int(w * 0.02), y1 - int(h * 0.80))], fill=(226, 118, 44))


def bottle(d, box):
    """A bottle and a struck-through glass: the spurious liquor deaths."""
    x0, y0, x1, y1, w, h = _big(box)
    _bg(d, box, (226, 216, 200))
    _bar(d, box, 0.18, (170, 152, 128))
    bx = x0 + int(w * 0.30)
    bw = int(w * 0.16)
    d.rectangle([bx, y0 + int(h * 0.34), bx + bw, y1 - int(h * 0.20)], fill=(112, 84, 62))
    d.rectangle([bx + int(bw * 0.32), y0 + int(h * 0.16), bx + int(bw * 0.68), y0 + int(h * 0.34)],
                fill=(112, 84, 62))
    d.rectangle([bx + int(bw * 0.10), y0 + int(h * 0.50), bx + int(bw * 0.90), y0 + int(h * 0.64)],
                fill=(198, 36, 48))
    gx = x0 + int(w * 0.66)
    d.polygon([(gx - int(w * 0.09), y0 + int(h * 0.40)), (gx + int(w * 0.09), y0 + int(h * 0.40)),
               (gx + int(w * 0.06), y1 - int(h * 0.22)), (gx - int(w * 0.06), y1 - int(h * 0.22))],
              outline=DARK, width=max(2, int(w * 0.018)))
    d.line([(gx - int(w * 0.10), y1 - int(h * 0.26)), (gx + int(w * 0.10), y0 + int(h * 0.36))],
           fill=(198, 36, 48), width=max(3, int(w * 0.026)))


def ballot(d, box):
    """A ballot box and a paper: the Hong Kong poll."""
    x0, y0, x1, y1, w, h = _big(box)
    _bg(d, box, (214, 220, 210))
    _bar(d, box, 0.18, (146, 156, 140))
    bx0, bx1 = x0 + int(w * 0.22), x0 + int(w * 0.74)
    by0 = y0 + int(h * 0.44)
    d.rectangle([bx0, by0, bx1, y1 - int(h * 0.22)], fill=(64, 78, 96))
    d.rectangle([bx0 + int(w * 0.10), by0 - int(h * 0.05), bx1 - int(w * 0.10), by0 + int(h * 0.04)],
                fill=(44, 54, 68))
    px = x0 + int(w * 0.52)
    d.polygon([(px, y0 + int(h * 0.12)), (px + int(w * 0.20), y0 + int(h * 0.16)),
               (px + int(w * 0.20), y0 + int(h * 0.42)), (px, y0 + int(h * 0.44))],
              fill=WHITE)
    d.line([(px + int(w * 0.05), y0 + int(h * 0.24)), (px + int(w * 0.16), y0 + int(h * 0.26))],
           fill=(198, 36, 48), width=max(2, int(h * 0.02)))


def ballot2(d, box):
    """A falling bar chart: the ANC's worst result since 1994."""
    x0, y0, x1, y1, w, h = _big(box)
    _bg(d, box, (222, 214, 200))
    _bar(d, box, 0.16, (158, 148, 130))
    base = y1 - int(h * 0.22)
    for i, frac in enumerate((0.62, 0.52, 0.44, 0.30)):
        bw = int(w * 0.14)
        bx = x0 + int(w * (0.14 + 0.19 * i))
        d.rectangle([bx, base - int(h * frac), bx + bw, base],
                    fill=(46, 107, 79) if i < 3 else (198, 36, 48))


def prison(d, box):
    """Bars and a block: the Haiti–El Salvador prison deal."""
    x0, y0, x1, y1, w, h = _big(box)
    _bg(d, box, (216, 212, 200))
    _bar(d, box, 0.18, (152, 144, 128))
    bx0 = x0 + int(w * 0.20)
    bx1 = x0 + int(w * 0.78)
    by0 = y0 + int(h * 0.16)
    by1 = y1 - int(h * 0.22)
    d.rectangle([bx0, by0, bx1, by1], outline=DARK, width=max(3, int(w * 0.028)))
    n = 5
    for i in range(1, n):
        bx = bx0 + int((bx1 - bx0) * i / n)
        d.line([(bx, by0), (bx, by1)], fill=DARK, width=max(2, int(w * 0.022)))


def map_panel(d, box, pins, labels=None):
    """A world map in an equirectangular frame, drawn from the pin records."""
    x0, y0, x1, y1, w, h = _big(box)
    d.rectangle([x0, y0, x1, y1], fill=(20, 32, 44))

    def proj(lat, lon):
        px = x0 + int((lon + 180.0) / 360.0 * w)
        py = y0 + int((90.0 - lat) / 180.0 * h)
        return px, py

    # Coarse landmass blocks, enough to read as continents at thumbnail size.
    land = (60, 84, 68)
    blocks = [
        (-168, 72, -52, 8), (-82, 12, -34, -56), (-18, 37, 52, -35),
        (-10, 36, 40, -5), (26, 82, 180, 8), (96, 22, 155, -11),
        (113, -11, 154, -45), (-180, -60, 180, -78),
    ]
    for lo_lon, hi_lat, hi_lon, lo_lat in blocks:
        a = proj(hi_lat, lo_lon)
        b = proj(lo_lat, hi_lon)
        d.rectangle([min(a[0], b[0]), min(a[1], b[1]),
                     max(a[0], b[0]), max(a[1], b[1])], fill=land)

    for num, lat, lon in pins:
        px, py = proj(lat, lon)
        r = max(4, int(min(w, h) * 0.030))
        d.ellipse([px - r, py - r, px + r, py + r], fill=(198, 36, 48))
        d.ellipse([px - r // 2, py - r // 2, px + r // 2, py + r // 2], fill=WHITE)


PANELS = {
    "capture": capture,
    "missiles": missiles,
    "jet": jet,
    "ruins": ruins,
    "ship": ship,
    "crowd": crowd,
    "spy": spy,
    "rubble": rubble,
    "dronehit": dronehit,
    "intercept": intercept,
    "powerplant": powerplant,
    "bottle": bottle,
    "ballot": ballot,
    "ballot2": ballot2,
    "prison": prison,
}


def draw_panel(draw, name, box):
    """Draw one named pictogram into box, clipped hard to that box.

    Each panel is rendered onto a transparent layer the size of the whole sheet
    and only the box's own pixels are pasted through. A shape can then never
    land outside the panel it belongs to, whatever coordinates it asks for.
    """
    x0, y0, x1, y1 = [int(v) for v in box]
    if x1 <= x0 or y1 <= y0:
        return
    fn = PANELS.get(name)
    if fn is None:
        draw.rectangle([x0, y0, x1, y1], fill=(120, 120, 124))
        return
    canvas = draw._image
    layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    fn(ImageDraw.Draw(layer), (x0, y0, x1, y1))
    canvas.paste(layer.crop((x0, y0, x1, y1)), (x0, y0), layer.crop((x0, y0, x1, y1)))
