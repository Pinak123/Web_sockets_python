import socket
import threading
import time

PORT = 5050
HEADER = 64
FORMAT = 'utf8'
# SERVER = '192.168.1.9'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR =(SERVER , PORT)
DISCONNECT_MESSAGE ="!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn , addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        msg_lngt = conn.recv(HEADER).decode(FORMAT)
        if msg_lngt:
            msg_lngt = int(msg_lngt)
            msg = conn.recv(msg_lngt).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Message Received".encode(FORMAT))

    conn.close()
        





def start():
    server.listen()
    print(f"[LISTENING] server is listning on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client , args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")  # start thread is already running so we do -1





print ("Starting the server")
start()
