# -*- coding: utf-8 -*-
# @Author: 四叶草
# @Date:   2017-11-04 19:15:46
# @Last Modified by:   Administrator
# @Last Modified time: 2017-11-08 17:03:48

import pygame
import sys
import math
from pygame.locals import *

# pygame 初始化
pygame.init()

# 设置背景颜色和线条颜色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 设置直线的坐标
points = [(200, 75), (300, 25), (400, 75)]

# 设置背景框大小
size = width, height = 600, 600
# position = width // 2, height // 2

# 设置帧率，返回clock 类
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("llls make")

while True:
    for event in pygame.event.get():
        # 查找关闭窗口事件
        if event.type == QUIT:
            sys.exit()

    # 填充背景色
    screen.fill(WHITE)

    # 画不封闭的两条直线
    # pygame.draw.lines(screen, GREEN, 0, points, 1)
    pygame.draw.line(screen,BLUE,(0,0),(400,400),3)


    # 画不抗锯齿的一条直线
    pygame.draw.line(screen, BLUE, (100, 200), (540, 250), 1)

    # 画抗锯齿的一条直线
    pygame.draw.aaline(screen, BLUE, (100, 250), (540, 300), 1)

    # 刷新图s
    pygame.display.flip()

    clock.tick(60)
