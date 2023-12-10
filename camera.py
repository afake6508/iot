'''
Required Components:
- Raspberry Pi: 1
- Power Supply 12 V/2 Amp: 1
- HDMI Port: 1
- USB Keyboard: 1
- USB Mouse: 1
- Micro SD Card: 1
- Pi Camera Module: 1

Connection:
Connect Pi Camera Module to CSI Camera Port

Commands to install Pi-camera packages:
sudo apt-get install python-picamera
sudo apt-get install python3-picamera
sudo pip install picamera
'''

import time
import picamera

camera = picamera.PiCamera()
camera.resolution = (1024, 768)

camera.start_preview()
time.sleep(2)  # Wait for 2 seconds to stabilize the camera

camera.capture('/home/pi/Desktop/visitor/images%s.jpg')

camera.stop_preview()
