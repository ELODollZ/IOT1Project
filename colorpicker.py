import neopixel
from machine import Pin
from time import sleep

pinNEOPixel = Pin(15, Pin.OUT)
neopixelLED = 12
r = 100
g = 100
b = 100
#color sætter
def set_color(r,g,b):
    for i in range(neopixelLED):
        np[i] = (r,g,b)
        np.write()
np = neopixel.NeoPixel(pinNEOPixel, neopixelLED)
