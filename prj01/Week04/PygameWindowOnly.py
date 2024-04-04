
import pygame
import sys

BLOSSOM = (255, 192, 203)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()
    
    window.fill(BLOSSOM)
    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)  
