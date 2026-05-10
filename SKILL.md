---
name: computer-use
description: Control a desktop computer via mouse, keyboard, and screenshots. Works on Linux (xdotool), Windows, and Mac (pyautogui). Use when the agent needs to interact with GUI applications — click buttons, type text, navigate menus, fill forms, or visually inspect what's on screen.
---

# Computer Use

Control a desktop computer programmatically: take screenshots, move/click the mouse, type text, and press key combos.

## Platform Support

| Platform | Mode | Backend | Setup |
|----------|------|---------|-------|
| **Linux (X11)** | Native | xdotool + scrot | `bash SKILL_DIR/scripts/setup.sh` |
| **Windows** | Cross-platform | pyautogui | `powershell SKILL_DIR/scripts/setup_windows.ps1` |
| **macOS** | Cross-platform | pyautogui | `pip install pyautogui Pillow` |

**Auto-detection:** Check the OS to decide which scripts to use:
- **Linux with X11:** Use the native scripts (`screenshot.sh`, `mouse.py`, `keyboard.py`) — faster and lighter
- **Windows/macOS (or Linux without X11):** Use the `*_cross.py` scripts

```bash
# Quick OS check
python3 -c "import platform; print(platform.system())"
# Returns: Linux, Windows, or Darwin
```

## Prerequisites

### Linux (Native Mode)
```bash
bash SKILL_DIR/scripts/setup.sh
```
Requires: `xdotool`, `scrot`, `python3`, `xdpyinfo`. Wayland is NOT supported.

### Windows / macOS (Cross-Platform Mode)
```bash
pip install pyautogui Pillow
```
Or on Windows: `powershell SKILL_DIR/scripts/setup_windows.ps1`

> **macOS note:** You may need to grant Accessibility permissions in System Preferences → Security & Privacy → Privacy → Accessibility.

---

## Taking Screenshots

### Linux (native)
```bash
bash SKILL_DIR/scripts/screenshot.sh [output_path] [x,y,w,h]
```

### Cross-platform (Windows/Mac/Linux)
```bash
python3 SKILL_DIR/scripts/screenshot_cross.py [output_path] [--region x,y,w,h]
```

Then use the `read` tool on the resulting PNG to see what's on screen.

## Screen Info

### Linux (native)
```bash
bash SKILL_DIR/scripts/screen-info.sh
```

### Cross-platform
```bash
python3 -c "import pyautogui; s=pyautogui.size(); p=pyautogui.position(); print(f'Screen: {s.width}x{s.height}, Mouse: {p.x},{p.y}')"
```

## Mouse Control

### Linux (native)
```bash
python3 SKILL_DIR/scripts/mouse.py <action> [args...]
```

### Cross-platform (Windows/Mac/Linux)
```bash
python3 SKILL_DIR/scripts/mouse_cross.py <action> [args...]
```

| Action | Args | Example |
|--------|------|---------|
| `move` | `x y` | `mouse_cross.py move 500 300` |
| `click` | `x y` | `mouse_cross.py click 500 300` |
| `doubleclick` | `x y` | `mouse_cross.py doubleclick 500 300` |
| `rightclick` | `x y` | `mouse_cross.py rightclick 500 300` |
| `drag` | `x1 y1 x2 y2` | `mouse_cross.py drag 100 100 500 500` |
| `scroll` | `x y amount` | `mouse_cross.py scroll 500 300 -5` (negative=down) |
| `position` | (none) | `mouse_cross.py position` — returns current mouse position |

All cross-platform scripts output JSON: `{"ok": true, "action": "click", "args": [500, 300]}`

## Keyboard Control

### Linux (native)
```bash
python3 SKILL_DIR/scripts/keyboard.py <action> [args...]
```

### Cross-platform (Windows/Mac/Linux)
```bash
python3 SKILL_DIR/scripts/keyboard_cross.py <action> [args...]
```

| Action | Args | Example |
|--------|------|---------|
| `type` | `"text"` | `keyboard_cross.py type "Hello world"` |
| `key` | `combo` | `keyboard_cross.py key ctrl+c` |
| `keys` | `k1 k2 ...` | `keyboard_cross.py keys ctrl+a ctrl+c` |

Key names: `enter`/`Return`, `tab`, `escape`, `backspace`, `delete`, `space`, `up`, `down`, `left`, `right`, `home`, `end`, `pageup`/`Page_Up`, `pagedown`/`Page_Down`, `F1`–`F12`, `ctrl`, `alt`, `shift`, `super`/`win`.

The cross-platform scripts auto-translate xdotool key names (e.g., `Return` → `enter`).

## Safety Rules

1. **Always screenshot before acting** — verify you're looking at what you expect
2. **Always screenshot after acting** — confirm the action worked
3. **Avoid destructive actions** without user confirmation
4. **Use small delays** between rapid actions — GUIs need time to respond
5. **Check active window** before typing — make sure the right window has focus

## Example Workflow

```bash
# 1. Detect platform and pick the right scripts
OS=$(python3 -c "import platform; print(platform.system())")

# 2. Screenshot
if [ "$OS" = "Linux" ]; then
    bash SKILL_DIR/scripts/screenshot.sh /tmp/screen.png
else
    python3 SKILL_DIR/scripts/screenshot_cross.py /tmp/screen.png
fi

# 3. Click somewhere
if [ "$OS" = "Linux" ]; then
    python3 SKILL_DIR/scripts/mouse.py click 500 300
else
    python3 SKILL_DIR/scripts/mouse_cross.py click 500 300
fi

# 4. Type text
if [ "$OS" = "Linux" ]; then
    python3 SKILL_DIR/scripts/keyboard.py type "Hello"
else
    python3 SKILL_DIR/scripts/keyboard_cross.py type "Hello"
fi
```
