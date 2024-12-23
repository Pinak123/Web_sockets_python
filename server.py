import socket

PORT = 5050
HEADER = 64
FORMAT = 'utf8'
DISCONNECT_MESSAGE ="!DISCONNECT"
SERVER = "192.168.1.9"
ADDR =(SERVER , PORT)


client =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_lnt = len(message)
    send_lnt = str(msg_lnt).encode(FORMAT)
    send_lnt+= b' ' * (HEADER - len(send_lnt))
    client.send(send_lnt)  
    client.send(message)
    print(client.recv(256).decode('utf8'))
send("Hey there")
