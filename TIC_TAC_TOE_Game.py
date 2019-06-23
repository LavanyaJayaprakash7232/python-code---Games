'''
CODE FOR "TIC TAC TOE" GAME
'''


#Function 1: To dispaly the board
def display_board(board):
    print ('   |   |')
    print (' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print ('   |   |')
    print ('-'*11)
    print ('   |   |')
    print (' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print ('   |   |')
    print ('-'*11)
    print ('   |   |')
    print (' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print ('   |   |')

#Function 2: To know about players choice marker = x or o
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want marker "X" or "O"? \t').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

#Function 3: Toss - choosing randomly
import random
def toss():
    if random.randint(0,1) == 0:
        return "Player 1"
    else:
        return "Player 2"
    
#Function 4: To assign the marker at the entered position
def place_marker(board, marker, position):
    board[position] = marker

#Function 5: To know whether position entered by the player is availble
def space_check(board, position):
    return board[position] == ' '

#Function 6: To know about the position where player is wants to enter the marker
def choose_position(board):
    position = 0
    while position not in range(1,10) or not space_check(board, position):
        position = int(input("Choose the position (1-9): \t"))

    return position

#Function 7: To check whether any player has won
def win_check(board, marker):
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or (board[4] == marker and board[5] == marker and board[6] == marker) or (board[7] == marker and board[8] == marker and board[9] == marker) or (board[1] == marker and board[4] == marker and board[7] == marker) or (board[2] == marker and board[5] == marker and board[8] == marker) or (board[3] == marker and board[6] == marker and board[9] == marker) or (board[1] == marker and board[5] == marker and board[7] == marker) or (board[1] == marker and board[5] == marker and board[9] == marker))
  
#Function 8: To check whether all the boxes were filled
def full_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False

    return True

#Function 9: To know whether the players are interested to play again
def replay():
    return input("Do you want to play again? Enter yes or no:\t")



print("WELCOME TO TIC TAC TOE XOXOXO\n")

print(' ' *100)

while True:
    playboard = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = toss()
    print ( turn + ' will play first' )

    play_game = input('Are you ready to start the game? Enter yes or no:\t ')

    if play_game[0].lower() == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
            #player 1's turn 
            display_board(playboard)
            print (turn)
            position = choose_position(playboard)
            place_marker(playboard, player1_marker, position)

            if win_check(playboard, player1_marker):
                display_board(playboard)
                print('Congratulations Player 1 !! You won the game ')
                game_on = False

            else:
                if full_check(playboard):
                    display_board(playboard)
                    print("Hey it's a tie! The game is draw")
                    break
                else:
                    turn = 'Player 2'

        else:
             #player 2's turn
             display_board(playboard)
             print (turn)
             position = choose_position(playboard)
             place_marker(playboard, player2_marker, position)

             if win_check(playboard, player2_marker):
                 display_board(playboard)
                 print ('Congratulations Player 2 !! You won the game ')
                 game_on = False

             else:
                 if full_check(playboard):
                     display_board(playboard)
                     print ("Hey it's a tie! The game is draw ")
                     break
                 else:
                      turn = 'Player 1'

    if not replay():
          break

                 
             
