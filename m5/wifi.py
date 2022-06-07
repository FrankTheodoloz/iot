# https://docs.micropython.org/en/latest/esp32/quickref.html

WLAN_SSID = ""
WLAN_KEY = ""
# WLAN_SSID = "MediaNet"
# WLAN_KEY = "ri0a-4a0b-lcyo-7qwb"

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(WLAN_SSID, WLAN_KEY)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
