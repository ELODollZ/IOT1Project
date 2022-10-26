from time import sleep
import umqtt_robust2 as mqtt
from machine import Pin, ADC
import colorpicker

bat = ADC(Pin(34))
bat.atten(ADC.ATTN_11DB)
bat.width(ADC.WIDTH_12BIT)
battery_percentage = 0
batValue

#Batteri måler
def batteryPowerReaderConverter():
        batValue = bat.read()
        m_spaending = batValue/4095*3.3
        spaending = m_spaending * 5
        battery_percentage = spaending/8.4 * 100
        sleep(1)
