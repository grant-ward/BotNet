echo off
cls
echo "This script will be use to install all the dependencies for use the botnet in windows!"
pause
echo "installing dependencies with pip!"
py -m pip install requests
py -m pip install cherrypy
py -m pip install winreglib
py -m pip install pyinstaller
py -m pip install pillow
py -m pip install pypiwin32
echo "Dependencies installed!"
pause
