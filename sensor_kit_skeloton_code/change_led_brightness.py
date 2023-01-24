import RPi.GPIO as GPIO
import time


LED = 24
GPIO.setmode(GPIO.BCM) #set which method to call the gpio bame. BCM == by name of pin
GPIO.setup(LED, GPIO.OUT) #call specific pin, let know whether the pin is for input or output

pwm = GPIO.PWM(LED, 100) #set duty(brightness), default is 100
pwm.start(0) #start the signal

duty = 100
count = 0

while(count<3):
	if duty == 0:
		count += 1
		duty = 100
		
	pwm.ChangeDutyCycle(duty) #change duty during
	duty -= 10
	time.sleep(0.5)

pwm.stop()
GPIO.cleanup() #important!, after using GPIO cleam up the autho


