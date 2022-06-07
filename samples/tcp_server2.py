import socket

LISTEN_IP = "192.168.1."
LISTEN_PORT = 65432

TCPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPServerSocket.bind((LISTEN_IP, LISTEN_PORT))

TCPServerSocket.listen()

while True:
    print("[TCP] Waiting for connection")

    conn, addr = TCPServerSocket.accept()

    done = False
    while not done:
        data = conn.recv(1024).decode("UTF-8")
        if data != "":
            print(data)
            conn.sendall(("[TCP] ACK : " + data).encode("UTF-8"))
        else:
            print("[TCP] connection closed")
            done = True
    conn.close()
