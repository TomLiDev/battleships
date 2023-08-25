import random

SHIPS = [
    {"name": "Battleship", "value": 4},
    {"name": "Cruiser", "value": 3}
]


def place_ship_computer(blank_board):
    """
    Function which places ships on the computer gameboard, uses ship 
    value in dict to determine length
    """
    ship_length = range(SHIPS[0]["value"])
    print(ship_length)
    print(len(ship_length))
    computer_board = blank_board

    computer_board[4][2] = len(ship_length)
    for i in ship_length:
        computer_board[4][2 + i] = len(ship_length)
    print("computer board", computer_board)

    return computer_board


def place_ship(blank_board):
    """
    Function which places ships on the human user gameboard, 
    uses ship value in dict to determine length
    """
    ship_length = range(SHIPS[0]["value"])
    print(ship_length)
    print(len(ship_length))
    player_board = blank_board

    for i in ship_length:
        player_board[2][2 + i] = len(ship_length)
    print("player board", player_board)

    return player_board


def create_board(boardsize):
    """
    Function which creates the game board based on user selection. Game board 
    is a list of lists populated with zero's initially to represent empty
    open sea. Game board either 6x6 or 10x10 
    based on user selection.
    """
    print("Game board creation")
    blank_board = []
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    if boardsize == 10:
        y = 1
        while y < 3:
            y += 1
            if y == 2:
                blank_board = [[0] * 10 for i in range(10)]
                print("list board", blank_board)
                for i in range(len(blank_board)):
                    blank_board[i].insert(0, letters[i])
                    print(blank_board[i])
                columns = [i for i in range(0, len(blank_board)+1)]
                print(columns)
                blank_board.insert(0, columns)
                print("final 10", blank_board)
                place_ship(blank_board)

            elif y == 3:
                blank_board = [[0] * 10 for i in range(10)]
                print("list board", blank_board)
                for i in range(len(blank_board)):
                    blank_board[i].insert(0, letters[i])
                    print(blank_board[i])
                columns = [i for i in range(0, len(blank_board)+1)]
                print(columns)
                blank_board.insert(0, columns)
                print("final 10", blank_board)
                place_ship_computer(blank_board)

    if boardsize == 6:
        y = 1
        while y < 3:
            y += 1
            if y == 2:
                blank_board = [[0] * 6 for i in range(6)]
                print("list board", blank_board)
                for i in range(len(blank_board)):
                    blank_board[i].insert(0, letters[i])
                    print(blank_board[i])
                columns = [i for i in range(0, len(blank_board)+1)]
                print(columns)
                blank_board.insert(0, columns)
                print("final 6", blank_board)
                place_ship(blank_board)

            elif y == 3:
                blank_board = [[0] * 6 for i in range(6)]
                print("list board", blank_board)
                for i in range(len(blank_board)):
                    blank_board[i].insert(0, letters[i])
                    print(blank_board[i])
                columns = [i for i in range(0, len(blank_board)+1)]
                print(columns)
                blank_board.insert(0, columns)
                print("final 6", blank_board)
                place_ship_computer(blank_board)


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
