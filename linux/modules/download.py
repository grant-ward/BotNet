import socket
import os 

#Script to make download from a server

def down(filename, s, host,port):
	arquivo = filename.decode("utf-8")
	if os.path.isfile(filename):
		s.send(str.encode("EXISTS" + str((os.path.getsize(filename)))))
		tamanho = os.path.getsize(filename)
		tamanho = int(tamanho)
		userResponse = s.recv(1024)
		if userResponse[:2].decode("utf-8") == 'OK':
			with open(arquivo, 'rb') as f:
				bytesToSend = f.read()
				s.send(bytesToSend)
				f.close()
	else:
		s.send(str.encode("ERROR"))

