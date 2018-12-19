'''
pygame.sprite.Sprite
精灵的使用
'''
import sys

import pygame


class Temp(pygame.sprite.Sprite):

    def __init__(self,color,initial_positon):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([30,30])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = initial_positon

screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])

b = Temp([81,195,50],[50,100])
c = Temp([81,195,50],[150,100])


screen.blit(b.image,b.rect)
screen.blit(c.image,c.rect)




pygame.display.update()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()