#!/usr/bin/env python2.7  
# script by Alex Eames https://raspi.tv/  
# https://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio  
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

pins = {'button1' : 19, 'led1' : 26, 'button2':5}  #dictionary containing pin definitions
states = {'led1' : False}
  
# GPIO 23 set up as input. It is pulled up to stop false signals  
#GPIO.setup(pins['button2'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pins['button1'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
pressedCount = 0

def my_callback(channel):
    global pressedCount
    global states
    states['led1'] = not(states['led1'])
    pressedCount += 1
    print("Rising Edge detected")
    print("test successful")
    print('-'* pressedCount)
GPIO.add_event_detect(pins['button1'], GPIO.FALLING, callback=my_callback, bouncetime=300)

def setPin(pin, state):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, state)

while True:
    if states['led1']:
        setPin(pins['led1'], True)
        time.sleep(.2)
        setPin(pins['led1'], False)
        time.sleep(.2)

GPIO.cleanup()           # clean up GPIO on normal exit  