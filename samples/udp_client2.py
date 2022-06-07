import socket

SERVER_IP = "192.168.1."
SERVER_PORT = 12345

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

msg = "[UDP] client to server"

UDPClientSocket.sendto(msg.encode('UTF-8'), (SERVER_IP, SERVER_PORT))
msgServeur, coordServeur = UDPClientSocket.recvfrom(1024)

print("[UDP] server reply: ", msgServeur.decode("UTF-8"))

UDPClientSocket.close()
print("[UDP] connection closed")
