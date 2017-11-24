# coding=utf-8
import pygame


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
