'''
更新英雄的位置
'''
import pygame
import sys


#初始化窗口
pygame.init()

#创建一个窗体
screen = pygame.display.set_mode((480,600))

#绘制背景图
bg = pygame.image.load('1.png')
screen.blit(bg,(0,0))

#绘制英雄飞机
hero = pygame.image.load("2.jpg")
screen.blit(hero,(150,300))

pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()


# 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150,300,102,126)

print(hero_rect)
#
while True:

    # 可以指定循环内部的代码执行的频率
    clock.tick(60)
    #修改飞机位置
    hero_rect.y -= 1
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)
    print(hero_rect)
    pygame.display.update()

pygame.quit()
