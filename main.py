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

pygame.quit()

