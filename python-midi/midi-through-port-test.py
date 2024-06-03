import pygame.midi

pygame.midi.init()

device = pygame.midi.Input(1)

while True:
    if device.poll():
        print(device.read(1)[0])
