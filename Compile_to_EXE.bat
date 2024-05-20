@echo off
title Compile to EXE

echo [+] Installing dependencies...
echo.

pip install pyinstaller
pip install pystyle

echo.
echo [+] Building EXE...
echo.

pyinstaller --onefile injector.py --icon Icon.ico --uac-admin

echo.
pause