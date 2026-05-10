#!/usr/bin/env bash
set -euo pipefail

# screen-info.sh — Get screen resolution, mouse position, active window

echo "=== Screen ==="
if command -v xdpyinfo &>/dev/null; then
    xdpyinfo | grep dimensions | head -1
else
    echo "xdpyinfo not available"
fi

echo ""
echo "=== Mouse Position ==="
if command -v xdotool &>/dev/null; then
    eval "$(xdotool getmouselocation --shell)"
    echo "X=$X Y=$Y SCREEN=$SCREEN WINDOW=$WINDOW"
else
    echo "xdotool not available"
fi

echo ""
echo "=== Active Window ==="
if command -v xdotool &>/dev/null; then
    WID=$(xdotool getactivewindow 2>/dev/null || echo "none")
    if [ "$WID" != "none" ]; then
        echo "Window ID: $WID"
        echo "Name: $(xdotool getactivewindow getwindowname 2>/dev/null || echo 'unknown')"
        echo "Geometry: $(xdotool getactivewindow getwindowgeometry 2>/dev/null || echo 'unknown')"
    else
        echo "No active window"
    fi
fi
