# coding=utf-8
import random

from SpriteHero import *
from SpriteBg import *
from SpriteEnemy import *

SCREEN_SIZE = pygame.Rect(0, 0, 480, 852)
CREATE_ENEMY_EVENT = pygame.USEREVENT
screen = pygame.display.set_mode(SCREEN_SIZE.size, 0, 0)


def main():
    pygame.init()
    click = pygame.time.Clock()
    # 初始化屏幕背景
    groups_bg = pygame.sprite.Group()
    bg = GSpriteBg("./feiji/background.png")
    bg1 = GSpriteBg("./feiji/background.png")
    bg1.rect.y = -852
    groups_bg.add(bg, bg1)
    # 初始化英雄
    groups_hero = pygame.sprite.Group()
    hero = GSpriteHero("./feiji/hero1.png")
    hero.rect.x = 190
    hero.rect.y = 700
    groups_hero.add(hero)
    # 初始化敌机事件
    pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
    groups_enemy = pygame.sprite.Group()

    while True:
        click.tick(60)
        add_image(groups_bg)
        add_image(groups_hero)
        add_image(groups_enemy)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = GSpriteEnemy("./feiji/enemy0.png", random.randint(0, 3))
                groups_enemy.add(enemy)
        pygame.display.update()


# 添加图片在屏幕上方
def add_image(groups):
    groups.update()
    groups.draw(screen)


if __name__ == '__main__':
    main()
