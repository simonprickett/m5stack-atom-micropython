import atom
import time
import dht
from machine import Pin, ADC

COLOR_OFF = (0, 0, 0)
COLOR_RED = (16, 0, 0)
COLOR_GREEN = (0, 16, 0)
COLOR_BLUE = (0, 0, 16)

UP_ARROW = [(2, 0), (1, 1), (2, 1), (3, 1), (0, 2), (2, 2), (4, 2), (2, 3), (2, 4)]
DOWN_ARROW = []
SIDE_ARROW = []

a = atom.Matrix()
a.set_pixels_color(*COLOR_OFF)

def set_pixel_color_x_y(x, y, r, g, b):
    n = (y * 5) + x
    a.set_pixel_color(n, r, g, b)
    
def set_pixels_color_x_y(pixels, r, g, b):
    for x, y in pixels:
        set_pixel_color_x_y(x, y, r, g, b)

# Grove pins are 26 and 32.

def pir_sensor():
    pir = Pin(26, Pin.IN)
    
    while True:
        print(f"motion: {pir.value()}")
        time.sleep(0.5)
        
        
def light_sensor():
    light = ADC(32)
    
    while True:
        print(f"light: {light.read_u16()}")
        time.sleep(0.5)
        
        
def temp_humidity_sensor():
    # https://randomnerdtutorials.com/esp32-esp8266-dht11-dht22-micropython-temperature-humidity-sensor/
    # https://docs.micropython.org/en/latest/esp8266/quickref.html#dht-driver
    dht11 = dht.DHT11(Pin(32))
    set_pixels_color_x_y(UP_ARROW, *COLOR_RED)
    
    while True:
        dht11.measure()
        print(f"temp: {dht11.temperature()}, humidity: {dht11.humidity()}")
        time.sleep(1)
        
        
#pir_sensor()
#light_sensor()
temp_humidity_sensor()
    