@echo off
title Compile to EXE

echo [+] Installing dependencies...
echo.

python.exe -m pip install --upgrade pip
pip install pyinstaller
pip install pystyle

echo.
echo [+] Building EXE...
echo.

pyinstaller --onefile injector.py --icon Icon.ico --uac-admin
xcopy "SaveFile.txt" "dist\"

echo.
pause