import gps_funktion
import umqtt_robust2 as mqtt
from machine import Pin, ADC
from time import sleep
import neopixel
import micropyGPS
from machine import UART



bat = ADC(Pin(34))
bat.atten(ADC.ATTN_11DB)
bat.width(ADC.WIDTH_12BIT)
battery_percentage = 0
pinNEOPixel = Pin(15, Pin.OUT)
neopixelLED = 12
r = 100
g = 100
b = 100

def set_color(r,g,b):
    for i in range(neopixelLED):
        np[i] = (r,g,b)
        np.write()
np = neopixel.NeoPixel(pinNEOPixel, neopixelLED)

        
# Her kan i placere globale varibaler, og instanser af klasser
while True:
    try:
        # Denne variabel vil have GPS data når den har fået kontakt til sattellitterne ellers vil den være None
        gps_data = gps_funktion.gps_to_adafruit
        print(f"\ngps_data er: {gps_data}")
        set_color(r,g,b)
        #For at sende beskeder til andre feeds kan det gøres sådan:
        #Indsæt eget username og feednavn til så det svarer til dit eget username og feed du har oprettet
        #mqtt.web_print(battery_percentage, 'Kasperfcb/feeds/batteri/csv')
        
        #For at vise lokationsdata på adafruit dashboard skal det sendes til feed med /csv til sidst
        #For at sende til GPS lokationsdata til et feed kaldet mapfeed kan det gøres således:
        mqtt.web_print(gps_data, 'Kasperfcb/feeds/mapfeed/csv')        
        sleep(4)# vent mere end 3 sekunder mellem hver besked der sendes til adafruit
        
        #mqtt.web_print("location") # Hvis der ikke angives et 2. argument vil default feed være det fra credentials filen      
        #sleep(4)  # vent mere end 3 sekunder mellem hver besked der sendes til adafruit
        if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
            mqtt.besked = ""            
        mqtt.sync_with_adafruitIO() # igangsæt at sende og modtage data med Adafruit IO             
        print(".", end = '') # printer et punktum til shell, uden et enter        
        
        #Batteri måler
        bat_val = bat.read()
        m_spaending = bat_val/4095*3.3
        print("Analog maalt vaerdi: ",m_spaending)
        spaending = m_spaending * 5
        print("Input spaending: ",spaending)
        sleep(1)

        #print("The voltage is:", volts, "v")
        sleep(4)
        battery_percentage = spaending/8.4 * 100
        print ("The battery percentage is:", battery_percentage, "%")
        mqtt.web_print(battery_percentage, 'Kasperfcb/feeds/batteri/csv')
        set_color(r, 0, 0)
        sleep(4)
        
        #sattelites sender to Adafruit
        totalSatellites()
 
        
# Stopper programmet når der trykkes Ctrl + c
        if len (mqtt.besked) != 0:
            mqtt.besked = ""
        mqtt.sync_with_adafruitIO()
        print(".", end = ' ')
        
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()

