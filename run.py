def create_board(userboard):
    """
    Function which creates the game board based on user selection. 
    Game board is a list of lists populated with zero's initially 
    to represent empty open sea. Game board either 6x6 or 10x10 
    based on user selection.
    """
    board = []
    row = []
    if userboard == 10:

        while len(board) < 10:
            while len(row) < 10:
                row.append(0)
            print(row)
            board.append(row)
        print("LargeBoard", board)
    else:
        while len(board) < 6:
            while len(row) < 6:
                row.append(0)
            print(row)
            board.append(row)
        print("SmallBoard", board)
    
    return board


def game_select ():
    """
    Function which displays welcome message and gets
    initial choice from user on board size
    """
    print("Welcome to Battleships!")
    print("Please select a board size")
    print("6 = 6x6 game board")
    print("10 = 10x10 game board")
    
    userinput = input("Enter 6 or 10: ")

    print(userinput)

    if userinput == "10":
        userboard = 10
    else:
        userboard = 6

    print(userboard)
    print(type(userboard))

    create_board(userboard)

    return userboard

game_select()


