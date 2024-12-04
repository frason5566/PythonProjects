import pygame as pg
from util import *
from random import randint

class Paddle(pg.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pg.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pg.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x <0:
            self.rect.x  = 0
    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x > SCREEN_SIZE[1] :
            self.rect.x  = SCREEN_SIZE[1] -1

class Brick(pg.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pg.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pg.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

class Ball(pg.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pg.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pg.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [randint(4, 8), randint(-8, 8)]
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)
