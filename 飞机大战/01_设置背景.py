import time

import pygame
from pygame.locals import *


'''
1.快速实现界面搭建工作
'''


def main():

    pygame.init()
    # 1. 创建窗口 和背景图一样大(480,852)高宽大小，0，32是规定的
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 2. 创建一个背景图片，加载到图片资源
    background = pygame.image.load('./feiji/background.png')
    hero = pygame.image.load('feiji/hero1.png')
    x = 150
    y = 700
    while True:
        # 防止加载的图片在0，0坐标点
        screen.blit(background, (0, 0))
        screen.blit(hero, (x, y))
        # 测试移动是否正常
        # x+=10
        # y-=10
        # 更新屏幕显示内容
        pygame.display.update()

        # 获取事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("已推出")
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                # 只能检测按下事件，不顺滑
                if event.key == K_a or event.key == K_LEFT:
                    x -= 10
                elif event.key == K_d or event.key == K_RIGHT:
                    x += 10
                elif event.key == K_SPACE:
                    print("space")

        time.sleep(0.09)


if __name__ == '__main__':
    main()
