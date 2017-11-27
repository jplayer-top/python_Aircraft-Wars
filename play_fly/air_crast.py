# coding=utf-8
import time
from pygame.locals import *
from SpriteHero import *
from SpriteBg import *
from SpriteHeroOver import *
from SpriteEnemy import *
from SpriteBullet import *

SCREEN_SIZE = pygame.Rect(0, 0, 480, 852)
CREATE_ENEMY_EVENT = pygame.USEREVENT
Bullet = pygame.USEREVENT+1
OVER = pygame.USEREVENT+2
screen = pygame.display.set_mode(SCREEN_SIZE.size, 0, 0)


def getff():
    print "sssssssssssssssssssssssssssss"


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

    groups_enemy = pygame.sprite.Group()
    groups_bullet = pygame.sprite.Group()
    groups_over = pygame.sprite.Group()

    # 初始化事件
    pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
    pygame.time.set_timer(Bullet, 500)
    pygame.time.set_timer(OVER, 200)
    a = True
    b = True
    is_boom = 0
    while True:
        click.tick(60)
        add_image(groups_bg)
        add_image(groups_hero)
        add_image(groups_enemy)
        add_image(groups_bullet)
        add_image(groups_over)
        pygame.sprite.groupcollide(groups_bullet, groups_enemy, True, True)
        enemys_list = pygame.sprite.spritecollide(hero, groups_enemy, True)
        if len(enemys_list) > 0:
            a = False
            hero.kill()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == CREATE_ENEMY_EVENT:
                if a:
                    enemy = GSpriteEnemy("./feiji/enemy0.png", random.randint(1, 4))
                    groups_enemy.add(enemy)
            elif event.type == OVER:
                if not a and b:     # 飞机boom
                    is_boom += 1
                    if is_boom < 5:
                        over = GSpriteHeroOver("./feiji/hero_blowup_n%s.png" % is_boom, hero.rect.x)
                        groups_over.add(over)

            elif event.type == Bullet:
                print "bullet"
                if a:
                    bullet = GSpriteBullet("./feiji/bullet.png", hero.rect.x + 40)
                    groups_bullet.add(bullet)
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    hero.is_to_left = -2
                    if hero.rect.x >= 430:
                        hero.rect.x = 420
                elif event.key == K_d or event.key == K_RIGHT:
                    hero.is_to_left = 2
                    if hero.rect.x <= -50:
                        hero.rect.x = -40
        if hero.rect.x < -50:
            hero.is_to_left = 0
        elif hero.rect.x > 430:
            hero.is_to_left = 0
        if a:
            hero.to_left(hero.is_to_left)
        pygame.display.update()


# 添加图片在屏幕上方!
def add_image(groups):
    groups.update()
    groups.draw(screen)


if __name__ == '__main__':
    main()
