import random
import string

column  = 5
rows = 4
coordianates_A = ["A", "B", "C", "D", "E"]
symbols = string.ascii_lowercase

def main():
    pass

def init_game(column, rows):
    hashed = init_hashed_board(column, rows)
    gameboard_list = get_factors(column, rows)

    for i in range(rows):
        hash_board.append("#" * column)

def print_board(table):
    
    print(coordianates_A.join(" "))

# def init_gameboard(col, row, hash_board):
#     for i in range(rows):
#         hash_board.append("#" * column)

def get_factors(row, cols): #ładuje literki wg logiki
    global symbols
    gen = []
    for i in range(cols*row):
        letter = random.choice(symbols)
        if letter in gen:
            continue
        gen.append(2*str(letter))
    random.shuffle(gen)
    return gen


def init_hashed_board(columns, rows):
    hashed_list = []
    for row in rows:
        lower_list = []
        for col in columns:
            lower_list.append('#')
        hashed_list.append(lower_list)
    return hashed_list