import time
import os


def print_board(board): #prints the board nicely
    print("A  B  C  D  E  F  G")
    for index, row in enumerate(board):     #"index, row" => a single tuple (1, something)
        print('  '.join(str(i) for i in row)) #learn more about this!!!


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


def place(board, turn, column): #determines if where to positon the piece
    clear_screen_os()
    row = -1
    for i in board:
        row += 1 
        if turn == True and board[row][column] == "○": #player 1 animation
            board[row][column] = "✪"
            print_board(board)
            time.sleep(0.1)
            board[row][column] = "○"

        elif turn == False and board[row][column] == "○": #player 2 animation
            board[row][column] = "◍"
            print_board(board)
            time.sleep(0.1)
            board[row][column] = "○"

        if board[row][column] != "○": #checks if a position is occupied and if so, palces a piece above
            if turn == True:
                board[row-1][column] = "✪"
                break
            else:
                board[row-1][column] = "◍"
                break
        elif row == 5: #checks if it has reached the bottom of the board
            if turn == True:
                board[row][column] = "✪"
                break
            else:
                board[row][column] = "◍"
                break
        clear_screen_os()


def check_horizontal_win(board): #self explanatory
    for row in board:
        player_one_win = 0 #resets the "scores" when a new line begins
        player_two_win = 0
        for i in row:
            if i == "✪": #counting consecutive pieces of player 1
                player_one_win += 1
                if player_one_win == 4:
                    return True
            else:
                player_one_win = 0 #resets if theres a piece other than player 1's

            if i == "◍": #counting consecutive pieces of player 2
                player_two_win += 1
                if player_two_win == 4:
                    return True 
            else:
                player_two_win = 0 #resets if theres a piece other than player 2's
    return False


def check_vertical_win(board): #self explanatory
    player_one_win = 0
    player_two_win = 0
    col = -1
    while col <= 5: #uhh.. what? check on this
        col += 1
        for row in board:
            if row[col] == "✪": #counting consecutive pieces of player 1
                player_one_win += 1
                if player_one_win == 4:
                    return True
            else:
                player_one_win = 0
            
            if row[col] == "◍": #counting consecutive pieces of player 2
                player_two_win += 1
                if player_two_win == 4:
                    return True
            else:
                player_two_win = 0
    return False



def check_diagonal(board): #self explanatory
    rows = len(board) #measure the board
    cols = len(board[0])
    for row in range(rows):
        for col in range(cols):
            if row + 3 < rows and col + 3 < cols:
                if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] and board[row][col] == "✪" or board[row][col] == "◍":
                    return True
            if row + 3 < rows and col - 3 >= 0:
                if board[row][col] == board[row + 1][col - 1] == board[row + 2][col - 2] == board [row + 3][col - 3] and board[row][col] == "✪" or board[row][col] == "◍":
                    return True
    return False


def not_a_column(board):
    clear_screen_os()
    print("Not a valid column!\nPlease select a column from A-G!")
    time.sleep(3)
    clear_screen_os()
    

def full_column():
    print("This column is full! Please select anther column!")