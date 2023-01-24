from grove.adc import ADC
import RPi.GPIO as GPIO
import time


LED = 24
GPIO.setmode(GPIO.BCM) #set which method to call the gpio bame. BCM == by name of pin
GPIO.setup(LED, GPIO.OUT) #call specific pin, let know whether the pin is for input or output

PIN = 2
adc = ADC()

print("ready")

pwm = GPIO.PWM(LED, 100) #set duty(brightness), default is 100
pwm.start(0) #start the signal

while 1:
	value = adc.read(PIN)
	print(f'analog read:{value}')
	
	if int(value) > 100:
		value = 100
	
	pwm.ChangeDutyCycle(int(value)) #change duty during
	time.sleep(0.5)
	#break

pwm.stop()
