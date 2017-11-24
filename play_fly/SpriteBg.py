from Sprite import *


class GSpriteBg(GSprite):

    def update(self):
        self.rect.y += 1
        if self.rect.y >= 852:
            self.rect.y = -852
