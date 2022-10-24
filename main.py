import umqtt_robust2 as mqtt
from machine import Pin
from time import sleep

# Her kan i placere globale varibaler, og instanser af klasser
red_LED = Pin(25, Pin.OUT) # instans af Pin klassen AKA et Pin objekt

while True:
    try:
        # Jeres kode skal starte her
        if mqtt.besked == "led_on":
            print("tænder led")
            red_LED.on()
            
        if mqtt.besked == "led_off":
            print("slukker led")
            red_LED.off()
                    
        if mqtt.besked == "svar_tilbage":
            mqtt.web_Print("ESP32 her!")
            
        # Jeres kode skal slutte her
        sleep(0.5)
        if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
            mqtt.besked = ""            
        mqtt.syncWithAdafruitIO() # igangsæt at sende og modtage data med Adafruit IO             
        print(".", end = '') # printer et punktum til shell, uden et enter        
    # Stopper programmet når der trykkes Ctrl + c
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()