# computer-use — OpenClaw Skill

AI-powered desktop control via mouse, keyboard, and screenshots. Lets an OpenClaw agent interact with GUI applications on Linux/X11.

## Features

- 📸 **Screenshots** — full screen or region capture
- 🖱️ **Mouse** — move, click, double-click, right-click, drag, scroll
- ⌨️ **Keyboard** — type text, press key combos (Ctrl+C, Alt+Tab, etc.)
- 🖥️ **Screen info** — resolution, mouse position, active window

## Requirements

- **Linux with X11** (Xorg) — does NOT work on Wayland
- **Python 3**
- **xdotool** — mouse/keyboard automation
- **scrot** — screenshot capture
- **xdpyinfo** — screen info (from x11-utils)

## Install

```bash
# Clone
git clone https://github.com/itziktdk/openclaw-computer-use.git

# Check/install dependencies
bash openclaw-computer-use/scripts/setup.sh
```

No Python pip dependencies — uses only stdlib + system tools.

## Usage (CLI)

```bash
# Screenshot
bash scripts/screenshot.sh /tmp/screen.png

# Mouse
python3 scripts/mouse.py click 500 300
python3 scripts/mouse.py drag 100 100 500 500
python3 scripts/mouse.py scroll 500 300 -3

# Keyboard
python3 scripts/keyboard.py type "Hello world"
python3 scripts/keyboard.py key ctrl+c
python3 scripts/keyboard.py keys ctrl+a ctrl+c

# Screen info
bash scripts/screen-info.sh
```

## As OpenClaw Skill

Copy or symlink into your OpenClaw skills directory. The agent reads `SKILL.md` for instructions on when and how to use each script.

## License

MIT
