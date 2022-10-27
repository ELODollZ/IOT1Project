import tm1637
from machine import Pin
from time import sleep
tm = tm1637.TM1637(clk=Pin(4), dio=Pin(2))

tm.brightness(5)
variableY = "Live"
variableX = str(100)

def display():
    sleep(1)
    tm.show(variableY)
    tm.show(variableX,"P")
    