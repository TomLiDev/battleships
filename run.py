import random
import copy
import sys
from colorama import Fore, Back, Style
import emoji

LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
SHIPS = [
    {"name": "Battleship", "value": 4},
    {"name": "Cruiser", "value": 3},
    {"name": "Destroyer", "value": 2},
    {"name": "Submarine", "value": 1}
]
player_shots_store = []
computer_shots_store = []
ships_remaining = bool
players_turn = bool


def end_game(c_hits, p_hits):
    """
    Function which is called when either computer or player hit counter
    reaches 10, signalling all ships have been sunk.
    """
    if p_hits > c_hits:
        print(Fore.GREEN + "Congratulations Captain, you won!")
        print(Style.RESET_ALL)
        print(emoji.emojize(":grinning_face_with_big_eyes:"))
        replay = input("Would you like to play again? (y/n): \n")
        if replay == "n":
            sys.exit()
        elif replay == "y":
            game_select()
    else:
        print(Fore.RED + "Captain we've been sunk, you lost")
        print(Style.RESET_ALL)
        replay = input("Would you like to play again? (y/n): \n")
        if replay == "n":
            sys.exit()
        elif replay == "y":
            game_select()


def computer_fire(player_board, computer_board, boardsize, p_hits, c_hits,
                  players_turn, ships_remaining, computer_board_for_player):
    """
    Function for controlling computer return fire on players board
    Creates random grid references for fire selection
    """
    print(Fore.RED + "Enemy fire incoming!")
    print(Style.RESET_ALL)
    computer_row_fire = random.randrange(1, boardsize)
    computer_column_fire = random.randrange(1, boardsize)
    computer_grid_fire = computer_row_fire, computer_column_fire
    print("computer grid fire", computer_grid_fire)

    if computer_grid_fire in computer_shots_store:
        print("computer repeat fire")
        computer_fire(player_board, computer_board, boardsize, p_hits, c_hits,
                      players_turn, ships_remaining, computer_board_for_player)
    else:
        computer_shots_store.append(computer_grid_fire)
        print("computer has fired on", computer_shots_store)

        if player_board[computer_row_fire][computer_column_fire] != 0:
            print(Fore.RED + "Captain we've been hit!")
            print(Style.RESET_ALL)
            ship_value = player_board[computer_row_fire][computer_column_fire]
            print("ship value", ship_value)
            player_board[computer_row_fire][computer_column_fire] = "H"
            check_ship_sunk(ship_value, computer_board, boardsize, True)
            c_hits += 1
            print("Enemy hits", c_hits)
            if c_hits == 10:
                ships_remaining = False
            else:
                ships_remaining = True
        else:
            print("The enemy missed")
            ships_remaining = True
        print("player board from computer fire", player_board)
        players_turn = True

    main_game(player_board, computer_board, boardsize, p_hits, c_hits,
              players_turn, ships_remaining, computer_board_for_player)
    return players_turn, ships_remaining


def fire_instructions(boardsize):
    """
    Function which displays different instructions for entering fire
    coordinates based on the boardsize. Used to simplify and shorten
    player fire function.
    """
    print(Fore.GREEN + "Where shall we fire captain?")
    print(Style.RESET_ALL)
    if boardsize == 6:
        print("Please enter a row and column reference \n"
              "the row reference must be A - F\n"
              "and the column reference be 1 - 6 \n")
    elif boardsize == 10:
        print("Please enter a row and column reference \n"
              "the row reference must be A - J\n"
              "and the column reference be 1 - 10\n")


def player_fire(player_board, computer_board, boardsize, p_hits, c_hits,
                players_turn, ships_remaining, computer_board_for_player):
    """
    Function which takes input from player to
    fire on a certain grid reference on the computer board
    """
    user_grid_fire = input("Enter row,column reference e.g B,3: \n")
    print("Fire reference", user_grid_fire)
    if user_grid_fire in player_shots_store:
        print(Fore.GREEN + "Captain we have alrady fired on those coordinates")
        print(Style.RESET_ALL)
        player_fire(player_board, computer_board, boardsize, p_hits, c_hits,
                    players_turn, ships_remaining, computer_board_for_player)
    else:
        try:
            player_shots_store.append(user_grid_fire)
            split_fire_reference = user_grid_fire.split(",")
            column_ref = int(split_fire_reference[1])
            ships_remaining = bool

            for row in computer_board:
                if row[0] == split_fire_reference[0]:
                    row_ref = computer_board.index(row)
                    if row[column_ref] != 0:
                        print(Fore.GREEN + "Hit! Good shot Captain",
                              emoji.emojize(":grinning_face_with_big_eyes:"))
                        print(Style.RESET_ALL)
                        ship_value = row[column_ref]
                        print("ship value", ship_value)
                        row[column_ref] = "H"
                        check_ship_sunk(ship_value, computer_board, boardsize,
                                        True)
                        p_hits += 1
                        print("Player hits", p_hits)
                        print("Computer board from pfire", computer_board)
                        computer_board_for_player[row_ref][column_ref] = "H"
                        if p_hits == 10:
                            ships_remaining = False
                        else:
                            ships_remaining = True
                    else:
                        print("You missed")
                        row[column_ref] = "X"
                        computer_board_for_player[row_ref][column_ref] = "X"
                        ships_remaining = True
            print("Player has fired on", player_shots_store)
        except IndexError:
            print(Fore.GREEN + "Invalid fire coordinates Captain")
            print(Style.RESET_ALL)
            print("please enter coordinates in the format described with \n"
                  "values within the board")
            player_fire(player_board, computer_board, boardsize, p_hits,
                        c_hits, players_turn, ships_remaining,
                        computer_board_for_player)

    players_turn = False
    main_game(player_board, computer_board, boardsize, p_hits, c_hits,
              players_turn, ships_remaining, computer_board_for_player)
    return players_turn, ships_remaining


