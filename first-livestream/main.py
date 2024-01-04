import atom
import network
import time
import secrets
from umqtt.simple import MQTTClient

RED = (16, 0, 0)
GREEN = (0, 16, 0)
OFF = (0, 0, 0)

def set_pixel_color_x_y(x, y, r, g, b):
    n = (y * 5) + x
    a.set_pixel_color(n, r, g, b)


def button_pressed(pin):
    print(pin)


def connect_wifi():
    a.set_pixels_color(*RED)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
    
    while not wlan.isconnected():
        time.sleep(0.5)
        if a.get_pixel_color(0) == RED:
            a.set_pixels_color(*OFF)
        else:
            a.set_pixels_color(*RED)
            
    a.set_pixels_color(*GREEN)
    time.sleep(2)
    a.set_pixels_color(*OFF)


def show_cheerlights(topic, msg):
    print(topic)
    print(msg)
    
    col_str = msg.decode()
    
    if col_str == "red":
        a.set_pixels_color(16, 0, 0)
    elif col_str == "green":
        a.set_pixels_color(0, 16, 0)
    elif col_str == "blue":
        a.set_pixels_color(0, 0, 16)
    elif col_str == "cyan":
        a.set_pixels_color(0, 16, 16)
    elif col_str == "white":
        a.set_pixels_color(16, 16, 16)
    elif col_str == "oldlace":
        a.set_pixels_color(15, 12, 12)
    elif col_str == "purple":
        a.set_pixels_color(8, 0, 8)
    elif col_str == "magenta":
        a.set_pixels_color(16, 0, 16)
    elif col_str == "yellow":
        a.set_pixels_color(16, 16, 0)
    elif col_str == "orange":
        a.set_pixels_color(16, 6, 0)
    elif col_str == "pink":
        a.set_pixels_color(16, 10, 13)


a = atom.Matrix()
a.set_pixels_color(*OFF)
a.set_button_callback(button_pressed)
connect_wifi()

mqtt_client = MQTTClient("M5StackAtom", "mqtt.cheerlights.com")
mqtt_client.connect()
mqtt_client.set_callback(show_cheerlights)
mqtt_client.subscribe(b"color")

while True:
    time.sleep(1)
    mqtt_client.check_msg()
