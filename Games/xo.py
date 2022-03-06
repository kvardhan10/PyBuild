import random
import time

# 00 01 02 03 04 05 06 -> 01 03 05 -> 1 2 3
# 10 11 12 13 14 15 16 -> 11 13 15 -> 4 5 6
# 20 21 22 23 24 25 26 -> 21 23 25 -> 7 8 9

wins =[123, 456, 789, 147, 258, 369, 159, 753]

x_pos = []
o_pos = []
winner = None
available_pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pos_dict = {
        1: (0, 1),
        2: (0, 3),
        3: (0, 5),
        4: (1, 1),
        5: (1, 3),
        6: (1, 5),
        7: (2, 1),
        8: (2, 3),
        9: (2, 5)
        }
board = [['|', '-', '|', '-', '|', '-', '|'],
         ['|', '-', '|', '-', '|', '-', '|'],
         ['|', '-', '|', '-', '|', '-', '|']]

def check_winner(player_pos, player):
    for a in range(0, len(player_pos)):
        for b in range(0, len(player_pos)):
            for c in range(0, len(player_pos)):
                sd = player_pos[a]*100 + player_pos[b]*10 + player_pos[c]
                if sd in wins:
                    print('\n', player, ' WINS')
                    exit(0)

def print_board():
    for i in board:
        print(' '.join(i))

def play():
    while len(available_pos) > 0:
        print('X\'s turn')
        x_sel = int(input('Where do you want to put X? Select (1-9): '))
        if x_sel in available_pos:
            board[pos_dict[x_sel][0]][pos_dict[x_sel][1]] = 'X'
            x_pos.append(x_sel)
            available_pos.remove(x_sel)
            print_board()
            check_winner(x_pos, 'X')
            print('X POS: ', x_pos)
            print('\n')
        else:
            print('Position already acquired. Try again\n')
            play()
        try:
            o_sel = random.choice(available_pos)
        except:
            print('DRAW')
        print('O Playing...')
        time.sleep(2)
        board[pos_dict[o_sel][0]][pos_dict[o_sel][1]] = 'O'
        o_pos.append(o_sel)
        available_pos.remove(o_sel)
        print_board()
        check_winner(o_pos, 'O')
        print('O POS: ', o_pos)
        print('\n')

print('WELCOME TO TicTacToe. YOU KNOW THE RULES')
print_board()
play()
