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
        #9335 volts 6500 = 2845 dif.
        if (volts > 6500):
            #28.45 = 1%
            volts = ((volts-6500)/(9335-6500))
            voltages = volts * 100
            battery_percentage = voltages
        else:
            battery_percentage = 000
        #print("reader", battery_percentage)
        return battery_percentage
battery_percentage = batteryPowerReaderConverter()
#print(battery_percentage)