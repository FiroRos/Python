board = [
   # A  B  C  D  E  F  G
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

turn = True
win_vert = False
win_diag =  False
win_hor = False

def print_board():
    print(" A  B  C  D  E  F  G")
    for row in board:
        print(row)



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



def place(column):
    row = 0
    for i in board:
        row += 1
        if board[row-1][column] != 0:
            if turn == True:
                board[row-2][column] = 1
                break
            else:
                board[row-2][column] = 2
                break
        elif row == 6:
            if turn == True:
                board[row-1][column] = 1
                break
            else:
                board[row-1][column] = 2
                break


def check_horizontal_win():
    for row in board:
        player_one_win = 0
        player_two_win = 0
        for i in row:
            if i == 1:
                player_one_win += 1
                if player_one_win == 4:
                    return True
            else:
                player_one_win = 0

            if i == 2:
                player_two_win += 1
                if player_two_win == 4:
                    return True 
            else:
                player_two_win = 0


def check_vertical_win():
    player_one_win = 0
    player_two_win = 0
    col = -1
    while col < 6:
        col += 1
        for row in board:
            if row[col] == 1:
                player_one_win += 1
                if player_one_win == 4:
                    return True
            else:
                player_one_win = 0
            
            if row[col] == 2:
                player_two_win += 1
                if player_two_win == 4:
                    return True
            else:
                player_two_win = 0


def check_diagonal():
    rows = len(board)
    cols = len(board[0])
    for row in range(rows):
        for col in range(cols):
            if row + 3 < rows and col + 3 < cols:
                if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] == 1:
                    return True
            if row + 3 < rows and col - 3 >= 0:
                if board[row][col] == board[row + 1][col - 1] == board[row + 2][col - 2] == board [row + 3][col - 3] == 1:
                    return True


            
print_board()
while win_vert != True and win_hor != True and win_diag != True:
    if turn == True:
        choice = input("Player 1 Please Choose a Column: ")
        if choice.lower() not in ["a", "b", "c", "d", "e", "f", "g"]:
            print("Not a Valid Input!")
        else:
            column = choice_translate(choice)
            if board [0][column] == 0:
                place(column)
                print_board()
                win_vert = check_vertical_win()
                win_hor = check_horizontal_win()
                win_diag = check_diagonal()
                turn = False
            else:
                print("The column is full! Please select anther column!")
    

    elif turn == False:
        choice = input("Player 2 Please Choose a Column: ")
        if choice.lower() not in ["a", "b", "c", "d", "e", "f", "g"]:
            print("Not a Valid Input!")
        else:
            column = choice_translate(choice)
            if board [0][column] == 0:
                place(column)
                print_board()
                win_vert = check_vertical_win()
                win_hor = check_horizontal_win()
                win_diag = check_diagonal()
                turn = True
            else:
                print("The column is full! Please select anther column!")

if turn == False:
    print("Player 1 Wins!")
else:
    print("Player 2 Wins!")




    


