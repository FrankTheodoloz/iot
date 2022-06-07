import socket

SERVER_IP = '192.168.1.19'
SERVER_PORT = 12345

# msg = "list"
# msg = "BTC-USD"
# msg = "ETH-USD"
msg = "XRP-USD"
# msg = "ADA-USD"

UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPClientSocket.sendto(msg.encode('UTF-8'), (SERVER_IP, SERVER_PORT))

'''REPLY'''
msgServeur, coordServeur = UDPClientSocket.recvfrom(1024)
print("Reply from server: ", msgServeur.decode("UTF-8"))
UDPClientSocket.close()
print("UDP Connection closed")
