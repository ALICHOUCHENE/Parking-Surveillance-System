### System Overview

This intelligent parking system based on image processing and implimented using a raspberry pi4 incorporates three main functionalities:
- Motion detection in the parking for security reasons.
- Licence plate recognition using pytesseract and loading it in a data base.
- the system generates a QR code for every vehicule owner for more secure access management.

## SETUP :

# Updating OS system :

sudo apt-get update

sudo apt-get upgrade

# Installing dependencies :

sudo apt-get install build-essential cmake pkg-config

sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev

sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev

sudo apt-get install libxvidcore-dev libx264-dev

sudo apt-get install libgtk2.0-dev libgtk-3-dev

sudo apt-get install libatlas-base-dev gfortran

# Installing Python 3 and Pip3:

sudo apt-get install python3-dev

sudo apt-get install python3-pip

# Installing Opencv package:

pip3 install opencv-python

# Extra depencies for Opencv and the Camera:

sudo apt-get install libqtgui4

sudo modprobe bcm2835-v4l2

# Installing Pyzbar module : 

- Installing the required dependencies :

sudo apt-get install libhdf5-dev -y 

sudo apt-get install libhdf5-serial-dev –y 

sudo apt-get install libatlas-base-dev –y 

sudo apt-get install libjasper-dev -y 

sudo apt-get install libqtgui4 –y

sudo apt-get install libqt4-test –y

- Installing Zbar package : 

pip3 install pyzbar

- Install imutils 

pip3 install imutils
























