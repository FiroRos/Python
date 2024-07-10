import functions



board = [
    ['○', '○', '○', '○', '○', '○', '○'],
    ['○', '○', '○', '○', '○', '○', '○'],
    ['○', '○', '○', '○', '○', '○', '○'],
    ['○', '○', '○', '○', '○', '○', '○'],
    ['○', '○', '○', '○', '○', '○', '○'],
    ['○', '○', '○', '○', '○', '○', '○']
]



turn = True #True == Player 1 turn |False == Player 2 turn
win_vert = False
win_diag = False
win_hor = False
player_one_name = input("Choose a name for player 1: ")
player_two_name = input("Choose a name for player 2: ")
board_full = False

while win_vert == False and win_hor == False and win_diag == False and board_full == False:
    functions.print_board(board)
    if turn == True: #player 1 turn
        choice = input("Choose a column "+player_one_name+": ")
        if choice.lower() not in ["a", "b", "c", "d", "e", "f", "g"]:
            functions.not_a_column(board)
        else:
            column = functions.choice_translate(choice)
            if board [0][column] == "○":
                functions.place(board, turn, column)
                functions.print_board(board)
                win_vert = functions.check_vertical_win(board)
                win_hor = functions.check_horizontal_win(board)
                win_diag = functions.check_diagonal(board)
                turn = False
                functions.clear_screen_os()
            else:
                functions.full_column()
    
    elif turn == False: #player 2 turn
        choice = input("Choose a column "+player_two_name+": ")
        if choice.lower() not in ["a", "b", "c", "d", "e", "f", "g"]:
            functions.not_a_column(board)
        else:  
            column = functions.choice_translate(choice)
            if board [0][column] == "○":
                functions.place(board, turn, column)
                functions.print_board(board)
                win_vert = functions.check_vertical_win(board)
                win_hor = functions.check_horizontal_win(board)
                win_diag = functions.check_diagonal(board)
                turn = True
                functions.clear_screen_os()
            else:
                functions.full_column()

functions.print_board(board)

if board_full == True:
    print("It's a tie!")
else:
    if turn == False:
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")




    


