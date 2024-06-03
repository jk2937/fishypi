import socket
import sys
import random
import time

HOST = ''  # Default localhost
PORT = int(sys.argv[1]) if len(sys.argv) >= 2 else 5555

udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for _ in range(5):  # Number of iterations specifying the duration of communication
    data = b'Hello World!' * random.randint(1, 10)  # Generate random length payload
    udp_client_socket.sendto(data, (HOST, PORT))
    print(f"Sent {len(data)} bytes to {HOST}:{PORT}")

    try:
        data, addr = udp_client_socket.recvfrom(4096)
        if len(data) > 0:
            print(f"Received {len(data)} bytes from {addr}, Data: '{data}'")

    except OSError:
        pass  # Ignore exceptions occurring during reception

    time.sleep(1 + random.uniform(0, 1))  # Random interval between transmissions

udp_client_socket.close()
