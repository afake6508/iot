'''
Required Components:
1. Raspberry Pi - 1
2. Power Supply 12 V/2 Amp - 1
3. HDMI Port - 1
4. USB Keyboard - 1
5. USB Mouse - 1
6. Micro SD Card - 1
7. LED Module - 1
8. Jumper Wires (Female to Female) - 5

Connection:
- Connect Pin no. 7 (GPIO 4) to LED1 of the LED module
- Connect Pin no. 11 (GPIO 17) to LED2 of the LED module
- Connect Pin no. 13 (GPIO 27) to LED3 of the LED module
- Connect Pin no. 15 (GPIO 22) to LED4 of the LED module
- Connect Pin no. 6 (GND) to GND of the LED module
'''

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
LED1_PIN = 7
LED2_PIN = 11
LED3_PIN = 13
LED4_PIN = 15


GPIO.setup(LED1_PIN, GPIO.OUT)
GPIO.setup(LED2_PIN, GPIO.OUT)
GPIO.setup(LED3_PIN, GPIO.OUT)
GPIO.setup(LED4_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED1_PIN, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(LED2_PIN, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(LED3_PIN, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(LED4_PIN, GPIO.LOW)
        time.sleep(0.2)

        print("LEDs are ON!")

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
