import random
import copy

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
SHIPS = [
    {"name": "Battleship", "value": 4},
    {"name": "Cruiser", "value": 3}
]


def computer_fire(player_board):
    """
    Function for controlling computer return fire on players board
    Creates random grid references for fire selection
    """
    print("Enemy fire incoming!")
    print(len(player_board))
    if len(player_board) == 7:
        computer_row_fire = random.randrange(1, 7)
        print(computer_row_fire)
        computer_column_fire = random.randrange(1, 7)
        print(computer_column_fire)

        if player_board[computer_row_fire][computer_column_fire] != 0:
            print("Captain we've been hit!")
            player_board[computer_row_fire][computer_column_fire] = "H"
            print(player_board)
        else:
            print("The enemy missed")
            player_board[computer_row_fire][computer_column_fire] = "X"
            print(player_board)

    elif len(player_board) == 11:
        print(random.randrange(1, 11))
        computer_row_fire = random.randrange(1, 11)
        print(computer_row_fire)
        computer_column_fire = random.randrange(1, 11)
        print(computer_column_fire)

        if player_board[computer_row_fire][computer_column_fire] != 0:
            print("Captain we've been hit!")
            player_board[computer_row_fire][computer_column_fire] = "H"
            print(player_board)
        else:
            print("The enemy missed")
            player_board[computer_row_fire][computer_column_fire] = "X"
            print(player_board)


def player_fire(player_board, computer_board):
    """
    Function which takes input from player to
    fire on a certain grid reference on the computer board
    """
    print("Where shall we fire captain?")
    user_grid_fire = input("Enter row,column reference e.g B,3: ")
    print("Fire reference", user_grid_fire)
    split_fire_reference = user_grid_fire.split(",")
    column_ref = int(split_fire_reference[1])

    for row in computer_board:
        if row[0] == split_fire_reference[0]:
            print("This row", row[0], split_fire_reference[0])
            if row[column_ref] != 0:
                print("Hit! Good shot captain")
                row[column_ref] = "H"
            else:
                print("You missed")
                row[column_ref] = "X"
    print(computer_board)
    computer_fire(player_board)
    return computer_board


def place_ship(blank_board):
    """
    Function which places ships on the human user gameboard,
    uses ship value in dict to determine length
    """
    print("Ship placement")
    computer_temp_board = copy.deepcopy(blank_board)
    player_board = []
    computer_board = []

    y = 1
    while y < 3:
        y += 1
        if y == 2:
            ship_length = range(SHIPS[0]["value"])
            print(ship_length)
            print(len(ship_length))

            for i in ship_length:
                player_board = blank_board
                player_board[2][2 + i] = len(ship_length)
            print("player board", player_board)
        elif y == 3:
            ship_length = range(SHIPS[0]["value"])
            print(ship_length)
            print(len(ship_length))

            for i in ship_length:
                computer_board = computer_temp_board
                computer_board[4][2 + i] = len(ship_length)
            print("computer board", computer_board)
            player_fire(player_board, computer_board)

    return player_board, computer_board


def create_board(boardsize):
    """
    Function which creates the game board based on user selection. Game board
    is a list of lists populated with zero's initially to represent empty
    open sea. Game board either 6x6 or 10x10
    based on user selection.
    """
    print("Game board creation")
    blank_board = []
    if boardsize == 10:
        blank_board = [[0] * 10 for i in range(10)]
        print("list board", blank_board)
        for i in range(len(blank_board)):
            blank_board[i].insert(0, letters[i])
            print(blank_board[i])
        columns = [i for i in range(0, len(blank_board)+1)]
        print(columns)
        blank_board.insert(0, columns)
        place_ship(blank_board)

    elif boardsize == 6:
        blank_board = [[0] * 6 for i in range(6)]
        print("list board", blank_board)
        for i in range(len(blank_board)):
            blank_board[i].insert(0, letters[i])
            print(blank_board[i])
        columns = [i for i in range(0, len(blank_board)+1)]
        print(columns)
        blank_board.insert(0, columns)
        place_ship(blank_board)


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
