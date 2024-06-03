import sys
import pygame
import socket
import random
import time

HOST = '192.168.1.227'  # Default localhost
PORT = int(sys.argv[1]) if len(sys.argv) >= 2 else 5555

udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

pygame.init()

# Initialize joystick subsystem
pygame.joystick.init()

# Get number of active joysticks
num_joysticks = pygame.joystick.get_count()
print(f"Number of joysticks found: {num_joysticks}")

if num_joysticks > 0:
    # Set up first joystick
    js = pygame.joystick.Joystick(0)
    js.init()

    while True:
        events = pygame.event.get()
        
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                message = "Button " + str(event.dict["button"]) + " Pressed"
                print(message)
                udp_client_socket.sendto(message.encode(), (HOST, PORT))
            if event.type == pygame.JOYBUTTONUP: 
                message = "Button " + str(event.dict["button"]) + " Released"
                print(message)
                udp_client_socket.sendto(message.encode(), (HOST, PORT))
            if event.type == pygame.JOYAXISMOTION:
                if event.dict["axis"] == 1:
                    if event.dict["value"] < -0.25:
                        message = "Joy Y Moved Up"
                        print(message)
                        udp_client_socket.sendto(message.encode(), (HOST, PORT))
                    elif event.dict["value"] > 0.25:
                        message = "Joy Y Moved Down"
                        print(message)
                        udp_client_socket.sendto(message.encode(), (HOST, PORT))
                    else:
                        message = "Joy Y Neutral"
                        print(message)
                        udp_client_socket.sendto(message.encode(), (HOST, PORT))
                if event.dict["axis"] == 0:
                    if event.dict["value"] < -0.25:
                        message = "Joy X Moved Left"
                        print(message)
                        udp_client_socket.sendto(message.encode(), (HOST, PORT))
                    elif event.dict["value"] > 0.25:
                        message = "Joy X Moved Right"
                        print(message)
                        udp_client_socket.sendto(message.encode(), (HOST, PORT))
                    else:
                        message = "Joy X Neutral"
                        print(message)
                        udp_client_socket.sendto(message.encode(), (HOST, PORT))


            if event.type == pygame.JOYHATMOTION:
                message = "Joy Hat Moved"
                print(message)
                udp_client_socket.sendto(message.encode(), (HOST, PORT))

udp_client_socket.close()
