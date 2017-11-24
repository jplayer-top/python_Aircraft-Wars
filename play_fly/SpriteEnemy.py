import random

from Sprite import *


class GSpriteEnemy(GSprite):
    def __init__(self, image_name, speed=1):
        GSprite.__init__(self, image_name, speed)
        self.speed = speed
        self.rect.y = 50
        self.rect.x = random.randint(0, 430)

    def update(self):
        if self.rect.y > 700:
            self.kill()

        self.rect.y += self.speed
