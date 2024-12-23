import socket
import threading
import time

PORT = 5050
# SERVER = '192.168.1.9'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR =(SERVER , PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn , addr):
    pass


def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client , args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")  # start thread is already running so we do -1
        



print ("Starting the server")
start()
