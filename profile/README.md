<!-- SPDX-License-Identifier: MPL-2.0 -->
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/NBTFoundry/.github/main/profile/assets/logo-dark.png">
    <img src="https://raw.githubusercontent.com/NBTFoundry/.github/main/profile/assets/logo-light.png" alt="NBTFoundry" height="56">
  </picture>
</p>

<p align="center">
  <b>Run new applications on BMW NBT Evo head units, and write your own.</b>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/NBTFoundry/.github/main/profile/assets/hero-dark.png">
    <img src="https://raw.githubusercontent.com/NBTFoundry/.github/main/profile/assets/hero-light.png" width="860"
         alt="The phone app and the desktop installer reach NBT Manager on the head unit; the driver approves on iDrive">
  </picture>
</p>

NBTFoundry is everything an application needs to live on the iDrive 6 screen.
NBT Manager runs on the head unit and hosts applications: it gives them the
screen, the iDrive controller, USB gamepads, the car's audio and car data,
supervises them, and brings back the last good version when an update fails.
Developers write applications in C++ with the SDK, try them on a Linux desktop
and compile them for the car with an open-source toolchain. Drivers install,
update and configure them from a paired phone, and approve every change on the
car.

**Supported head units:** BMW NBT Evo (iDrive 6). Support for the earlier NBT may
come later.

