import colorama
from colorama import Fore

colorama.init(autoreset=True)

# ----- Global variables ----- #
board = ["#",
         " ", " ", " ",
         " ", " ", " ",
         " ", " ", " ", ]

player = "X"

game_is_over = True


# ----- Functions -----#
# 1) Display function
def display_board():
    print(f" {board[1]} | {board[2]} | {board[3]}")
    print("---+---+---")
    print(f" {board[4]} | {board[5]} | {board[6]}")
    print("---+---+---")
    print(f" {board[7]} | {board[8]} | {board[9]}")


# 2) input function for players
def handle_player():
    global player
    print(f"{player}'s turn")

    valid = False

    position = int(input("Choose a number between 1-9: "))
    while not valid:
        while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            position = int(input(Fore.YELLOW + "Choose a number between 1-9: "))

        if board[position] == " ":
            valid = True
        else:
            print(Fore.RED + f"That position {position} is already taken")
            position = int(input(Fore.YELLOW + "Choose a number between 1-9: "))

    board[position] = player
    display_board()


# 3) change the players input

def flip_player():
    global player

    if player == 'X':
        player = 'O'
    else:
        player = 'X'


# 4) winner checker
def is_winner():
    top = (board[7] == board[8] == board[9] != " ")  # across the top
    middle = (board[4] == board[5] == board[6] != " ")  # across the middle
    bottom = (board[1] == board[2] == board[3] != " ")  # across the bottom
    row_1 = (board[7] == board[4] == board[1] != " ")  # down the middle
    row_2 = (board[8] == board[5] == board[2] != " ")  # down the middle
    row_3 = (board[9] == board[6] == board[3] != " ")  # down the right side
    diagonal1 = (board[7] == board[5] == board[3] != " ")  # diagonal
    diagonal2 = (board[9] == board[5] == board[1] != " ")  # diagonal
    global game_is_over, player
    # ----- if any one statement is true then the player is win ----#
    if top or middle or bottom:
        print(Fore.BLUE + f"{player}'s is win")
        game_is_over = False
    elif row_1 or row_2 or row_3:
        print(Fore.BLUE + f"{player}'s is win")
        game_is_over = False
    elif diagonal1 or diagonal2:
        print(Fore.BLUE + f"{player}'s is win")
        game_is_over = False
    # ---- if all above statements are False the game become tie ---#
    elif " " not in board:
        print(Fore.YELLOW + 'Game is Tie')
        game_is_over = False


# 5) here play game

def play_game():
    handle_player()
    is_winner()
    flip_player()


# ----- output -----#
display_board()
while game_is_over:
    play_game()
