
import socket
import sys
import random
import time

HOST = '192.168.1.139'  
PORT = 5555

udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

import pygame.midi

pygame.midi.init()

device_id = None

global device_count
device_count = pygame.midi.get_count()
for i in range(device_count):
    device_info = pygame.midi.get_device_info(i)
    if device_info[2] == 1 and b"Midi Through" in device_info[1]:
        device_id = i

device = pygame.midi.Input(device_id)

while True:
    if device.poll():
        message = device.read(1)[0]
        print(message)
        if message[0][0] == 144:
            print("Note On")
            pc = message[0][1] % 12
            print(f"Pitch Class: {pc}")
            if pc == 0:
                udp_client_socket.sendto("A Negative".encode(), (HOST, PORT))
            if pc == 1:
                udp_client_socket.sendto("A Positive".encode(), (HOST, PORT))
            if pc == 2:
                udp_client_socket.sendto("B Negative".encode(), (HOST, PORT))
            if pc == 3:
                udp_client_socket.sendto("B Positive".encode(), (HOST, PORT))
        if message[0][0] == 128:
            print("Note Off")
            pc = message[0][1] % 12
            print(f"Pitch Class: {pc}")
            if pc == 0:
                udp_client_socket.sendto("A Neutral".encode(), (HOST, PORT))
            if pc == 1:
                udp_client_socket.sendto("A Neutral".encode(), (HOST, PORT))
            if pc == 2:
                udp_client_socket.sendto("B Neutral".encode(), (HOST, PORT))
            if pc == 3:
                udp_client_socket.sendto("B Neutral".encode(), (HOST, PORT))
        if message[0][0] != 144 and message[0][0] != 128 and message[0][1] == 120:
            print("All Notes Off")
            udp_client_socket.sendto("A Neutral".encode(), (HOST, PORT))
            udp_client_socket.sendto("B Neutral".encode(), (HOST, PORT))
    time.sleep(0.001)


udp_client_socket.close()
