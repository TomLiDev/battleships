import random
import copy
import sys
from colorama import Fore, Back, Style, init
import emoji
init(autoreset=True)

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
c_hits = int
p_hits = int


def end_game(c_hits, p_hits):
    """
    Function which is called when either computer or player hit counter
    reaches 10, signalling all ships have been sunk.
    """
    if p_hits > c_hits:
        print(Fore.GREEN + "Congratulations Captain, you won!")
        print(emoji.emojize(":grinning_face_with_big_eyes:"))
        replay = input("Would you like to play again? (y/n): \n")
        if replay == "n":
            sys.exit()
        elif replay == "y":
            game_select()
    else:
        print(Fore.RED + "Captain we've been sunk, you lost")
        replay = input("Would you like to play again? (y/n): \n")
        if replay == "n":
            sys.exit()
        elif replay == "y":
            game_select()


def computer_fire(player_board, computer_board, boardsize, p_hits, c_hits,
                  players_turn, ships_remaining, computer_board_for_player):
    """
    Function for controlling computer return fire on players board
    Creates random grid references for fire selection. This is then stored
    in computer shots store, which is used for validation for future shots
    to make sure the computer can't fire on the same coordinates.
    """
    computer_row_fire = random.randrange(1, boardsize)
    computer_column_fire = random.randrange(1, boardsize)
    computer_grid_fire = computer_row_fire, computer_column_fire

    if computer_grid_fire in computer_shots_store:
        computer_fire(player_board, computer_board, boardsize, p_hits, c_hits,
                      players_turn, ships_remaining, computer_board_for_player)
    else:
        computer_shots_store.append(computer_grid_fire)
        print(Fore.RED + "Enemy fire incoming!")
        if player_board[computer_row_fire][computer_column_fire] != 0:
            print(Fore.RED + "Captain we've been hit!")
            ship_value = player_board[computer_row_fire][computer_column_fire]
            player_board[computer_row_fire][computer_column_fire] = "H"
            check_ship_sunk(ship_value, computer_board, boardsize, False)
            c_hits += 1
            print("Enemy hits", c_hits)
            if c_hits == 10:
                ships_remaining = False
            else:
                ships_remaining = True
        else:
            print(Fore.RED + "The enemy missed")
            player_board[computer_row_fire][computer_column_fire] = "X"
            ships_remaining = True
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
        print("Please enter a row and column reference separeted by a comma\n"
              "e.g. B,3. The row reference must be A - F\n"
              "The column reference be 1 - 6 \n")
    elif boardsize == 10:
        print("Please enter a row and column reference separeted by a comma\n"
              "e.g. B,3. The row reference must be A - J\n"
              "and the column reference be 1 - 10\n")


def player_fire(player_board, computer_board, boardsize, p_hits, c_hits,
                players_turn, ships_remaining, computer_board_for_player):
    """
    Function which takes input from player to fire on the computer board,
    carried out multiple validation checks to ensure fire will be accepted
    or asks the player to retry entering coordinates accordingly.
    List comprehension code for creating row_references adapted from external
    source. Details in readme.
    """
    user_grid_fire = input("Enter fire reference e.g B,3: \n")
    if user_grid_fire in player_shots_store:
        print(Fore.GREEN + "Captain we have alrady fired on those coordinates")
        player_fire(player_board, computer_board, boardsize, p_hits, c_hits,
                    players_turn, ships_remaining, computer_board_for_player)
    else:
        try:
            player_shots_store.append(user_grid_fire)
            split_fire_reference = user_grid_fire.split(",")
            column_ref = int(split_fire_reference[1])
            player_row_ref = (split_fire_reference[0])
            row_references = [item[0] for item in computer_board]
            column_references = computer_board[0]
            ships_remaining = bool
            if player_row_ref not in row_references:
                print("Invalid row")
                player_fire(player_board, computer_board, boardsize, p_hits,
                            c_hits, players_turn, ships_remaining,
                            computer_board_for_player)
            if column_ref not in column_references:
                print("Invalid column")
                player_fire(player_board, computer_board, boardsize, p_hits,
                            c_hits, players_turn, ships_remaining,
                            computer_board_for_player)
        except IndexError:
            print(Fore.GREEN + "Invalid fire coordinates Captain")
            print("please enter coordinates in the format described with \n"
                  "values within the board")
            player_fire(player_board, computer_board, boardsize, p_hits,
                        c_hits, players_turn, ships_remaining,
                        computer_board_for_player)
    player_fire_placement(user_grid_fire, computer_board_for_player,
                          computer_board, boardsize, player_board, p_hits,
                          c_hits)
    return players_turn, ships_remaining


