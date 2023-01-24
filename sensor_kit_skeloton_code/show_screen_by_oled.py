import os, time, board
import adafruit_ssd1306
from PIL import Image, ImageOps

#/home/pi/Downloads/happycat_oled_64.ppm

width = 128
height = 64
i2c = board.I2C()

#setup width,height, i2c controller, i2c address
OLED = adafruit_ssd1306.SSD1306_I2C(width, height, i2c, addr=0x3C)

image = Image.open("./happycat_oled_64.ppm").convert("1")
#image draw in memory first -> then showed in oled
OLED.image(image)
#show image drawed in memory
OLED.show()
time.sleep(2)

OLED.fill(0)
OLED.show()

box = (0,0,60,60)
cutout = image.crop(box)
cutout = cutout.transpose(Image.ROTATE_180)
image.paste(cutout, (20,20,60,60))
OLED.image(image)
OLED.show()
time.sleep(2)
