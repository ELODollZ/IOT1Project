import tm1637
from machine import Pin
from time import sleep
import Batteryreader

tm = tm1637.TM1637(clk=Pin(4), dio=Pin(2))

tm.brightness(5)
variableY = "LIVE"
sleep(1)
tm.show("PPPP")
def display():
    variableX = Batteryreader.battery_percentage
    #converter til en intigere variable
    variableX = int(variableX)
    #tjekker om variablen er ligemed eller under 100
    if(variableX >= 100):
        #converter outputtet til en string og intigere
        tm.show(("{}{}".format("0", variableX, "P")))
    else:
        #converter outputtet til en string og intigere
        tm.show(("{}{}".format(variableX,"P")))
    