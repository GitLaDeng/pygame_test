import pygame
import sys


pygame.init()

screen = pygame.display.set_mode((500,600))

#绘制背景图
bg = pygame.image.load('1.png')
screen.blit(bg,(0,0))

taget_list = [
    '11.png',
    '22.png'
]


#绘制英雄飞机
hero = pygame.image.load("11.png")
hero_ = pygame.image.load("22.png")
screen.blit(hero,(150,300))
screen.blit(hero_,(150,300))

pygame.display.update()

clock = pygame.time.Clock()


hero_rect = pygame.Rect(150,300,200,200)
i = 0
while True:
    clock.tick(2)

    if i % 2 == 0:
        screen.blit(bg, (0, 0))
        screen.blit(hero_,(150,300))

    else:
        screen.blit(bg, (0, 0))
        screen.blit(hero,(150,300))
        print('====')
    i += 1
    pygame.display.update()
pygame.quit()

