# coding=utf-8
import pygame
import time, sched, random
from pygame.locals import *
from asdas import *


class Bullet(object):
    def __init__(self, screen, x, y):
        self.bullet = pygame.image.load("./feiji/bullet.png")
        self.screen = screen
        self.x = x
        self.y = y
        pass

    def to_display(self):
        self.y -= 5
        self.screen.blit(self.bullet, (self.x + 38, self.y))


class EBullet(object):
    def __init__(self, screen, x, y):
        self.bullet = pygame.image.load("./feiji/bullet1.png")
        self.screen = screen
        self.x = x
        self.y = y
        pass

    def to_display(self):
        self.y += 2
        self.screen.blit(self.bullet, (self.x + 25, self.y + 15))


class HeroPlane(object):
    def __init__(self, screen):
        self.x = 190
        self.y = 700
        self.a = 0
        self.cur = 0
        self.screen = screen
        self.hero = pygame.image.load("./feiji/hero1.png")
        self.bullets = []
        pass

    def to_move(self):
        self.x += self.a
        if self.x <= -50:
            self.a = 0
        elif self.x >= 420:
            self.a = 0

    def to_left(self):
        self.a = -5

    def to_right(self):
        self.a = +5

    def to_bullet(self, cur_x, cur_y):
        self.cur += 1
        if self.cur % 10 == 0:
            self.bullets.append(Bullet(self.screen, cur_x, cur_y))

    def to_display(self):
        self.screen.blit(self.hero, (self.x, self.y))
        print self.bullets.__len__()
        for bullet in self.bullets:
            if bullet.y < 0:
                self.bullets.remove(bullet)
            bullet.to_display()


class Enemy(object):
    def __init__(self, screen):
        self.screen = screen
        self.enemys = []
        self.bullets = []
        self.is_right = True
        self.cur = 0
        for i in range(0, 5):
            self.add_enemy()

    def add_enemy(self):
        enemy_map = {}
        enemy = pygame.image.load("./feiji/enemy0.png")
        enemy_map["enemy"] = enemy
        enemy_map["x"] = random.randint(0, 480)
        enemy_map["y"] = 0
        enemy_map["r_y"] = random.randint(1, 4)
        enemy_map["is_r"] = True
        self.enemys.append(enemy_map)

    def to_display(self):
        for i in self.enemys:
            if i["is_r"]:
                i["x"] -= 5
            else:
                i["x"] += 5
            if i["x"] > 430:
                i["is_r"] = True
            elif i["x"] < 0:
                i["is_r"] = False

            i["y"] += i["r_y"]
            if i["y"] > 700:
                self.enemys.remove(i)
                self.add_enemy()
            self.screen.blit(i["enemy"], (i["x"], i["y"]))
            self.cur += 1
            a = (random.randint(1, 100))
            if a == 10:
                self.bullets.append(EBullet(self.screen, i["x"], i["y"]))
            for bullet in self.bullets:
                if bullet.y > 700:
                    self.bullets.remove(bullet)
                bullet.to_display()


def main():
    pygame.init()
    screen = pygame.display.set_mode((480, 852), 0, 32)
    game = pygame.image
    bg = game.load("./feiji/background.png")
    big_enemy = GameSprite("./feiji/enemy1.png")
    ggg = pygame.sprite.Group(big_enemy)
    a_hero = HeroPlane(screen)
    e_enemy = Enemy(screen)
    cur_y = 670
    while True:

        screen.blit(bg, (0, 0))
        a_hero.to_display()
        e_enemy.to_display()
        ggg.update()
        ggg.draw(screen)
        for event in pygame.event.get():
            # 判断是否是点击了退出按钮
            if event.type == QUIT:
                print("exit")
                pygame.quit()
                exit()
            # 判断是否是按下了键
            elif event.type == KEYDOWN:
                # 检测按键是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    a_hero.to_left()
                # 检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    a_hero.to_right()

                # 检测按键是否是空格键
                elif event.key == K_SPACE:
                    print a_hero.x
        a_hero.to_move()
        a_hero.to_bullet(a_hero.x, cur_y)
        pygame.display.update()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
