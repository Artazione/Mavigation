import pygame
import pyautogui
import webbrowser
import math

pygame.init()

# Set the width and height of the screen (width, height).
screen = pygame.display.set_mode((400, 600))

pygame.display.set_caption("gamepad")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates.
clock = pygame.time.Clock()

# Initialize the joysticks.
pygame.joystick.init()

# -------- Main Program Loop -----------
while not done:
    #
    # EVENT PROCESSING STEP
    #
    # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
    # JOYBUTTONUP, JOYHATMOTION
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

# Get count of joysticks.
    joystick_count = pygame.joystick.get_count()

    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

axes = joystick.get_numaxes()

    # For each joystick:
for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()



for i in range(axes):
            axis = joystick.get_axis(i)
            xx=0
            yy=0
            if i==0:
                xx=axis*1366
                pyautogui.moveRel(xx/10,0,duration=1)
            elif i==1:
                yy=axis*768
                pyautogui.moveRel(0,yy/10,duration=1)
            elif i==3 and axis < 0.2:
                pyautogui.hscroll((2))
            elif i==3 and axis > 0.2:
                pyautogui.hscroll(-(2))
            elif i==4 and axis < 0.2:
                pyautogui.scroll((2))
            elif i==4 and axis > 0.2:
                pyautogui.scroll(-(2))
            elif i==2 and (axis!=-1 and axis!=0):
                pyautogui.hotkey('ctrl','tab')
                print("aaaa")
            elif i==5 and (axis!=-1 and axis!=0):
                pyautogui.hotkey('ctrl','shift','tab')

clock.tick(20)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()


