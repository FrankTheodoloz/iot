# https://docs.micropython.org/en/latest/esp32/quickref.html

import network
import time

def connect(ssid, key):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    start = time.ticks_ms;
    if not wlan.isconnected():
        print('connecting to network', ssid)
        wlan.connect(ssid, key)
        while not wlan.isconnected():
            time.sleep_ms(1000)
            if (time.ticks_ms - start > 20000):
                print("Wifi connection timeout")
                break
    if (wlan.isconnected()):
        print("Network connected : ", wlan.ifconfig())
    return wlan

