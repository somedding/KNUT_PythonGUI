
import pygame
from pygame.locals import *
import sys
import pygwidgets
from Game import *

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

background = pygwidgets.Image(window, (0, 0),
                            'images/background.png')
newGameButton = pygwidgets.TextButton(window, (20, 530),
                            'New Game', width=100, height=45)
higherButton = pygwidgets.TextButton(window, (540, 520),
                            'Higher', width=120, height=55)
lowerButton = pygwidgets.TextButton(window, (340, 520),
                            'Lower', width=120, height=55)
quitButton = pygwidgets.TextButton(window, (880, 530),
                            'Quit', width=100, height=45)
toZeroButton = pygwidgets.TextButton(window, (880, 100),
                            'To zero', width=120, height=55)
oGame = Game(window)

while True:
    for event in pygame.event.get():

        if ((event.type == QUIT) or
            ((event.type == KEYDOWN) and (event.key == K_ESCAPE)) or
            (quitButton.handleEvent(event))):
            pygame.quit()
            sys.exit()

        if newGameButton.handleEvent(event):
            oGame.reset()
            lowerButton.enable()
            higherButton.enable()

        if higherButton.handleEvent(event):
            gameOver = oGame.hitHigherOrLower(HIGHER)
            newGameButton.disable()
            if gameOver:
                higherButton.disable()
                lowerButton.disable()
                newGameButton.enable()

        if lowerButton.handleEvent(event):
            gameOver = oGame.hitHigherOrLower(LOWER)
            newGameButton.disable()
            if gameOver:
                higherButton.disable()
                lowerButton.disable()
                newGameButton.enable()

        if toZeroButton.handleEvent(event):
            oGame.toZero()

    background.draw()

    oGame.draw()
    # Draw remaining user interface components
    newGameButton.draw()
    higherButton.draw()
    lowerButton.draw()
    quitButton.draw()
    toZeroButton.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
