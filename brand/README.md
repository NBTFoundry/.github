<!-- SPDX-License-Identifier: MPL-2.0 -->
# NBTFoundry brand kit

The mark is the iDrive controller's detent ring around a grid of applications,
one of them highlighted. The wordmark is "NBT" in Space Grotesk Bold and
"Foundry" in Space Grotesk Regular, converted to outlines.

| File | Use |
| --- | --- |
| `logo-light.svg`, `logo-dark.svg` | Mark and wordmark, for light and dark pages (README headers) |
| `mark-light.svg`, `mark-dark.svg`, `mark-mono.svg` | The mark alone; `mono` is one colour |
| `avatar.svg`, `png/avatar-512.png` | The organization's avatar |
| `app-icon.svg`, `app-adaptive-*.svg`, `png/app-*`, `png/splash-*` | The phone app's launcher icon, adaptive icon layers and splash |
| `png/idrive-63x54.png`, `png/idrive-549x484.png` | The iDrive menu icon (8-bit RGBA, one colour) |
| `png/mark-{light,dark}-<size>.png` | The mark from 16 to 1024 px |

## Colours

| | Light pages | Dark pages and the car |
| --- | --- | --- |
| Ink | `#141a22` | `#e8eef4` |
| Accent | `#245bb5` | `#4d8fe0` |
| Car screen | | `#0a0f17` background, `#1d5fa8` selection |

## Rebuilding

```sh
python3 brand/render.py   # needs fontTools, Space Grotesk and Inkscape; pngquant when present
python3 brand/hero.py     # the profile's illustration, profile/assets/hero-{light,dark}.svg
```

The manager's `plugin/assets/` and the phone app's `assets/` hold copies of the
PNG exports.
