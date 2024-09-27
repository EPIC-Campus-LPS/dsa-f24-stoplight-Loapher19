import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
# Would Use GPIO.setup(40,GPIO.OUT) But We Don't Need Blue Where We're Going
GPIO.setup(36,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)
GPIO.output(32,False)
GPIO.output(36,False)
for i in range(5):
    GPIO.output(36,True)
    time.sleep(5)
    GPIO.output(32,True)
    time.sleep(1)
    GPIO.output(36,False)
    time.sleep(4)
    GPIO.output(32,False)
GPIO.cleanup
