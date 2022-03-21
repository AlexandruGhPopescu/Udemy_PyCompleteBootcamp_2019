''' Here we go '''


import sys

print("**XO** Welcome to TIC-TAC-TOE **OX**")

player_1_sign = ''
player_2_sign = ''


# Users choose X or O
def choose_sides():
    global player_1_sign
    global player_2_sign

    player_1_sign = input("\n\t\tHello Player 1 :)\
                           \n\t\tPlease choose 'x' or 'o': ")

    while (player_1_sign not in ['x', 'o']):
        print(f"\n\tMnope, only 'x's and 'o's please!")
        player_1_sign = input("\n\t\tPlease choose 'x' or 'o': ")

    if player_1_sign == 'x':
        player_2_sign = 'o'
        print(
            f"\t\t\tPlayer1: {player_1_sign}\n\t\t\tPlayer2: {player_2_sign}\n")

    elif player_1_sign == 'o':
        player_2_sign = 'x'
        print(
            f"\t\t\tPlayer1: {player_1_sign}\n\t\t\tPlayer2: {player_2_sign}\n")


#### THE TIC-TAC-TOE ####

def tictactoe_start():

    choose_sides()

    # variables to store the succesive moves of each player
    move_store_player1 = ''
    move_store_player2 = ''

    # list to check the wining combinations
    # winning_positions_sets = ['123', '456', '789',
    #                           '147', '258', '369', '357', '159']

    winning_positions_sets = {'set1': ['1', '2', '3'], 'set2': ['4', '5', '6'], 'set3': ['7', '8', '9'],
                              'set4': ['1', '4', '7'], 'set5': ['2', '5', '8'], 'set6': ['3', '6', '9'],
                              'set7': ['3', '5', '7'], 'set8': ['1', '5', '9']}

    # dictionary of posible positions - as the game progreses each key(position) will marked with the played character
    position_map = {'1': ' ', '2': ' ', '3': ' ', '4': ' ',
                    '5': ' ', '6': ' ', '7': ' ', '8': ' ',  '9': ' '}

    # variables to order the moves ascendig and check if they match the winning positions
    win_check_player1 = []
    win_check_player2 = []

    # the game is split in 5 rounds with 2 moves per round (one move from each player)
    for turn_count in range(1, 6):
        global board

        print(f"\n\tRound {turn_count}:")

        ###### PLAYER 1 ######
        p1_move = input("\t\tPlayer1's turn: ")

        # check to see that the position was not filled/played before and that the input is correct
        while position_map[p1_move] != ' ' or p1_move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print(f"\tInvalid move :/ Please try again!")
            p1_move = input("\t\tPlayer1's turn: ")

        # storing the move for player_1
        move_store_player1 = move_store_player1 + p1_move
        ''' print(f"\t\t\tmove_store_player1: {move_store_player1}\n\t\t\tmove_store_player2: {move_store_player2}")'''

        # completing the game board - blocking the played position for the next check
        position_map[p1_move] = player_1_sign
        ''' print(f"\t\t\tposition_map: {position_map}")'''

        # board drawing
        board = '\t\t\t   |   |   \n' + \
            '\t\t\t ' + position_map['7'].upper() + ' | ' + position_map['8'].upper() + ' | ' + position_map['9'].upper() + ' \n' + \
            '\t\t\t   |   |   \n' + \
            '\t\t\t-----------\n' + \
            '\t\t\t   |   |   \n' + \
            '\t\t\t ' + position_map['4'].upper() + ' | ' + position_map['5'].upper() + ' | ' + position_map['6'].upper() + ' \n' + \
            '\t\t\t   |   |   \n' + \
            '\t\t\t-----------\n' + \
            '\t\t\t   |   |   \n' + \
            '\t\t\t ' + position_map['1'].upper() + ' | ' + position_map['2'].upper() + ' | ' + position_map['3'].upper() + ' \n' + \
            '\t\t\t   |   |   \n'

        print("\n" * 20)
        print(board)

        # checking to see if this move has completed a wining sets
        win_check_player1 = list(move_store_player1)

        for set in winning_positions_sets.values():
            # print(f"\n\t the set is: {set}")
            # print(f"\n\t the win_check_player1 is: {win_check_player1}")

            if all(elem in win_check_player1 for elem in set):
                print(f"\n\t====================================\
                            \n\n\t======= !!! Player 1 WON !!! =======\
                            \n\n\t====================================\n\n")
                sys.exit(0)

        # ending the game as a tie - player2 has one move less than player1
        if not(' ' in position_map.values()):
            print(f"\n\t===========================\
                        \n\n\t======= >>> TIE <<< =======\
                        \n\n\t===========================\n\n")
            sys.exit(0)

        ###### PLAYER 2 ######
        p2_move = input("\t\tPlayer2's turn: ")

        # check to see that the position was not filled/played before and that the input is correct
        while position_map[p2_move] != ' ' or p2_move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print(f"\tInvalid move :/ Please try again!")
            p2_move = input("\t\tPlayer2's turn: ")

        # storing the move for player_2
        move_store_player2 = move_store_player2 + p2_move
        '''print(f"\t\t\tmove_store_player1: {move_store_player1}\n\t\t\twin_check_player2: {move_store_player2}")'''

        # completing the game board - blocking the played position for the next check
        position_map[p2_move] = player_2_sign
        '''print(f"\t\t\tposition_map: {position_map}")'''

        # board drawing
        board = '\t\t\t   |   |   \n' + \
            '\t\t\t ' + position_map['7'].upper() + ' | ' + position_map['8'].upper() + ' | ' + position_map['9'].upper() + ' \n' + \
            '\t\t\t   |   |   \n' + \
            '\t\t\t-----------\n' + \
            '\t\t\t   |   |   \n' + \
            '\t\t\t ' + position_map['4'].upper() + ' | ' + position_map['5'].upper() + ' | ' + position_map['6'].upper() + ' \n' + \
            '\t\t\t   |   |   \n' + \
            '\t\t\t-----------\n' + \
            '\t\t\t   |   |   \n' + \
            '\t\t\t ' + position_map['1'].upper() + ' | ' + position_map['2'].upper() + ' | ' + position_map['3'].upper() + ' \n' + \
            '\t\t\t   |   |   \n'

        print("\n" * 20)
        print(board)

        # checking to see if this move has completed a wining sets
        win_check_player2 = list(move_store_player2)

        for set in winning_positions_sets.values():
            # print(f"\n\t the set is: {set}")
            # print(f"\n\t the win_check_player1 is: {win_check_player1}")

            if all(elem in win_check_player2 for elem in set):
                print(f"\n\t====================================\
                            \n\n\t======= !!! Player 2 WON !!! =======\
                            \n\n\t====================================\n\n")
                sys.exit(0)


tictactoe_start()
