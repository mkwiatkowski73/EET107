#Name:  Fading LED testy
#Written by:  Mike Kwiatkowski
#Date:  Feb 19, 2020
#

import RPi.GPIO as GPIO  #sets up library to access the GPIO pins
import time  #imports the time library

GPIO.setmode(GPIO.BCM)  #sets the GPIO pins mapping to match the Broadcom mapping

ledRed = 21

GPIO.setup(ledRed, GPIO.OUT) #set LED pin to ouput
pwmRed = GPIO.PWM(ledRed, 250)  #creates a PWM object with a cycle frequency of 250Hz
pwmRed.start(100)  #initiates the PWM cycle and sets it to 100% duty cycle


duty = int(input("Set LED brightness (0 to 100):"))
pwmRed.ChangeDutyCycle(duty)
 
#the following line clears out all the settings on the GPIO pins 
#GPIO.cleanup()




