column  = 5
rows = 5
coordianates_A = ["A", "B", "C", "D", "E"]

def main():
    pass

def init_board(column, rows):
    l = []
    for i in range(rows):
        l.append("#" * column)

def print_board(table):
    
    print(coordianates_A.join(" "))
