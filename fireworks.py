import pygame
import random
import math
import time

# 初始化 Pygame
pygame.init()

# 设置窗口大小和标题
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame 烟花")
font_size = max(12, screen.get_width() // 40)
font = pygame.font.Font("方正水云简体_粗.TTF", font_size)

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_text(text, font, color, surface, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(surface.get_width() // 2, y))
    surface.blit(text_obj, text_rect)

# 粒子类
class Particle:
    def __init__(self, x, y, angle, speed, color):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.color = color
        self.life = 100

    def update(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.life -= 1
        self.speed *= 0.95  # 减速效果

    def draw(self, screen):
        if self.life > 0:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 3)


# 烟花类
class Firework:
    def __init__(self):
        self.particles = []
        for _ in range(50):
            angle = random.uniform(0, 3 * math.pi)
            speed = random.uniform(1, 5)
            color = [random.randint(128, 255) for _ in range(3)]
            particle = Particle(500, 300, angle, speed, color)
            self.particles.append(particle)

    def update(self):
        for particle in self.particles:
            particle.update()

    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)


# 主循环
def fireworks():
    running = True
    clock = pygame.time.Clock()
    fireworks = [Firework()]
    start_time = time.time()

    while running:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time > 3:  # 播放3秒后退出
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        draw_text("加载下一题",font,WHITE,screen,300)
        for firework in fireworks:
            firework.update()
            firework.draw(screen)

        pygame.display.flip()
        clock.tick(30)