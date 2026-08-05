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