#!/usr/bin/env python3
# SPDX-License-Identifier: MPL-2.0
"""Draws the organization profile's hero illustration, light and dark: the phone
app and the desktop installer around the head unit's screen, the driver's
approval on the iDrive controller below it.

    python3 brand/hero.py      # writes profile/assets/hero-{light,dark}.svg

Plain SVG, no fonts embedded: labels use the viewer's sans-serif. The palette
and the mark come from render.py, so fontTools must be importable.
"""

from pathlib import Path

from render import BLUE_DARK, BLUE_LIGHT, CAR_BG, CAR_BLUE, CAR_INK, INK_LIGHT, mark_body

OUT = Path(__file__).resolve().parents[1] / "profile" / "assets"
FONT = "system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"

THEMES = {
    "light": dict(ink=INK_LIGHT, muted="#5b6573", line="#aeb8c4", accent=BLUE_LIGHT, surface="#ffffff",
                  page="#f6f7fa", body="#1b1e24", rule="#e3e7ec"),
    "dark": dict(ink=CAR_INK, muted="#9aa6b4", line="#4a5462", accent=BLUE_DARK, surface="#1c222b",
                 page="#111318", body="#2a303a", rule="#2c333d"),
}


def text(x, y, value, size, fill, weight=400, anchor="middle"):
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}">{value}</text>')


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
    for i, (name, tag) in enumerate((("doom", True), ("media-player", False), ("test", False))):
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
        text(x + 24, y + 62, "doom", 12, CAR_INK, 500, "start"),
        text(x + 24, y + 90, "media-player", 12, CAR_INK, 400, "start"),
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


def arrow(t, x1, y1, x2, y2, label, label_x, label_y):
    return "".join([
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{t["accent"]}" stroke-width="2.5" '
        f'stroke-dasharray="7 6" stroke-linecap="round" marker-end="url(#head)"/>',
        text(label_x, label_y, label, 12.5, t["muted"], 500),
    ])


def hero(t):
    w, h = 960, 380
    body = [
        f'<defs><marker id="head" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="7" markerHeight="7" '
        f'orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="{t["accent"]}"/></marker></defs>',
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
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="The phone app and the desktop installer reach NBT Manager on the head '
            f'unit; the driver approves on iDrive">{"".join(body)}</svg>\n')


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, theme in THEMES.items():
        (OUT / f"hero-{name}.svg").write_text(hero(theme))
    print(f"hero in {OUT}")


if __name__ == "__main__":
    main()
