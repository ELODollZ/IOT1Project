from machine import UART
from micropyGPS import MicropyGPS
import _thread

# denne variabel opdateres til at holde gps data
gps_to_adafruit = None
# instans af gps klassen opdateres her
gps = None
uart = UART(2, baudrate=9600, bits=8, parity=None, stop=1, timeout=5000, rxbuf=1024)
#Variabel
GPSTiden = None
GPSSatellitesUsed = None
def gps_main():
    global gps
    gps = MicropyGPS()
    gpsSecondFunktion()

def gpsSecondFunktion():
    buf = uart.readline()
    if buf:
        for char in buf:
            gps.update(chr(char)) # Note the conversion to to chr, UART outputs ints normally 
    #different gps methods that can be used:
    print('UTC Timestamp:', gps.timestamp)
    GPSTiden = gps.timestamp
    print('Date:', gps.date_string('long'))
    print('Satellites:', gps.satellites_in_use)
    GPSSatellitesUsed = gps.satellites_in_use
    print('Altitude:', gps.altitude)
    print('Latitude:', gps.latitude_string())
    print('Longitude:', gps.longitude_string())
    print('Horizontal Dilution of Precision:', gps.hdop)
    print('Compas direction: ', gps.compass_direction())
    return GPSTiden
    return GPSSatellitesUsed
    print("Tiden", GPSTiden)
    print("Satell",GPSSatellitesUsed)

    formattedLat = gps.latitude_string()
    formattedLat = formattedLat[:-3]
    formattedLon = gps.longitude_string()
    formattedLon = formattedLon[:-3]
    formattedAlt = str(gps.altitude)
    formattedSpd = gps.speed_string()
    formattedSpd = formattedSpd[:-5]
    #print(gps.speed_string())
    gps_ada = formattedSpd+","+formattedLat+","+formattedLon+","+formattedAlt     
    if formattedLat != "0.0" and formattedLon != "0.0":
        #print("gps_ada: ",gps_ada)
        global gps_to_adafruit
        gps_to_adafruit = gps_ada
gps_main()