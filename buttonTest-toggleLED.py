#Name:  Button Test
#Written by:  Mike Kwiatkowski
#Date:  Feb 25, 2020
#
import RPi.GPIO as GPIO  #sets up library to access the GPIO pins
import time  #imports the time library
GPIO.setmode(GPIO.BCM)  #sets the GPIO pins mapping to match the Broadcom mapping

redLed = 21
buttonPin = 12


#the line below sets up buttonPin as INPUT and uses the internal
#pull up resistor to avoid shorting out the pin
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def setPin(pin, state):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, state)
    

def readPin(pin):
    GPIO.setup(pin, GPIO.IN)
    value = GPIO.input(pin)
    return value

def toggle(pin):
    pinState = readPin(pin)
    setPin(pin, not(pinState))


setPin(redLed, False)
while True:
    inputState = GPIO.input(buttonPin)
    if inputState == False:
        print("Button pressed!!")
        toggle(redLed)
        time.sleep(.2)
        
 
#the following line clears out all the settings on the GPIO pins 
GPIO.cleanup()




