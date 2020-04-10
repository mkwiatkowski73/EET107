#Name:  Toggle LEDs
#Written by:  Mike Kwiatkowski
#Date:  Feb 4, 2020
#The purpose of this project is to using keyboard input to toggle
#LEDs connected to the GPIO pins of the Raspberry Pi

import RPi.GPIO as GPIO  #sets up library to access the GPIO pins
import time  #imports the time library

GPIO.setmode(GPIO.BCM)  #sets the GPIO pins mapping to match the Broadcom mapping

ledRed = 21
GPIO.setup(ledRed, GPIO.IN)  #sets LED pin to input
redState = GPIO.input(ledRed) #checks current state of LED
GPIO.setup(ledRed, GPIO.OUT) #set LED pin to ouput


lightString = input("What light do you want to toggle?")

if lightString == 'r':
    redState = not(redState)
    GPIO.output(ledRed, redState)



