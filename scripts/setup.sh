#!/bin/bash

cp src/startup.py ~/

# Read Arguments
i=$(($#-1))
while [ $i -ge 0 ];
do
	if [ ${BASH_ARGV[$i]} = 'server' ]
	then
		# Set Up Server

        cp src/performance-server.py ~/
        echo "os.system("python3 ~/performance-server.py")\n" >> ~/startup.py
    
        # Copy Libraries
        cp examples/bluetooth/bt.py ~

        cp examples/motor/stepper.py ~
        cp examples/motor/alphabot.py ~
    elif [ ${BASH_ARGV[$i]} = 'client' ]
	then
		# Set Up Client
        cp src/performance-client.py ~/
        echo "os.system("python3 ~/performance-client.py")\n" >> ~/startup.py

        # Copy Libraries
        cp examples/bluetooth/bt.py ~

        cp examples/motor/stepper.py ~
        cp examples/motor/alphabot.py ~
    elif [ ${BASH_ARGV[$i]} = 'install' ]
	then
        # Install Libraries

        # Install/Update Pip
        sudo apt install python3-pip -y
        pip3 install --upgrade pip

        # Install OpenCV
        sudo pip3 install opencv-contrib-python==4.4.0.46

        # Install Bluetooth Library
        sudo apt install bluetooth bluez libbluetooth-dev -y
        sudo python3 -m pip install pybluez

        # Install Pip
        sudo apt install -y python3-pip
        pip3 install --upgrade pip
        ```

        # Install OpenCV Dependencies
        sudo apt install -y libhdf5-dev libharfbuzz-dev libavcodec-dev libavformat-dev libswscale-dev libopenexr-dev libatlas-base-dev

        # Install OpenCV
        sudo pip3 install opencv-contrib-python-headless==4.4.0.46

        # Install/Update NumPy
        sudo pip3 install numpy
        pip install -U numpy
        ```

        # Install Bluetooth Library
        sudo apt install -y bluetooth bluez libbluetooth-dev
        sudo python3 -m pip install pybluez
	elif [ ${BASH_ARGV[$i]} = 'help' ]
	then
		echo "RCJ Code Setup"
		echo "install   -   Install dependencies"
		echo "server    -   Set Up as Server"
		echo "client    -   Set Up as Client"
		exit 0
	else
		echo "Invalid Argument: '${BASH_ARGV[$i]}'"
	fi

    i=$((i-1))
done