import umqtt_robust2 as mqtt
from machine import Pin, ADC
from time import sleep
#from GPSInformation import gps_main, GPSPrint
import gps_funktion
import neopixel
from colorpicker import set_color
from Display4X7 import display, variableY, variableX
from Tiltsensor import tiltSensor, direction, countTackels
import Batteryreader

# Her kan i placere globale varibaler, og instanser af klasser
r = 255     
g = 255
b = 255
GPSInformation = ['','']
set_color(0,0,0)
Batteryreader.batteryPowerReaderConverter()

while True:
    try:
        # Denne variabel vil have GPS data når den har fået kontakt til sattellitterne ellers vil den være None
        gps_data = gps_funktion.gps_to_adafruit
        print(f"\ngps_data er: {gps_data}")
        mqtt.web_print(gps_data, 'dani636e/feeds/iot.iotmaps')
        set_color(r, 0, 0)
        sleep(4)# vent mere end 3 sekunder mellem hver besked der sendes til adafruit
        Batteryreader.batteryPowerReaderConverter()
        print("The battery percentage is:", Batteryreader.battery_percentage, "%")
        #print("Display test", variableY)
        mqtt.web_print(Batteryreader.battery_percentage, 'dani636e/feeds/iot.iotbatteri')
        sleep(4)
        set_color(0,g,0)
        display()
        #print("tilt test")
        tiltSensor(direction, countTackels)
        print(countTackels)
        gps_funktion.GPSPrint()
        #print(gps_funktion.GPSPrint())
        #GPSInformation = GPSTiden
        #print(GPSInformation)
        #mqtt.web_print(GPSInformation, 'dani636e/feeds/iot.iotfeed')
        #GPSInformation = gps_funktion.GPSSatellitesUsed
        #mqtt.web_print(GPSInformation, 'dani636e/feeds/iot.iotfeed')
        set_color(r, g, b)
        
        # Jeres kode skal slutte her
        sleep(0.5)
        if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
            mqtt.besked = ""            
        mqtt.sync_with_adafruitIO() # igangsæt at sende og modtage data med Adafruit IO             
        print(".", end = '') # printer et punktum til shell, uden et enter        
    # Stopper programmet når der trykkes Ctrl + c
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()

