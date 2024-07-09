def print_board(board):
    print("A  B  C  D  E  F  G")
    for i, row in enumerate(board):
        print('  '.join(str(cell) for cell in row))


def choice_translate(choice):
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
    else:
        print("Not an Option")
    return column


def place(board, turn, column):
    row = 0
    for i in board:
        row += 1
        if board[row-1][column] != "○":
            if turn == True:
                board[row-2][column] = "✪"
                break
            else:
                board[row-2][column] = "◍"
                break
        elif row == 6:
            if turn == True:
                board[row-1][column] = "✪"
                break
            else:
                board[row-1][column] = "◍"
                break


def check_horizontal_win(board):
    for row in board:
        player_one_win = 0
        player_two_win = 0
        for i in row:
            if i == "●":
                player_one_win += 1
                if player_one_win == 4:
                    return True
            else:
                player_one_win = 0

            if i == "◍":
                player_two_win += 1
                if player_two_win == 4:
                    return True 
            else:
                player_two_win = 0
    return False


def check_vertical_win(board):
    player_one_win = 0
    player_two_win = 0
    col = -1
    while col < 6:
        col += 1
        for row in board:
            if row[col] == "●":
                player_one_win += 1
                if player_one_win == 4:
                    return True
            else:
                player_one_win = 0
            
            if row[col] == "◍":
                player_two_win += 1
                if player_two_win == 4:
                    return True
            else:
                player_two_win = 0
        return False



def check_diagonal(board):
    rows = len(board)
    cols = len(board[0])
    for row in range(rows):
        for col in range(cols):
            if row + 3 < rows and col + 3 < cols:
                if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] and board[row][col] == "●" or board[row][col] == "◍":
                    return True
            if row + 3 < rows and col - 3 >= 0:
                if board[row][col] == board[row + 1][col - 1] == board[row + 2][col - 2] == board [row + 3][col - 3] and board[row][col] == "●" or board[row][col] == "◍":
                    return True
    return False


def not_a_column():
    print("Not a valid column!\nPlease select a column from A-G!")

def full_column():
    print("This column is full! Please select anther column!")