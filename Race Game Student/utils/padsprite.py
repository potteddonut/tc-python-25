import pygame, math, sys, time
from pygame.locals import *

class PadSprite(pygame.sprite.Sprite):
    normal = pygame.image.load('images/race_pads.png')
    hit = pygame.image.load('images/collision.png')
    
    def __init__(self, position):
        super(PadSprite, self).__init__()
        self.rect = pygame.Rect(self.normal.get_rect())
        self.rect.center = position
        self.image = self.normal

    def update(self, hit_list):
        if self in hit_list:
            self.image = self.hit
        else:
            self.image = self.normal