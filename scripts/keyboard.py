#!/usr/bin/env python3
"""Keyboard control via xdotool. Usage: keyboard.py <action> [args...]"""

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
        print("Usage: keyboard.py <type|key|keys> [args...]")
        sys.exit(1)

    action = sys.argv[1].lower()

    if action == "type":
        if len(sys.argv) < 3:
            print("Usage: keyboard.py type \"text to type\""); sys.exit(1)
        text = " ".join(sys.argv[2:])
        run(["xdotool", "type", "--delay", "12", "--clearmodifiers", text])
        print(f"OK: typed {len(text)} chars")

    elif action == "key":
        if len(sys.argv) != 3:
            print("Usage: keyboard.py key <combo> (e.g. ctrl+c, alt+Tab, Return)"); sys.exit(1)
        run(["xdotool", "key", "--clearmodifiers", sys.argv[2]])
        print(f"OK: key {sys.argv[2]}")

    elif action == "keys":
        if len(sys.argv) < 3:
            print("Usage: keyboard.py keys <combo1> <combo2> ..."); sys.exit(1)
        for combo in sys.argv[2:]:
            run(["xdotool", "key", "--clearmodifiers", combo])
        print(f"OK: keys {' '.join(sys.argv[2:])}")

    else:
        print(f"Unknown action: {action}")
        sys.exit(1)

if __name__ == "__main__":
    main()
