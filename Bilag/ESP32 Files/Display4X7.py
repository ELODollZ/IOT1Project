import tm1637
from machine import Pin
from time import sleep
import Batteryreader

tm = tm1637.TM1637(clk=Pin(4), dio=Pin(2))

tm.brightness(5)
variableY = "LIVE"

def display():
    variableX = Batteryreader.battery_percentage
    variableX = int(variableX)
    #tm.show(variableY)
    sleep(1)
    tm.show("PPPP")
    tm.show(("{}{}".format(variableX,"P")))
    if(variableX < 100):
        tm.show(("{}{}".format("0", variableX, "P")))
    