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
            print(f"Pitch Class: {message[0][1] % 12}")
        if message[0][0] == 128:
            print("Note Off")
            print(f"Pitch Class: {message[0][1] % 12}")
        if message[0][0] != 144 and message[0][0] != 128 and message[0][1] == 120:
            print("All Notes Off")
