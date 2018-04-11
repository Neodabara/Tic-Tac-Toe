import games
import random

'''
    CS316 TicTacToe Minimax demo program
'''

# play a game of TicTacToe


def play_ttt(game):

    # The initial state is a blank board
    state = game.initial

    # We'll cycle between the 2 players, X and O
    players = ['X', 'O']

    while True:
        turn = firstMove()
        print('The ' + turn + ' goes first')
        gameInProgress = True

        while gameInProgress:
            # Player turn
            if turn == 'Player':
                move = games.query_player(game, state)
                print('The ' + turn + ' made a move')

                # update the game state
                state = game.result(state, move)
                # game.display(state)
               # print()
                turn = 'Computer'

            # Computer turn
            else:
                move = games.alphabeta_player(game,state)
                print('The ' + turn + ' made a move')

                # update the game state
                state = game.result(state, move)
                # game.display(state)
                turn = 'Player'
            
            if game.terminal_test(state):
                game.display(state)
                return

# decide who goes first


def firstMove():
    if random.randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Player'


if __name__ == "__main__":
    game = games.TicTacToe()    # create a new game object
    play_ttt(game)              # play the game
