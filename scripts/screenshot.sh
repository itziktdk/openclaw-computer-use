#!/usr/bin/env bash
set -euo pipefail

# screenshot.sh — Take a screenshot
# Usage: screenshot.sh [output_path] [region: x,y,w,h]

OUTPUT="${1:-/tmp/screenshot.png}"
REGION="${2:-}"

if ! command -v scrot &>/dev/null; then
    if command -v import &>/dev/null; then
        # ImageMagick fallback
        if [ -n "$REGION" ]; then
            IFS=',' read -r x y w h <<< "$REGION"
            import -window root -crop "${w}x${h}+${x}+${y}" "$OUTPUT"
        else
            import -window root "$OUTPUT"
        fi
    else
        echo "ERROR: Neither scrot nor ImageMagick (import) found. Run setup.sh" >&2
        exit 1
    fi
else
    if [ -n "$REGION" ]; then
        IFS=',' read -r x y w h <<< "$REGION"
        scrot -a "${x},${y},${w},${h}" "$OUTPUT"
    else
        scrot "$OUTPUT"
    fi
fi

echo "$OUTPUT"
