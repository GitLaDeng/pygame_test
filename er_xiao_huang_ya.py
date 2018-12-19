import sys

import pygame


def createGUI():
    taget_list = []
    for x in range(1,98):
        temp = "./images/666/1 (" + str(x) + ").png"
        taget_list.append(temp)

    pygame.init()
    screen = pygame.display.set_mode((500, 600))
    pygame.display.set_caption("小黄鸭")

    # 绘制背景图
    #bg = pygame.image.load('1.png')
    #screen.blit(bg, (0, 0))
    white = (250,250,250)
    screen.fill(white)
    # 加载小黄鸭
    hero = pygame.image.load(taget_list[0])
    screen.blit(hero, (170, 300))

    # 106 * 171
    pygame.display.update()
    #定时
    clock = pygame.time.Clock()


    hero_rect = pygame.Rect(170,300,106,171)

    i = 0
    while True:

        # 监听事件
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                # 卸载所有的模块
                pygame.quit()

                sys.exit("退出")

        # 控制平率
        clock.tick(15)

        taget_index = i % len(taget_list)   #数组的下标是从 0 到len()-1
        hero_ = pygame.image.load(taget_list[taget_index])  # 中间的那个
        hero_rect_ = hero_.get_rect()
        hero_rect_.bottomleft = [170,360]

        hero_1 = pygame.image.load(taget_list[taget_index])
        hero_1_rect = hero_1.get_rect()
        hero_1_rect.bottomleft = [170,180]

        hero_2 = pygame.image.load(taget_list[taget_index])
        hero_2_rect = hero_1.get_rect()
        hero_2_rect.bottomleft = [170,550]


        hero_3 = pygame.image.load(taget_list[taget_index])
        hero_3_rect = hero_1.get_rect()
        hero_3_rect.bottomleft = [40, 360]

        hero_4 = pygame.image.load(taget_list[taget_index])
        hero_4_rect = hero_1.get_rect()
        hero_4_rect.bottomleft = [320, 360]

        hero_5 = pygame.image.load(taget_list[taget_index])
        hero_5_rect = hero_1.get_rect()
        hero_5_rect.bottomleft = [40, 550]

        hero_6 = pygame.image.load(taget_list[taget_index])
        hero_6_rect = hero_1.get_rect()
        hero_6_rect.bottomleft = [320, 550]

        hero_7 = pygame.image.load(taget_list[taget_index])
        hero_7_rect = hero_1.get_rect()
        hero_7_rect.bottomleft = [40, 180]

        hero_8 = pygame.image.load(taget_list[taget_index])
        hero_8_rect = hero_1.get_rect()
        hero_8_rect.bottomleft = [320, 180]

        screen.fill(white)
        screen.blit(hero_,hero_rect_)
        screen.blit(hero_1,hero_1_rect)
        screen.blit(hero_2, hero_2_rect)
        screen.blit(hero_3, hero_3_rect)
        screen.blit(hero_4, hero_4_rect)
        screen.blit(hero_5, hero_5_rect)
        screen.blit(hero_6, hero_6_rect)
        screen.blit(hero_7, hero_7_rect)
        screen.blit(hero_8, hero_8_rect)


        pygame.display.update()
        i += 1

    pygame.quit()



def main():
    createGUI()
    # pass



if __name__ == '__main__':
    main()
    lst = []





    # import time

    # test_list = [1,2,3,4,5,6]
    # i = 0
    # while True:
    #     a = i % len(test_list)
    #     i += 1
    #     time.sleep(1)
    #     print(a)