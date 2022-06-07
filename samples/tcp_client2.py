import socket

SERVER_IP = "192.168.1."
SERVER_PORT = 65432

TCPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("TCP Connection to ", SERVER_IP, ":", SERVER_PORT)
TCPClientSocket.connect((SERVER_IP, SERVER_PORT))

msg = "[TCP] client to server"

for i in range(1, 5):
    msg2 = msg + str(i)
    TCPClientSocket.sendall(msg.encode('UTF-8'))

    msgServeur = TCPClientSocket.recv(1024)
    print("[TCP] server reply: ", msgServeur.decode('UTF-8'))

TCPClientSocket.send(b"")
TCPClientSocket.close()
print("[TCP] connection closed")
