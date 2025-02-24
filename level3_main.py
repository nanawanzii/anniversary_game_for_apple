import pygame
import sys
from test import *
from level2_main import *
# 初始化Pygame
pygame.init()

# 屏幕设置
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
gift1 = pygame.image.load("./image/gift1.png")
gift1 = pygame.transform.scale(gift1,(100,100))
gift1.set_colorkey((255,255,255))

gift2 = pygame.image.load('./image/gift2.png')
gift2 = pygame.transform.scale(gift2,(100,100))
gift2.set_colorkey((255,255,255))

# 颜色定义
WHITE = (255, 255, 255)
black= (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
lightblue = (173, 216, 230)  # 设置背景色为lightblue
lightpink = (255, 182, 193)
klein_blue = (0, 47, 167)
white = (255, 255, 255)
lightgreen = (144, 238, 144)

# 字体设置
try:
    font = pygame.font.Font("方正水云简体_粗.TTF", font_size)
except:
    font = pygame.font.Font(None, 60)
font_size = max(12, screen.get_width() // 40)

# 加载游戏素材
try:
    apple = pygame.image.load("./image/apple.png").convert_alpha()
    apple = pygame.transform.scale(apple, (50, 50))

    prince = pygame.image.load("./image/prince.png").convert_alpha()
    prince = pygame.transform.scale(prince, (50, 50))

    cat = pygame.image.load("./image/cat.png").convert_alpha()
    cat = pygame.transform.scale(cat, (50, 50))
except pygame.error as e:
    print("图片加载失败:", e)
    sys.exit()


# 游戏对象类定义
class Tank:
    def __init__(self, x, y, image, controls):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.image = image
        self.controls = controls  # [上, 下, 左, 右, 射击]
        self.bullets = []
        self.direction = "up"

    def move(self, keys, walls):
        # 保存移动前的位置
        prev_pos = self.rect.copy()

        # 处理移动
        if keys[self.controls[0]]:  # 上
            self.rect.y -= 5
            self.direction = "up"
        if keys[self.controls[1]]:  # 下
            self.rect.y += 5
            self.direction = "down"
        if keys[self.controls[2]]:  # 左
            self.rect.x -= 5
            self.direction = "left"
        if keys[self.controls[3]]:  # 右
            self.rect.x += 5
            self.direction = "right"

        # 边界检测
        self.rect.clamp_ip(screen.get_rect())

        # 墙体碰撞检测
        for wall in walls:
            if self.rect.colliderect(wall):
                self.rect = prev_pos
                break

    def shoot(self):
        # 根据方向计算子弹初始位置
        offset = 20
        if self.direction == "up":
            pos = [self.rect.centerx - 5, self.rect.top - offset]
        elif self.direction == "down":
            pos = [self.rect.centerx - 5, self.rect.bottom + offset]
        elif self.direction == "left":
            pos = [self.rect.left - offset, self.rect.centery - 5]
        else:  # right
            pos = [self.rect.right + offset, self.rect.centery - 5]

        self.bullets.append({
            "pos": pos,
            "direction": self.direction,
            "rect": pygame.Rect(pos[0], pos[1], 10, 10)
        })


class Wall(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50)


# 初始化游戏对象
def init_game():
    global tank1, tank2, walls, cat_rect

    # 创建坦克
    tank1 = Tank(100, 100, apple,
                 [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_j])
    tank2 = Tank(100, 200, prince,
                 [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_l])

    # 创建围墙（保护猫）
    walls = []
    # 中心点坐标
    center_x, center_y = 700, 300
    # 创建多层环形围墙
    layers = 3  # 围墙层数
    spacing = 50  # 每层围墙之间的间距

    for layer in range(layers):
        # 计算当前层的范围
        start_x = center_x - 100 - layer * spacing
        start_y = center_y - 100 - layer * spacing
        end_x = center_x + 150 + layer * spacing
        end_y = center_y + 150 + layer * spacing

        # 生成当前层的围墙
        for x in range(start_x, end_x, 50):
            for y in range(start_y, end_y, 50):
                # 判断是否在内部空白区域
                inner_start_x = center_x - 50 + layer * spacing
                inner_start_y = center_y - 50 + layer * spacing
                inner_end_x = center_x + 100 - layer * spacing
                inner_end_y = center_y + 100 - layer * spacing

                if not (inner_start_x < x < inner_end_x and inner_start_y < y < inner_end_y):
                    walls.append(Wall(x, y))
    # 猫的位置
    cat_rect = pygame.Rect(center_x + 25, center_y + 25, 50, 50)


# 游戏主循环
def level3():
    clock = pygame.time.Clock()
    init_game()
    running = True
    while running:
        # 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == tank1.controls[4]:
                    tank1.shoot()
                if event.key == tank2.controls[4]:
                    tank2.shoot()

        # 按键状态获取
        keys = pygame.key.get_pressed()

        # 更新游戏状态
        tank1.move(keys, walls)
        tank2.move(keys, walls)

        # 更新子弹位置
        for tank in [tank1, tank2]:
            for bullet in tank.bullets[:]:
                # 根据方向移动
                speed = 10
                if bullet["direction"] == "up":
                    bullet["pos"][1] -= speed
                elif bullet["direction"] == "down":
                    bullet["pos"][1] += speed
                elif bullet["direction"] == "left":
                    bullet["pos"][0] -= speed
                else:  # right
                    bullet["pos"][0] += speed

                # 更新碰撞矩形
                bullet["rect"].topleft = bullet["pos"]

                # 边界检测
                if not screen.get_rect().colliderect(bullet["rect"]):
                    tank.bullets.remove(bullet)
                    continue

                # 墙体碰撞检测
                for wall in walls[:]:
                    if bullet["rect"].colliderect(wall):
                        try:
                            tank.bullets.remove(bullet)
                            walls.remove(wall)
                        except:
                            pass
                        break

        # 胜利条件检测
        if tank1.rect.colliderect(cat_rect) or tank2.rect.colliderect(cat_rect):
            show_victory_screen()  # 完成目标，展示胜利界面

        # 绘制游戏画面
        screen.fill(lightblue)  # 修改背景颜色为 lightblue

        # 绘制围墙
        for wall in walls:
            pygame.draw.rect(screen, BLUE, wall)

        # 绘制猫
        screen.blit(cat, cat_rect)

        # 绘制坦克
        screen.blit(tank1.image, tank1.rect)
        screen.blit(tank2.image, tank2.rect)

        # 绘制子弹
        for tank in [tank1, tank2]:
            for bullet in tank.bullets:
                pygame.draw.rect(screen, RED, bullet["rect"])

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
    sys.exit()

def show_victory_screen():
    """显示‘游戏成功’画面"""
    screen.fill(lightblue)

    draw_text("恭喜你，成功解救了Jin女士！", font, (0,0,0), screen, 300)

    pygame.display.flip()

    pygame.time.wait(2000)  # 等待2秒，等待显示胜利画面

    # 等待用户点击后跳转到 final_1
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                waiting = False
                final_1()  # 调用 final_1 来进入最终界面

def final_1():
    while True:
        screen.fill(lightpink)
        draw_text('恭喜你，完成了所有的挑战', font, black, screen, 300)

        draw_text('属于你的礼物是——————', font, black, screen, 350)

        pygame.display.flip()

        # 在 final 界面上等待退出
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                final_2()

def final_2():
    gift1_y = SCREEN_HEIGHT  # 初始位置，屏幕底部
    gift2_y = SCREEN_HEIGHT  # 初始位置，屏幕底部
    gift1_speed = 5  # 礼物1上升速度
    gift2_speed = 5  # 礼物2上升速度

    while True:
        screen.fill(lightgreen)
        draw_text("一周年快乐宝宝，我们以后还会有很多很多个一周年。", font, black, screen, 300)

        # 控制礼物浮现
        if gift1_y > SCREEN_HEIGHT // 2 - 200:  # 控制浮现的停止位置
            gift1_y -= gift1_speed  # 逐渐向上浮现

        if gift2_y > SCREEN_HEIGHT // 2 -200:  # 控制浮现的停止位置
            gift2_y -= gift2_speed  # 逐渐向上浮现

        # 绘制礼物
        screen.blit(gift1, (SCREEN_WIDTH // 2 - 150, gift1_y))  # 礼物1
        screen.blit(gift2, (SCREEN_WIDTH // 2 + 50, gift2_y))   # 礼物2

        pygame.display.flip()

        # 监听事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()