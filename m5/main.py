from m5stack import lcd, buttonA, buttonB, buttonC

import socket
import time
import pir
import wifi

WLAN_SSID = "MediaNet"
WLAN_KEY = "ri0a-4a0b-lcyo-7qwb"
SERVER_IP = "16d.internet-box.ch"
SERVER_PORT = 65432
TCPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PIR_LASTSTATE = 0

lcd.clear()
lcd.setCursor(0, 0)
lcd.setColor(lcd.WHITE)
lcd.print("ButtonA : Ticker BTC-USD\n")
lcd.print("ButtonB : Ticker ETH-USD\n")
lcd.print("ButtonC : Ticker ADA-USD\n")


def sendmsg(ip, port, message):
    TCPClientSocket.connect((ip, port))
    TCPClientSocket.sendall(message.encode('UTF-8'))
    msgServeur = TCPClientSocket.recv(1024)
    print("[TCP] server reply: ", msgServeur.decode('UTF-8'))
    TCPClientSocket.close()


wifi.connect(WLAN_SSID, WLAN_KEY)
PIR_MODULE = pir.PIR()

while True:
    time.sleep(0.5)
    if buttonA.isPressed():
        sendmsg(SERVER_IP, SERVER_PORT, "buttonA")
    if buttonB.isPressed():
        sendmsg(SERVER_IP, SERVER_PORT, "buttonB")
    if buttonC.isPressed():
        sendmsg(SERVER_IP, SERVER_PORT, "buttonC")

    PIR_CURRENTSTATE = PIR_MODULE.read()
    if (PIR_CURRENTSTATE != PIR_LASTSTATE):
        if (PIR_CURRENTSTATE == 1):
            sendmsg(SERVER_IP, SERVER_PORT, "PIR_ON")
        if (PIR_CURRENTSTATE == 0):
            sendmsg(SERVER_IP, SERVER_PORT, "PIR_OFF")
        PIR_LASTSTATE = PIR_CURRENTSTATE
    time.sleep(0.2)
