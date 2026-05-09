@echo off
REM ─────────────────────────────────────────────────────────────
REM  ENF Diagnostics – Windows launcher
REM  Double-click this file OR run it from a terminal.
REM ─────────────────────────────────────────────────────────────

cd /d "%~dp0"

echo.
echo  Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo  ERROR: Python not found. Install it from https://python.org
    pause
    exit /b 1
)

echo  Installing / verifying dependencies...
python -m pip install --quiet -r requirements.txt
if errorlevel 1 (
    echo  ERROR: pip install failed. Check your internet connection.
    pause
    exit /b 1
)

echo  Launching ENF Diagnostics...
echo.
python plot_diagnostics.py
pause
