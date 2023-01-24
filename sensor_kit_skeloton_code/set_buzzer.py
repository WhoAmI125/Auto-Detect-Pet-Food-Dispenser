import RPi.GPIO as GPIO
import time

PIN = 5
GPIO.setmode(GPIO.BCM) #set which method to call the gpio bame. BCM == by name of pin
GPIO.setup(PIN, GPIO.OUT) #call specific pin, let know whether the pin is for input or output

buzzer = GPIO.PWM(PIN,370)
buzzer.start(50)
time.sleep(1)
