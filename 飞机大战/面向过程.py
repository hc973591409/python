import pygame
from plane_sprites import *
from pygame.locals import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((480, 852), 0, 32)

    background = pygame.image.load("./feiji/background.png")
    hero = pygame.image.load("./feiji/hero1.png")
    clock = pygame.time.Clock()

    enemy = PlaneSprite("./feiji/enemy-1.gif")
    enemy_group = pygame.sprite.Group(enemy)

    x = 150
    y = 700
    # 设计一个游戏时钟
    while True:
        clock.tick(60)
        screen.blit(background, (0, 0))
        screen.blit(hero, (x, y))
        
        # update会调用精灵种所有的update方法
        enemy_group.update()
        # 会把精灵中所有的精灵绘制到指定位置
        enemy_group.draw(screen)
        # 这句话一定要放在所有图像绘制完成以后
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

if __name__ == '__main__':
    main()