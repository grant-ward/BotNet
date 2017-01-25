#!/bin/bash

if [ -e /etc/pacman.conf ]
then
	sudo pacman -Syy
	sudo pacman -S python3-pip
	sudo pacman -S python-dev
	sudo pip3 install pyscreenshot
	sudo pacman -S unzip
	sudo pip3 install cherrypy
	wget https://pypi.python.org/packages/b4/6d/f313f1bff98f6d1e353918e0a4e8e17a22af86f0ad10c231228342edf74d/Pillow-2.2.1.zip#md5=d1d20d3db5d1ab312da0951ff061e6bf
 	unzip Pillow-2.2.1.zip
	cd Pillow-2.2.1/
	sudo python3 setup.py build
	sudo python3 setup.py install
	sudo pip3 install winreglib
	sudo pip3 install requests
	clear
	echo "Installed, use script 'generate.py', to use the botnet!"
elif [ -e /etc/apt ]
then
	sudo apt-get update
	sudo apt-get install python3-pip
    	sudo apt-get install python-dev
    	sudo apt-get install unzip
    	sudo pip3 install cherrypy
    	sudo pip3 install pyscreenshot
    	wget https://pypi.python.org/packages/b4/6d/f313f1bff98f6d1e353918e0a4e8e17a22af86f0ad10c231228342edf74d/Pillow-2.2.1.zip#md5=d1d20d3db5d1ab312da0951ff061e6bf
    	unzip Pillow-2.2.1.zip
    	cd Pillow-2.2.1/
    	sudo python3 setup.py build
    	sudo python3 setup.py install
    	sudo pip3 install winreglib
	sudo pip3 install requests
    	echo "Installed, use script 'generate.py', to use the botnet!"


else 
	echo "Your system is unsupported by this script"
	echo "Please install the dependencies manually"
	echo "They are: Cherrypy, pyscreenshot, winreglib, requests"
	
fi

