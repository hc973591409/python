import random

import pygame

# 全局变量保存屏幕大小位置
SCREEN_SIZE = pygame.Rect(0, 0, 480, 852)
FRAME_RATE = 60
# 自定义敌机出场事件
ENEMY_APPARE = pygame.USEREVENT
BULLET_SHOOT = pygame.USEREVENT+1


class PlaneSprite(pygame.sprite.Sprite):
    '''游戏精灵组'''

    def __init__(self, img_name, speed=1):
        '''初始化各种属性'''
        # 调用父类的初始化方法
        super().__init__()
        # 加载图像
        # 名字是固定的，不能改变
        self.image = pygame.image.load(img_name)

        # 返回值为img的位置(0,0) 宽高（图像宽高）
        self.rect = self.image.get_rect()
        print(self.rect)
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        # 默认垂直方向移动


class BackGroud(PlaneSprite):
    def __init__(self, flag=False):
        # 调用父类方法
        super().__init__("./feiji/background.png")
        self.__flag = flag
        # 设置初始位置
        if not self.__flag:
            # print("我在底部 %d" %self.rect.bottom)
            self.rect.bottom = SCREEN_SIZE.bottom
        else:
            # print("我在顶部 %d" %self.rect.bottom)
            self.rect.bottom = 0

    def update(self):
        super().update()
        # 如果飞出屏幕，就重新回到屏幕顶部
        if self.rect.top == SCREEN_SIZE.bottom:
            print("我已经被召唤回来")
            self.rect.bottom = 0


class EnameyPlane(PlaneSprite):
    def __init__(self):
        # 随机速度
        self.speed = random.randint(1, 3)
        super().__init__('feiji/enemy-1.gif', self.speed)
        self.rect.bottom = 0
        # 随机位置
        self.rect.left = random.randint(0, SCREEN_SIZE.width-self.rect.width)

    def update(self):
        super().update()
        if self.rect.top == SCREEN_SIZE.bottom:
            print("被kill了")
            self.kill()


class HeroPlane(PlaneSprite):
    def __init__(self, speed=0):
        self.speed = speed
        super().__init__('./feiji/hero.gif', self.speed)
        self.rect.bottom = SCREEN_SIZE.bottom - 120
        self.rect.centerx = SCREEN_SIZE.centerx
        # 创建子弹精灵组
        self.bullte_group = pygame.sprite.Group()

    def update(self):
        # 这里父类方法不能满足英雄，我们需要重写父类方法
        self.rect.x += self.speed
        if self.rect.right >= SCREEN_SIZE.right:
            self.rect.right = SCREEN_SIZE.right

        if self.rect.left <= SCREEN_SIZE.left:
            self.rect.left = SCREEN_SIZE.left

    def fire(self):
        for i in range(0, 3):
            bullet = Bullet()
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.bottom = self.rect.top - (i*25)
            self.bullte_group.add(bullet)


class Bullet(PlaneSprite):
    def __init__(self):
        super().__init__("./feiji/bullet.png", -3)

    def update(self):
        super().update()
        if self.rect.bottom <= 0:
            print("子弹悲剧了")
            self.kill()
