import time
import os



###############################################################PRINT FUNCTIONS

def print_board(board): #prints the board nicely
    print("A  B  C  D  E  F  G")
    for index, row in enumerate(board):     #"index, row" => a single tuple (1, something)
        print('  '.join(str(i) for i in row)) #learn more about this!!!


def not_a_column(board):
    clear_screen_os()
    print("Not a valid column!\nPlease select a column from A-G!")
    time.sleep(2)
    clear_screen_os()
    

def full_column():
    clear_screen_os()
    print("This column is full! Please select anther column!")
    time.sleep(2)
    clear_screen_os()

###############################################################TRANSLATORS

def clear_screen_os(): #clears terminal
    if os.name == "nt":  #nt == windows
        _ = os.system("cls")
    else: #mac & linux
        _ = os.system("clear")


def choice_translate(choice): #translates between letters to the column's index
    if choice.lower() == "a":
        column = 0
    elif choice.lower() == "b":
        column = 1
    elif choice.lower() == "c":
        column = 2
    elif choice.lower() == "d":
        column = 3
    elif choice.lower() == "e":
        column = 4
    elif choice.lower() == "f":
        column = 5
    elif choice.lower() == "g":
        column = 6
    return column

###############################################################CHECK FOR...

def place(board, turn, column):
    for row in range(len(board)):
        if board[row][column] == "○":  # Check for empty position
            if turn:
                board[row][column] = "✪"
            else:
                board[row][column] = "◍"
            print_board(board)
            time.sleep(0.1)
            clear_screen_os()
            board[row][column] = "○"
        else:  # If the position is occupied
            if row > 0:  # Place the piece above the occupied position
                if turn:
                    board[row-1][column] = "✪"
                else:
                    board[row-1][column] = "◍"
                break
        if row == len(board) - 1:  # If it has reached the bottom of the board
            if turn:
                board[row][column] = "✪"
            else:
                board[row][column] = "◍"
            break
    clear_screen_os()

def full_board(board): 
    places = 0
    for row in board: 
        for i in row:
            if i != "○": #counts occupied spaces
                places += 1
                if places == 42: #42 occupied spaces == empty places on the board
                    return True
    return False

###############################################################WINNING CONDITIONS

def check_horizontal_win(board): #self explanatory
    for row in board:
        player_one_win = 0 #resets the "scores" when a new line begins
        player_two_win = 0
        for i in row:
            if i == "✪": #counting consecutive pieces of player 1
                player_one_win += 1
                player_two_win = 0
                if player_one_win == 4:
                    return True
            elif i == "◍": #counting consecutive pieces of player 2
                player_two_win += 1
                player_one_win = 0
                if player_two_win == 4:
                    return True 
            else:
                player_one_win = 0 #resets if theres an empty place
                player_two_win = 0
    return False


def check_vertical_win(board): #self explanatory
    for col in range(len(board[0])): 
        player_one_win = 0
        player_two_win = 0
        for row in board:
            if row[col] == "✪": #counting consecutive pieces of player 1
                player_one_win += 1
                player_two_win = 0
                if player_one_win == 4:
                    return True
            elif row[col] == "◍": #counting consecutive pieces of player 2
                player_two_win += 1
                player_one_win = 0
                if player_two_win == 4:
                    return True
            else:
                player_two_win = 0
                player_one_win = 0
    return False

def check_diagonal(board): #self explanatory
    rows = len(board) #measure the board
    cols = len(board[0])
    for row in range(rows):
        for col in range(cols):
            if row + 3 < rows and col + 3 < cols: #checks if it has sapce for a "\" diagonal
                if (board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3]) and (board[row][col] == "✪" or board[row][col] == "◍"):
                    return True
            if row + 3 < rows and col - 3 >= 0: #checks if it has sapce for a "/" diagonal
                if (board[row][col] == board[row + 1][col - 1] == board[row + 2][col - 2] == board [row + 3][col - 3]) and (board[row][col] == "✪" or board[row][col] == "◍"):
                    return True
    return False

###############################################################

