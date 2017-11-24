import random

from Sprite import *


class GSpriteEnemy(GSprite):
    def __init__(self, image_name, speed=1):
        GSprite.__init__(self, image_name, speed)
        self.speed = speed
        self.rect.x = random.randint(0, 430)
        self.rect.y = -50
        print self.rect

    def update(self):
        if self.rect.y > 900:
            self.kill()

        self.rect.y += self.speed
