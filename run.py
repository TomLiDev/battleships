import random


SHIPS = [
    {"name": "Battleship", "value": 4},
    {"name": "Cruiser", "value": 3}
]


def place_ship(board):
    """
    Function which places ships on the gameboard, uses ship value in dict
    to determine length
    """
    print("board in place function", board)
    print("ship value", SHIPS[0]["value"])
    print(len(board))

    ship_length = range(SHIPS[0]["value"])
    print(ship_length)
    print(len(ship_length))

    board[2][2] = len(ship_length)
    print(board)
    for i in ship_length:
        board[2][2 + i] = len(ship_length)
    print(board)


def create_board(boardsize):
    """
    Function which creates the game board based on user selection. Game board 
    is a list of lists populated with zero's initially to represent empty
    open sea. Game board either 6x6 or 10x10 
    based on user selection.
    """
    print("Game board creation")
    board = []
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    if boardsize == 10:
        board = [[0] * 10 for i in range(10)]
        print("list board", board)
        for i in range(len(board)):
            board[i].insert(0, letters[i])
            print(board[i])
        columns = [i for i in range(0, len(board)+1)]
        print(columns)
        board.insert(0, columns)
        print("final 10", board)

    if boardsize == 6:
        board = [[0] * 6 for i in range(6)]
        print("list board", board)
        for i in range(len(board)):
            board[i].insert(0, letters[i])
            print(board[i])
        columns = [i for i in range(0, len(board)+1)]
        print(columns)
        board.insert(0, columns)
        print("final 6", board)

    place_ship(board)
    return board


def game_select():
    """
    Function which displays welcome message and gets
    initial choice from user on board size
    """
    print("Please select a game board size")
    print("6 = 6x6 game board")
    print("10 = 10x10 game board")
    
    userinput = input("Enter 6 or 10: ")

    print(userinput)
    print(type(userinput))

    if userinput == "6":
        boardsize = 6
        print("boardsize", boardsize)
        create_board(boardsize)
    elif userinput == "10":
        boardsize = 10
        print("boardsize", boardsize)
        create_board(boardsize)
    else:
        print(f"Sorry {userinput} isn't valid, please enter either 10 or 6")
        game_select()


print("Welcome to Battleships!")
game_select()
