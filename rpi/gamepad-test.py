import sys
import pygame

def main():
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
                    print("Button " + str(event.dict["button"]) + " Pressed")
                if event.type == pygame.JOYBUTTONUP: 
                    print("Button " + str(event.dict["button"]) + " Released")
                if event.type == pygame.JOYAXISMOTION:
                    if event.dict["axis"] == 1:
                        if event.dict["value"] < -0.25:
                            print("Joy Y Moved Up")
                        elif event.dict["value"] > 0.25:
                            print("Joy Y Moved Down")
                        else:
                            print("Joy Y Neutral")
                    if event.dict["axis"] == 0:
                        if event.dict["value"] < -0.25:
                            print("Joy X Moved Left")
                        elif event.dict["value"] > 0.25:
                            print("Joy X Moved Right")
                        else:
                            print("Joy X Neutral")


                if event.type == pygame.JOYHATMOTION:
                    print("Joy Hat Moved")
                    print(event)

if __name__ == "__main__":
    main()
