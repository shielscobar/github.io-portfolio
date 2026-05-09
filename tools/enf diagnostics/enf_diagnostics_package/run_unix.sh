#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────
#  ENF Diagnostics – macOS / Linux launcher
#  Run with:  bash run_unix.sh
# ─────────────────────────────────────────────────────────────

set -e
cd "$(dirname "$0")"

echo
echo "  Checking Python..."
if ! command -v python3 &>/dev/null; then
    echo "  ERROR: python3 not found."
    echo "  Install it via your package manager or https://python.org"
    exit 1
fi
python3 --version

# On macOS matplotlib needs a non-framework Python for TkAgg.
# If TkAgg is unavailable the script falls back automatically.
echo "  Installing / verifying dependencies..."
python3 -m pip install --quiet -r requirements.txt

echo "  Launching ENF Diagnostics..."
echo
python3 plot_diagnostics.py
