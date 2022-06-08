''' These are only the CHANGES on main.py'''
import json
from realtcp import *

port = 1234
server = RealTCPServer()

client = None


def onTCPNewClient(client):
    '''This is a new function'''

    def onTCPConnectionChange(type):
        print("connection to " + client.remoteIP() + " changed to state " + str(type))

    def onTCPReceive(data):
        print("received from " + client.remoteIP() + " with data: " + data)
        if (data != ""):
            json_object = json.loads(data)
            if (json_object["topic"] == "LOG"):
                mqttclient.publish("LOG", json_object["value"], 1)
            if (json_object["topic"] == "LIGHT"):
                mqttclient.publish("LIGHT", "ON", 1)
        # send back same data
        client.send(data)

    client.onConnectionChange(onTCPConnectionChange)
    client.onReceive(onTCPReceive)


def check_conn():
    '''This is a new function'''
    while (mqttclient.state()['broker_address'] == ""):
        sleep(5)
        mqttclient.connect("192.168.1.150", "", "")
    while (len(mqttclient.state()['subscriptions']) < 1):
        sleep(5)
        # mqttclient.subscribe("Topic1")
        check_conn()


def main():
    '''ADD check_conn() right before "while True:"'''
    check_conn()

    server.onNewClient(onTCPNewClient)
    print(server.listen(port))

    # don't let it finish
    while True:
        sleep(3600)
