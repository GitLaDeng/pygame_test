'''
练习pygame模块

'''

import time

import pygame
from pygame.locals import * #导入一些常用的函数常亮
from sys import exit        #导入exit函数


#
def createMyFirstWind():
    background_image = '1.png'  # 背景图片
    mouse_image = '2.jpg'       # 跟随鼠标移动的图片

    pygame.init()

    screnn = pygame.display.set_mode((640,400),0,32)   # set_mode返回一个Surface对象
    pygame.display.set_caption('hello world!')
    background = pygame.image.load(background_image).convert()
    '''
    convert函数是将图像数据组转化为Surface对象，每次加载完成图像以后就应该做这件事件
    convert_alpha相比convert保留Alpha通道信息(可以简单理解为透明的部分)
    '''
    mouse_cursor = pygame.image.load(mouse_image).convert_alpha()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            screnn.blit(background,(0,0))
            x,y = pygame.mouse.get_pos()
            x-=mouse_cursor.get_width()/2
            y-=mouse_cursor.get_height()/2

            screnn.blit(mouse_cursor,(x,y))
            '''
                blit函数：
                第一个参数为Surface对象，第二个为左上角位置，
            '''
            pygame.display.update()


def mySecondWid():
    white = 255, 255, 255
    blue = 0, 0, 100

    pygame.init()
    screen = pygame.display.set_mode((480, 853), pygame.RESIZABLE, 0)
    pygame.display.set_caption("pygame学习（一）文字显示")

    myfont = pygame.font.Font(None, 100)# 100字体的大小
    textImage = myfont.render("Hello Pygame", True, white)
    while True:
        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN):
                exit()

        screen.fill(blue)# 指定背景色
        screen.blit(textImage, (50, 200))# 后面的元组是指距离左上角的坐标
        pygame.display.update()








if __name__ == '__main__':
    mySecondWid()





