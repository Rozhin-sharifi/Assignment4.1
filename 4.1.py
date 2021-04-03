from termcolor import colored
import time
import random

def game_timer():
    end_time=time.time()
    elapsed_time=end_time-start
    print ('elapsed_time: ', elapsed_time)
    exit()

def show():
    for i in range(3):
        for j in range(3):
            if game[i][j]=='X':
                print (colored(game[i][j],'red'),end=' ')
            elif game [i][j]=='O':
                print (colored(game[i][j],'green'),end=' ')
            else:
                print(game[i][j],end=' ')
        print()

def check():
    if game[0][0]=='X'and game[1][1]=='X'and game[2][2]=='X' or game[0][2]=='X'and game[1][1]=='X'and game[2][0]=='X':
        print ('player 1 wins')
        game_timer()
    elif game[0][0]=='O'and game[1][1]=='O'and game[2][2]=='O' or game[0][2]=='O'and game[1][1]=='X'and game[2][0]=='X':
        print ('player 2 wins')
        game_timer()
    else:
        for i in range(3):
            if game[i][0]=='X' and game[i][1]=='X' and game [i][2]=='X':
                print ('player 1 wins')
                game_timer()
            elif game[0][i]=='X' and game[1][i]=='X' and game [2][i]=='X':
                print ('player 1 wins')
                game_timer()
            elif game[i][0]=='O' and game[i][1]=='O' and game [i][2]=='O':
                print ('player 2 wins')
                game_timer()
            elif game[0][i]=='O' and game[1][i]=='O' and game [2][i]=='O':
                print ('player 2 wins')
                game_timer()
            elif sum([row.count('-') for row in game])==0:
                print ('equal')
                game_timer()


def two_player():
    while True:

        # player 1
        while True:
            row = int(input('please enter row number\n'))
            col = int(input('please enter col number\n'))
            if 0 <= row <= 2 and 0 <= col <= 2:
                if game[row][col]=='-':
                    game[row][col] = 'X'
                    break
                else:
                    print('it is not empty')      
            else:
                print('index out of range! try again')
        show()
        check()
    # player2
        while True:
            row = int(input('please enter row number\n'))
            col = int(input('please enter row number\n'))

            if 0 <= row <= 2 and 0 <= col <= 2:
                if game[row][col]=='-':
                    game[row][col] = 'O'
                    break
                else:
                    print('it is not empty') 
            else:
                print('index out of range! try again')
        show()
        check()


def one_player():
    while True:

        # player 1
        while True:
            row = int(input('please enter row number\n'))
            col = int(input('please enter col number\n'))
            if 0 <= row <= 2 and 0 <= col <= 2:
                if game[row][col]=='-':
                    game[row][col] = 'X'
                    break
                else:
                    print('it is not empty')      
            else:
                print('index out of range! try again')
        show()
        check()
    # player2
        while True:
            row = random.randint(0,2)
            col = random.randint(0,2)

            if 0 <= row <= 2 and 0 <= col <= 2:
                if game[row][col]=='-':
                    game[row][col] = 'O'
                    break
                else:
                    print('it is not empty') 
            else:
                print('index out of range! try again')
        show()
        check()




start=time.time()
game = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]

show()
game_mode=int(input('select game mode: 1-one_player 2-two_player\n'))
if game_mode==1:
    one_player()
elif game_mode==2:
    two_player()
