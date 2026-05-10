# computer-use — OpenClaw Skill

AI-powered desktop control via mouse, keyboard, and screenshots. Lets an OpenClaw agent interact with GUI applications on **Linux, Windows, and macOS**.

## Features

- 📸 **Screenshots** — full screen or region capture
- 🖱️ **Mouse** — move, click, double-click, right-click, drag, scroll
- ⌨️ **Keyboard** — type text, press key combos (Ctrl+C, Alt+Tab, etc.)
- 🖥️ **Screen info** — resolution, mouse position, active window
- 🪟 **Cross-platform** — native xdotool on Linux, pyautogui on Windows/Mac

## Platform Support

| Platform | Backend | Scripts |
|----------|---------|---------|
| Linux (X11) | xdotool + scrot | `mouse.py`, `keyboard.py`, `screenshot.sh` |
| Windows | pyautogui | `mouse_cross.py`, `keyboard_cross.py`, `screenshot_cross.py` |
| macOS | pyautogui | `mouse_cross.py`, `keyboard_cross.py`, `screenshot_cross.py` |

## Install

### Linux
```bash
git clone https://github.com/itziktdk/openclaw-computer-use.git
bash openclaw-computer-use/scripts/setup.sh
```

### Windows
```powershell
git clone https://github.com/itziktdk/openclaw-computer-use.git
cd openclaw-computer-use
powershell scripts/setup_windows.ps1
```

### macOS
```bash
git clone https://github.com/itziktdk/openclaw-computer-use.git
cd openclaw-computer-use
pip install -r requirements.txt
```

> **macOS:** Grant Accessibility permissions in System Preferences → Security & Privacy → Privacy → Accessibility.

## Usage (CLI)

### Linux (native — faster)
```bash
bash scripts/screenshot.sh /tmp/screen.png
python3 scripts/mouse.py click 500 300
python3 scripts/keyboard.py type "Hello world"
bash scripts/screen-info.sh
```

### Cross-platform (Windows/Mac/Linux)
```bash
python3 scripts/screenshot_cross.py /tmp/screen.png
python3 scripts/screenshot_cross.py /tmp/region.png --region 100,200,800,600
python3 scripts/mouse_cross.py click 500 300
python3 scripts/mouse_cross.py drag 100 100 500 500
python3 scripts/mouse_cross.py scroll 500 300 -3
python3 scripts/mouse_cross.py position
python3 scripts/keyboard_cross.py type "Hello world"
python3 scripts/keyboard_cross.py key ctrl+c
python3 scripts/keyboard_cross.py keys ctrl+a ctrl+c
```

Cross-platform scripts output JSON for easy parsing.

## As OpenClaw Skill

Copy or symlink into your OpenClaw skills directory. The agent reads `SKILL.md` for instructions on when and how to use each script, with auto-detection for the right platform.

## License

MIT
