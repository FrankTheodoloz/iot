import mqttclient
from realtcp import *
from time import *

from cli import *
from gui import *
import json
import mqttclient
from time import *

port = 1234
server = RealTCPServer()

client = None


def onTCPNewClient(client):
    def onTCPConnectionChange(type):
        print("connection to " + client.remoteIP() + " changed to state " + str(type))

    def onTCPReceive(data):
        print("received from " + client.remoteIP() + " with data: " + data)
        if (data != ""):
            if (data == "1"):
                mqttclient.publish("Topic1", "msgTopic1", 1)
        # send back same data
        client.send(data)

    client.onConnectionChange(onTCPConnectionChange)
    client.onReceive(onTCPReceive)


def on_connect(status, msg, packet):
    if status == "Success" or status == "Error":
        print
        status + ": " + msg
    elif status == "":
        print
        msg

    CLI.exit()


def on_disconnect(status, msg, packet):
    if status == "Success" or status == "Error":
        print
        status + ": " + msg
    elif status == "":
        print
        msg

    CLI.exit()


def on_subscribe(status, msg, packet):
    if status == "Success" or status == "Error":
        print
        status + ": " + msg
    elif status == "":
        print
        msg

    CLI.exit()


def on_unsubscribe(status, msg, packet):
    if status == "Success" or status == "Error":
        print
        status + ": " + msg
    elif status == "":
        print
        msg

    CLI.exit()


def on_publish(status, msg, packet):
    if status == "Success" or status == "Error":
        print
        status + ": " + msg
    elif status == "":
        print
        msg

    CLI.exit()


def on_message_received(status, msg, packet):
    if status == "Success" or status == "Error":
        print
        status + ": " + msg
    elif status == "":
        print
        msg

    CLI.exit()


def check_conn():
    while (mqttclient.state()['broker_address'] == ""):
        sleep(5)
        mqttclient.connect("192.168.1.150", "", "")

    while (len(mqttclient.state()['subscriptions']) < 1):
        sleep(5)
        mqttclient.subscribe("Topic1")
        check_conn()


def main():
    mqttclient.init();

    mqttclient.init()
    mqttclient.onConnect(on_connect)
    mqttclient.onDisconnect(on_disconnect)
    mqttclient.onSubscribe(on_subscribe)
    mqttclient.onUnsubscribe(on_unsubscribe)
    mqttclient.onPublish(on_publish)
    mqttclient.onMessageReceived(on_message_received)

    check_conn()

    server.onNewClient(onTCPNewClient)
    print(server.listen(port))

    # don't let it finish
    while True:
        sleep(3600)


if __name__ == "__main__":
    main()