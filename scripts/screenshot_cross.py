#!/usr/bin/env python3
"""Cross-platform screenshot using pyautogui. Works on Windows, Mac, and Linux."""

import argparse
import json
import sys

def main():
    parser = argparse.ArgumentParser(description="Take a screenshot using pyautogui")
    parser.add_argument("output", nargs="?", default="/tmp/screenshot.png", help="Output file path")
    parser.add_argument("--region", type=str, help="Region as x,y,width,height")
    args = parser.parse_args()

    try:
        import pyautogui
    except ImportError:
        print(json.dumps({"error": "pyautogui not installed. Run: pip install pyautogui Pillow"}))
        sys.exit(1)

    try:
        region = None
        if args.region:
            parts = [int(x) for x in args.region.split(",")]
            if len(parts) != 4:
                print(json.dumps({"error": "Region must be x,y,width,height"}))
                sys.exit(1)
            region = tuple(parts)

        screenshot = pyautogui.screenshot(region=region)
        screenshot.save(args.output)
        print(json.dumps({"ok": True, "path": args.output, "size": list(screenshot.size)}))
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
