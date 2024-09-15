import pygame,sys
from pygame.locals import *
from player import *

pygame.init()

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500
BLACK = pygame.color.Color(0,0,0)


window = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))

fps = pygame.time.Clock()
fps.tick(60) #sets the fps to 60

window.fill(BLACK)
pygame.display.set_caption("Space Invaders")

player = Player()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

