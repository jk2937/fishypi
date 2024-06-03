import pygame.midi

pygame.midi.init()

def print_devices():
    global device_count
    device_count = pygame.midi.get_count()
    for i in range(device_count):
        print(pygame.midi.get_device_info(i))

print_devices()

while True:
    for i in range(device_count):
        device_info = pygame.midi.get_device_info(i)
        device_is_input = device_info[2]
        if not device_is_input:
            continue
        print(i)
        print_devices()
        device = pygame.midi.Input(i)
        print('debug')
        if device.poll():
            print(device.read())
