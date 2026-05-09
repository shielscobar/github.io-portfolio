# ENF Crack Diagnostics – Interactive Inspector

A Matplotlib-based tool for visualising and probing Von-Mises (VM) strain fields
computed from DIC (Digital Image Correlation) on ENF fracture specimens.

---

## Quick Start

### 1 — Prerequisites

| Requirement | Minimum version | How to get it |
|---|---|---|
| Python | 3.10 | https://python.org |
| pip | bundled with Python | — |
| Tk (GUI backend) | bundled on Windows/Linux | macOS: `brew install python-tk` |

### 2 — First-time setup

```
# Windows
run_windows.bat          ← double-click or run in terminal

# macOS / Linux
bash run_unix.sh
```

Both launchers automatically install all Python packages from `requirements.txt`
and then start the tool. You only need internet access the first time.

### 3 — Manual setup (optional)

```bash
pip install -r requirements.txt
python plot_diagnostics.py          # Windows
python3 plot_diagnostics.py         # macOS / Linux
```

---


## Usage

### Batch selector (terminal)

On launch the terminal shows a numbered list of frame batches:

```
====================================================
  ENF DIAGNOSTICS – BATCH SELECTOR
====================================================
  [ 0]  Frames: [1, 2, 3, 4]
  [ 1]  Frames: [5, 6, 7, 8]
  ...
  [ Q]  Quit
```

Type a batch number and press Enter to open the inspector window.

### Inspector window controls

| Control | What it does |
|---|---|
| **Strain threshold slider / textbox** | Highlights (red dots) all pixels where VM strain ≥ value |
| **Abs-diff probe gap slider / textbox** | Finds the pixel pair separated by Δx mm with the largest \|ΔVM\| jump; marks them in cyan/yellow |
| **Cmap Min / Cmap Max sliders** | Adjusts the colour scale live across all subplots |
| **CLEAR ALL button** | Removes all markers and resets the result text |
| **C key** | Same as CLEAR ALL |
| **Hover** | Status bar (bottom-left) shows X, Y coordinates and VM strain at cursor |

### Reading the result

The bottom-right status bar prints:

```
MAX |ΔVM|: 4.217%  ·  X = 12.30 → 18.30 mm  ·  Y = 2.14 mm  ·  Frame 7
```

This means the largest absolute VM strain jump across the probe gap was found at
Y = 2.14 mm from the midline, between X = 12.30 and X = 18.30 mm, in Frame 7.

---

## File layout

```
enf_diagnostics/
├── config.py              ← EDIT THIS for your paths and settings
├── plot_diagnostics.py    ← main script (do not edit)
├── requirements.txt       ← Python dependencies
├── run_windows.bat        ← Windows one-click launcher
├── run_unix.sh            ← macOS / Linux launcher
└── README.md              ← this file
```

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `No .tif/.tiff files found` | Check `IMAGE_DIR` in `config.py` |
| Blank / black figure | Adjust `Cmap Min` and `Cmap Max` sliders |
| Window does not appear (macOS) | Install `python-tk`: `brew install python-tk@3.xx` |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` again |
| Slow first batch | DIC computation is cached; subsequent batches are instant |

---

*Developed for ENF fracture analysis · Python 3.10+ · matplotlib · scikit-image*
