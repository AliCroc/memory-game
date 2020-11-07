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
        gen.append(letter)
        gen.append(letter)
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

def set_difficulty(level):
    dif = {"e":4,"m":6,"h":10}
    return dif[level]


def init_game(column, rows):
    while True:
        print("WELCOME IN MEMORY GAME")
        level = input("Choose difficulty level (E)asy/(M)edium/(H)ard: \n").lower()
        if level in ["e","m","h"]:
            rows = set_difficulty(level)
            break
        else:
            print("Wrong input")
    counter_to_reach = int((column*rows)/2)
    counter = 0
    hashed = init_hashed_board(column, rows)
    gameboard_list = get_factors(column, rows)
    gameboard = init_gameboard(gameboard_list, column, rows)
    while counter != counter_to_reach:
        print_board(hashed)
        card1 = set_coordinates(hashed, gameboard, gameboard_list)
        card2 = set_coordinates(hashed, gameboard, gameboard_list)
        if card1[0] is not card2[0]:
            hashed[card1[1]][card1[2]] = "#"
            hashed[card2[1]][card2[2]] = "#"
            continue
        counter += 1
    print('Yay, you win')



    # for i in range(rows):
    #     hash_board.append("#" * column)

    print_board(hashed)

def print_board(table):
    print('  '+' '.join(coordianates_A))
    n = 1
    for i in table: 
        print(f"{n} {' '.join(i)}")
        n += 1


def set_coordinates(hashed, gameboard, list):
    global symbols, coordianates_A
    while True:
        coord = input("Type in coordinates of desired pick (ex. B2): \n").upper()
        print(coord)
        if len(coord) == 2:
            x = list(coord)
            print(x)
            if x[0].isalpha() == True and x[1].isdigit() == True and x[0] in coordianates_A:
                index = symbols.index(x[0])
                print(index)
                hashed[index][x[1]] = gameboard[index][x[1]]
                break
            else:
                print("Wrong input")
        else:
            print("Wrong input")
    print(gameboard[index][x[1]], index, x[1])
    return gameboard[index][x[1]], index, x[1]


init_game(column, rows)