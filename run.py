def game_select ():
    """
    Function which displays welcome message and gets
    initial choice from user on board size
    """
    print("Welcome to Battleships!")
    print("Please select a board size")
    print("small = 6x6 game board")
    print("large = 10x10 game board")
    
    userinput = input("Enter small or large")

game_select()

def create_board():
    board = [0]
    row = [0]
    while len(board) < 10:
        while len(row) < 10:
            row.append(0)
        print(row)

create_board()