'''

'''
import pygame


class createSprite(pygame.sprite.Sprite):
    '''pygame的精灵类'''

    def __init__(self,color,initial_positon=[0,0],chunk_size=[30,30]):
        '''
        初始化
        :param color:               chunk的颜色  用的是元组() rgb
        :param initial_positon:     左上角的坐标      list
        :param chunk_size:          chunk的大小      list
        '''
        super().__init__()  #调用父类的构造方法

        self.chunk = pygame.Surface(chunk_size)
        self.chunk.fill(color)
        self.chunk_rect = self.chunk.get_rect()
        self.chunk_rect.topleft = initial_positon  # 左上角
if __name__ == '__main__':
    pass