import pygame
from draw_functions import *
from chessboard import *

pygame.init()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))


run = True
turn = 1
clicked_piece = 0
clicked_index = -1
legal_moves = []

while run:
    mouse_pos = pygame.mouse.get_pos()
    draw_board(screen, mouse_pos)
    draw_position(get_position(),screen)
    if clicked_piece != 0: draw_legal_moves(legal_moves, screen)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # remember the piece that is currently picked
            last_clicked_index = clicked_index
            
            mouse_pos = pygame.mouse.get_pos()
            clicked_index = get_square_index(mouse_pos[0], mouse_pos[1])
            print(clicked_index)
            if clicked_index in legal_moves:
                move_piece(last_clicked_index, clicked_index)
                # change turn after move
                turn *= -1
        
            clicked_piece = get_piece(clicked_index)
            # check if clicked piece has the right color
            if clicked_piece*turn < 0: 
                clicked_piece = 0
                clicked_index = -1
            legal_moves = get_legal_moves_bishop(clicked_index)
    
    
pygame.quit()

