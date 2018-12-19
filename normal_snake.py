import random

import pygame
from pygame.locals import *
from snake_sprite import *


# 1 -1 -2 2 代表当前方向
fangxiang = 1
# 每次走的步长
speed = 1
# 控制游戏更新
control = True
# 控制按钮的事件
control_botton = False


class Snake():
    '''窗口类'''
    def __init__(self):
        # 初始化身体的坐标
        self.init_body_list = [(10,10),(10,11),(10,12)]
        # 1. 初始化窗口
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE.size)
        # 2. 创建刷新频率
        self.clock = pygame.time.Clock()
        # 3. 创建初始化
        self.__create_init_screen()
        # 4.身体的坐标
        self.bodyFrame = [(10,10),
                          (10, 11),
                          (10, 12)]
        # 5.食物坐标
        self.foodFrame = [(
                            random.randint(1,int(SCREEN_SIZE.width / grid_size) -1),
                            random.randint(1,int(SCREEN_SIZE.height / grid_size) -1)
                        )]
        # 5.定时任务 REFRESH_TIME是刷新时间
        self.timing = pygame.time.set_timer(EVENT_REFRESH,REFRESH_TIEM)


    def __create_init_screen(self):
        ''' 画地图 '''
        self.screen.fill(BACKGROUND_COLOR)
        for i in range(0,SCREEN_SIZE.width + 1,grid_size):
            pygame.draw.line(self.screen,LINE_COLOR,(i,0),(i,SCREEN_SIZE.height),LINE_WIDTH)
        for i in range(0,SCREEN_SIZE.height + 1,grid_size):
            pygame.draw.line(self.screen,LINE_COLOR,(0,i),(SCREEN_SIZE.width,i),LINE_WIDTH)

    def __create_one_body(self, color, initial_positon):
        """
        创建单个 body块
        :param color:           块的color
        :param initial_positon: 左上角的坐标
        :return:                块的对象,块的方位坐标
        """
        image = pygame.Surface([grid_size, grid_size])
        image.fill(color)
        rect = image.get_rect()
        rect.topleft = initial_positon
        return image,rect.topleft

    def __create_hero(self,x,y,body_color=BODY_COLOR):
        '''
        结合__create_one_body()方法成倍(grid_size)的来创建body
        :param x:           x轴上的第几个格
        :param y:           y轴上的第几个格
        :param body_color:  创建格子的颜色 默认是BODY_color
        :return:
        '''
        body,body_topleft = self.__create_one_body(body_color,(grid_size * x,grid_size * y))
        self.screen.blit(body,body_topleft)

    def start_game(self):
        while True:
            # 1.控制刷新频率
            self.clock.tick(SHUA_XIN_PIN_LV)
            # 2.时间监听
            self.__event_handler()
            # 3.吃食物
            self.__eat_food()
            # 4.判断是否超出屏幕
            self.__is_out_of_screen_size()
            # 5.检测是否结束游戏
            if self.__is_game_over():
                # 暂停
                self.__stop_game()
            # 6.更新绘图
            self.__update_draw()
            # 7.刷新
            pygame.display.update()

    # 暂停
    def __stop_game(self):
        global control
        control = False  # 暂停

    def __create_botton(self,color,code,initial_postion=()):
        '''
        创建按钮方法
        :param color:           # 按钮颜色
        :param code:            # 按钮上面的字
        :param initial_postion: # 按钮的左上角在屏幕上的位置
        :return:                # 按钮的rect
        '''
        # 打开监控按钮的事件
        global control_botton
        control_botton =True
        # 1.创建按钮
        botton_next = pygame.Surface([grid_size*BOTTON_WIDTH,grid_size*BOTTON_HEIGHT])
        botton_next.fill(color)
        rect = botton_next.get_rect()
        rect.topleft = initial_postion
        self.screen.blit(botton_next,initial_postion)
        # 2.在按钮上写东西
        # ZiTiDuiXiang = pygame.font.Font('freesansbold.ttf', 32)
        ZiTiDuiXiang = pygame.font.SysFont('SimHei', 28)
        WenBenKuangDuiXiang = ZiTiDuiXiang.render(code, True, BOTTON_FONT_COLOER)
        KuangDuiXiang = WenBenKuangDuiXiang.get_rect()
        KuangDuiXiang.topleft = (initial_postion[0],initial_postion[1]+int(grid_size/2))
        self.screen.blit(WenBenKuangDuiXiang, KuangDuiXiang)
        return rect

    # 上下可穿越
    def __is_out_of_screen_size(self):
        screenHeightSize = int(SCREEN_SIZE.size[1]/grid_size) - 1
        for i in range(len(self.bodyFrame)):
            body = self.bodyFrame[i]
            if body[1] < 0:
                self.bodyFrame[i] = body[0],screenHeightSize
            elif body[1] > screenHeightSize:
                self.bodyFrame[i] = body[0],0



    def __is_game_over(self):
        head = self.bodyFrame[0]
        if head[0] < 0:  # 左边
            return True
        if head[0] > int(SCREEN_SIZE.width/grid_size) - 1:  # 右边框
            return True
        for i in range(2,len(self.bodyFrame)):  # 自己身体
            body = self.bodyFrame[i]
            if head == body and body not in self.foodFrame:
                return True
        return False

    def __eat_food(self):
        head = self.bodyFrame[0]
        for food in self.foodFrame:
            if head == food:
                food = self.foodFrame.pop()
                self.bodyFrame.insert(1,food)
                width = int(SCREEN_SIZE.width / grid_size)
                heigth = int(SCREEN_SIZE.height / grid_size)
                food_x = random.randint(1,width-1)
                food_y = random.randint(1,heigth-1)
                self.foodFrame.append((food_x,food_y))

    # 创建食物
    def __create_food(self):
        self.__create_hero(30,30)

    # 更新画面
    def __update_draw(self):
        # 画屏幕
        self.__create_init_screen()

        # 画食物
        for x, y in self.foodFrame:
            self.__create_hero(x, y)

        # 画人物
        for i in range(1,len(self.bodyFrame)):
            x,y = self.bodyFrame[i]
            self.__create_hero(x,y)
        # 画头
        x,y = self.bodyFrame[0]
        self.__create_hero(x,y,body_color=HEAD_COLOR)

        # 画按钮
        if not control:
            # 调用按钮 # 创建按钮
            self.next_botton_rect = self.__create_botton(BOTTON_COLOR, '开  始',(grid_size * BOTTON_WIDTH_SIZE, grid_size * BOTTON_HEIGHT_SIZE))
            self.quit_botton_rect = self.__create_botton(BOTTON_COLOR, "退  出", (grid_size * BOTTON_QUIT_WIDTH_SIZE, grid_size * BOTTON_QUIT_HEIGHT))

    def __check_head(self,newFangxing):
        '''
        检测方向
        :param newF: 要改变的方向标识
        :return:
                True: 可以进行
                False:不可以
        '''
        global fangxiang
        if not (newFangxing + fangxiang):
            return False
        return True

    # 定时移动的方法
    def __clcok_move(self):
        global fangxiang,speed
        if fangxiang == 1:
            self.decoratorCheckHead(0, -speed, 1)
        elif fangxiang == -1:
            self.decoratorCheckHead(0,speed,-1)
        elif fangxiang == 2:
            self.decoratorCheckHead(speed, 0, 2)
        elif fangxiang == -2:
            self.decoratorCheckHead(-speed, 0, -2)

    def __event_handler(self):
        global fangxiang,control,control_botton
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 退出
                self.__game_over()
            elif event.type == EVENT_REFRESH:
                # 控制定时
                if control:
                    # 定时移动
                    self.__clcok_move()

            if control_botton:
                myMouse = pygame.mouse # 保存当前的鼠标
                if event.type == pygame.MOUSEBUTTONDOWN:
                    left_mouse,center,right_mouse = myMouse.get_pressed()  # 返回 (1|0,1|0,1|0)  (左,中,右)
                    if left_mouse:
                        if self.__check_mouse(myMouse, self.next_botton_rect):
                            fangxiang = 1
                            control = True
                            control_botton = False
                            # 这里有切片赋值的速度比较快 用别的会报错
                            self.bodyFrame[:] = self.init_body_list

                        if self.__check_mouse(myMouse, self.quit_botton_rect):
                            self.__game_over()



        # 控制是否继续监听事件
        if control:
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_LEFT]:
                if self.__check_head(-2):
                    self.decoratorCheckHead(-1,0,-2)
            elif keys_pressed[pygame.K_RIGHT]: # 右
                if self.__check_head(2):
                    self.decoratorCheckHead(1,0,2)
            elif keys_pressed[pygame.K_UP]:  # 方向代码是 1
                if self.__check_head(1):
                    self.decoratorCheckHead(0,-1,1)
            elif keys_pressed[pygame.K_DOWN]: # 方向代码是 -1
                if self.__check_head(-1):
                    self.decoratorCheckHead(0,1,-1)


    def __check_mouse(self,myMouse,botton_rect):
        '''
        判断是否在指定区域内点击鼠标
        :param myMouse:     当前鼠标对象
        :param botton_rect: 按钮的rect对象
        :return:            bool: True|False
        '''
        pos_x,pos_y = myMouse.get_pos() # 返回一个元组
        max_width = botton_rect.x + botton_rect.size[0]
        min_width = botton_rect.x
        max_height = botton_rect.y + botton_rect.size[1]
        min_height = botton_rect.y
        if pos_x >= min_width and pos_x <= max_width:
            if pos_y >= min_height and pos_y <= max_height:
                return True
        return False

    def decoratorCheckHead(self,x,y,change_head):
        '''
        方向代码的装饰器
        移动身体的方法
        :param x:           x轴
        :param y:           y轴
        :param change_head: 改变head的方向
        :return:            null
        '''
        global fangxiang
        fangxiang = change_head
        frist_x,frist_y = self.bodyFrame[0]
        self.bodyFrame.insert(0,(frist_x + x,frist_y + y))
        self.bodyFrame.pop()

    @staticmethod
    def __game_over():
        pygame.quit()
        exit()

    def __draw_font_on_screen(self, code, code_color=(0, 0, 0), code_size=28, topleft=(0, 0)):
        '''
        往screen上写字
        :param screen:      #当前的screen
        :param code:        #要写的code
        :param code_color:  #code的颜色
        :param code_size:   #字体大小
        :param topleft:     #左上角的位置
        :return:
        '''
        ZiTiDuiXiang = pygame.font.SysFont('SimHei', code_size)  # 支持中文的写法
        WenBenKuangDuiXiang = ZiTiDuiXiang.render(code, True, code_color)
        KuangDuiXiang = WenBenKuangDuiXiang.get_rect()
        KuangDuiXiang.topleft = topleft
        self.screen.blit(WenBenKuangDuiXiang, KuangDuiXiang)



if __name__ == '__main__':
    snake = Snake()
    snake.start_game()
