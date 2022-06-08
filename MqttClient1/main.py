''' These are only the CHANGES on main.py'''

from gpio import *

pinMode(0, OUT)


def on_message_received(status, msg, packet):
    '''Change on_message_received function'''
    if (packet["payload"] == "OFF"):
        customWrite(0, 0)
    if (packet["payload"] == "ON"):
        customWrite(0, 2)
    if status == "Success" or status == "Error":
        print(status + ": " + msg)
    elif status == "":
        print(msg)
    CLI.exit()


def check_conn():
    '''This is a new function'''
    while (mqttclient.state()['broker_address'] == ""):
        sleep(5)
        mqttclient.connect("192.168.1.150", "", "")

    while (len(mqttclient.state()['subscriptions']) < 1):
        sleep(5)
        mqttclient.subscribe("LIGHT")
        check_conn()


def main():
    '''ADD check_conn() right before "while True:"'''
    check_conn()

    while True:
        delay(60000)
