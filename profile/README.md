<!-- SPDX-License-Identifier: MPL-2.0 -->
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.svg">
    <img src="assets/logo-light.svg" alt="NBTFoundry" height="56">
  </picture>
</p>

<p align="center">
  <b>Applications for BMW NBT Evo head units, installed from your phone.</b>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
    <img src="assets/hero-light.svg" width="860"
         alt="The phone app and the desktop installer reach NBT Manager on the head unit; the driver approves on iDrive">
  </picture>
</p>

NBTFoundry turns the iDrive 6 screen into a small application platform. NBT
Manager runs on the head unit and adds an entry to the iDrive menu; applications
start from it, get the screen, the controller and the car's audio, and hand them
back when they close. A paired phone installs, updates and configures them, and
every change is approved by the driver on the car.

**Supported head units:** BMW NBT Evo (iDrive 6). Support for the earlier NBT may
come later.

### What you can do

- **Install from your phone.** Pair once with a code on the car's screen, then
  send applications and updates over the car's Wi-Fi. The car checks each
  package's signature and the driver confirms it on iDrive.
- **Stay safe from bad updates.** A new version must start and stay healthy;
  otherwise the previous one comes back by itself.
- **Use the car's own controls.** Applications read the iDrive controller and a
  wired USB gamepad, and change their settings live from the phone.
- **Write your own.** The C++ SDK gives an application the screen (OpenGL ES 2),
  audio, input and the manager's lifecycle, and builds the same code for a Linux
  desktop. The NBT toolchain, prebuilt for Linux, macOS and Windows, compiles it
  for the car with open-source tools only, without the QNX SDK.
- **Play Doom on the dashboard.** The shareware episode, as the example
  application.

<table>
  <tr>
    <td width="56%" align="center"><img src="assets/manager-install.gif" alt="On the car: an update arrives, the driver reviews and installs it, the health check passes"><br>
      <sub>On the car: review, install, health check</sub></td>
    <td width="22%" align="center"><img src="assets/mobile-install.webp" alt="On the phone: an install is requested, approved on the car, and listed"><br>
      <sub>On the phone</sub></td>
    <td width="22%" align="center"><img src="assets/doom-demo.webp" alt="Doom running on the head unit's screen"><br>
      <sub>Doom, the example application</sub></td>
  </tr>
</table>

### Projects

| Repository | What it is | License |
| --- | --- | --- |
| [manager](https://github.com/NBTFoundry/manager) | NBT Manager, on the head unit: the iDrive menu entry, the manager's screen, signed installs and updates with rollback, the application bridge | MPL-2.0 |
| [mobile-app](https://github.com/NBTFoundry/mobile-app) | The Android app: pairing, the package library, installs, updates, settings and logs | MPL-2.0 |
| [installer](https://github.com/NBTFoundry/installer) | The desktop installer: puts NBT Manager on the car over the ENET cable, updates it, collects diagnostics | GPL-3.0-or-later; shared core/bindings MPL-2.0 |
| [sdk](https://github.com/NBTFoundry/sdk) | The C++11 SDK for applications: lifecycle, display, audio, controller and gamepad input, files, a reusable front end and a libretro host for emulators | MPL-2.0 |
| [toolchains](https://github.com/NBTFoundry/toolchains) | The NBT toolchain: Clang and LLD with the runtime applications link (picolibc, libc++), released for Linux, macOS and Windows | MPL-2.0; LLVM and picolibc under their own licenses |
| [nf-doom](https://github.com/NBTFoundry/nf-doom) | PrBoom+ on the head unit, built on the SDK | GPL-2.0-or-later; game data separate |

### How the pieces fit

```mermaid
flowchart LR
  PHONE["Phone app"] -->|"signed packages · Wi-Fi"| MANAGER["NBT Manager<br/>on the head unit"]
  INSTALLER["Desktop installer"] -->|"SSH · ENET"| MANAGER
  IDRIVE["iDrive menu and controller"] <--> MANAGER
  MANAGER -->|"screen · input · audio · settings"| APP["Applications<br/>built with the SDK"]
  SDK["SDK"] -.-> APP
  TOOLCHAIN["NBT toolchain"] -.-> APP
```

### Safety

> **Warning: installing or modifying this software can brick your head unit. Recovery may require professional service or replacement, at your expense. Provided AS IS; use at your own risk, subject to applicable law.** [Read the risk and liability disclaimer](../DISCLAIMER.md).

Use applications only while parked. Changing the software of a head unit is at
your own risk: it can affect the car's systems and its warranty.

---

<sub>Not affiliated with or endorsed by BMW AG. BMW, iDrive and NBT are trademarks of
BMW AG. DOOM is a trademark of id Software.</sub>

## License

Copyright (c) 2026 Fabien Poussin. Original code, tests, build scripts and documentation are licensed under **MPL-2.0**; see [LICENSE](../LICENSE).

Original NBTFoundry logos, artwork and screenshots are under **MPL-2.0**, including copies in other NBTFoundry repositories. Third-party code, fonts, game data and their notices retain their own terms. Copyright permission for artwork does not grant trademark rights or imply endorsement by BMW AG or id Software.

See [legal/README.md](../legal/README.md) for third-party license notices.
