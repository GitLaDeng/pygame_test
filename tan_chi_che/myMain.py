'''
主程序
'''
import sys

import pygame

import mySprite

'''常量定义'''
screenWidth = 601
screenHeight = 721
screenWidthAndHeight = (screenWidth,screenHeight)

# 帧
zhenSize = 50

# 方向 1 上 -1 下  2 右 -2 左
fangxiang = 1

# 身体存在的坐标
bodyList = [[60,61],[60,91]]
# 身体的句柄
bodyHandler = []


def moveBody():
    pass






def eventHandler(screen,events,head_rect,head):
    global fangxiang
    global bodyList
    global bodyHandler

    for event in events:

        if event.type == pygame.KEYDOWN:
            downKey = event.key   # 按下键盘
            # 上右下左 273 275 274 276 w d s a 119 100 115 97
            if downKey in (273,119):  # 上
                if head_rect.y <= 1:
                    head_rect.y = 721
                head_rect.y -= 30
                for i in range(len(bodyList)):
                    if bodyList[i][1] <= 1:
                        bodyList[i][1] = 721
                    bodyList[i][1] = bodyList[i][1] - 30


            elif downKey in(275,100):  # 右
                head_rect.x += 30
                if head_rect.x >= 601:
                    head_rect.x = 1
                print(bodyList)
                headx,heady = head_rect.x,head_rect.y
                bodyList.insert(0,[headx,heady])



            elif downKey in (274,115): # 下
                head_rect.y += 30
                if head_rect.y > 691:
                    head_rect.y = 1

            elif downKey in (276,97): # 左

                if head_rect.x <= 1:
                    head_rect.x = 601
                head_rect.x -= 30




def fangXiang():
    pass


# 创建身体
def createBody(screen,postion=[1,1],color=(0, 0, 220)):
    global bodyList,bodyHandler
    ''' 'bottom', 'bottomleft', 'bottomright', 'center', 'centerx', 'centery', 'clamp', 'clamp_ip', 'clip', 'collidedict', 'collidedictall', 'collidelist', 'collidelistall', 'collidepoint', 'colliderect', 'contains', 'copy', 'fit', 'h', 'height', 'inflate', 'inflate_ip', 'left', 'midbottom', 'midleft', 'midright', 'midtop', 'move', 'move_ip', 'normalize', 'right', 'size', 'top', 'topleft', 'topright', 'union', 'union_ip', 'unionall', 'unionall_ip', 'w', 'width', 'x', 'y']'''

    body = pygame.Surface((29, 29))
    body.fill(color)
    body_rect = body.get_rect()
    body_rect.topright = postion
    screen.blit(body,body_rect)



#退出
def quitGaem(events):
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()

# 1.创建画布
def createFrame(screen):
    tempList = []
    for x in range(1, 600, 30):  # 1 31
        for y in range(1, 720, 30):
            temp = mySprite.createSprite((230, 230, 230), initial_positon=[x, y], chunk_size=[29, 29])
            tempList.append(temp)
    for emp in tempList:
        screen.blit(emp.chunk, emp.chunk_rect)


def main():
    global bodyList
    pygame.init()
    screen = pygame.display.set_mode(screenWidthAndHeight)
    pygame.display.set_caption("hello world!")

    clock = pygame.time.Clock()
    pygame.display.update()

    head_rect = pygame.Rect(31, 31, 30, 30)

    while True:

        clock.tick(zhenSize)
        events = pygame.event.get()
        # 退出
        quitGaem(events)

        # 1. 创建画布
        createFrame(screen)

        # 2.画头
        head = pygame.Surface((29,29))
        head.fill((230,3,230))

        # 3.画身体
        for x in bodyList:
            createBody(screen,postion=x)
            createBody(screen,postion=x)





        eventHandler(screen,events,head_rect,head)
        screen.blit(head,head_rect)







        # 2. 监听事件
        #eventHandler()




        pygame.display.update()








if __name__ == '__main__':
    main()