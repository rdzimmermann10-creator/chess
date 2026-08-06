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

position = starting_position

def get_position():
    return position

def get_square_index(x,y):
    index = (y//100) * 8 + (x//100)
    return index

def get_piece(index):
    return position[index]

def move_piece(start, end):
    if start not in range(64) or end not in range(64): return
    if position[start] == 0: return
    position[end] = position[start]
    position[start] = 0


def get_legal_moves_pawn(index):
    if position[index] < 0: black = True
    elif position[index] > 0: black = False
    else: return []

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

    # check for opponents pieces to captcher
    if black and index % 8 != 0 and position[index+7] in [1,2,3,4,5]:
        legal_moves.append(index+7)
    if black and index % 8 != 7 and position[index+9] in [1,2,3,4,5]:
        legal_moves.append(index+9)
    if not black and index % 8 != 0 and position[index-9] in [-1,-2,-3,-4,-5]:
            legal_moves.append(index-9)
    if not black and index % 8 != 7 and position[index-7] in [-1,-2,-3,-4,-5]:
            legal_moves.append(index-7)

    return legal_moves


def get_legal_moves_knight(index):
    if position[index] < 0: black = True
    elif position[index] > 0: black = False
    else: return []
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