'''
精灵
'''
import pygame


# 屏幕的大小常量
SCREEN_SIZE = pygame.Rect(0,0,900,600)
# 刷新频率
SHUA_XIN_PIN_LV = 10
# 背景颜色
BACKGROUND_COLOR = (230,230,230)
# 线的颜色
LINE_COLOR = (0,0,0)
# 每个线的宽度
LINE_WIDTH = 1
# 每个格子的大小
grid_size = 30
# 精灵的颜色
SPRITE_COLOR = (230,0,230)
# 身体颜色
BODY_COLOR = (0,230,230)
# 头颜色
HEAD_COLOR = (240,0,0)
# 按钮颜色
BOTTON_COLOR = (50,165,248)
# 按钮的大小
BOTTON_WIDTH,BOTTON_HEIGHT = (3,2)
# 按钮上字的颜色
BOTTON_FONT_COLOER = (151,188,138)
# 按钮的位置控制数
BOTTON_WIDTH_SIZE,BOTTON_HEIGHT_SIZE = (10,8)
# 退出按钮的位置
BOTTON_QUIT_WIDTH_SIZE,BOTTON_QUIT_HEIGHT = (16,8)
# 定时刷新
EVENT_REFRESH = pygame.USEREVENT
# 定时刷新 1s
REFRESH_TIEM = 500



class SankeSprite(pygame.sprite.Sprite):

    def __init__(self,color,initial_positon,speedx=0,speedy=1):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([grid_size,grid_size])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = initial_positon
        self.speedx = speedx
        self.speedy = speedy


    def update(self, *args):
        super().update()

        # 向上移动
        self.rect.x += self.speedx * grid_size
        self.rect.y += -self.speedy * grid_size

        # 判断超出屏幕
        if self.rect.y < 0:
            self.rect.y = SCREEN_SIZE.height - grid_size



