#!/usr/bin/env python3
"""Builds the NBTFoundry brand kit: the mark (the iDrive knob's detent ring
around a grid of apps), the wordmark lockups, and the PNG exports used by the
repositories, the phone app and the iDrive menu.

    python3 brand/render.py

Needs fontTools, Space Grotesk (Regular and Bold) and Inkscape. Everything is
written next to this script; the SVGs contain outlines only, no fonts.
"""

import math
from pathlib import Path
import shutil
import subprocess
import sys

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

HERE = Path(__file__).resolve().parent
FONT_DIRS = [Path("/usr/share/fonts/truetype/space-grotesk"), Path.home() / ".local/share/fonts"]

# Palette: the manager's car interface and the phone app.
CAR_BG = "#0a0f17"
CAR_INK = "#e8eef4"
CAR_BLUE = "#1d5fa8"
INK_LIGHT = "#141a22"
BLUE_LIGHT = "#245bb5"
BLUE_DARK = "#4d8fe0"


def ticks_path(cx=32.0, cy=32.0, r=23.0, count=24, width=1.7, length=4.0):
    """The knob's detents: `count` short radial bars centred on radius `r`."""
    parts = []
    for i in range(count):
        a = 2 * math.pi * i / count
        ux, uy = math.cos(a), math.sin(a)          # radial
        tx, ty = -uy, ux                           # tangential
        r0, r1 = r - length / 2, r + length / 2
        corners = [
            (cx + ux * r0 + tx * width / 2, cy + uy * r0 + ty * width / 2),
            (cx + ux * r1 + tx * width / 2, cy + uy * r1 + ty * width / 2),
            (cx + ux * r1 - tx * width / 2, cy + uy * r1 - ty * width / 2),
            (cx + ux * r0 - tx * width / 2, cy + uy * r0 - ty * width / 2),
        ]
        parts.append("M" + " L".join(f"{x:.3f} {y:.3f}" for x, y in corners) + " Z")
    return " ".join(parts)


TICKS = ticks_path()


def mark_body(ink, accent, tick_opacity=0.85):
    """The mark in a 64x64 box."""
    return (
        f'<circle cx="32" cy="32" r="28" fill="none" stroke="{ink}" stroke-width="3"/>'
        f'<path d="{TICKS}" fill="{ink}" fill-opacity="{tick_opacity}"/>'
        f'<rect x="20.5" y="20.5" width="10" height="10" rx="2.5" fill="{ink}"/>'
        f'<rect x="33.5" y="20.5" width="10" height="10" rx="2.5" fill="{accent}"/>'
        f'<rect x="20.5" y="33.5" width="10" height="10" rx="2.5" fill="{ink}"/>'
        f'<rect x="33.5" y="33.5" width="10" height="10" rx="2.5" fill="{ink}"/>'
    )


def svg(width, height, body, view=None):
    view = view or f"0 0 {width} {height}"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="{view}">{body}</svg>\n')


def find_font(name):
    for directory in FONT_DIRS:
        path = directory / name
        if path.is_file():
            return path
    sys.exit(f"{name} not found (install Space Grotesk)")


def text_path(font_file, text, size, x, baseline, tracking=0.0):
    """`text` as one SVG path, at font size `size` (units per em scaled), starting at x."""
    font = TTFont(font_file)
    glyphs = font.getGlyphSet()
    cmap = font.getBestCmap()
    scale = size / font["head"].unitsPerEm
    pen = SVGPathPen(glyphs)
    cursor = x
    for ch in text:
        name = cmap[ord(ch)]
        glyph = glyphs[name]
        glyph.draw(TransformPen(pen, (scale, 0, 0, -scale, cursor, baseline)))
        cursor += glyph.width * scale + tracking
    return pen.getCommands(), cursor


def lockup(ink, accent, word_ink):
    """The mark and the "NBTFoundry" wordmark side by side."""
    size = 34.0
    baseline = 44.0
    bold, end = text_path(find_font("SpaceGrotesk-Bold.ttf"), "NBT", size, 78.0, baseline, -0.2)
    regular, end = text_path(find_font("SpaceGrotesk-Regular.ttf"), "Foundry", size, end + 1.0,
                             baseline, -0.2)
    width = math.ceil(end + 4)
    body = (mark_body(ink, accent)
            + f'<path d="{bold}" fill="{word_ink}"/><path d="{regular}" fill="{word_ink}"/>')
    return svg(width, 64, body)