**Status:** early. [NBT Manager 0.3.1](https://github.com/NBTFoundry/manager/releases/tag/v0.3.1)
is a pre-release, as is the [desktop installer 0.1.0](https://github.com/NBTFoundry/installer/releases/tag/v0.1.0)
(Windows, macOS, Linux); the phone app has no public release yet and is built
from source.

### What you can do

- **Install from your phone.** Pair once with a code on the car's screen, then
  send applications and updates over the car's Wi-Fi. The car checks each
  package's signature and the driver confirms it on iDrive.
- **Stay safe from bad updates.** A new version must start and stay healthy;
  otherwise the previous one comes back by itself. An application too old for
  the installed manager stays disabled until it is updated, instead of crashing.
- **Bring your own games and files.** Send them from the phone, or plug a USB
  stick into the car and import them; they are kept on the head unit's hard disk.
- **Use the car's own controls.** Applications read the iDrive controller and a
  wired USB gamepad, play through the car's speakers, and change their settings
  live from the phone.
- **Start with the car.** An application can start by itself when the head unit
  boots.
- **In your language.** English, French, German, Italian, Spanish, Chinese and
  Japanese; the manager follows iDrive's language.
- **Write your own.** The C++ SDK gives an application the screen (OpenGL ES 2),
  audio, input, files and the manager's lifecycle, and builds the same code for a
  Linux desktop. A front end and a libretro host turn an emulator core into an
  application. The NBT toolchain, prebuilt for Linux, macOS and Windows, compiles
  it for the car with open-source tools only, without the QNX SDK.
- **Apps in minutes.** Open the [template](https://github.com/NBTFoundry/template),
  start your coding agent and tell it what you want on the screen. The SDK ships
  the [skills](https://github.com/NBTFoundry/sdk/blob/main/docs/porting.md) that
  teach it the API, the car's controls and packaging, and the compiler is a free
  download, so the app runs on your desktop first and the same code builds for
  the car. Doom and four emulators reached the car this way.
- **Publish it.** Open a pull request on
  [community-apps](https://github.com/NBTFoundry/community-apps): we build your
  application from its source, sign it and list it in Get apps.

### Coming soon

- **Your own key.** Sign an app with your own key, add the key from the phone,
  and run your builds on your car.
- **Engine data.** Engine readings and fault codes for the apps that ask for them.
- **Phone companions.** An app can bring its own screen to the phone app, for
  settings, files or a second display.

<table>
  <tr>
    <td width="56%" align="center"><img src="https://raw.githubusercontent.com/NBTFoundry/.github/main/profile/assets/manager-install.gif" alt="On the car: an update arrives, the driver reviews and installs it, the health check passes"><br>
      <sub>On the car: review, install, health check</sub></td>
    <td width="22%" align="center"><img src="https://raw.githubusercontent.com/NBTFoundry/.github/main/profile/assets/mobile-install.webp" alt="On the phone: an install is requested, approved on the car, and listed"><br>
      <sub>On the phone</sub></td>
    <td width="22%" align="center"><img src="https://raw.githubusercontent.com/NBTFoundry/.github/main/profile/assets/doom-demo.webp" alt="Doom running on the head unit's screen"><br>
      <sub>Doom on the head unit</sub></td>
  </tr>
</table>

### Applications

| Application | What it is | State | License |
| --- | --- | --- | --- |
| [nf-doom](https://github.com/NBTFoundry/nf-doom) | Doom (PrBoom+), with the shareware episode | [1.0.23](https://github.com/NBTFoundry/nf-doom/releases/tag/v1.0.23) | GPL-2.0-or-later; game data separate |
| [nf-snes9x](https://github.com/NBTFoundry/nf-snes9x) | Snes9x: Super Nintendo games you own, from the phone or a USB stick | [1.63.4](https://github.com/NBTFoundry/nf-snes9x/releases/tag/v1.63.4) | MPL-2.0; Snes9x non-commercial |
| [nf-fbneo](https://github.com/NBTFoundry/nf-fbneo) | FinalBurn Neo: arcade games from zipped romsets | [0.1.0](https://github.com/NBTFoundry/nf-fbneo/releases/tag/v0.1.0) beta | MPL-2.0; FinalBurn Neo non-commercial |
| [nf-pcsx-rearmed](https://github.com/NBTFoundry/nf-pcsx-rearmed) | PCSX ReARMed: PlayStation games you own, from a USB stick | [0.1.0](https://github.com/NBTFoundry/nf-pcsx-rearmed/releases/tag/v0.1.0) beta | GPL-2.0-or-later |
| [nf-picodrive](https://github.com/NBTFoundry/nf-picodrive) | PicoDrive: Mega Drive, Mega-CD, 32X and Master System games you own | [0.1.0](https://github.com/NBTFoundry/nf-picodrive/releases/tag/v0.1.0) beta | MPL-2.0; PicoDrive non-commercial |
| [nf-android-auto](https://github.com/NBTFoundry/nf-android-auto) | Android Auto: [NBT-AAD](https://github.com/Sq00ky/Supra-iDrive6-Android-Auto), installed and updated like any application | [0.1.0](https://github.com/NBTFoundry/nf-android-auto/releases/tag/v0.1.0) beta | MPL-2.0; NBT-AAD PolyForm Noncommercial 1.0.0 |
| [nf-gauges](https://github.com/NBTFoundry/nf-gauges) | Gauges: live engine gauges read from the car's own computers, no OBD adapter | [0.1.0](https://github.com/NBTFoundry/nf-gauges/releases/tag/v0.1.0) beta | MPL-2.0 |

Apart from Doom's shareware episode, no game, ROM or BIOS is included: use only
games you have the right to use.

### Projects

| Repository | What it is | License |
| --- | --- | --- |
| [manager](https://github.com/NBTFoundry/manager) | NBT Manager, on the head unit: the iDrive menu entry, the manager's screen, signed installs and updates with rollback, the application bridge | MPL-2.0 |
| [mobile-app](https://github.com/NBTFoundry/mobile-app) | The Android app: pairing, the package library, installs, updates, settings, files and logs | MPL-2.0 |
| [installer](https://github.com/NBTFoundry/installer) | The desktop installer: puts NBT Manager on the car over the ENET cable, updates it, collects diagnostics | GPL-3.0-or-later; shared core/bindings MPL-2.0 |
| [sdk](https://github.com/NBTFoundry/sdk) | The C++11 SDK for applications: lifecycle, display, audio, controller and gamepad input, files, a reusable front end and a libretro host for emulators | MPL-2.0 |
| [toolchains](https://github.com/NBTFoundry/toolchains) | The NBT toolchain: Clang and LLD with the runtime applications link (picolibc, libc++), released for Linux, macOS and Windows | MPL-2.0; LLVM and picolibc under their own licenses |

### How the pieces fit

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/NBTFoundry/.github/main/profile/assets/pieces-dark.png">
    <img src="https://raw.githubusercontent.com/NBTFoundry/.github/main/profile/assets/pieces-light.png" width="860"
         alt="The phone app (signed packages over Wi-Fi) and the desktop installer (SSH over ENET) reach NBT Manager on the head unit, driven by iDrive's menu and controller; NBT Manager gives the applications, built with the SDK and the NBT toolchain, the screen, input, audio, files and settings">
  </picture>
</p>

### Support

If NBTFoundry is useful to you, you can support its development on
[GitHub Sponsors](https://github.com/sponsors/fpoussin) or
[Ko-fi](https://ko-fi.com/fpoussin). Donations are optional and buy nothing:
every application stays free.

<p>
  <a href="https://github.com/sponsors/fpoussin"><img src="https://img.shields.io/badge/Sponsor_on_GitHub-ea4aaa?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="Sponsor on GitHub" height="28"></a>
  <a href="https://ko-fi.com/fpoussin"><img src="https://img.shields.io/badge/Support_on_Ko--fi-FF5E5B?style=for-the-badge&logo=kofi&logoColor=white" alt="Support on Ko-fi" height="28"></a>
</p>

### Safety

> **Warning: installing or modifying this software can brick your head unit. Recovery may require professional service or replacement, at your expense. Provided AS IS; use at your own risk, subject to applicable law.** [Read the risk and liability disclaimer](https://github.com/NBTFoundry/.github/blob/main/DISCLAIMER.md).

Use applications only while parked. Changing the software of a head unit is at
your own risk: it can affect the car's systems and its warranty.

---

<sub>Not affiliated with or endorsed by BMW AG or any other trademark owner named here.
BMW, iDrive and NBT are trademarks of BMW AG; DOOM of id Software; Super Nintendo of
Nintendo; PlayStation of Sony Interactive Entertainment Inc.; Mega Drive, Mega-CD, 32X and
Master System of Sega Corporation; Android Auto of Google LLC;
QNX of BlackBerry Limited.</sub>

## License

Copyright (c) 2026 Fabien Poussin. Original code, tests, build scripts and documentation are licensed under **MPL-2.0**; see [LICENSE](https://github.com/NBTFoundry/.github/blob/main/LICENSE).

Original NBTFoundry logos, artwork and screenshots are under **MPL-2.0**, including copies in other NBTFoundry repositories. Third-party code, fonts, game data and their notices retain their own terms. Copyright permission for artwork does not grant trademark rights or imply endorsement by BMW AG or any other trademark owner.

See [legal/README.md](https://github.com/NBTFoundry/.github/blob/main/legal/README.md) for third-party license notices.
