import RPi.GPIO as GPIO
import time

Button = 5
GPIO.setmode(GPIO.BCM) #set which method to call the gpio bame. BCM == by name of pin
GPIO.setup(Button, GPIO.IN, pull_up_down = GPIO.PUD_UP) #call specific pin, let know whether the pin is for input or output

count = 0
button_save = 0

while 1:
    state = GPIO.input(Button)
    
    if state == GPIO.HIGH and button_save == 0:
        button_save = 1
        print("HIGH")
    elif state == GPIO.LOW and button_save == 1:
        button_save = 0
        print("LOW")

GPIO.cleanup() #important!, after using GPIO cleam up the autho


