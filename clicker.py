import pygame 
from random import randint
from time import time

pygame.init()
screen_w = 500
screen_h = 500
screen = pygame.display.set_mode((screen_w, screen_h))
GOLD = (255,238,153)
BLACK = (0, 0, 0)
RED = (255,0,0)
GREEN = (0,255,0)
screen.fill(GOLD)

#Шрифты
font = pygame.font.Font(None,74)
font1 = pygame.font.Font(None,74)

#Создаем игрока-квадрат
player = pygame.Rect(screen_w // 2 - 50, screen_h // 2 - 50, 100,100)

#Создаем надпись победы
win_text = font.render('Победа!',True,BLACK)
score = 0
run =  True
cur_time = time()
fill_color = RED
#игровой циклn
while run == True: #run == Trust или ран жто одно и тоже
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            if player.collidepoint(x, y):
                score += 1
                fill_color = GREEN
    new_time = time()
    if int(new_time) - int(cur_time) == 1:
        player.x = (randint(0, screen_w - player.width))
        player.y = (randint(0, screen_h - player.height))
        cur_time = new_time


    screen.fill(GOLD)
    pygame.draw.rect(screen,fill_color,player)
    fill_color = RED
    score_text = font.render('Очки: ' + str(score), True, BLACK)
    screen.blit(score_text,(10,10))

    if score == 10:
        screen.fill(GOLD)
        screen.blit(win_text,(140,220))
    pygame.display.update()
pygame.quit()