def check_ship_sunk(ship_value, board, boardsize, is_player):
    """
    Function which checks whether or not a ship has been sunk after a hit.
    Takes the hit ship value and scans the remaining board to see if that
    value is still present or not.
    """
    print("Checking for sunk ship")
    y = boardsize*boardsize
    x = 0
    board_ship_check = board[1:]
    ship_sunk = bool
    for row in board_ship_check:
        row_ship_check = row[1:]
        for item in row_ship_check:
            x += 1
            if item == ship_value:
                print("Ship remaining")
                ship_sunk = False
                break
            elif x == y:
                if is_player is True:
                    print(Fore.GREEN + "We sunk an enemy ship!")
                    print(Style.RESET_ALL)
                else:
                    print(Fore.RED + "The enemy sunk one of our ships!")
                    print(Style.RESET_ALL)
        if ship_sunk is False:
            break


def main_game(player_board, computer_board, boardsize, p_hits, c_hits,
              players_turn, ships_remaining, computer_board_for_player):
    """
    Function which controls the player fire, computer fire, and ends the game
    when no ships are left on one of the boards
    """
    print(Fore.RED + "Enemy ships Captain. .")
    print(Style.RESET_ALL)
    while ships_remaining is not False:
        if players_turn is True:
            print(Fore.GREEN + "Our ship positions Captain")
            print(Style.RESET_ALL)
            display_board(player_board)
            print(Fore.GREEN + "This is where we have fired Captain")
            print(Style.RESET_ALL)
            display_board(computer_board_for_player)
            fire_instructions(boardsize)
            player_fire(player_board, computer_board, boardsize, p_hits,
                        c_hits, players_turn, ships_remaining,
                        computer_board_for_player)
        else:
            computer_fire(player_board, computer_board, boardsize, p_hits,
                          c_hits, players_turn, ships_remaining,
                          computer_board_for_player)
    end_game(c_hits, p_hits)


def place_ship(board, boardsize):
    """
    Function which places ships on the human user and computer gameboard,
    uses ship value in dict to determine length
    """
    numbers_to_select = []
    for item in range(boardsize):
        numbers_to_select.append(item)
    for ship in SHIPS:
        temp_ship_length = range(ship["value"])
        ship_length = len(temp_ship_length)
        row_number = random.randrange(1, len(numbers_to_select))
        chosen_row = numbers_to_select[row_number]
        end_value = boardsize - ship_length
        grid = random.randrange(1, end_value)
        for i in range(ship_length):
            board[chosen_row][grid + i] = ship_length
        numbers_to_select.pop(row_number)
    return board


def display_board(board):
    """
    Simple function to be called to show playerboard row by row, making it
    much easier to see where the computer has fired.
    """
    for row in board:
        x = 0
        for char in row:
            x += 1
            if x < len(row):
                print(char, end=" ")
            else:
                print(char)


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
    columns = [i for i in range(0, len(blank_board)+1)]
    blank_board.insert(0, columns)
    player_board = copy.deepcopy(blank_board)
    computer_board = copy.deepcopy(blank_board)
    computer_board_for_player = copy.deepcopy(blank_board)
    player_board = place_ship(player_board, boardsize)
    computer_board = place_ship(computer_board, boardsize)
    print("Blank computer board", computer_board_for_player)
    print("Player board")
    display_board(player_board)
    print("Computer board", computer_board)
    p_hits = 0
    c_hits = 0
    players_turn = True
    ships_remaining = True
    main_game(player_board, computer_board, boardsize, p_hits, c_hits,
              players_turn, ships_remaining, computer_board_for_player)
    return player_board, computer_board, boardsize


def game_select():
    """
    Function which displays welcome message and gets
    initial choice from user on board size
    """
    print("Please select a game board size")
    print("6 = 6x6 game board")
    print("10 = 10x10 game board")
    userinput = input("Enter 6 or 10: \n")

    boardsize = int(userinput)

    if boardsize == 6:
        create_board(boardsize)
    elif boardsize == 10:
        create_board(boardsize)
    else:
        print(f"Sorry {boardsize} isn't valid, please enter either 10 or 6")
        game_select()


print(Back.CYAN, Fore.WHITE + "Welcome to Battleships!",
      emoji.emojize(":grinning_face_with_big_eyes:"))
print(Style.RESET_ALL)
game_select()
