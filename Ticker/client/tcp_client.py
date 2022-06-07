import socket

SERVER_IP = '192.168.1.19'
SERVER_PORT = 65432

# msg = "list"
# msg = "BTC-USD"
# msg = "ETH-USD"
msg = "XRP-USD"
# msg = "ADA-USD"

TCPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPClientSocket.connect((SERVER_IP, SERVER_PORT))
print("TCP Connection open")

TCPClientSocket.sendall(msg.encode('UTF-8'))

# for i in range(1, 5):
#     TCPClientSocket.sendall("hello".encode('UTF-8'))
#     print(TCPClientSocket.recv(1024).decode('UTF-8'))
#     time.sleep(5)

'''REPLY'''
# response = TCPClientSocket.recv(1024).decode('UTF-8')
# if response == 200:
# print(response)

TCPClientSocket.send(b"")

TCPClientSocket.close()
print("TCP Connection closed")
