import pygame
import sys
from pygame.locals import *
import math
import random

# Set up the constants
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_SHAPES = 10
FIRST_SHAPE = 'first'
SECOND_SHAPE = 'second'

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
clock = pygame.time.Clock()

class Circle:
    def __init__(self, surface):
        self.surface = surface
        self.radius = random.randint(20, 50)  # Random radius between 20 and 50
        self.color = random.choice((RED, GREEN, BLUE))
        self.x = random.randint(0, WINDOW_WIDTH - 2 * self.radius)  # Random x position within window
        self.y = random.randint(0, WINDOW_HEIGHT - 2 * self.radius)  # Random y position within window

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x + self.radius, self.y + self.radius), self.radius, 0)

    def clickedInside(self, pos):
        return math.sqrt((pos[0] - (self.x + self.radius))**2 + (pos[1] - (self.y + self.radius))**2) <= self.radius

shapesList = []
for i in range(N_SHAPES):
    shape = Circle(window)
    shapesList.append(shape)

whichShape = FIRST_SHAPE

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            for shape in shapesList:
                if shape.clickedInside(event.pos):
                    print('Clicked on', whichShape, 'shape.')

                    if whichShape == FIRST_SHAPE:
                        firstShape = shape
                        whichShape = SECOND_SHAPE

                    elif whichShape == SECOND_SHAPE:
                        secondShape = shape
                        # User has chosen 2 shapes, let's compare
                        if firstShape.radius == secondShape.radius:
                            print('Shapes are the same size.')
                        elif firstShape.radius < secondShape.radius:
                            print('First shape is smaller than second shape.')
                        else:
                            print('First shape is larger than second shape.')
                        whichShape = FIRST_SHAPE

    # Clear the window and draw all shapes
    window.fill(WHITE)
    for shape in shapesList:
        shape.draw()

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
