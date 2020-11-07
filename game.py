import random
import string

column  = 5
rows = 4
coordianates_A = ["A", "B", "C", "D", "E"]
symbols = string.ascii_lowercase

def main():
    pass




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
    for row in range(rows):
        lower_list = []
        for col in range(columns):
            lower_list.append('#')
        hashed_list.append(lower_list)
    return hashed_list


def init_gameboard(list, rows, columns): 
    visible_list = []
    n = 0
    for row in range(rows):
        lower_list = []
        for col in range(columns):
            lower_list.append(list[n])
        visible_list.append(lower_list)
    return visible_list




def init_game(column, rows):
    print("WELCOME IN MEMORY GAME")
    level = input("Choose difficulty level (E)asy/(M)edium/(H)ard: ")
    hashed = init_hashed_board(column, rows)
    gameboard_list = get_factors(column, rows)
    gameboard = init_gameboard(gameboard_list, column, rows)

    # for i in range(rows):
    #     hash_board.append("#" * column)

    print_board(hashed)

def print_board(table):
    print('  '+' '.join(coordianates_A))
    n = 1
    for i in table: 
        print(f"{n} {' '.join(i)}")
        n += 1

init_game(column, rows)