import pygame
from pygame.locals import *
import sys
import random
from Ball import *
from SimpleText import *
from SimpleButton import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
oFrameCountLabel = SimpleText(window, (30, 20),
                              'Time', WHITE)
oFrameCountDisplay = SimpleText(window, (220, 20), '', WHITE)
oRestartButton = SimpleButton(window, (280, 60),
                              'images/restartUp.png', 'images/restartDown.png')
frameCounter = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oRestartButton.handleEvent(event):
            frameCounter = 0

    oBall.update()
    frameCounter += clock.tick_busy_loop(1000) / 1000

    milliseconds = int(frameCounter * 1000)
    seconds = milliseconds // 1000
    minutes = seconds // 60
    hours = minutes // 60

    time_str = f'{hours:02}:{minutes % 60:02}:{seconds % 60:02}.{milliseconds % 1000:03}'
    oFrameCountDisplay.setValue(time_str)

    window.fill(BLACK)

    oBall.draw()
    oFrameCountLabel.draw()
    oFrameCountDisplay.draw()
    oRestartButton.draw()

    pygame.display.update()