def write(name, text):
    (HERE / name).write_text(text)
    return HERE / name


def png(svg_file, out, width, height=None, background=None, quantize=True):
    """Exports with Inkscape at the given pixel size (8-bit RGBA unless quantized)."""
    cmd = ["inkscape", str(svg_file), "--export-type=png", f"--export-filename={out}",
           f"--export-width={width}"]
    if height:
        cmd.append(f"--export-height={height}")
    if background:
        cmd += [f"--export-background={background}", "--export-background-opacity=1"]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if quantize and shutil.which("pngquant"):
        subprocess.run(["pngquant", "--force", "--skip-if-larger", "--output", str(out), "--", str(out)])


def main():
    if not shutil.which("inkscape"):
        sys.exit("inkscape is required")
    exports = HERE / "png"
    exports.mkdir(exist_ok=True)

    # Marks: for light backgrounds, for dark backgrounds, and one colour.
    light = write("mark-light.svg", svg(64, 64, mark_body(INK_LIGHT, BLUE_LIGHT)))
    dark = write("mark-dark.svg", svg(64, 64, mark_body(CAR_INK, BLUE_DARK)))
    write("mark-mono.svg", svg(64, 64, mark_body("#000000", "#000000", 1.0)))
    idrive = write("mark-idrive.svg", svg(64, 64, mark_body(CAR_INK, CAR_INK, 1.0)))

    # Lockups for README headers (light and dark page).
    write("logo-light.svg", lockup(INK_LIGHT, BLUE_LIGHT, INK_LIGHT))
    write("logo-dark.svg", lockup(CAR_INK, BLUE_DARK, CAR_INK))

    for size in (16, 32, 64, 128, 256, 512, 1024):
        png(light, exports / f"mark-light-{size}.png", size)
        png(dark, exports / f"mark-dark-{size}.png", size)

    # Organization avatar: the mark on the car's dark background.
    avatar = write("avatar.svg", svg(512, 512,
                                     f'<rect width="512" height="512" fill="{CAR_BG}"/>'
                                     f'<g transform="translate(64 64) scale(6)">{mark_body(CAR_INK, BLUE_DARK)}</g>'))
    png(avatar, exports / "avatar-512.png", 512)

    # Phone app: launcher icon, adaptive icon layers (mark in the 66 % safe
    # zone), splash images for light and dark.
    icon = write("app-icon.svg", svg(1024, 1024,
                                     f'<rect width="1024" height="1024" fill="{CAR_BLUE}"/>'
                                     f'<g transform="translate(192 192) scale(10)">{mark_body("#ffffff", CAR_BG, 0.9)}</g>'))
    png(icon, exports / "app-icon-1024.png", 1024)
    fg = write("app-adaptive-foreground.svg", svg(432, 432,
                                                  f'<g transform="translate(88 88) scale(4)">{mark_body("#ffffff", CAR_BG, 0.9)}</g>'))
    png(fg, exports / "app-adaptive-foreground-432.png", 432)
    mono = write("app-adaptive-monochrome.svg", svg(432, 432,
                                                    f'<g transform="translate(88 88) scale(4)">{mark_body("#ffffff", "#ffffff", 1.0)}</g>'))
    png(mono, exports / "app-adaptive-monochrome-432.png", 432)
    png(light, exports / "splash-light-512.png", 512)
    png(dark, exports / "splash-dark-512.png", 512)

    # iDrive menu icons: one colour on transparent, the mark as tall as the
    # icon, 8-bit RGBA as BMW's own plugin images.
    for w, h in ((63, 54), (549, 484)):
        side = min(w, h)
        out = exports / f"idrive-{w}x{h}.png"
        tmp = write(f".idrive-{w}x{h}.svg", svg(w, h,
                                                 f'<g transform="translate({(w - side) / 2:.2f} {(h - side) / 2:.2f}) '
                                                 f'scale({side / 64:.5f})">{mark_body(CAR_INK, CAR_INK, 1.0)}</g>'))
        png(tmp, out, w, h, quantize=False)
        tmp.unlink()
    idrive.unlink()
    print(f"brand kit in {HERE}")


if __name__ == "__main__":
    main()
