from Sprite import *


class GSpriteHero(GSprite):
    def __init__(self, image_name, speed=1):
        super(GSpriteHero, self).__init__(image_name, speed)
        self.is_to_left = 0

    def update(self):
        self.rect.y -= 0

    def to_left(self, value):
        self.rect.x += value

