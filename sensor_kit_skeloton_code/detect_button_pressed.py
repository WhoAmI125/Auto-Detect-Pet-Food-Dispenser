from grove.grove_button import GroveButton
import time

Button = 5

button = GroveButton(Button)

def onPress():
	print("pressed")

def releasedPress():
	print("released")
	
button.on_press = onPress()
button.on_release = releasedPress()

while(1):
	print("...")
	time.sleep(5)
