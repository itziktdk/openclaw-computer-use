#!/usr/bin/env bash
set -euo pipefail

# setup.sh — Check and install dependencies for computer-use skill

echo "=== Computer Use Skill — Dependency Check ==="

MISSING=()

for cmd in xdotool scrot xdpyinfo python3; do
    if command -v "$cmd" &>/dev/null; then
        echo "✅ $cmd"
    else
        echo "❌ $cmd — MISSING"
        MISSING+=("$cmd")
    fi
done

# Check DISPLAY
if [ -z "${DISPLAY:-}" ]; then
    echo ""
    echo "⚠️  WARNING: \$DISPLAY is not set. X11 may not be available."
    echo "   Set it with: export DISPLAY=:0"
fi

if [ ${#MISSING[@]} -eq 0 ]; then
    echo ""
    echo "All dependencies installed! ✅"
    exit 0
fi

echo ""
echo "Missing: ${MISSING[*]}"
echo ""

# Map commands to packages
declare -A PKG_MAP=(
    [xdotool]=xdotool
    [scrot]=scrot
    [xdpyinfo]=x11-utils
    [python3]=python3
)

PKGS=()
for cmd in "${MISSING[@]}"; do
    PKGS+=("${PKG_MAP[$cmd]:-$cmd}")
done

if command -v apt-get &>/dev/null; then
    echo "Installing with apt: ${PKGS[*]}"
    sudo apt-get update -qq && sudo apt-get install -y -qq "${PKGS[@]}"
elif command -v dnf &>/dev/null; then
    echo "Installing with dnf: ${PKGS[*]}"
    sudo dnf install -y "${PKGS[@]}"
elif command -v pacman &>/dev/null; then
    echo "Installing with pacman: ${PKGS[*]}"
    sudo pacman -S --noconfirm "${PKGS[@]}"
else
    echo "Could not detect package manager. Please install manually: ${MISSING[*]}"
    exit 1
fi

echo ""
echo "Done! ✅"
