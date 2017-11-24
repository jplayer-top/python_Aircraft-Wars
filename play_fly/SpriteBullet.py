import random

from Sprite import *


class GSpriteBullet(GSprite):
    def __init__(self, image_name, hero_x, speed=5):
        GSprite.__init__(self, image_name, speed)
        self.speed = speed
        self.rect.x = hero_x
        self.rect.y = 680

    def update(self):
        if self.rect.y < 0:
            self.kill()
        self.rect.y -= self.speed
