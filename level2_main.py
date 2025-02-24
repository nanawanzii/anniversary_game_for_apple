import sys
import pygame
from test import *
from level3_main import *

pygame.init()

# 屏幕 & 颜色
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

WHITE = (255, 255, 255)
lightpink = (255, 182, 193)
black = (0, 0, 0)
green = (0, 255, 0)

# 加载字体（如果失败则使用默认字体）
try:
    font = pygame.font.Font("方正水云简体_粗.TTF", 60)
except FileNotFoundError:
    font = pygame.font.Font(None, 60)  # 使用默认字体

# 加载背景 & 玩家
background = pygame.image.load("./image/background.jpg")  # 背景图片
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))  # 缩放背景
player = pygame.image.load("./image/pig.png")
player = pygame.transform.scale(player, (100, 100))
player.set_colorkey((255, 255, 255))  # 设置透明色
target = pygame.image.load('./image/target.jpg')
target = pygame.transform.scale(target, (100, 100))  # 设置目标图片大小
target.set_colorkey((255, 255, 255))

# 加载敌人
enemy_image = pygame.image.load("./image/enemy1.png")
enemy_image = pygame.transform.scale(enemy_image, (40, 40))
enemy_image.set_colorkey((255, 255, 255))  # 设置透明色

# 计算背景重复次数
MAP_WIDTH = 3000  # 地图总宽度
num_backgrounds = MAP_WIDTH // SCREEN_WIDTH  # 背景需要绘制几次

# 角色起始位置 & 物理参数
player_rect = player.get_rect()
player_rect.bottomleft = (0, SCREEN_HEIGHT)

gravity = 2   # 重力
jump_height = -20  # 跳跃力度
velocity_y = 0  # 竖直速度
is_jumping = False

# 摄像机偏移量
camera_x = 0  # 画面左上角的 x 位置

# 敌人列表，设置不同位置和速度
enemies = [
    {"rect": enemy_image.get_rect(), "speed": 10, "x_pos": 600, "y_pos": SCREEN_HEIGHT - 100},
    {"rect": enemy_image.get_rect(), "speed": 8, "x_pos": 1000, "y_pos": SCREEN_HEIGHT - 150},
    {"rect": enemy_image.get_rect(), "speed": 6, "x_pos": 2000, "y_pos": SCREEN_HEIGHT - 130},
    {"rect": enemy_image.get_rect(), "speed": 9, "x_pos": 2500, "y_pos": SCREEN_HEIGHT - 110},
    {"rect": enemy_image.get_rect(), "speed": 8, "x_pos": 2500, "y_pos": SCREEN_HEIGHT - 200},
    {"rect": enemy_image.get_rect(), "speed": 10, "x_pos": 2500, "y_pos": SCREEN_HEIGHT}
]

# 初始化敌人位置
for enemy in enemies:
    enemy["rect"].bottomleft = (enemy["x_pos"], enemy["y_pos"])

clock = pygame.time.Clock()

def show_game_over_screen():
    """显示‘游戏失败’画面"""
    text = font.render("游戏失败!", True, (200, 0, 0))  # 红色字体
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    screen.fill(WHITE)  # 清空屏幕
    screen.blit(text, text_rect)  # 显示失败文字
    pygame.display.flip()

    # 等待用户点击任意按键
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

def game_loop():
    global velocity_y, is_jumping, camera_x, player_rect

    # 重置玩家位置和状态
    player_rect.bottomleft = (0, SCREEN_HEIGHT)
    velocity_y = 0
    is_jumping = False

    # 设置目标物体的位置
    target_rect = target.get_rect()
    target_rect.bottomright = (MAP_WIDTH - 50, SCREEN_HEIGHT)  # 让目标物放在地图最右端

    while True:
        screen.fill(WHITE)

        # 事件监听
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not is_jumping:  # 只能跳一次
                    velocity_y = jump_height
                    is_jumping = True

        # 获取按键状态
        keys = pygame.key.get_pressed()
        speed = 10
        if keys[pygame.K_LEFT]:  # 左移
            player_rect.x -= speed
            if player_rect.left < 0:
                player_rect.left = 0  # 限制左边界
        if keys[pygame.K_RIGHT]:  # 右移
            player_rect.x += speed
            if player_rect.right > MAP_WIDTH:  # 限制地图右边界
                player_rect.right = MAP_WIDTH

        # 摄像机跟随 player（保证 player 在屏幕中央）
        camera_x = player_rect.centerx - SCREEN_WIDTH // 2
        camera_x = max(0, min(camera_x, MAP_WIDTH - SCREEN_WIDTH))  # 限制摄像机不能超出背景边界

        # 重力作用
        velocity_y += gravity
        player_rect.y += velocity_y

        # 限制 player 不能掉出地面
        if player_rect.bottom >= SCREEN_HEIGHT:
            player_rect.bottom = SCREEN_HEIGHT
            velocity_y = 0
            is_jumping = False

        # 限制 player 不能跳出屏幕上方
        if player_rect.top < 0:
            player_rect.top = 0
            velocity_y = 0

        # 检测玩家与敌人碰撞
        for enemy in enemies:
            if player_rect.colliderect(enemy["rect"]):
                show_game_over_screen()
                return  # 结束游戏循环

        # 检测玩家与目标物的碰撞
        if player_rect.colliderect(target_rect):
            # 显示成功界面
            show_success_screen()
            return

        # **循环绘制背景**
        for i in range(num_backgrounds + 1):
            screen.blit(background, (i * SCREEN_WIDTH - camera_x, 0))

        # **绘制角色**（相对于摄像机偏移）
        screen.blit(player, (player_rect.x - camera_x, player_rect.y))

        # **绘制目标物**（相对于摄像机偏移）
        screen.blit(target, (target_rect.x - camera_x, target_rect.y))

        # **绘制敌人**（敌人从右向左移动）
        for enemy in enemies:
            enemy["rect"].x -= enemy["speed"]  # 每个敌人以不同的速度移动
            if enemy["rect"].right < 0:  # 如果敌人超出左边界，重新回到右边
                enemy["rect"].left = MAP_WIDTH

            screen.blit(enemy_image, (enemy["rect"].x - camera_x, enemy["rect"].y))

        pygame.display.flip()
        clock.tick(30)  # 30 FPS

def show_success_screen():
    """显示‘游戏成功’画面"""
    text = font.render("恭喜！", True, green)  # 绿色字体
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    screen.fill(WHITE)  # 清空屏幕
    screen.blit(text, text_rect)  # 显示成功文字
    pygame.display.flip()

    # 等待用户点击任意按键后进入 final 页面
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False
                level_two_end()  # 进入最终界面




def level_2_main():
    while True:
        screen.fill(WHITE)
        text = font.render("点击任意按键开始游戏", True, (0, 0, 0))
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                game_loop()  # 开始游戏

