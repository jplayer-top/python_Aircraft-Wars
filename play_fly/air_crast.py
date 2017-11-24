# coding=utf-8
from pygame.locals import *
from SpriteHero import *
from SpriteBg import *
from SpriteEnemy import *
from SpriteBullet import *

SCREEN_SIZE = pygame.Rect(0, 0, 480, 852)
CREATE_ENEMY_EVENT = pygame.USEREVENT
Bullet = 31
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

    groups_enemy = pygame.sprite.Group()
    groups_bullet = pygame.sprite.Group()

    # 初始化事件
    pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
    pygame.time.set_timer(Bullet, 500)

    while True:
        click.tick(60)
        add_image(groups_bg)
        add_image(groups_hero)
        add_image(groups_enemy)
        add_image(groups_bullet)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = GSpriteEnemy("./feiji/enemy0.png", random.randint(1, 4))
                groups_enemy.add(enemy)
            elif event.type == Bullet:
                print "bullet"
                bullet = GSpriteBullet("./feiji/bullet.png", hero.rect.x + 40)
                groups_bullet.add(bullet)
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    hero.is_to_left = -2
                elif event.key == K_d or event.key == K_RIGHT:
                    hero.is_to_left = 2
        if hero.rect.x <= -50:
            hero.is_to_left = 0
        elif hero.rect.x >= 430:
            hero.is_to_left = 0
        hero.to_left(hero.is_to_left)
        pygame.display.update()


# 添加图片在屏幕上方!
def add_image(groups):
    groups.update()
    groups.draw(screen)


if __name__ == '__main__':
    main()
