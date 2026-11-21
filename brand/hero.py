#!/usr/bin/env python3
# SPDX-License-Identifier: MPL-2.0
"""Draws the organization profile's illustrations, light and dark, and exports
them as PNG: GitHub's mobile app shows no SVG image.

- hero: the phone app and the desktop installer around the head unit's
  screen, the driver's approval on the iDrive controller below it;
- pieces: how the projects fit together;
- the logo, from profile/assets/logo-{light,dark}.svg (brand/render.py).

    python3 brand/hero.py   # profile/assets/{hero,pieces}-{light,dark}.svg and every .png

The SVGs are the sources: no fonts embedded, labels in Noto Sans (else the
viewer's sans-serif). The palette, the mark and the PNG export (Inkscape,
pngquant) come from render.py, so fontTools must be importable. Light PNGs get
a white background, so they stay readable where a dark page shows them.
"""

from pathlib import Path
import re
import shutil
import sys

from render import BLUE_DARK, BLUE_LIGHT, CAR_BG, CAR_BLUE, CAR_INK, INK_LIGHT, mark_body, png

OUT = Path(__file__).resolve().parents[1] / "profile" / "assets"
FONT = "'Noto Sans', system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
HEADER = "<!-- SPDX-License-Identifier: MPL-2.0 -->\n"
SCALE = 2           # PNG pixels per SVG unit
LOGO_HEIGHT = 168   # the profile shows the logo 56 px high: 3x

THEMES = {
    "light": dict(ink=INK_LIGHT, muted="#5b6573", line="#aeb8c4", accent=BLUE_LIGHT, surface="#ffffff",
                  page="#f6f7fa", body="#1b1e24", rule="#e3e7ec", background="#ffffff"),
    "dark": dict(ink=CAR_INK, muted="#9aa6b4", line="#4a5462", accent=BLUE_DARK, surface="#1c222b",
                 page="#111318", body="#2a303a", rule="#2c333d", background=None),
}


def text(x, y, value, size, fill, weight=400, anchor="middle"):
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}">{value}</text>')


def defs(t):
    return (f'<defs><marker id="head" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="{t["accent"]}"/></marker></defs>')


def drawing(w, h, label, body):
    return (f'{HEADER}<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-label="{label}">{"".join(body)}</svg>\n')


def phone(t, x, y):
    """A phone showing the Car tab: the car's name and three applications."""
    w, h = 132, 264
    parts = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="{t["body"]}"/>',
        f'<rect x="{x + 7}" y="{y + 7}" width="{w - 14}" height="{h - 14}" rx="16" fill="{t["page"]}"/>',
        text(x + 18, y + 40, "Car", 8, t["muted"], 600, "start"),
        text(x + 18, y + 58, "My car", 16, t["ink"], 700, "start"),
        f'<rect x="{x + 16}" y="{y + 72}" width="{w - 32}" height="22" rx="11" fill="{t["accent"]}"/>',
    ]
    for i, (name, tag) in enumerate((("snes9x", True), ("fbneo", False), ("doom", False))):
        row = y + 116 + i * 34
        parts.append(text(x + 18, row, name, 10, t["ink"], 600, "start"))
        parts.append(f'<rect x="{x + 18}" y="{row + 6}" width="28" height="4" rx="2" fill="{t["line"]}"/>')
        if tag:
            parts.append(f'<circle cx="{x + w - 24}" cy="{row - 3}" r="4" fill="{t["accent"]}"/>')
        parts.append(f'<rect x="{x + 16}" y="{row + 16}" width="{w - 32}" height="1" fill="{t["rule"]}"/>')
    parts.append(f'<rect x="{x + w / 2 - 18}" y="{y + h - 16}" width="36" height="3" rx="1.5" '
                 f'fill="{t["muted"]}"/>')
    return "".join(parts)


def head_unit(t, x, y):
    """The head unit's wide screen with NBT Manager's menu and an application tile."""
    w, h = 384, 144
    parts = [
        f'<rect x="{x - 10}" y="{y - 10}" width="{w + 20}" height="{h + 20}" rx="18" fill="{t["body"]}"/>',
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{CAR_BG}"/>',
        text(x + 22, y + 32, "NBT App Manager", 15, CAR_INK, 600, "start"),
        f'<rect x="{x + 16}" y="{y + 46}" width="{w - 150}" height="22" rx="3" fill="{CAR_BLUE}"/>',
        text(x + 24, y + 62, "snes9x", 12, CAR_INK, 500, "start"),
        text(x + 24, y + 90, "doom", 12, CAR_INK, 400, "start"),
        text(x + 24, y + 118, "Settings", 12, "#a8c7ff", 400, "start"),
        f'<g transform="translate({x + w - 118} {y + 22}) scale(1.6)">{mark_body(CAR_INK, BLUE_DARK, 0.7)}</g>',
    ]
    return "".join(parts)


def laptop(t, x, y):
    w, h = 150, 96
    return "".join([
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{t["body"]}"/>',
        f'<rect x="{x + 6}" y="{y + 6}" width="{w - 12}" height="{h - 12}" rx="3" fill="{t["page"]}"/>',
        text(x + 14, y + 26, "NBT Manager Installer", 8.5, t["ink"], 600, "start"),
        f'<rect x="{x + 14}" y="{y + 36}" width="40" height="12" rx="3" fill="{t["accent"]}"/>',
        f'<rect x="{x + 58}" y="{y + 36}" width="40" height="12" rx="3" fill="{t["line"]}"/>',
        f'<rect x="{x + 14}" y="{y + 56}" width="{w - 40}" height="3" rx="1.5" fill="{t["line"]}"/>',
        f'<rect x="{x + 14}" y="{y + 64}" width="{w - 60}" height="3" rx="1.5" fill="{t["line"]}"/>',
        f'<path d="M{x - 14} {y + h + 2} H{x + w + 14} l-10 12 H{x - 4} Z" fill="{t["body"]}"/>',
    ])


