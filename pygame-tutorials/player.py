import pygame
from pygame.locals import *
from main import *

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super.__init__()
        self.image = pygame.image.load('Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    def update(self):
        pressed_keys = pygame.key.get_pressed()

        # if pressed_keys[K_UP]:
        #     self.rect.move_ip(0, -5) #it's negative cause the window grid increases downwards
        # if pressed_keys[K_DOWN]:
        #     self.rect.move_ip(0,5)

        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0) #negative because the window grid increases left to right
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)