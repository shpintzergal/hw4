import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_adress = ('127.0.0.1', 6116)
client_socket.connect(server_adress)

message = "hello, server!"
client_socket.send(message.encode())

data = client_socket.recv(1024)
if data:
    print(f"received: {data.decode()}")
