import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_adress = ('127.0.0.1', 6116)
server_socket.bind(server_adress)

server_socket.listen(5)
print("очікуємо з'єднання")

while True:
    client_socket, client_adress = server_socket.accept()
    print("Client connected")
    data = client_socket.recv(1024)
    if data:
        print(f"received:{data.decode()}")
    message = "hello, client!"
    client_socket.send(message.encode())
