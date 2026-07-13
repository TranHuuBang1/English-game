# -*- coding: utf-8 -*-
import pygame
import random
import sys

# Thiết lập các thông số cho trò chơi
WIDTH, HEIGHT = 800, 600
FONT_NAME = "Arial"
FPS = 60


# Màu sắc
WHITE = (240, 240, 240)
BLACK = (40, 40, 40)
GREEN = (0, 153, 76)
RED = (255, 77, 77)
BLUE = (0, 102, 204)
DARK_GRAY = (44, 62, 80)
LIGHT_GRAY = (200, 200, 200)
GREY = (169, 169, 169)
LIGHT_GREY = (211, 211, 211)
YELLOW = (255, 255, 0)

# Khởi tạo Pygame
pygame.init()
pygame.key.start_text_input()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("English Game")
font = pygame.font.Font(r"C:\Windows\Fonts\arial.ttf", 30)
title_font = pygame.font.Font(r"C:\Windows\Fonts\arialbd.ttf", 30)
clock = pygame.time.Clock()
class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()

        # Đổi màu khi rê chuột
        if self.rect.collidepoint(mouse):
            pygame.draw.rect(screen, LIGHT_GRAY, self.rect, border_radius=10)
        else:
            pygame.draw.rect(screen, self.color, self.rect, border_radius=10)

        pygame.draw.rect(screen, BLACK, self.rect, 2, border_radius=10)

        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        return (event.type == pygame.MOUSEBUTTONDOWN and
                event.button == 1 and
                self.rect.collidepoint(event.pos))


# ==========================
# Tạo các nút
# ==========================
btn_add = Button(250, 220, 300, 60, "Thêm từ vựng", GREEN)
btn_play = Button(250, 320, 300, 60, "Bắt đầu chơi", BLUE)
btn_exit = Button(250, 420, 300, 60, "Kết thúc", RED)
#danh sách từ vựng 
vocabulary = []
#số mạng 
lives = 10
score = 0
def input_text(prompt):
    text = ""

    while True:
        screen.fill(WHITE)

        title = title_font.render(prompt, True, BLACK)
        screen.blit(title, (50, 150))

        box = pygame.Rect(50, 220, 700, 50)
        pygame.draw.rect(screen, WHITE, box)
        pygame.draw.rect(screen, BLACK, box, 2)

        txt = font.render(text, True, BLACK)
        screen.blit(txt, (60, 230))
        title = title_font.render(prompt, True, BLACK)
        screen.blit(title, (50, 150))

        note1 = font.render("Enter: Lưu từ", True, BLUE)
        screen.blit(note1, (50, 320))

        note2 = font.render("ESC: Quay về menu", True, RED)
        screen.blit(note2, (50, 360))

        pygame.display.update()
        

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.TEXTINPUT:
                text += event.text

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    return text

                elif event.key == pygame.K_ESCAPE:
                    return None

                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
def add_vocabulary():

    while True:

        english = input_text("Nhập từ tiếng Anh")

        if english is None:
            return

        vietnamese = input_text("Nhập nghĩa tiếng Việt")

        if vietnamese is None:
            return

        vocabulary.append((english, vietnamese))

        print(vocabulary)

def play_game():
    global lives, score

    if len(vocabulary) == 0:
        return

    lives = 10
    score = 0

    while lives > 0:

        english, vietnamese = random.choice(vocabulary)

        if random.choice([True, False]):
            question = english
            answer = vietnamese
            title = "Nhập nghĩa tiếng Việt"
        else:
            question = vietnamese
            answer = english
            title = "Nhập từ tiếng Anh"

        user = input_text(f"{title}: {question}")

        if user is None:
            return

        if user.strip().lower() == answer.strip().lower():

            score += 1

        else:

            lives -= 1

            screen.fill(WHITE)

            txt1 = title_font.render("Sai!", True, RED)
            txt2 = font.render(f"Đáp án: {answer}", True, BLACK)

            screen.blit(txt1, (320, 220))
            screen.blit(txt2, (180, 300))

            pygame.display.update()

            pygame.time.delay(2000)

    game_over()
    
def game_over():

    while True:

        screen.fill(WHITE)

        t1 = title_font.render("GAME OVER", True, RED)
        t2 = font.render("Nhấn ENTER để quay lại menu", True, BLACK)

        screen.blit(t1, (270, 220))
        screen.blit(t2, (180, 300))

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    return


# ==========================
# Menu chính
# ==========================
def main_menu():
    while True:
        screen.fill(WHITE)

        # Tiêu đề
        title = title_font.render("Chào mừng bạn đến với English Game", True, DARK_GRAY)
        title_rect = title.get_rect(center=(WIDTH // 2, 100))
        screen.blit(title, title_rect)

        # Vẽ nút
        btn_add.draw(screen)
        btn_play.draw(screen)
        btn_exit.draw(screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if btn_add.is_clicked(event):
                 add_vocabulary()

            if btn_play.is_clicked(event):
                play_game()

            if btn_exit.is_clicked(event):
                pygame.quit()
                sys.exit()

        clock.tick(FPS)


# ==========================
# Chạy chương trình
# ==========================
main_menu()