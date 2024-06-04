import pygame.midi

pygame.midi.init()

device_id = 5

global device_count
device_count = pygame.midi.get_count()
for i in range(device_count):
    device_info = pygame.midi.get_device_info(i)
    if device_info[2] == 1 and b"Midi Through" in device_info[1]:
        device_id = i

device = pygame.midi.Input(device_id)

while True:
    if device.poll():
        print(device.read(1)[0])
