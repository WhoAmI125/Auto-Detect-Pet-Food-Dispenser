from adafruit_bmp280 import Adafruit_BMP280_I2C
import board, time

i2c = board.I2C()

sensor = Adafruit_BMP280_I2C(i2c) #setup airpressure

time.sleep(2)

temp = sensor.temperature
airpressure = sensor.pressure #since pressure is related to altitude, knowing altitude can tell height

sensor.sea_level_pressure = 1025.9 #the value changes depending
alt = sensor.altitude #get altitute

print(temp, airpressure)