def player_fire_placement(user_grid_fire, computer_board_for_player,
                          computer_board, boardsize, player_board, p_hits,
                          c_hits):
    """
    Function which takes validated player fire coordinates and checks if they
    have hit or missed, prints relevant messages to communicate to player,
    and returns the game board accordingly.
    """
    split_fire_reference = user_grid_fire.split(",")
    column_ref = int(split_fire_reference[1])
    for row in computer_board:
        if row[0] == split_fire_reference[0]:
            row_ref = computer_board.index(row)
            if row[column_ref] != 0:
                print(Fore.GREEN + "Hit! Good shot Captain",
                      emoji.emojize(":grinning_face_with_big_eyes:"))
                ship_value = row[column_ref]
                row[column_ref] = "H"
                check_ship_sunk(ship_value, computer_board, boardsize,
                                True)
                p_hits += 1
                computer_board_for_player[row_ref][column_ref] = "H"
                if p_hits == 10:
                    ships_remaining = False
                else:
                    ships_remaining = True
            else:
                print(Fore.GREEN + "We missed Captain")
                row[column_ref] = "X"
                computer_board_for_player[row_ref][column_ref] = "X"
                ships_remaining = True
    players_turn = False
    main_game(player_board, computer_board, boardsize, p_hits, c_hits,
              players_turn, ships_remaining, computer_board_for_player)
    return computer_board, computer_board_for_player


def check_ship_sunk(ship_value, board, boardsize, is_player):
    """
    Function which checks whether or not a ship has been sunk after a hit.
    Takes the hit ship value and scans the remaining board to see if that
    value is still present or not.
    """
    y = boardsize*boardsize
    x = 0
    board_ship_check = board[1:]
    ship_sunk = bool
    for ship in SHIPS:
        if ship["value"] == ship_value:
            ship_name = ship["name"]
    for row in board_ship_check:
        row_ship_check = row[1:]
        for item in row_ship_check:
            x += 1
            if item == ship_value:
                ship_sunk = False
                break
            elif x == y:
                if is_player is True:
                    print(Fore.GREEN + f"We sunk an enemy {ship_name}!")
                    print(Style.RESET_ALL)
                else:
                    print(Fore.RED + f"The enemy sunk our {ship_name}!")
                    print(Style.RESET_ALL)
        if ship_sunk is False:
            break


def main_game(player_board, computer_board, boardsize, p_hits, c_hits,
              players_turn, ships_remaining, computer_board_for_player):
    """
    Function which controls the player fire, computer fire, and ends the game
    when no ships are left on one of the boards
    """
    while ships_remaining is not False:
        if players_turn is True:
            print(Fore.GREEN + "Our ship positions")
            display_board(player_board)
            print(Fore.GREEN + "This is where we have fired Captain")
            display_board(computer_board_for_player)
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
    Simple function to be called to show player and computer board row by row,
    this produces a much better view of the board for the player and allows
    Colorama styling.
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
    based on user selection. List comprehension code is adapted from external
    source, details in readme.
    """
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
    p_hits = 0
    c_hits = 0
    players_turn = True
    ships_remaining = True
    fire_instructions(boardsize)
    main_game(player_board, computer_board, boardsize, p_hits, c_hits,
              players_turn, ships_remaining, computer_board_for_player)
    return player_board, computer_board, boardsize


def instructions():
    """
    Simple optional function which displays instruction text to player if
    they choose it.
    """
    print("Battleships! Is a python driven game based on the classic\n"
          "battleships boardgame.\n"
          "The aim of the game is to sink all the enemy ships before yours\n"
          "are sunk. After your choice of game board size, the game will\n"
          "randomly place your ships on your board and these positions are\n"
          "displayed to you.\n"
          "4 = Battleship\n"
          "3 = Cruiser\n"
          "2 = Destroyer\n"
          "1 = Submarine\n"
          "You will then have the option to choose where you will fire on\n"
          "the enemies board. This must be entered with a captial letter to\n"
          "select the row, and a number to select the column, as you would\n"
          "with map coordinates. These two characters must be separated by\n"
          "a comma. Eg. A,4.\n"
          "The game will tell you if you have hit or missed the computers\n"
          "ships, and your shots will be displayed on a separate board for\n"
          "you to view. An X represents a missed hit, a H represents a hit\n"
          "After each of your shots, the computer will return fire, if they\n"
          "hit/miss you this will be displayed with X/H, with messages from\n"
          "the game to confirm this. Keep firing until you have sunk all\n"
          "the computers ships or they have sunk yours.\n"
          "Good luck Captain!")
    game_select()


def game_select():
    """
    Function which displays welcome message and gets
    initial choice from user on board size
    """
    instruct_choice = input("View game instructions? (y/n): \n")
    if instruct_choice == "y":
        instructions()
    else:
        print("Please select a game board size")
        print("6 = 6x6 game board")
        print("10 = 10x10 game board")
        userinput = input("Enter 6 or 10: \n")
        try:
            boardsize = int(userinput)
            if boardsize == 6:
                create_board(boardsize)
            elif boardsize == 10:
                create_board(boardsize)
            else:
                print(f"Sorry {boardsize} isn't valid, please enter 10 or 6")
                game_select()
        except ValueError:
            print("Please enter 6 or 10")


print(Fore.BLACK, Back.CYAN + Style.BRIGHT + "Welcome to Battleships!",
      emoji.emojize(":grinning_face_with_big_eyes:"))
game_select()
