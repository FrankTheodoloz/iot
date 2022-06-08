import json
import socket

import ticker

UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPServerSocket.bind(("192.168.1.19", 12345))

TICKERS = [
    "BTC-USD",
    "ETH-USD",
    "XRP-USD",
    "ADA-USD",
]

while True:
    print("Waiting for UDP connection")

    msgClient, coordClient = UDPServerSocket.recvfrom(1024)

    # print("Message received from " + coordClient[0] + ":" + str(coordClient[1]) + " : " + msgClient.decode("UTF-8"))
    UDPServerSocket.sendto(("UDP Server received : " + msgClient.decode("UTF-8")).encode('UTF-8'), coordClient)

    data = msgClient.decode("UTF-8")
    print(data)
    if data != "":
        if data == "list":
            res = json.dumps(TICKERS)
            UDPServerSocket.sendto(res.encode('UTF-8'), coordClient)
        if data in TICKERS:
            print("True " + data)
            ticker.get_chart(data)

UDPServerSocket.close()
