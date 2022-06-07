import socket

LISTEN_IP = "192.168.1."
LISTEN_PORT = 12345

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((LISTEN_IP, LISTEN_PORT))

print("[UDP] Waiting for connection")

msgClient, coordClient = UDPServerSocket.recvfrom(1024)

print("[UDP] Message received from " + coordClient[0] + ":" + str(coordClient[1]) + " : " + msgClient.decode("UTF-8"))
UDPServerSocket.sendto(("[UDP] ACK : " + msgClient.decode("UTF-8")).encode('UTF-8'), coordClient)

UDPServerSocket.close()