def arrow(t, x1, y1, x2, y2, label="", label_x=0, label_y=0, dashed=True, both=False, anchor="middle"):
    dash = ' stroke-dasharray="7 6"' if dashed else ""
    start = ' marker-start="url(#head)"' if both else ""
    return "".join([
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{t["accent"]}" stroke-width="2.5"{dash} '
        f'stroke-linecap="round"{start} marker-end="url(#head)"/>',
        text(label_x, label_y, label, 12.5, t["muted"], 500, anchor) if label else "",
    ])


def hero(t):
    body = [
        defs(t),
        phone(t, 40, 40),
        head_unit(t, 288, 70),
        laptop(t, 776, 82),
        arrow(t, 188, 150, 268, 150, "Wi-Fi", 228, 136),
        arrow(t, 760, 150, 692, 150, "ENET", 726, 136),
        # The driver's approval on the controller, below the screen.
        f'<line x1="480" y1="234" x2="480" y2="268" stroke="{t["line"]}" stroke-width="2"/>',
        f'<g transform="translate(446 270) scale(1.06)">{mark_body(t["ink"], t["accent"])}</g>',
        text(106, 336, "Phone app", 15, t["ink"], 700),
        text(106, 356, "install · update · settings", 12.5, t["muted"]),
        text(480, 360, "NBT Manager on the head unit · approved on iDrive", 15, t["ink"], 700),
        text(851, 226, "Desktop installer", 15, t["ink"], 700),
        text(851, 246, "puts the manager on the car", 12.5, t["muted"]),
    ]
    return drawing(960, 380, "The phone app and the desktop installer reach NBT Manager on the head unit; "
                   "the driver approves on iDrive", body)


def box(t, x, y, w, h, title, lines=(), strong=False, title_y=None, size=15):
    """A labelled box: a title and muted lines below it, centred."""
    stroke = f'stroke="{t["accent"]}" stroke-width="2.5"' if strong else f'stroke="{t["line"]}" stroke-width="1.5"'
    cx = x + w / 2
    ty = title_y if title_y is not None else y + h / 2 + 5 - 9 * len(lines)
    parts = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{t["surface"]}" {stroke}/>',
             text(cx, ty, title, size, t["ink"], 700)]
    for i, line in enumerate(lines):
        parts.append(text(cx, ty + 21 + 18 * i, line, 12.5, t["muted"]))
    return "".join(parts)


def pieces(t):
    """Phone app and installer to the manager, the manager to the applications,
    iDrive below the manager, the SDK and toolchain below the applications."""
    body = [
        defs(t),
        box(t, 24, 40, 180, 64, "Phone app", ("Android",)),
        box(t, 24, 168, 180, 64, "Desktop installer", ("first install",)),
        box(t, 380, 40, 200, 192, "NBT Manager", ("on the head unit",), strong=True, title_y=168),
        f'<g transform="translate(451 70) scale(0.9)">{mark_body(t["ink"], t["accent"])}</g>',
        # The driver drives and approves on iDrive, below the manager (as in the hero).
        f'<line x1="480" y1="232" x2="480" y2="276" stroke="{t["line"]}" stroke-width="2"/>',
        box(t, 380, 276, 200, 44, "iDrive menu and controller", size=13.5, title_y=303),
        box(t, 736, 40, 200, 120, "Applications", ("Doom · Snes9x", "FinalBurn Neo", "Android Auto"),
            title_y=78),
        box(t, 736, 216, 200, 64, "SDK · NBT toolchain", ("C++11, no QNX SDK needed",)),
        arrow(t, 204, 72, 372, 72, "signed packages · Wi-Fi", 288, 62),
        arrow(t, 204, 200, 372, 200, "SSH · ENET", 288, 190),
        arrow(t, 580, 100, 728, 100, "screen · input · audio", 654, 76),
        text(654, 92, "files · settings", 12.5, t["muted"], 500),
        arrow(t, 836, 210, 836, 168, "builds", 850, 194, anchor="start"),
    ]
    return drawing(960, 336, "The phone app and the desktop installer reach NBT Manager on the head unit; "
                   "iDrive's menu and controller drive it; it gives applications built with the SDK and "
                   "the NBT toolchain the screen, input, audio, files and settings", body)


def svg_size(path):
    head = path.read_text()[:400]
    width = re.search(r'<svg[^>]* width="([\d.]+)"', head)
    height = re.search(r'<svg[^>]* height="([\d.]+)"', head)
    return float(width.group(1)), float(height.group(1))


def main():
    if not shutil.which("inkscape"):
        sys.exit("inkscape is required")
    OUT.mkdir(parents=True, exist_ok=True)
    for name, theme in THEMES.items():
        for kind, draw in (("hero", hero), ("pieces", pieces)):
            source = OUT / f"{kind}-{name}.svg"
            source.write_text(draw(theme))
            width, _ = svg_size(source)
            png(source, OUT / f"{kind}-{name}.png", int(width * SCALE), background=theme["background"])
        logo = OUT / f"logo-{name}.svg"
        width, height = svg_size(logo)
        png(logo, OUT / f"logo-{name}.png", round(width * LOGO_HEIGHT / height), LOGO_HEIGHT,
            background=theme["background"])
    print(f"profile illustrations in {OUT}")


if __name__ == "__main__":
    main()
