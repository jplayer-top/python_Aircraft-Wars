from Sprite import *


class GSpriteHeroOver(GSprite):
    def __init__(self, image_name, x, speed=1):
        GSprite.__init__(self, image_name, speed)
        self.rect.x = x
        self.rect.y = 700

    def update(self):
        self.rect.y -= 0
