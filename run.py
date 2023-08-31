import random
import copy
import sys

LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
SHIPS = [
    {"name": "Battleship", "value": 4},
    {"name": "Cruiser", "value": 3},
    {"name": "Destroyer", "value": 2},
    {"name": "Submarine", "value": 1}
]


def check_ships_remain(board, board_name):
    """
    Function for checking if there are any remaining ships, if there are none
    then the game is ended and a winner declared.
    """
    print("Full board", board)
    check_row = [x for x in board[1:]]
    print("check row", check_row)
    ships_surviving = 1
    if ships_surviving == 1:
        y = 0
        for row in check_row:
            second_check = [x for x in row[1:]]
            for item in second_check:
                y += 1
                if item == 4:
                    print("This is a ship")
                    ships_surviving += 1
                    break
                elif y > 35 and ships_surviving == 1:
                    print("No ships remaining")
                    break
            if ships_surviving == 2:
                print("Second break")
                break
            elif y > 35 and ships_surviving == 1:
                print("No ships second break")
                if board_name == "computer":
                    print("Congratulations Captain, you won!")
                    replay = input("Would you like to play again? (y/n): ")
                    if replay == "n":
                        sys.exit()
                    elif replay == "y":
                        game_select()
                elif board_name == "player":
                    print("Captain we've been sunk, you lost")
                    replay = input("Would you like to play again? (y/n): ")
                    if replay == "n":
                        sys.exit()
                    elif replay == "y":
                        game_select()

        return ships_surviving


def computer_fire(player_board, computer_board, boardsize):
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
            check_ships_remain(player_board, "player")
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
            check_ships_remain(player_board, "player")
        else:
            print("The enemy missed")
            player_board[computer_row_fire][computer_column_fire] = "X"
            print(player_board)
    player_fire(player_board, computer_board, boardsize)


def player_fire(player_board, computer_board, boardsize):
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
                check_ships_remain(computer_board, "computer")
                computer_fire(player_board, computer_board, boardsize)
            else:
                print("You missed")
                row[column_ref] = "X"
                computer_fire(player_board, computer_board, boardsize)
    return computer_board


def place_ship(board, boardsize):
    """
    Function which places ships on the human user and computer gameboard,
    uses ship value in dict to determine length
    """
    print("Ship placement")
    numbers_to_select = []
    for item in range(boardsize):
        numbers_to_select.append(item)
    print("Test list of numbers", numbers_to_select)
    for ship in SHIPS:
        temp_ship_length = range(ship["value"])
        ship_length = len(temp_ship_length)
        print("Actual ship length", ship_length)
        row_number = random.randrange(1, len(numbers_to_select))
        chosen_row = numbers_to_select[row_number]
        end_value = boardsize - ship_length
        grid = random.randrange(1, end_value)
        for i in range(ship_length):
            board[chosen_row][grid + i] = ship_length
        numbers_to_select.pop(row_number)
    return board


def create_board(boardsize):
    """
    Function which creates the game board based on user selection. Game board
    is a list of lists populated with zero's initially to represent empty
    open sea. Game board either 6x6 or 10x10
    based on user selection.
    """
    print("Game board creation")
    blank_board = []
    blank_board = [[0] * boardsize for i in range(boardsize)]
    for i in range(len(blank_board)):
        blank_board[i].insert(0, LETTERS[i])
        print(blank_board[i])
    columns = [i for i in range(0, len(blank_board)+1)]
    print(columns)
    blank_board.insert(0, columns)
    player_board = copy.deepcopy(blank_board)
    computer_board = copy.deepcopy(blank_board)
    player_board = place_ship(player_board, boardsize)
    computer_board = place_ship(computer_board, boardsize)
    print("Player board", player_board)
    print("Computer board", computer_board)
    return player_board, computer_board


def game_select():
    """
    Function which displays welcome message and gets
    initial choice from user on board size
    """
    print("Please select a game board size")
    print("6 = 6x6 game board")
    print("10 = 10x10 game board")
    userinput = input("Enter 6 or 10: ")

    boardsize = int(userinput)
    print(type(boardsize))

    if boardsize == 6:
        create_board(boardsize)
    elif boardsize == 10:
        create_board(boardsize)
    else:
        print(f"Sorry {boardsize} isn't valid, please enter either 10 or 6")
        game_select()


print("Welcome to Battleships!")
game_select()
