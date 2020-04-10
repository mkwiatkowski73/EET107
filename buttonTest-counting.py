#Name:  Button Test
#Written by:  Mike Kwiatkowski
#Date:  Feb 25, 2020
#

import RPi.GPIO as GPIO  #sets up library to access the GPIO pins
import time  #imports the time library

GPIO.setmode(GPIO.BCM)  #sets the GPIO pins mapping to match the Broadcom mapping

ledRed = 21
buttonPin = 12

#the line below sets up buttonPin as INPUT and uses the internal
#pull up resistor to avoid shorting out the pin
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
def main():
    buttonPresses = 0
    try:
        while True:
            inputState = GPIO.input(buttonPin)
            if inputState == False:
                print("Button pressed!! <Ctrl>C to exit")
                buttonPresses += 1
            time.sleep(.2)
    except:
        print("\nButton pressing is done.")
        print("The button was pressed", buttonPresses, "times")
        GPIO.cleanup()
        exit()

main()




