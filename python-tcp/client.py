from socket import *

server_ip = 'localhost'
server_port = 7000

_socket = socket(AF_INET, SOCK_STREAM)

_socket.connect((server_ip, server_port))

_socket.send('Hello, server!'.encode())

data = _socket.recv(1024)

_socket.close()

print('Recieved data: ' + data.decode())
