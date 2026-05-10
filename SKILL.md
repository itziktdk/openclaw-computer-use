---
name: computer-use
description: Control a desktop computer via mouse, keyboard, and screenshots. Use when the agent needs to interact with GUI applications — click buttons, type text, navigate menus, fill forms, or visually inspect what's on screen. Requires Linux with X11, xdotool, and scrot.
---

# Computer Use

Control a desktop computer programmatically: take screenshots, move/click the mouse, type text, and press key combos.

## Prerequisites

Linux with X11 (Xorg). Install dependencies:

```bash
bash SKILL_DIR/scripts/setup.sh
```

Requires: `xdotool`, `scrot`, `python3`, `xdpyinfo`. The setup script checks and installs missing ones.

> **Wayland note:** xdotool does not work under Wayland. Use X11/Xorg sessions only.

## Taking Screenshots

```bash
# Full screen → saves to /tmp/screenshot.png
bash SKILL_DIR/scripts/screenshot.sh

# Custom output path
bash SKILL_DIR/scripts/screenshot.sh /tmp/my-screenshot.png

# Region (x,y,width,height)
bash SKILL_DIR/scripts/screenshot.sh /tmp/region.png 100,200,800,600
```

Then use the `read` tool on the resulting PNG to see what's on screen.

## Screen Info

```bash
bash SKILL_DIR/scripts/screen-info.sh
```

Returns screen resolution, mouse position, and active window info.

## Mouse Control

```bash
python3 SKILL_DIR/scripts/mouse.py <action> [args...]
```

| Action | Args | Example |
|--------|------|---------|
| `move` | `x y` | `mouse.py move 500 300` |
| `click` | `x y` | `mouse.py click 500 300` |
| `doubleclick` | `x y` | `mouse.py doubleclick 500 300` |
| `rightclick` | `x y` | `mouse.py rightclick 500 300` |
| `drag` | `x1 y1 x2 y2` | `mouse.py drag 100 100 500 500` |
| `scroll` | `x y amount` | `mouse.py scroll 500 300 -5` (negative=down) |

## Keyboard Control

```bash
python3 SKILL_DIR/scripts/keyboard.py <action> [args...]
```

| Action | Args | Example |
|--------|------|---------|
| `type` | `"text"` | `keyboard.py type "Hello world"` |
| `key` | `combo` | `keyboard.py key ctrl+c` |
| `key` | `combo` | `keyboard.py key alt+Tab` |
| `key` | `combo` | `keyboard.py key Return` |
| `keys` | `k1 k2 ...` | `keyboard.py keys ctrl+a ctrl+c` |

Key names follow xdotool conventions: `Return`, `Tab`, `Escape`, `BackSpace`, `Delete`, `space`, `Up`, `Down`, `Left`, `Right`, `Home`, `End`, `Page_Up`, `Page_Down`, `F1`–`F12`, `ctrl`, `alt`, `shift`, `super`.

## Safety Rules

1. **Always screenshot before acting** — verify you're looking at what you expect
2. **Always screenshot after acting** — confirm the action worked
3. **Avoid destructive actions** without user confirmation (closing unsaved work, deleting files)
4. **Use small delays** between rapid actions — GUIs need time to respond
5. **Check active window** before typing — make sure the right window has focus

## Example Workflow: Open Browser and Navigate

```bash
# 1. Check current screen
bash SKILL_DIR/scripts/screenshot.sh /tmp/before.png
# (read the screenshot to see current state)

# 2. Open browser
python3 SKILL_DIR/scripts/keyboard.py key super
sleep 1
bash SKILL_DIR/scripts/screenshot.sh /tmp/launcher.png
python3 SKILL_DIR/scripts/keyboard.py type "firefox"
sleep 1
python3 SKILL_DIR/scripts/keyboard.py key Return
sleep 3

# 3. Navigate to URL
bash SKILL_DIR/scripts/screenshot.sh /tmp/browser.png
python3 SKILL_DIR/scripts/keyboard.py key ctrl+l
sleep 0.5
python3 SKILL_DIR/scripts/keyboard.py type "https://example.com"
python3 SKILL_DIR/scripts/keyboard.py key Return
sleep 3

# 4. Verify
bash SKILL_DIR/scripts/screenshot.sh /tmp/result.png
```
