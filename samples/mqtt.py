import paho.mqtt.client as mqtt  # import the client1
import time
import keyboard


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)


broker_address = "192.168..Y"

print("creation de la nouvelle instance")
client = mqtt.Client("client1")
client.on_message = on_message

print("connection au broker")
client.connect(broker_address)
client.loop_start()  # demarrage de la boucle

print("Inscription au topic", "salon/temp")
client.subscribe("salon/temp")

# print("Publishing message to topic","salon/temp")
# client.publish("salon/temp","23.4")
fin = False
while fin == False:
    if keyboard.is_pressed('q'):
        print('On a fini!')
        fin = True
    # ToDo----------
    # FinToDo----------

client.loop_stop()
