import random

SHIPS = [
    {"Name": "Battleship", "Map_value": 4, "Size": 4},
    {"Name": "Cruiser", "Map_value": 3, "Size": 3},
    {"Name": "Destroyer", "Map_value": 2, "Size": 2}
]

def place_ship(board):
    """
    Function to loop through the ships list of dicts and place them
    on the board for both human player and computer
    """
    print("Ships board", board)
    print(SHIPS)
    print(SHIPS[1])
    ship_row = random.randrange(0, 10)
    print("ship row", ship_row)
    ship_start = random.randrange(0, 10)
    print("ship start", ship_start)
    print("ship value", SHIPS["Map_value"])

    for ship in SHIPS:
        board[ship_row] = ["Map_value"]
        print(board[ship_row])

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
    
    place_ship(board)
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
        boardsize = 10
        create_board(boardsize)
    if userinput == "6":
        boardsize = 6
        create_board(boardsize)
    else:
        print("Please enter either 10 or 6")
        game_select()

    return boardsize

game_select()