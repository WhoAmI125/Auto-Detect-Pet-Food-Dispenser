import RPi.GPIO as GPIO
import time

from grove.grove_led import GroveLed

def raspVer():
	LED = 24
	GPIO.setmode(GPIO.BCM) #set which method to call the gpio bame. BCM == by name of pin
	GPIO.setup(LED, GPIO.OUT) #call specific pin, let know whether the pin is for input or output

	count = 0

	while(count<5):
		GPIO.output(LED, GPIO.HIGH) #set GPIO24 to +, letting current flow
		time.sleep(2)
		GPIO.output(LED, GPIO.LOW) #set GPIO24 to -, letting current block
		time.sleep(0.5)
		count += 1

	GPIO.cleanup() #important!, after using GPIO cleam up the autho

def groveVer():
	PIN = 24
	led = GroveLed(PIN)
	
	for i in range(5):
		led.on()
		time.sleep(1)
		led.off()
		time.sleep(1)
		
groveVer()


