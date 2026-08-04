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


def draw_starting_position(screen):
    # black pawns
    i = 0
    while i<8:
        draw_pawn(i*100, 100, False, screen)
        i += 1
    # white pawns
    i = 0
    while i<8:
            draw_pawn(i*100, 600, True, screen)
            i += 1
    # rooks
    draw_rook(0,0,False,screen)
    draw_rook(700,0,False,screen)
    draw_rook(0,700,True,screen)
    draw_rook(700,700,True,screen)
    # knights
    draw_knight(100,0,False,screen)
    draw_knight(600,0,False,screen)
    draw_knight(100,700,True,screen)
    draw_knight(600,700,True,screen)
    # bishops
    draw_bishop(200,0,False,screen)
    draw_bishop(500,0,False,screen)
    draw_bishop(200,700,True,screen)
    draw_bishop(500,700,True,screen)
    # queens
    draw_queen(300,0,False,screen)
    draw_queen(300,700,True,screen)
    # kings
    draw_king(400,0,False,screen)
    draw_king(400,700,True,screen)


def _colors(white):
    if white:
        fill = (245, 245, 235)
        outline = (20, 20, 20)
    else:
        fill = (45, 45, 45)
        outline = (230, 230, 230)
    return fill, outline


def _circle(screen, color, outline, pos, r):
    pygame.draw.circle(screen, color, pos, r)
    pygame.draw.circle(screen, outline, pos, r, 3)


def _rect(screen, color, outline, rect, radius=0):
    pygame.draw.rect(screen, color, rect, border_radius=radius)
    pygame.draw.rect(screen, outline, rect, 3, border_radius=radius)


def _polygon(screen, color, outline, points):
    pygame.draw.polygon(screen, color, points)
    pygame.draw.polygon(screen, outline, points, 3)


def draw_pawn(x, y, white, screen):
    fill, outline = _colors(white)

    _circle(screen, fill, outline, (x + 50, y + 28), 13)
    _circle(screen, fill, outline, (x + 50, y + 47), 18)
    _rect(screen, fill, outline, pygame.Rect(x + 37, y + 58, 26, 18), 6)
    _rect(screen, fill, outline, pygame.Rect(x + 25, y + 76, 50, 10), 4)


def draw_rook(x, y, white, screen):
    fill, outline = _colors(white)

    for i in range(3):
        _rect(
            screen,
            fill,
            outline,
            pygame.Rect(x + 28 + i * 15, y + 18, 10, 12),
            2,
        )

    _rect(screen, fill, outline, pygame.Rect(x + 25, y + 30, 50, 42), 4)
    _rect(screen, fill, outline, pygame.Rect(x + 20, y + 72, 60, 14), 4)


def draw_knight(x, y, white, screen):
    fill, outline = _colors(white)

    body = [
        (x + 30, y + 75),
        (x + 72, y + 75),
        (x + 68, y + 48),
        (x + 58, y + 22),
        (x + 45, y + 18),
        (x + 36, y + 32),
        (x + 48, y + 38),
        (x + 38, y + 48),
        (x + 30, y + 60),
    ]

    _polygon(screen, fill, outline, body)

    pygame.draw.circle(screen, outline, (x + 54, y + 31), 2)


def draw_bishop(x, y, white, screen):
    fill, outline = _colors(white)

    _circle(screen, fill, outline, (x + 50, y + 22), 8)

    body = [
        (x + 50, y + 28),
        (x + 64, y + 44),
        (x + 58, y + 72),
        (x + 42, y + 72),
        (x + 36, y + 44),
    ]

    _polygon(screen, fill, outline, body)

    pygame.draw.line(
        screen,
        outline,
        (x + 46, y + 36),
        (x + 54, y + 64),
        2,
    )

    _rect(screen, fill, outline, pygame.Rect(x + 25, y + 76, 50, 10), 4)


def draw_queen(x, y, white, screen):
    fill, outline = _colors(white)

    for px in (34, 50, 66):
        _circle(screen, fill, outline, (x + px, y + 18), 5)

    body = [
        (x + 28, y + 30),
        (x + 40, y + 60),
        (x + 50, y + 40),
        (x + 60, y + 60),
        (x + 72, y + 30),
        (x + 66, y + 74),
        (x + 34, y + 74),
    ]

    _polygon(screen, fill, outline, body)

    _rect(screen, fill, outline, pygame.Rect(x + 22, y + 76, 56, 10), 4)


def draw_king(x, y, white, screen):
    fill, outline = _colors(white)

    pygame.draw.line(
        screen,
        outline,
        (x + 50, y + 10),
        (x + 50, y + 24),
        4,
    )
    pygame.draw.line(
        screen,
        outline,
        (x + 43, y + 17),
        (x + 57, y + 17),
        4,
    )

    _circle(screen, fill, outline, (x + 50, y + 30), 8)

    body = [
        (x + 38, y + 38),
        (x + 62, y + 38),
        (x + 66, y + 72),
        (x + 34, y + 72),
    ]

    _polygon(screen, fill, outline, body)

    _rect(screen, fill, outline, pygame.Rect(x + 22, y + 76, 56, 10), 4)