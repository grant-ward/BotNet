echo off
cls
echo "This script will generate a .exe file using Pyinstaller"
pause
py -m PyInstaller --noconsole --onefile --icon=icon.ico agent.py 

echo "The .exe file is in dist\agent.exe" 
pause