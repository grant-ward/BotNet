#!/bin/bash

if [ -e /etc/pacman.conf ]
then
	sudo pacman -S python-pip
	sudo pacman -S python-dev
	sudo pip3 install pyscreenshot
	sudo pacman -S unzip
	sudo pip3 install cherrypy
	echo "Installing image library for Python3..."	
	wget https://pypi.python.org/packages/b4/6d/f313f1bff98f6d1e353918e0a4e8e17a22af86f0ad10c231228342edf74d/Pillow-2.2.1.zip#md5=d1d20d3db5d1ab312da0951ff061e6bf
 	unzip Pillow-2.2.1.zip
	cd Pillow-2.2.1/
	sudo python3 setup.py build
	sudo python3 setup.py install
	echo "Installing windows registry module..."
	sudo pip3 install winreglib
	clear
	echo "Installed, use script 'generate.sh', to use the botnet!"
elif [ -e /etc/apt ]
then
	sudo apt-get install -S python-pip
    sudo apt-get install-S python-dev
    sudo apt-get install unzip
    sudo pip3 install cherrypy
    sudo pip3 install pyscreenshot
    echo "Installing image library for Python3..."
    wget https://pypi.python.org/packages/b4/6d/f313f1bff98f6d1e353918e0a4e8e17a22af86f0ad10c231228342edf74d/Pillow-2.2.1.zip#md5=d1d20d3db5d1ab312da0951ff061e6bf
    unzip Pillow-2.2.1.zip
    cd Pillow-2.2.1/
    sudo python3 setup.py build
    sudo python3 setup.py install
    echo "Installing windows registry module..."
    sudo pip3 install winreglib
    clear
    echo "Installed, use script 'generate.sh', to use the botnet!"


else 
	echo "Your system is unsupported by this script"
	echo "Please install the dependencies manually"
	
fi

