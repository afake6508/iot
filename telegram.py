'''
Required Components:
Raspberry Pi - 1
Power Supply 12 V/2 Amp - 1 
HDMI Port - 1
USB Keyboard - 1 
USB Mouse - 1 
Micro SD Card - 1 
LED Module - 1 
Jumper (F to F) - 2 

Connection:
Connect Pin no.3 (GPIO 2) to LED1 of LED module 
Connect Pin no.6 (GND) to GND of LED module

Step 1: Install Telegram Bot on Raspberry Pi.
•	sudo apt-get update
•	sudo apt-get upgrade
•	sudo apt-get install python-pip
•	sudo pip install telepot

Step 2: Create Telegram Bot and copy the token
'''
import time
import datetime
import RPi.GPIO as GPIO
import telepot
import sys

def on(pin):
    GPIO.output(pin, GPIO.HIGH)

def off(pin):
    GPIO.output(pin, GPIO.LOW)

def setup_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(11, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print('Got command: %s' % command)
    
    if command == '/on':
        on(11)
        bot.sendMessage(chat_id, 'LED is now ON')
    elif command == '/off':
        off(11)
        bot.sendMessage(chat_id, 'LED is now OFF')
def main():
    setup_gpio()
    bot = telepot.Bot('YOUR_BOT_TOKEN_HERE')
    bot.message_loop(handle)
    print("I am Listening....")
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print('Program interrupted')
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
