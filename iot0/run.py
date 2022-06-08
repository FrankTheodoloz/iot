import socket

LISTEN_IP = "192.168.1.22"
LISTEN_PORT = 65432

IOT1_IP = "192.168.1.19"
IOT1_PORT = 12345
IOT2_IP = "192.168.1.20"
IOT2_PORT = 12345
PT_RealTcpServer_IP = "192.168.1.30"
PT_RealTcpServer_PORT = 1234

TCPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPServerSocket.bind((LISTEN_IP, LISTEN_PORT))
TCPServerSocket.listen()


def send_udp_message(server, port, message):
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPClientSocket.sendto(message.encode('UTF-8'), (server, port))
    msgServeur, coordServeur = UDPClientSocket.recvfrom(1024)
    print("[UDP] server reply: ", msgServeur.decode("UTF-8"))
    UDPClientSocket.close()


def send_tcp_message(server, port, message):
    TCPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPClientSocket.connect((server, port))
    TCPClientSocket.sendall(message.encode('UTF-8'))
    msgServeur = TCPClientSocket.recv(1024)
    print("[TCP] server reply: ", msgServeur.decode("UTF-8"))
    TCPClientSocket.close()


while True:
    print("[TCP] Waiting for connection")

    conn, addr = TCPServerSocket.accept()

    done = False
    while not done:
        data = conn.recv(1024).decode("UTF-8")
        if data != "":
            if (data == "buttonA"):
                print("buttonA")
                send_udp_message(IOT1_IP, IOT1_PORT, "BTC-USD")
                send_udp_message(IOT2_IP, IOT2_PORT, "BTC-USD")
                send_tcp_message(PT_RealTcpServer_IP, PT_RealTcpServer_PORT,
                                 '{topic: "LOG", value: "Changed ticker to BTC-USD"}')

            if (data == "buttonB"):
                print("buttonB")
                send_udp_message(IOT1_IP, IOT1_PORT, "ETH-USD")
                send_udp_message(IOT2_IP, IOT2_PORT, "ETH-USD")
                send_tcp_message(PT_RealTcpServer_IP, PT_RealTcpServer_PORT,
                                 '{topic: "LOG", value: "Changed ticker to ETH-USD"}')

            if (data == "buttonC"):
                print("buttonC")
                send_udp_message(IOT1_IP, IOT1_PORT, "ADA-USD")
                send_udp_message(IOT2_IP, IOT2_PORT, "ADA-USD")
                send_tcp_message(PT_RealTcpServer_IP, PT_RealTcpServer_PORT,
                                 '{topic: "LOG", value: "Changed ticker to ADA-USD"}')

            if (data == "PIR_ON"):
                print("PIR_ON")
                send_tcp_message(PT_RealTcpServer_IP, PT_RealTcpServer_PORT, '{topic: "LIGHT", value: "ON"}')
                send_tcp_message(PT_RealTcpServer_IP, PT_RealTcpServer_PORT, '{topic: "LOG", value: "Turned light on"}')

            if (data == "PIR_OFF"):
                print("PIR_OFF")
                send_tcp_message(PT_RealTcpServer_IP, PT_RealTcpServer_PORT, '{topic: "LIGHT", value: "OFF"}')
                send_tcp_message(PT_RealTcpServer_IP, PT_RealTcpServer_PORT,
                                 '{topic: "LOG", value: "Turned light off"}')

        conn.sendall(("[TCP] ACK : " + data).encode("UTF-8"))
    else:
        print("[TCP] connection closed")
        done = True

    conn.close()
