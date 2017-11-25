# 导入需要的模块
import pygame, sys
from pygame.locals import *
# 初始化pygame
pygame.init()
# 设置帧率
FPS = 30
# 获得pygame的时钟
fpsClock = pygame.time.Clock()
# 设置窗口大小
screen = pygame.display.set_mode((1200, 600), 0, 32)
# 设置标题
pygame.display.set_caption('Pygame_Animation')
# 定义颜色
WHITE =(255, 255, 255)
# 加载一张图片
img = pygame.image.load('chrome.png')
# 初始化图片的位置
imgx0=10
imgy0=570
imgx=imgx0
imgy=imgy0
RED = (255, 0, 0)
BLUE = ( 0, 0, 255)
# 初始化图片的移动方向
i=1
direction = 'right'
# 程序主循环
while True:
    # 每次都要重新绘制背景白色
    screen.fill(WHITE)
    if direction == 'right':
        imgx=imgx0+4.6*i
        imgy=imgy0-4.6*i+0.02*i*i
        if imgx>=1180:
           imgx=imgx0
           imgy=imgy0
           i=1
        if imgy>=570:
           imgx=imgx0
           imgy=imgy0
           i=1
    i=i+1
    # 该方法将用于图片绘制到相应的坐标中
    screen.blit(img, (imgx, imgy))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.draw.ellipse(screen, RED, [1060, 550, 60, 60], 2)
    pygame.draw.rect(screen,BLUE, [500, 290, 50,60], 2)
    # 刷新屏幕
    pygame.display.update()
    # 设置pygame时钟的间隔时间
    fpsClock.tick(FPS)
