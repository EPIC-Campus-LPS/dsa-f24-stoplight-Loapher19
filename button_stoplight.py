import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
# Light Pins
GPIO.setup(36,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
GPIO.output(36,False)
GPIO.output(40,False)
# Button Pin
GPIO.setup(32,GPIO.IN)
# Thingias
while True:
    if GPIO.input(32):
        GPIO.output(40,True)
        time.sleep(5)
        GPIO.output(36,True) 
        time.sleep(1)
        GPIO.output(40,False)
        time.sleep(4)
        GPIO.output(36,False)
GPIO.cleanup
