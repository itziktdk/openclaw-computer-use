#!/usr/bin/env python3
"""Cross-platform keyboard control using pyautogui. Works on Windows, Mac, and Linux."""

import argparse
import json
import sys

# Map xdotool key names to pyautogui key names
KEY_MAP = {
    "return": "enter", "Return": "enter",
    "BackSpace": "backspace", "backspace": "backspace",
    "Escape": "escape", "escape": "escape",
    "Delete": "delete", "Tab": "tab",
    "space": "space", "Space": "space",
    "Up": "up", "Down": "down", "Left": "left", "Right": "right",
    "Home": "home", "End": "end",
    "Page_Up": "pageup", "Page_Down": "pagedown",
    "super": "win", "Super_L": "win", "Super_R": "win",
    "ctrl": "ctrl", "alt": "alt", "shift": "shift",
}

def translate_key(k):
    return KEY_MAP.get(k, k.lower())

def parse_combo(combo):
    """Parse 'ctrl+c' into ['ctrl', 'c']"""
    return [translate_key(k) for k in combo.split("+")]

def main():
    parser = argparse.ArgumentParser(description="Keyboard control via pyautogui")
    parser.add_argument("action", choices=["type", "key", "keys"])
    parser.add_argument("args", nargs="*", help="Text or key combos")
    args = parser.parse_args()

    try:
        import pyautogui
        pyautogui.FAILSAFE = True
    except ImportError:
        print(json.dumps({"error": "pyautogui not installed. Run: pip install pyautogui Pillow"}))
        sys.exit(1)

    try:
        if args.action == "type":
            text = " ".join(args.args)
            pyautogui.write(text, interval=0.02)
            print(json.dumps({"ok": True, "action": "type", "chars": len(text)}))

        elif args.action == "key":
            if len(args.args) != 1:
                print(json.dumps({"error": "Usage: key <combo> e.g. ctrl+c"}))
                sys.exit(1)
            keys = parse_combo(args.args[0])
            pyautogui.hotkey(*keys)
            print(json.dumps({"ok": True, "action": "key", "combo": args.args[0]}))

        elif args.action == "keys":
            for combo in args.args:
                keys = parse_combo(combo)
                pyautogui.hotkey(*keys)
            print(json.dumps({"ok": True, "action": "keys", "combos": args.args}))

    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
