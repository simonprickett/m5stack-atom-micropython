import atom
import time
import dht
from machine import Pin, ADC

COLOR_OFF = (0, 0, 0)
COLOR_RED = (16, 0, 0)
COLOR_GREEN = (0, 16, 0)
COLOR_BLUE = (0, 0, 16)

UP_ARROW = [(2, 0), (1, 1), (2, 1), (3, 1), (0, 2), (2, 2), (4, 2), (2, 3), (2, 4)]
DOWN_ARROW = [(2, 0), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (2, 3), (3, 3), (2, 4)]
SIDE_ARROW = [(2, 0), (3, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (3, 3), (2, 4)]

a = atom.Matrix()
a.set_pixels_color(*COLOR_OFF)

def set_pixel_color_x_y(x, y, r, g, b):
    n = (y * 5) + x
    a.set_pixel_color(n, r, g, b)
    
def set_pixels_color_x_y(pixels, r, g, b):
    for x, y in pixels:
        set_pixel_color_x_y(x, y, r, g, b)

def update_display(old_val, new_val, threshold):
    # Clear the display.
    a.set_pixels_color(*COLOR_OFF)
    
    # Is the value going up?
    # TODO work threshold into this...
    if new_val > old_val:
        set_pixels_color_x_y(UP_ARROW, *COLOR_RED)
    elif new_val < old_val:
        set_pixels_color_x_y(DOWN_ARROW, *COLOR_GREEN)
    else:
        set_pixels_color_x_y(SIDE_ARROW, *COLOR_BLUE)


# Grove pins are 26 and 32.

def pir_sensor():
    pir = Pin(26, Pin.IN)
    last_triggered_at = 0
    
    while True:
        curr_ticks = time.ticks_ms()
        motion = pir.value()

        if motion == 1 and time.ticks_diff(curr_ticks, last_triggered_at) > 4000:
            print(f"{curr_ticks}: motion!")
            
            # Run a short "animation" on the LEDs.
            set_pixels_color_x_y([(2, 2)], *COLOR_RED)
            time.sleep(0.5)
            a.set_pixels_color(*COLOR_OFF)
            set_pixels_color_x_y([(1, 1), (2, 1), (3, 1), (1, 2), (3, 2), (1, 3), (2, 3), (3, 3)], *COLOR_BLUE)
            time.sleep(0.5)
            a.set_pixels_color(*COLOR_OFF)
            set_pixels_color_x_y([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (4, 1), (0, 2), (4, 2), (0, 3), (4, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)], *COLOR_GREEN)
            time.sleep(0.5)
            a.set_pixels_color(*COLOR_OFF)
            
            # Prevent double trigger.
            last_triggered_at = curr_ticks
        else:
            print(f"{curr_ticks}: no motion")
            
        time.sleep(0.1)
        
        
def light_sensor():
    light = ADC(32)
    old_val = 0
    
    while True:
        new_val = light.read_u16()
        print(f"light: {new_val}")
        # TODO appropriate threshold level.
        update_display(old_val, new_val, 0)
        old_val = new_val
        time.sleep(0.5)
        
        
def temp_humidity_sensor():
    # https://randomnerdtutorials.com/esp32-esp8266-dht11-dht22-micropython-temperature-humidity-sensor/
    # https://docs.micropython.org/en/latest/esp8266/quickref.html#dht-driver
    dht11 = dht.DHT11(Pin(32))
    old_val = 0
    
    while True:
        dht11.measure()
        new_val = dht11.humidity()
        print(f"temp: {dht11.temperature()}, humidity: {new_val}")
        # TODO appropriate threshold level.
        update_display(old_val, new_val, 0)
        old_val = new_val
        time.sleep(1)
        
        
#pir_sensor()
#light_sensor()
temp_humidity_sensor()
    