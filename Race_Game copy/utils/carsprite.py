import pygame, math, sys, time
from pygame.locals import *

class CarSprite(pygame.sprite.Sprite):
    MAX_FORWARD_SPEED = 10
    MAX_REVERSE_SPEED = 10
    ACCELERATION = 2
    TURN_SPEED = 10

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.position = position
        self.speed = self.direction = 0

        self.k_left = self.k_right = self.k_down = self.k_up = 0
    
    def update(self, deltat):
        #SIMULATION
        self.speed += (self.k_up + self.k_down)
        if self.speed > self.MAX_FORWARD_SPEED:
            self.speed = self.MAX_FORWARD_SPEED
        if self.speed < -self.MAX_REVERSE_SPEED:
            self.speed = -self.MAX_REVERSE_SPEED
        self.direction += (self.k_right + self.k_left)
        x, y = (self.position)
        rad = self.direction * math.pi / 180
        x += -self.speed*math.sin(rad)
        y += -self.speed*math.cos(rad)
        self.position = (x, y)
        self.image = pygame.transform.rotate(self.src_image, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    # utils for simple movement
    def move_right(self, down: bool):
        self.k_right = down * -5
    
    def move_left(self, down: bool):
        self.k_left = down * 5
    
    def move_up(self, down: bool):
        self.k_up = down * 2
    
    def move_down(self, down: bool):
        self.k_down = down * -2
