import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
for i in range(5):
    GPIO.output(37,True)
    time.sleep(5)
    GPIO.output(37,False)
    GPIO.output(33,True)
    time.sleep(1)
    GPIO.output(33,False)
    GPIO.output(29,True)
    time.sleep(4)
    GPIO.output(29,False)
GPIO.cleanup
