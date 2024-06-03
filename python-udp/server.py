import socket

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 5555  # Arbitrary non-privileged ports are > 1023

udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_socket.setblocking(False)  # Non-blocking mode
udp_server_socket.bind((HOST, PORT))
print(f"Echo server started on {HOST}:{PORT}")

while True:
    try:
        data, addr = udp_server_socket.recvfrom(4096)
        if len(data) > 0:
            print(data.decode())
            udp_server_socket.sendto(data, addr)

    except BlockingIOError:
        pass  # No data was ready to read, continue to next iteration
