import json
import socket

import ticker

TCPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPServerSocket.bind(('192.168.1.20', 65432))
TCPServerSocket.listen()

TICKERS = [
    "BTC-USD",
    "ETH-USD",
    "XRP-USD",
    "ADA-USD",
]

while True:
    print("Waiting for TCP connection")

    conn, addr = TCPServerSocket.accept()

    done = False
    while not done:
        data = conn.recv(1024).decode("UTF-8")
        if data != "":
            if data == "list":
                res = json.dumps(TICKERS)
                conn.sendall(res.encode("UTF-8"))
            if data in TICKERS:
                ticker.get_chart(data)
        else:
            print("Connection terminated")
            done = True
    conn.close()
