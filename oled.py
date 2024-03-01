
from machine import Pin, SoftI2C
import ssd1306
from time import sleep

# ESP32 Pin assignment
i2c = SoftI2C(scl=Pin(44), sda=Pin(43))

# ESP8266 Pin assignment
#i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('19 gradi!!', 0, 10)
#oled.text('Hello, World 2!', 0, 10)
#oled.text('Hello, World 3!', 0, 20)

oled.show()