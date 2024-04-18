import pygame
from pygame.locals import *
import sys

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

ballImage = pygame.image.load('images/ball.png')
manImage = pygame.image.load('images/IMG_6767.jpg')

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(BLACK)

    window.blit(ballImage, (100, 200))
    window.blit(manImage, (200, 200))
    window.blit(ballImage, (300, 200))

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)