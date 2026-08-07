position = []
# 0 = leeres Feld
# 1/-1 = Bauer
# 2/-2 = Turm
# 3/-3 = Springer
# 4/-4 = Läufer
# 5/-5 = Dame
# 6/-6 = König

starting_position = [-2,-3,-4,-5,-6,-4,-3,-2,
                     -1,-1,-1,-1,-1,-1,-1,-1,
                     0, 0, 0 ,0 ,0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0 ,0 ,0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     1, 1, 1, 1, 1, 1, 1, 1,
                     2, 3, 4, 5, 6, 4, 3, 2]

test_position = [-2, 0, 0 ,0 ,0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, -6 ,-5 ,0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0 ,0 ,0, 0, 0, 0,
                 0, 0, 6, 0, 0, 0, 0, 5,
                 0, 0, 0 ,0 ,0, 0, 0, 0,
                 2, 0, 0, 0, 0, 0, 0, 0,]

position = test_position

def get_position():
    return position

def get_square_index(x,y):
    index = (y//100) * 8 + (x//100)
    return index

def get_piece(index):
    return position[index]

def move_piece(start, end, position = position):
    if start not in range(64) or end not in range(64): return
    if position[start] == 0: return
    position[end] = position[start]
    position[start] = 0


def copy_position(position = position):
    return position


def get_legal_moves(index, check_search = True, position = position):
    if position[index] < 0: black = True
    elif position[index] > 0: black = False
    else: return []

    if position[index] in (1,-1): moves = get_legal_moves_pawn(index, black)
    elif position[index] in (2,-2): moves = get_legal_moves_rook(index, black)
    elif position[index] in (3,-3): moves = get_legal_moves_knight(index, black)
    elif position[index] in (4,-4): moves = get_legal_moves_bishop(index, black)
    elif position[index] in (5,-5): moves = get_legal_moves_queen(index, black)
    elif position[index] in (6,-6):
        if not check_search: moves = get_legal_moves_king(index, black, False) 
        else: moves = get_legal_moves_king(index, black)
    else: moves = []

    if check_search:
        king_index = get_king_index(black)
        legal_moves = look_for_checks(index, king_index, moves, black)
        return legal_moves
    else: return moves
    



def get_legal_moves_pawn(index, black, position = position):

    # get moves forward or two squares forward
    if black:
        if index < 16: 
            moves = [index + 8, index + 16]
        else: 
            moves = [index + 8]
    else: 
        if index > 47: 
            moves = [index - 8, index - 16]
        else: 
            moves = [index - 8]
    legal_moves = []

    # check if piece is blocking the way
    for m in moves:
        if position[m] == 0: legal_moves.append(m)
    if index+8 not in legal_moves and index+16 in legal_moves: legal_moves.remove(index+16)
    if index-8 not in legal_moves and index-16 in legal_moves: legal_moves.remove(index-16)

    # check for opponents pieces to captcher
    if black and index % 8 != 0 and position[index+7] in [1,2,3,4,5,6]:
        legal_moves.append(index+7)
    if black and index % 8 != 7 and position[index+9] in [1,2,3,4,5,6]:
        legal_moves.append(index+9)
    if not black and index % 8 != 0 and position[index-9] in [-1,-2,-3,-4,-5,-6]:
            legal_moves.append(index-9)
    if not black and index % 8 != 7 and position[index-7] in [-1,-2,-3,-4,-5,-6]:
            legal_moves.append(index-7)

    return legal_moves


def get_legal_moves_knight(index, black, position = position):
    moves = []

    # add all 8 possible moves for the knight
    moves.append(index + 10) # unten rechts rechts
    moves.append(index + 6)  # unten links links
    moves.append(index + 17) # unten unten rechts
    moves.append(index + 15) # unten unten links

    moves.append(index - 10) # oben links links
    moves.append(index - 6)  # oben rechts rechts
    moves.append(index - 17) # oben oben links
    moves.append(index - 15) # oben oben rechts

    # remove the moves that arent possible due to the position of the knight (for example on the edge)
    # row 1
    if index // 8 == 0:
        if index-10 in moves: moves.remove(index-10)
        if index-6 in moves: moves.remove(index-6)
        if index-17 in moves: moves.remove(index-17)
        if index-15 in moves: moves.remove(index-15)
    # row 2
    if index // 8 == 1:
        if index-17 in moves: moves.remove(index-17)
        if index-15 in moves: moves.remove(index-15)
    # row 8
    if index // 8 == 7:
        if index+10 in moves: moves.remove(index+10)
        if index+6 in moves: moves.remove(index+6)
        if index+17 in moves: moves.remove(index+17)
        if index+15 in moves: moves.remove(index+15)
    # row 7
    if index // 8 == 6:
        if index+17 in moves: moves.remove(index+17)
        if index+15 in moves: moves.remove(index+15)

    # column 1:
    if index % 8 == 0:
        if index+6 in moves: moves.remove(index+6)
        if index+15 in moves: moves.remove(index+15)
        if index-10 in moves: moves.remove(index-10)
        if index-17 in moves: moves.remove(index-17)
    # column 2:
    if index % 8 == 1:
        if index+6 in moves: moves.remove(index+6)
        if index-10 in moves: moves.remove(index-10)
    # column 8:
    if index % 8 == 7:
        if index+10 in moves: moves.remove(index+10)
        if index+17 in moves: moves.remove(index+17)
        if index-6 in moves: moves.remove(index-6)
        if index-15 in moves: moves.remove(index-15)
    # column 7:
    if index % 8 == 6:
        if index+10 in moves: moves.remove(index+10)
        if index-6 in moves: moves.remove(index-6)

    legal_moves = []
    if black:
        for m in moves: 
            if position[m] >= 0: legal_moves.append(m)
    else: 
        for m in moves:
            if position[m] <= 0: legal_moves.append(m)

    return legal_moves


def get_legal_moves_bishop(index, black, position = position):

    top_dist = index // 8
    bot_dist = 7 - top_dist
    left_dist = index % 8
    right_dist = 7 - left_dist

    moves = []
    # top right direction
    move = index
    i = 0
    while i < right_dist and i < top_dist:
        move -= 7
        i += 1
        if position[move] == 0: moves.append(move)
        elif position[move] < 0 and black: break
        elif position[move] > 0 and black:
            moves.append(move)
            break
        elif position[move] > 0 and not black: break
        elif position[move] < 0 and not black:
            moves.append(move)
            break
    # top left direction
    move = index
    i = 0
    while i < left_dist and i < top_dist:
        move -= 9
        i += 1
        if position[move] == 0: moves.append(move)
        elif position[move] < 0 and black: break
        elif position[move] > 0 and black:
            moves.append(move)
            break
        elif position[move] > 0 and not black: break
        elif position[move] < 0 and not black:
            moves.append(move)
            break
    # bottom right direction
    move = index
    i = 0
    while i < right_dist and i < bot_dist:
        move += 9
        i += 1
        if position[move] == 0: moves.append(move)
        elif position[move] < 0 and black: break
        elif position[move] > 0 and black:
            moves.append(move)
            break
        elif position[move] > 0 and not black: break
        elif position[move] < 0 and not black:
            moves.append(move)
            break
    # bottom left direction
    move = index
    i = 0
    while i < left_dist and i < bot_dist:
        move += 7
        i += 1
        if position[move] == 0: moves.append(move)
        elif position[move] < 0 and black: break
        elif position[move] > 0 and black:
            moves.append(move)
            break
        elif position[move] > 0 and not black: break
        elif position[move] < 0 and not black:
            moves.append(move)
            break
    return moves


def get_legal_moves_rook(index, black, position = position):

    top_dist = index // 8
    bot_dist = 7 - top_dist
    left_dist = index % 8
    right_dist = 7 - left_dist

    moves = []
    # top direction
    move = index
    i = 0
    while i < top_dist:
        move -= 8
        i += 1
        if position[move] == 0: moves.append(move)
        elif position[move] < 0 and black: break
        elif position[move] > 0 and black:
            moves.append(move)
            break
        elif position[move] > 0 and not black: break
        elif position[move] < 0 and not black:
            moves.append(move)
            break
    # left direction
    move = index
    i = 0
    while i < left_dist:
        move -= 1
        i += 1
        if position[move] == 0: moves.append(move)
        elif position[move] < 0 and black: break
        elif position[move] > 0 and black:
            moves.append(move)
            break
        elif position[move] > 0 and not black: break
        elif position[move] < 0 and not black:
            moves.append(move)
            break
    # bottom direction
    move = index
    i = 0
    while i < bot_dist:
        move += 8
        i += 1
        if position[move] == 0: moves.append(move)
        elif position[move] < 0 and black: break
        elif position[move] > 0 and black:
            moves.append(move)
            break
        elif position[move] > 0 and not black: break
        elif position[move] < 0 and not black:
            moves.append(move)
            break
    # right direction
    move = index
    i = 0
    while i < right_dist:
        move += 1
        i += 1
        if position[move] == 0: moves.append(move)
        elif position[move] < 0 and black: break
        elif position[move] > 0 and black:
            moves.append(move)
            break
        elif position[move] > 0 and not black: break
        elif position[move] < 0 and not black:
            moves.append(move)
            break
    return moves


def get_legal_moves_queen(index, black, position = position):
    moves_diagonal = get_legal_moves_bishop(index, black, position)
    moves_horizontal = get_legal_moves_rook(index, black, position)
    return moves_diagonal + moves_horizontal


def get_legal_moves_king(index, black, check_search = True, position = position):
    moves = []

    moves = []
    moves.append(index-9) # oben links
    moves.append(index-8) # oben
    moves.append(index-7) # oben rechts
    moves.append(index+1) # rechts
    moves.append(index+9) # unten rechts
    moves.append(index+8) # unten
    moves.append(index+7) # unten links
    moves.append(index-1) # links

    if index // 8 == 0:
        if index-9 in moves: moves.remove(index-9)
        if index-8 in moves: moves.remove(index-8)
        if index-7 in moves: moves.remove(index-7)
    if index // 8 == 7:
        if index+9 in moves: moves.remove(index+9)
        if index+8 in moves: moves.remove(index+8)
        if index+7 in moves: moves.remove(index+7)
    if index % 8 == 0:
        if index-9 in moves: moves.remove(index-9)
        if index+7 in moves: moves.remove(index+7)
        if index-1 in moves: moves.remove(index-1)
    if index % 8 == 7:
        if index-7 in moves: moves.remove(index-7)
        if index+1 in moves: moves.remove(index+1)
        if index+9 in moves: moves.remove(index+9)

    legal_moves = []
    if black:
        for m in moves: 
            if position[m] >= 0: legal_moves.append(m)

    else: 
        for m in moves:
            if position[m] <= 0: legal_moves.append(m)
    if not check_search: return legal_moves
    else: legal_moves = look_for_checks(index, index, legal_moves, black)
    return legal_moves


def look_for_checks(index, king_index, moves, black):
    legal_moves = []
    if index == king_index: king = True 
    else: king = False
    for m in moves:
        copy = position
        remember_piece = position[m]
        if king: king_index = m
        move_piece(index, m, copy)
        check = False
        if black:
            for i in range(64):
                if position[i] in (1,2,3,4,5,6):
                    if king_index in get_legal_moves(i, False, copy): check = True
        else:
            for i in range(64):
                if position[i] in (-1,-2,-3,-4,-5,-6):
                    if king_index in get_legal_moves(i, False, copy): check = True
        if not check: legal_moves.append(m)
        move_piece(m , index, copy)
        position[m] = remember_piece
    return legal_moves


def get_king_index(black):
    if black:
        for i in range(64):
            if position[i] == -6: return i
    else:
        for i in range(64):
            if position[i] == 6: return i

    return -1