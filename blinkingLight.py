import RPi.GPIO as GPIO
import time

led = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

while(True):
	GPIO.output(led, True)
	time.sleep(0.5)
	GPIO.output(led, False)
	time.sleep(0.5)
	
