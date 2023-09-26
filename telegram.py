import time
import datetime
import RPi.GPIO as GPIO
import telepot
import sys
def on(pin):
 GPIO.output(pin, GPIO.HIGH)
def off(pin):
 GPIO.output(pin, GPIO.LOW)
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
bot = telepot.Bot('YOUR_BOT_TOKEN_HERE')
bot.message_loop(handle)
print("I am Listening....")
try:
 while 1:
 time.sleep(10)
except KeyboardInterrupt:
 print('Program interrupted')
 GPIO.cleanup()
except Exception as e:
 print("An error occurred:", str(e))
 GPIO.cleanup()
