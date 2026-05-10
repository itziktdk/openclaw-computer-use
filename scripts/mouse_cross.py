#!/usr/bin/env python3
"""Cross-platform mouse control using pyautogui. Works on Windows, Mac, and Linux."""

import argparse
import json
import sys

def main():
    parser = argparse.ArgumentParser(description="Mouse control via pyautogui")
    parser.add_argument("action", choices=["move", "click", "doubleclick", "rightclick", "drag", "scroll", "position"])
    parser.add_argument("args", nargs="*", type=int, help="Coordinates and parameters")
    args = parser.parse_args()

    try:
        import pyautogui
        pyautogui.FAILSAFE = True
    except ImportError:
        print(json.dumps({"error": "pyautogui not installed. Run: pip install pyautogui Pillow"}))
        sys.exit(1)

    try:
        a = args.action
        p = args.args

        if a == "position":
            pos = pyautogui.position()
            print(json.dumps({"ok": True, "x": pos.x, "y": pos.y}))
            return

        if a == "move":
            if len(p) != 2: _die("Usage: move x y")
            pyautogui.moveTo(p[0], p[1])

        elif a == "click":
            if len(p) != 2: _die("Usage: click x y")
            pyautogui.click(p[0], p[1])

        elif a == "doubleclick":
            if len(p) != 2: _die("Usage: doubleclick x y")
            pyautogui.doubleClick(p[0], p[1])

        elif a == "rightclick":
            if len(p) != 2: _die("Usage: rightclick x y")
            pyautogui.rightClick(p[0], p[1])

        elif a == "drag":
            if len(p) != 4: _die("Usage: drag x1 y1 x2 y2")
            pyautogui.moveTo(p[0], p[1])
            pyautogui.drag(p[2] - p[0], p[3] - p[1], duration=0.5)

        elif a == "scroll":
            if len(p) != 3: _die("Usage: scroll x y amount (negative=down)")
            pyautogui.moveTo(p[0], p[1])
            pyautogui.scroll(p[2])

        print(json.dumps({"ok": True, "action": a, "args": p}))

    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

def _die(msg):
    print(json.dumps({"error": msg}))
    sys.exit(1)

if __name__ == "__main__":
    main()
