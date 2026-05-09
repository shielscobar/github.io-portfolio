"""
config.py
=========
Edit the paths and parameters in this file to match YOUR machine.
Do NOT edit plot_diagnostics.py itself.
"""

from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────────────
# Get the folder where this config.py file is actually located
BASE_DIR = Path(__file__).parent

# Look for images inside the 'data/images' subfolder
IMAGE_DIR = BASE_DIR / "data" / "images"

# Create/use an 'outputs' subfolder in the project directory
OUTPUT_DIR = BASE_DIR / "outputs" / "diagnostics"

# ── Specimen geometry ──────────────────────────────────────────────────────
PIXEL_SIZE_MM = 0.0444        # physical size of one pixel in millimetres
MIDLINE_ROW   = 1070          # image row that corresponds to the crack midline

# Region-of-interest crop (pixels)
SPECIMEN_ROI_Y = (671,  1163)   # (top_row, bottom_row)
SPECIMEN_ROI_X = (15,   2432)   # (left_col, right_col)

# ── DIC / optical-flow settings ───────────────────────────────────────────
ILK_RADIUS = 15   # ILK window radius (pixels)
ILK_WARPS  = 5    # number of warp iterations

DS_DISP = 12      # displacement Gaussian-smoothing sigma
SS_DISP = 10      # strain Gaussian-smoothing sigma

# ── Search window (Y, relative to midline in mm) ──────────────────────────
Y_SEARCH_MIN = 0.0
Y_SEARCH_MAX = 10.0

# ── Initial colour-map range for VM strain display (%) ────────────────────
VMIN_DEFAULT = 0.0
VMAX_DEFAULT = 15.0

# ── Batch size (frames per inspector window) ──────────────────────────────
BATCH_SIZE = 4
