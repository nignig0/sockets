import pygame
from pygame.locals import *
from main import *

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self):
        super.__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40),0) 

    def move(self):
        self.rect.move_ip(0,10) #we are moving down
        if self.rect.bottom > 600: #if we move down and we're 'downer' than the screen height
            self.rect.top = 0 #move back up
            self.rect.center = (random.randint(30, 370), 0) #center at some random location

    def draw(self, surface):
        surface.blit(self.image, self.rect)