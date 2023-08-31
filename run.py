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
player_shots_store = []
computer_shots_store = []


def end_game(who_won):
    """
    Function which is called when either computer or player hit counter
    reaches 10, signalling all ships have been sunk.
    """
    if who_won == "player":
        print("Congratulations Captain, you won!")
        replay = input("Would you like to play again? (y/n): ")
        if replay == "n":
            sys.exit()
        elif replay == "y":
            game_select()
    elif who_won == "computer":
        print("Captain we've been sunk, you lost")
        replay = input("Would you like to play again? (y/n): ")
        if replay == "n":
            sys.exit()
        elif replay == "y":
            game_select()


def computer_fire(player_board, computer_board, boardsize, p_hits, c_hits):
    """
    Function for controlling computer return fire on players board
    Creates random grid references for fire selection
    """
    print("Enemy fire incoming!")
    computer_row_fire = random.randrange(1, boardsize)
    print(computer_row_fire)
    computer_column_fire = random.randrange(1, boardsize)
    print(computer_column_fire)
    computer_grid_fire = computer_row_fire, computer_column_fire
    print("computer grid fire", computer_grid_fire)
    if computer_grid_fire in computer_shots_store:
        print("computer repeat fire")
        computer_fire(player_board, computer_board, boardsize, p_hits, c_hits)
    else:
        computer_shots_store.append(computer_grid_fire)
        print("computer has fired on", computer_shots_store)

        if player_board[computer_row_fire][computer_column_fire] != 0:
            print("Captain we've been hit!")
            player_board[computer_row_fire][computer_column_fire] = "H"
            c_hits += 1
            print("Computer hits", c_hits)
            print("player board from computer fire", player_board)
            player_fire(player_board, computer_board, boardsize,
                        p_hits, c_hits)
        else:
            print("The enemy missed")
            player_fire(player_board, computer_board, boardsize,
                        p_hits, c_hits)


def player_fire(player_board, computer_board, boardsize, p_hits, c_hits):
    """
    Function which takes input from player to
    fire on a certain grid reference on the computer board
    """
    print("Where shall we fire captain?")
    user_grid_fire = input("Enter row,column reference e.g B,3: ")
    print("Fire reference", user_grid_fire)
    if user_grid_fire in player_shots_store:
        print("Captain we have alrady fired on those coordinates")
        player_fire(player_board, computer_board, boardsize, p_hits, c_hits)
    else:
        player_shots_store.append(user_grid_fire)
        print("Player has fired on", player_shots_store)
        split_fire_reference = user_grid_fire.split(",")
        column_ref = int(split_fire_reference[1])

        for row in computer_board:
            if row[0] == split_fire_reference[0]:
                print("This row", row[0], split_fire_reference[0])
                if row[column_ref] != 0:
                    print("Hit! Good shot captain")
                    row[column_ref] = "H"
                    p_hits += 1
                    print("Player hits", p_hits)
                    print("Computer board from pfire", computer_board)
                    if p_hits == 10:
                        end_game("player")
                    computer_fire(player_board, computer_board, boardsize,
                                  p_hits, c_hits)
                else:
                    print("You missed")
                    row[column_ref] = "X"
                    computer_fire(player_board, computer_board, boardsize,
                                  p_hits, c_hits)
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
    p_hits = 0
    c_hits = 0
    player_fire(player_board, computer_board, boardsize, p_hits, c_hits)
    return player_board, computer_board, boardsize


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
