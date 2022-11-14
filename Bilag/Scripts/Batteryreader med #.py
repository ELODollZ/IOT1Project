from time import sleep
from machine import Pin, ADC
#vi opretter en variabel og giver den en værdi 
analog_Pin = ADC(Pin(34))
#Måler værdien over en spædning fra 0 til 3,3 volt 
analog_Pin.atten(ADC.ATTN_11DB)
#For at finde gennemsnittet af spændingen der måles. Fordi spædningen svinger
analog_Pin.width(ADC.WIDTH_12BIT)
#En variabel som er sat til int. Int er en tal værdi 
battery_percentage = 0

#Vi oprette en funktion og giver den navnet "batteryPowerReaderConverter"
def batteryPowerReaderConverter():
        #sætter en variabel og sætter den til en værdi af det den har læst fra analog pins 
        analog_val = analog_Pin.read()
        sleep(1)
        #Analog Val: 1869
        volts = (analog_val * 5)
        #9335 volts 6500 = 2845 dif.
        if (volts > 6500):
            #28.45 = 1%
            volts = ((volts-6500)/(9335-6500))
            voltages = volts * 100
            battery_percentage = voltages
        else:
            battery_percentage = 000
            #Vi tager værdien ud, hvis vi ikke bruger return vil vi bare få en "None" værdi ud 
        return battery_percentage
    #Sætter værdien den modtager fra linje 28 til variablen batteriprocent 
battery_percentage = batteryPowerReaderConverter()
