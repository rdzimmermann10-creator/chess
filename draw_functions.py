import pygame


def draw_board(screen):
    white = (238,238,210)
    black = (118,150,86)
    color = white
    size = 100
    i = 0
    j = 0
    while j<8:
        while i<8:
            pygame.draw.rect(screen, color, (i * size, j * size, 100,100))
            if color == black: color = white
            else: color = black
            i += 1
        j += 1
        i = 0
        if color == black: color = white
        else: color = black
    
        
    