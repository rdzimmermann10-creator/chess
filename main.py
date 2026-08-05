import pygame
from draw_functions import *
from chessboard import *

pygame.init()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))


run = True
while run:
    mouse_pos = pygame.mouse.get_pos()
    draw_board(screen, mouse_pos)
    draw_position(get_position(),screen)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(get_square_index(mouse_pos[0], mouse_pos[1]))
pygame.quit()

