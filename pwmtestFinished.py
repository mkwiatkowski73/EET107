#Name:  Fading LED testy
#Written by:  Mike Kwiatkowski
#Date:  Feb 19, 2020
#

import RPi.GPIO as GPIO  #sets up library to access the GPIO pins
import time  #imports the time library

GPIO.setmode(GPIO.BCM)  #sets the GPIO pins mapping to match the Broadcom mapping

ledRed = 21

GPIO.setup(ledRed, GPIO.OUT) #set LED pin to ouput
pwmRed = GPIO.PWM(ledRed, 250)  #creates a PWM object with a cycle frequency of 500Hz
pwmRed.start(100)

done = False

while not done:
    duty = int(input("Set LED brightness (0 to 100, -1 to quit):"))
    if duty < 0:
        done = True
    elif duty >= 0 and duty <= 100:
        pwmRed.ChangeDutyCycle(duty)
    else:
        print("You must enter a value between 0 and 100 or -1 to finish")
    
GPIO.cleanup()




