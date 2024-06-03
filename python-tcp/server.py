from socket import *

server_ip = 'localhost'
server_port = 7000

_socket = socket(AF_INET, SOCK_STREAM)
_socket.bind((server_ip, server_port))

_socket.listen(1)
print('Server listening on ' + str(server_ip) + ':' + str(server_port))

while True:
    client_socket, client_address = _socket.accept()
    print('Connection established from ' + str(client_address[0]) + ':' + str(client_address[1]))

    while True:
        try:
            data = client_socket.recv(1024)
            print('Recieved data: ' + data.decode())
        except Exception as e:
            print(e)
            break

#client_socket.send('Hello, client!'.encode())

#client_socket.close()
_socket.close()
