#!/usr/bin/env python3
"""Mouse control via xdotool. Usage: mouse.py <action> [args...]"""

import subprocess
import sys

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"ERROR: {r.stderr.strip()}", file=sys.stderr)
        sys.exit(1)
    if r.stdout.strip():
        print(r.stdout.strip())

def main():
    if len(sys.argv) < 2:
        print("Usage: mouse.py <move|click|doubleclick|rightclick|drag|scroll> [args...]")
        sys.exit(1)

    action = sys.argv[1].lower()

    if action == "move":
        if len(sys.argv) != 4:
            print("Usage: mouse.py move <x> <y>"); sys.exit(1)
        run(["xdotool", "mousemove", sys.argv[2], sys.argv[3]])

    elif action == "click":
        if len(sys.argv) != 4:
            print("Usage: mouse.py click <x> <y>"); sys.exit(1)
        run(["xdotool", "mousemove", sys.argv[2], sys.argv[3]])
        run(["xdotool", "click", "1"])

    elif action == "doubleclick":
        if len(sys.argv) != 4:
            print("Usage: mouse.py doubleclick <x> <y>"); sys.exit(1)
        run(["xdotool", "mousemove", sys.argv[2], sys.argv[3]])
        run(["xdotool", "click", "--repeat", "2", "--delay", "100", "1"])

    elif action == "rightclick":
        if len(sys.argv) != 4:
            print("Usage: mouse.py rightclick <x> <y>"); sys.exit(1)
        run(["xdotool", "mousemove", sys.argv[2], sys.argv[3]])
        run(["xdotool", "click", "3"])

    elif action == "drag":
        if len(sys.argv) != 6:
            print("Usage: mouse.py drag <x1> <y1> <x2> <y2>"); sys.exit(1)
        run(["xdotool", "mousemove", sys.argv[2], sys.argv[3]])
        run(["xdotool", "mousedown", "1"])
        run(["xdotool", "mousemove", "--delay", "50", sys.argv[4], sys.argv[5]])
        run(["xdotool", "mouseup", "1"])

    elif action == "scroll":
        if len(sys.argv) != 5:
            print("Usage: mouse.py scroll <x> <y> <amount> (negative=down)"); sys.exit(1)
        run(["xdotool", "mousemove", sys.argv[2], sys.argv[3]])
        amount = int(sys.argv[4])
        button = "4" if amount > 0 else "5"  # 4=up, 5=down
        for _ in range(abs(amount)):
            run(["xdotool", "click", button])

    else:
        print(f"Unknown action: {action}")
        sys.exit(1)

    print(f"OK: {action} {' '.join(sys.argv[2:])}")

if __name__ == "__main__":
    main()
