import sys
from pkgutil import find_loader

import pygame
from fireworks import *
from level2_main import *
from level3_main import *

# Initialize Pygame
pygame.init()

# Define colors
lightpink = (255, 182, 193)
klein_blue = (0, 47, 167)
black = (0, 0, 0)
white = (255, 255, 255)
lightgreen = (144, 238, 144)


# gift



# Set up the screen




screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("宝宝一周年快乐")

# Set up the font
font_size = max(12, screen.get_width() // 40)
font = pygame.font.Font("方正水云简体_粗.TTF", font_size)

# Define button areas
buttons = {
    "A": pygame.Rect(200, 250, 600, 40),
    "B": pygame.Rect(200, 300, 600, 40),
    "C": pygame.Rect(200, 350, 600, 40),
    "D": pygame.Rect(200, 400, 600, 40),
}


# Draw text function
def draw_text(text, font, color, surface, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(surface.get_width() // 2, y))
    surface.blit(text_obj, text_rect)


def correct_answer_animation():
    for i in range(6):  # Flashing effect
        screen.fill(klein_blue if i % 2 == 0 else white)
        draw_text("回答正确！", font, klein_blue if i % 2 == 0 else white, screen, 500)
        pygame.display.flip()
        pygame.time.delay(100)


# Start screen
def main():
    while True:
        screen.fill(lightpink)
        draw_text("欢迎来到属于我们的冒险故事，在这里，你要面对一些挑战", font, black, screen, 200)
        draw_text("如果你能全部通过的话，你就能找到属于你的纪念日礼物", font, black, screen, 300)
        draw_text("点击屏幕任意位置进入第一关", font, black, screen, 400)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                level_one_1()  # Enter the first level
                return


# Level one - Question one
def level_one_1():
    result = ""  # Store answer feedback

    while True:
        screen.fill(klein_blue)
        draw_text("我们第一次看《白塔之光》的时候，是在哪一家电影院看的？", font, white, screen, 150)
        draw_text("A. 英皇电影城三里屯店", font, white, screen, 250)
        draw_text("B. 北京百老汇电影中心", font, white, screen, 300)
        draw_text("C. 北京百丽宫影城", font, white, screen, 350)
        draw_text("D. 华夏影城（安贞门）", font, white, screen, 400)

        if result:
            draw_text(result, font, white, screen, 500)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Listen for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for key, rect in buttons.items():
                    if rect.collidepoint(mouse_pos):
                        if key == "B":  # Correct answer
                            fireworks()
                            level_one_2()  # Enter the next question
                            return
                        else:
                            result = "回答错误，再试试！"


# Level one - Question two
def level_one_2():
    result = ""  # Store answer feedback

    while True:
        screen.fill(klein_blue)
        draw_text("我们在邯郸吃的那个餐厅叫什么？", font, white, screen, 150)
        draw_text("A. 海底捞", font, white, screen, 250)
        draw_text("B. 小菜园", font, white, screen, 300)
        draw_text("C. 小放牛", font, white, screen, 350)
        draw_text("D. 小牛蛙", font, white, screen, 400)

        if result:
            draw_text(result, font, white, screen, 500)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Listen for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for key, rect in buttons.items():
                    if rect.collidepoint(mouse_pos):
                        if key == "C":  # Correct answer
                            fireworks()
                            level_one_3()  # Enter the next question
                            return
                        else:
                            result = "回答错误，再试试！"


# Level one - Question three
def level_one_3():
    result = ""  # Store answer feedback
    while True:
        screen.fill(klein_blue)
        draw_text("2024年的2月26日，我们当时在Agora喝饮料，我当时喝的是什么？", font, white, screen, 150)
        draw_text("A. Sunday Evening", font, white, screen, 250)
        draw_text("B. Sonic Youth", font, white, screen, 300)
        draw_text("C. Venus in Fur", font, white, screen, 350)
        draw_text("D. Sunday Morning", font, white, screen, 400)

        if result:
            draw_text(result, font, white, screen, 500)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Listen for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for key, rect in buttons.items():
                    if rect.collidepoint(mouse_pos):
                        if key == "D":  # Correct answer
                            fireworks()
                            level_one_4()  # Enter the next question
                            return
                        else:
                            result = "回答错误，再试试！"


# Level one - Question four
def level_one_4():
    result = ""  # Store answer feedback
    while True:
        screen.fill(klein_blue)
        draw_text("去看国安比赛的时候，国安的对手是谁？", font, white, screen, 150)
        draw_text("A. 沧州", font, white, screen, 250)
        draw_text("B. 青岛", font, white, screen, 300)
        draw_text("C. 成都", font, white, screen, 350)
        draw_text("D. 石家庄", font, white, screen, 400)

        if result:
            draw_text(result, font, white, screen, 500)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Listen for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for key, rect in buttons.items():
                    if rect.collidepoint(mouse_pos):
                        if key == "A":  # Correct answer
                            fireworks()
                            level_one_5()  # Enter the next question
                            return
                        else:
                            result = "回答错误，再试试！"


# Level one - Question five
def level_one_5():
    result = ""  # Store answer feedback
    while True:
        screen.fill(klein_blue)
        draw_text("在天津旅游时，去过的cocktail bar叫什么？", font, white, screen, 150)
        draw_text("A. Gosip", font, white, screen, 250)
        draw_text("B. MILO'S SGARAGE", font, white, screen, 300)
        draw_text("C. EPOCH", font, white, screen, 350)
        draw_text("D. Sip bar", font, white, screen, 400)

        if result:
            draw_text(result, font, white, screen, 500)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Listen for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for key, rect in buttons.items():
                    if rect.collidepoint(mouse_pos):
                        if key == "B":  # Correct answer
                            result = "回答正确！"
                            fireworks()
                            level_two()  # Enter the next level
                            return
                        else:
                            result = "回答错误，再试试！"


# Level two
def level_two():
    while True:
        screen.fill(lightgreen)
        draw_text("很棒的宝宝。全都答对了。接下来，你进入了第二关，要面临新的挑战。", font, black, screen, 300)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                level_two_1()


def level_two_1():
    while True:
        screen.fill(lightgreen)
        draw_text("第二关的名字，叫做————————费大厨历险记", font, black, screen, 300)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                level_2_main()



def level_two_end():
    while True:
        screen.fill(lightgreen)
        draw_text("恭喜你，成功过关，完成第二关的挑战！", font, black, screen, 300)
        draw_text("接下来，你要面对最后一关，也是最难的一关。", font, black, screen, 350)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                level_three_before()


def level_three_before():
    while True:
        screen.fill(lightgreen)
        draw_text('本关的名字————解救Jin女士', font, black, screen, 300)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                level3()








# 运行final_2函数
if __name__ == "__main__":
    main()

