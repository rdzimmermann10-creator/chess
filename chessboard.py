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
    if black:
        if index < 16: return [index + 8, index + 16]
        else: return [index + 8]
    else: 
        if index > 47: return [index - 8, index - 16]
        else: return [index - 8]