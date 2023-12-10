'''
Required Components:
Raspberry Pi - 1
Power Supply 12 V/2 Amp - 1
Power Supply with Red & Black extension - 1 
HDMI Port - 1
USB Keyboard - 1 
USBMouse - 1 
Micro SD Card - 1 
Ethernet - 1
RFID Card Reader - 1 
USB to TTL Converter - 1 
Jumper (F to F) - 4 

Note - If (/dev/ttyUSB0) error occurs run the following commands in the Terminal:
•	sudo apt-get update
•	sudo apt-get upgrade
•	sudo raspi-config (in ‘Interface’ option ‘enable spi’)
•	sudo reboot (compulsory)
•	sudo apt-get install python3-dev python3-pip
•	sudo pip3 install spidev

Connection:
Connect TX of Card Reader to RX of TTL 
Connect GND of Card Reader to GND of TTL
Connect Red of Power Supply to VCC of Card Reader 
Connect Black of Power Supply to GND of Card Reader 
Connect TTL to Raspberry Pi
'''

import RPi.GPIO as GP
import time
import serial

GP.setmode(GP.BOARD)

def read_rfid():
    ser = serial.Serial("/dev/ttyUSB0")
    ser.baudrate = 9600
    data = ser.read(12)
    ser.close()
    return data

try:
    while True:
        id = read_rfid()
        print(id)
        
        if id == b'1C0034C824C4':
            print("Access Granted")
            time.sleep(2)
        else:
            print("Access Denied")
            time.sleep(2)

finally:
    GP.cleanup()
