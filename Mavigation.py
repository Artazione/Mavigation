import pygame
import pyautogui
import webbrowser
import math

BLACK = pygame.Color('black')
WHITE = pygame.Color('white')

pyautogui.FAILSAFE = False

class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def tprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


pygame.init()

#Defini la hauteur et la largeur de l'affichage(largeur, hauteur).
screen = pygame.display.set_mode((400, 600))

pygame.display.set_caption("Manette")

done = False

# Defini la fréquence de rafraichissement
clock = pygame.time.Clock()

# Initialise les joysticks.
pygame.joystick.init()

# Preparation pour l'affichage
textPrint = TextPrint()

# -------- Boucle du programme -----------
while not done:
    #
    # Etape des evenements:
    #
    # Action possible sur les joysticks: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN, JOYBUTTONUP, JOYHATMOTION.
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

    #
    # Apparition de l'affichage
    #
    # Rempli l'affichage de blanc, a faire avant les autres commandes ou elle seront effaces par cette commande
    screen.fill(WHITE)
    textPrint.reset()

    # Compte les joysticks.
    joystick_count = pygame.joystick.get_count()

    textPrint.tprint(screen, "Nombre de joysticks: {}".format(joystick_count))
    textPrint.indent()

    # Pour chaque joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        textPrint.tprint(screen, "Joystick {}".format(i))
        textPrint.indent()

        # Recupere le nom du périphérique.
        name = joystick.get_name()
        textPrint.tprint(screen, "Nom du peripherique: {}".format(name))

        # Les axes des joysticks fonctionnent par paires : haut/bas et gauche/droite
        axes = joystick.get_numaxes()
        textPrint.tprint(screen, "Nombre  d'axes: {}".format(axes))
        textPrint.indent()

        for i in range(axes):
            axis = joystick.get_axis(i)
            textPrint.tprint(screen, "Axe {} valeur: {:>6.3f}".format(i, axis))
            xx=0
            yy=0
            if i==3 and axis <= -0.9:
                pyautogui.scroll(100)
            elif i==3 and axis >=0.9:
                pyautogui.scroll(-100)
            elif i==3 and axis <= -0.5:
                pyautogui.scroll(50)
            elif i==3 and axis >=0.5:
                pyautogui.scroll(-50)
            elif i==3 and axis <= -0.2:
                pyautogui.scroll(20)
            elif i==3 and axis >=0.2:
                pyautogui.scroll(-20)
            
        textPrint.unindent()

        buttons = joystick.get_numbuttons()
        textPrint.tprint(screen, "Nombre de boutons: {}".format(buttons))
        textPrint.indent()

        for i in range(buttons):
            button = joystick.get_button(i)
            textPrint.tprint(screen,
                             "Button {:>2} value: {}".format(i, button))
            if i==8 and button==1:
                webbrowser.open("https://google.com/",2)
            elif i==4 and button==1:
                pyautogui.click()
            elif i==0 and button==1:
                pyautogui.click(button="left")
 
        textPrint.unindent()

        hats = joystick.get_numhats()
        textPrint.tprint(screen, "Nombre de boutons de la croix directionnel: {}".format(hats))
        textPrint.indent()

        # Valeur de la croix directionnel, binaire : soit pressé ou non (1 ou 0, format :(x, y)).
        for i in range(hats):
            hat = joystick.get_hat(i)
            textPrint.tprint(screen, "Boutton {} valeur: {}".format(i, str(hat)))
        textPrint.unindent()

        textPrint.unindent()

    #
    # Tout code de dessin doit etre au dessus de ce commentaire
    #

    # Met a jour la fenetre avec ce que l'on a dessine
    pygame.display.flip()

    #Limite a 20 images par seconde.
    clock.tick(20)

# Ferme la fenetre et le programme.
pygame.quit()