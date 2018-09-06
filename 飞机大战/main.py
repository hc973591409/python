import pygame
from pygame.locals import *

from plane_sprites import *


class GamePlane(object):
    '''游戏主框架类'''

    def __init__(self):
        '''初始化属性'''
        # 游戏屏幕
        self.__screen = pygame.display.set_mode(SCREEN_SIZE.size)
        # 设置窗口标题
        pygame.display.set_caption('胡超开发的飞机大战游戏')

        # 游戏循环时钟
        self.__clock = pygame.time.Clock()

        # 自定义事件，事件定时器
        pygame.time.set_timer(ENEMY_APPARE, 1000)
        pygame.time.set_timer(BULLET_SHOOT, 500)

        self.enemy_group = pygame.sprite.Group()

        # 创建精灵和精灵组
        self.__create_sprites()

    def __create_sprites(self):
        # 创建，屏幕背景精灵精灵组
        self.bg_sprite1 = BackGroud()
        self.bg_sprite2 = BackGroud(flag=True)
        self.bg_group = pygame.sprite.Group(self.bg_sprite1, self.bg_sprite2)

        # 创建，英雄以及英雄精灵组
        self.hero_sprite = HeroPlane()
        self.hero_group = pygame.sprite.Group(self.hero_sprite)

    def __update_sprite(self):
        # 更新，屏幕背景精灵精灵组
        self.bg_group.update()
        self.bg_group.draw(self.__screen)

        # 更新，英雄以及英雄精灵组
        self.hero_group.update()
        self.hero_group.draw(self.__screen)

        # 更新，敌机以及敌机精灵组
        self.enemy_group.update()
        self.enemy_group.draw(self.__screen)

        self.hero_sprite.bullte_group.update()
        self.hero_sprite.bullte_group.draw(self.__screen)

        pygame.display.update()

    def start_game(self):
        while True:
            # 设置游戏循环
            # 事件监听
            self.__event_handler()

            # 设置时钟
            self.__clock.tick(FRAME_RATE)
            # 更新游戏精灵精灵组
            self.__update_sprite()
            # 碰撞检测
            self.__check_dead()

    def __check_dead(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(
            self.hero_sprite.bullte_group, self.enemy_group, True, True)
        # 敌机撞毁英雄.返回一个列表，里面是碰撞单位的精灵
        enemies = pygame.sprite.spritecollide(
            self.hero_sprite, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero_sprite.kill()
            print("U lose")
            self.game_over()

    def __event_handler(self):
        # 遍历事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("您已经退出")
                # 释放pygame的内存
                pygame.quit()
                exit()

            elif event.type == ENEMY_APPARE:
                # 一秒增加一个敌机
                enemy = EnameyPlane()
                self.enemy_group.add(enemy)

            elif event.type == BULLET_SHOOT:
                self.hero_sprite.fire()
        # 使用键盘提供的方法 返回值为按键列表，判断按键是什么
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_a]:
            self.hero_sprite.speed = 3

        elif key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_d]:
            self.hero_sprite.speed = -3
        else:
            self.hero_sprite.speed = 0

    @staticmethod
    def game_over():
        print("游戏结束")
        pygame.quit()
        exit()


def main():
    player = GamePlane()
    player.start_game()


if __name__ == '__main__':
    main()
