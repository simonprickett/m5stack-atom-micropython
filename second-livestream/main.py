from mpu6886 import MPU6886, AFS_4G
from machine import Pin, SoftI2C
from math import *
import atom
import time

COLOR_OFF = (0, 0, 0)
COLOR_RED = (16, 0, 0)
MOVEMENT_THRESHOLD = 5

def set_pixel_color_x_y(x, y, r, g, b):
    n = (y * 5) + x
    a.set_pixel_color(n, r, g, b)


def compute_angles(ax, ay, az):
    # https://roboticsclubiitk.github.io/2017/12/21/Beginners-Guide-to-IMU.html
    pitch = 180 * atan (ax / sqrt(ay ** 2 + az ** 2))/ pi
    roll = 180 * atan (ay / sqrt(ax ** 2 + az ** 2))/ pi
    return pitch, roll


def calculate_new_position(p, angle, size):
    if (angle > MOVEMENT_THRESHOLD) and (p < 4):
        p = p + 1
    elif (angle < -MOVEMENT_THRESHOLD) and (p > 0):
        p = p - 1
        
    return p


i2c = SoftI2C(scl=Pin(21), sda=Pin(25))
mpu6886 = MPU6886(i2c, AFS_4G)

a = atom.Matrix()
a.set_pixels_color(*COLOR_OFF)

x = 2 
y = 2

while True:
    ax, ay, az = mpu6886.getAccelData()
    print(ax, ay, az)

    pitch, roll = compute_angles(ax, ay, az)
    print(f"pitch: {pitch}, roll: {roll}")
    
    set_pixel_color_x_y(x, y, *COLOR_OFF)
    x = calculate_new_position(x, pitch, 5)
    y = calculate_new_position(y, roll, 5)
    set_pixel_color_x_y(x, y, *COLOR_RED)
    
    time.sleep(0.2)