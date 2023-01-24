from grove.grove_sound_sensor import GroveSoundSensor
import time

PIN = 0

sound_sensor = GroveSoundSensor(PIN)

while 1:
	value = sound_sensor.sound
	print(value)
	time.sleep(1)
