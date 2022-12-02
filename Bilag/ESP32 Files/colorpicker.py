import neopixel
from machine import Pin
from time import sleep

pinforNEOPixel = Pin(12, Pin.OUT)
neopixelLEDantal = 12
r = 255
g = 255
b = 255

#color sætter
def set_color(r,g,b):
    for i in range(neopixelLEDantal):
        np[i] = (r,g,b)
        np.write()
np = neopixel.NeoPixel(pinforNEOPixel, neopixelLEDantal)
