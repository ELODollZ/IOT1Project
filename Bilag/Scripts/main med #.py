#Her importere vi en trejdeparts modul og giver det et lidt kortere navn 
import umqtt_robust2 as mqtt
#Her vælger vi, hvilket modul vi skal hente class fra og så henter vi class ved import. 
from machine import Pin, ADC
#vælger modul og importer sleep funktionen fra time modulet  
from time import sleep
#importere førsteparts modul
import gps_funktion
#fra display modulet importere vi display funktion 
from Display4X7 import display
#importere førsteparts modul
import Batteryreader


while True:
    try:
        # Denne variabel vil have GPS data når den har fået kontakt til sattellitterne ellers vil den være None
        gps_data = gps_funktion.gps_to_adafruit
        print(f"\ngps_data er: {gps_data}")
        sleep(4)
        mqtt.web_print(gps_data, 'dani636e/feeds/iot.iotmaps/csv')
        sleep(4)# vent mere end 3 sekunder mellem hver besked der sendes til adafruit
        Batteryreader.battery_percentage = Batteryreader.batteryPowerReaderConverter()
        print("The battery percentage is:", Batteryreader.battery_percentage, "%")
        mqtt.web_print(Batteryreader.battery_percentage, 'dani636e/feeds/iot.iotbatteri')
        sleep(4)
        display()
        
        
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

