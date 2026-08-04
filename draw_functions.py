import pygame


def draw_board(screen,mouse_pos):
    white = (238,238,210)
    black = (118,150,86)
    special_white = (246,246,105)
    special_black = (186,202,68)
    color = white
    size = 100

    special_square = (mouse_pos[0]//size, mouse_pos[1]//size)

    i = 0
    j = 0
    while j<8:
        while i<8:
            if i == special_square[0] and j == special_square[1]:
                if color == black: color = special_black
                else: color = special_white
            pygame.draw.rect(screen, color, (i * size, j * size, 100, 100))
            color = change_color(color, white, black, special_black)
            i += 1
        j += 1
        i = 0
        color = change_color(color, white, black, special_black)


def change_color(color,white,black,special_black):

    if color == black or color == special_black: color = white
    else: color = black
    return color
    