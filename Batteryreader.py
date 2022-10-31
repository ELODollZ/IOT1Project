from time import sleep
from machine import Pin, ADC

analog_Pin = ADC(Pin(34))
analog_Pin.atten(ADC.ATTN_11DB)
analog_Pin.width(ADC.WIDTH_12BIT)
battery_percentage = 0

#Batteri måler
def batteryPowerReaderConverter():
        #Batteri måler
        analog_val = analog_Pin.read()
        #print("Raw analog value: ", analog_val)
        sleep(1)
        #Analog Val: 1869
        volts = (analog_val * 5)
        #print("The voltage is:", volts, "v")
        #9335 volts
        volts = volts/100
        battery_percentage = volts
        print(battery_percentage)
        return battery_percentage
battery_percentage = batteryPowerReaderConverter()
#print(battery_percentage)