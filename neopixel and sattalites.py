from machine import UART
from micropyGPS import MicropyGPS
import neopixel
from machine import Pin
n = 12
p = 22

np = neopixel.NeoPixel(Pin(p), n)

def set_color(r, g, b):
    for i in range(n):
        np[i]=(r, g, b)
        np.write()



def gps_main():
    uart = UART(2, baudrate=9600, bits=8, parity=None,
                stop=1, timeout=5000, rxbuf=1024)
    gps = MicropyGPS()

    while True:
        buf = uart.readline()
        i = gps.satellites_in_use
            
        for char in buf:
# Note the conversion to to chr, UART outputs ints normally
            gps.update(chr(char))
            
        print('UTC Timestamp:', gps.timestamp)
        print('Date:', gps.date_string('long'))
        print('Satellites:', gps.satellites_in_use)
        print('Altitude:', gps.altitude)
        print('Latitude:', gps.latitude_string())
        print('Longitude:', gps.longitude_string())
        print('Horizontal Dilution of Precision:', gps.hdop)
        
        if i < 0:
            
            set_color(255, 0, 0)
            print(i)
        i += 1
#         if gps.satellites_in_use >= 3:
#             set_color(255, 0, 0)
#             print("3 or more than 3 SAT")
# 
#         if gps.satellites_in_use < 3:
#             set_color(0, 0, 0)
#             print("less than 3 SAT")
            
                 
gps_main()

