from grove.grove_servo import GroveServo
import time

servo = GroveServo(18)


servo.setAngle(179)
time.sleep(3)
servo.setAngle(1)
time.sleep(3)


servo.setAngle(179)
time.sleep(3)
servo.setAngle(1)
time.sleep(3)
