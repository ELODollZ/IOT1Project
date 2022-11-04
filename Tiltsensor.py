from imu import MPU6050  # https://github.com/micropython-IMU/micropython-mpu9x50
import time
from machine import Pin, I2C

i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)
imu = MPU6050(i2c)
countTackels = 0
direction = ['']
def tiltSensor(Direction, AntalTackels):
    global countTackels
    time.sleep(1)
    acceleration = imu.accel
    gyroscope = imu.gyro  
    direction = print("Acceleration x: ", round(acceleration.x,2), " y:", round(acceleration.y,2), "z: ", round(acceleration.z,2))
    #print ("gyroscope x: ", round(gyroscope.x,2), " y:", round(gyroscope.y,2), "z: ", round(gyroscope.z,2))
    # data interpretation (accelerometer)
    if abs(acceleration.x) > 0.8:
        if (acceleration.x > 0):
            print("The x axis points upwards")
        else:
            print("The x axis points downwards")
            countTackels += 1
            
    if abs(acceleration.y) > 0.8:
        if (acceleration.y > 0):
            print("The y axis points upwards")
            countTackels += 1
        else:
            print("The y axis points downwards")
            countTackels += 1
            
    if abs(acceleration.z) > 0.8:
        if (acceleration.z > 0):
            print("The z axis points upwards")
            countTackels += 1
        else:
            print("The z axis points downwards")
            countTackels += 1
    # data interpretation (gyroscope)

    if abs(gyroscope.x) > 20:
        print("Rotation around the x axis")

    if abs(gyroscope.y) > 20:
        print("Rotation around the y axis")

    if abs(gyroscope.z) > 20:
        print("Rotation around the z axis") 
    time.sleep(0.25)
    print(countTackels)
    return countTackels
    return Direction
countTackels = tiltSensor(Direction=direction, AntalTackels=countTackels)
print(countTackels)