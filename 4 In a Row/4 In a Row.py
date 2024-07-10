import functions as fns


###################################################################VRIABLES

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

###################################################################THE GAME

while win_vert == False and win_hor == False and win_diag == False and board_full == False:
    fns.print_board(board)
    if turn == True: #player 1 turn
        choice = input("Choose a column "+player_one_name+": ")
        if choice.lower() not in ["a", "b", "c", "d", "e", "f", "g"]: #checks for a valid input
            fns.not_a_column(board)
        else:
            column = fns.choice_translate(choice) #decides where the piece will end up
            if board [0][column] == "○": #checks i fthe column is not full
                fns.place(board, turn, column)
                fns.print_board(board)
                win_vert = fns.check_vertical_win(board)
                win_hor = fns.check_horizontal_win(board)
                win_diag = fns.check_diagonal(board)
                board_full = fns.full_board(board)
                turn = False
                fns.clear_screen_os()
            else:
                fns.full_column()
    
    elif turn == False: #player 2 turn
        choice = input("Choose a column "+player_two_name+": ")
        if choice.lower() not in ["a", "b", "c", "d", "e", "f", "g"]:
            fns.not_a_column(board)
        else:  
            column = fns.choice_translate(choice)
            if board [0][column] == "○":
                fns.place(board, turn, column)
                fns.print_board(board)
                win_vert = fns.check_vertical_win(board)
                win_hor = fns.check_horizontal_win(board)
                win_diag = fns.check_diagonal(board)
                board_full = fns.full_board(board)
                turn = True
                fns.clear_screen_os()
            else:
                fns.full_column()

###################################################################END OF GAME

fns.print_board(board)
if board_full == True: #checks if the board is full
    print("It's a tie!")
else: #determines who won
    if turn == False:
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")




    


