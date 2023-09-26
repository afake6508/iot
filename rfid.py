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
