import gps_funktion
import umqtt_robust2 as mqtt
from machine import Pin, ADC
from time import sleep
import simple_gps_example

analog_Pin = ADC(Pin(34))
analog_Pin.atten(ADC.ATTN_11DB)
analog_Pin.width(ADC.WIDTH_12BIT)
# Her kan i placere globale varibaler, og instanser af klasser

while True:
    try:
        # Denne variabel vil have GPS data når den har fået kontakt til sattellitterne ellers vil den være None
        gps_data = gps_funktion.gps_to_adafruit
        print(f"\ngps_data er: {gps_data}")
        
        #For at sende beskeder til andre feeds kan det gøres sådan:
        #Indsæt eget username og feednavn til så det svarer til dit eget username og feed du har oprettet
        mqtt.web_print(gps_data, 'Royaro/feeds/mapfeed/csv')
        
        #For at vise lokationsdata på adafruit dashboard skal det sendes til feed med /csv til sidst
        #For at sende til GPS lokationsdata til et feed kaldet mapfeed kan det gøres således:
        #mqtt.web_print(gps_data, 'DIT_ADAFRUIT_USERNAME/feeds/mapfeed/csv')        
        sleep(4)# vent mere end 3 sekunder mellem hver besked der sendes til adafruit
        
        #mqtt.web_print("location") # Hvis der ikke angives et 2. argument vil default feed være det fra credentials filen      
        #sleep(4)  # vent mere end 3 sekunder mellem hver besked der sendes til adafruit
        if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
            mqtt.besked = ""            
        mqtt.sync_with_adafruitIO() # igangsæt at sende og modtage data med Adafruit IO             
        print(".", end = '') # printer et punktum til shell, uden et enter        
    # Stopper programmet når der trykkes Ctrl + c
        analog_val = analog_Pin.read()
    #print("Raw analog value: ", analog_val)
    #sleep(1)
        volts = (analog_val * 0.00095238)*5

#     print("The voltage is:", volts, "v")
        sleep(4)
        battery_percentage = volts*100 - 320
        print ("The battery percentage is:", battery_percentage/2, "%")

        mqtt.web_print(battery_percentage/2)

        sleep(4)
        
        
        
        if len (mqtt.besked) != 0:
            mqtt.besked = ""
        mqtt.sync_with_adafruitIO()
        print(".", end = ' ')
        
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()

 
 