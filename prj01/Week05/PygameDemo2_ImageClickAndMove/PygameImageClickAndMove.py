import pygame
import random
import sys

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

ballImage = pygame.image.load('images/ball.png')

ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            if ballRect.collidepoint(event.pos):
                ballX = random.randrange(MAX_WIDTH)
                ballY = random.randrange(MAX_HEIGHT)
                ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

        if event.type == pygame.KEYUP:
            ballX = WINDOW_HEIGHT / 2
            ballY = WINDOW_WIDTH / 2
            break

    window.fill(BLACK)

    window.blit(ballImage, (ballX, ballY))    

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
