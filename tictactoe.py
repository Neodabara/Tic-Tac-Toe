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

    # Initial game mode choice
    while True:
        print("0) Exit",
              "1) Player vs Player",
              "2) Player vs Computer",
              "3) Computer vs Computer",
              sep="\n")
        
        choice = input("Enter choice: ")
        print()
        if choice == '0':
            return
        if choice in menu:
            menu[choice](state, players)


def playerVsPlayer(state, players):
    # Keep making moves until we reach a terminal state
    while True:
        for player in players:

            # Select a move based on alpha beta search
            move = games.query_player(game, state)

            # print("Player {} made a move:".format(player))
            print("Player {} made a move:".format(player))

            # Update the state/board of the game with the move
            state = game.result(state, move)
            game.display(state)
            print()

            # We're done once the game is over
            if game.terminal_test(state):
                return


def playerVsComputer(state, players):

    # Choose if Player or Computer goes first
    current = firstMove()

    # Keep making moves until we reach a terminal state
    while True:
        for player in players:

            # Select a move based on alpha beta search
            if current[player] == 'Computer':
                move = games.alphabeta_player(game, state)
            else:
                move = games.query_player(game, state)

            # print("Player {} made a move:".format(player))
            print(current[player] + " as {} made a move.".format(player))

            # Update the state/board of the game with the move
            state = game.result(state, move)
            game.display(state)
            print()

            # We're done once the game is over
            if game.terminal_test(state):
                return


def computerVsComputer(state, players):
    # Keep making moves until we reach a terminal state
    while True:
        for player in players:

            # Select a move based on alpha beta search
            move = games.alphabeta_player(game, state)

            print("Player {} made a move:".format(player))

            # Update the state/board of the game with the move
            state = game.result(state, move)
            game.display(state)
            print()

            # We're done once the game is over
            if game.terminal_test(state):
                return


def firstMove():
    if random.randint(0, 1) == 0:
        return {'X': 'Computer', 'O': 'Player'}
    else:
        return {'X': 'Player', 'O': 'Computer'}


menu = {'1': playerVsPlayer,
        '2': playerVsComputer,
        '3': computerVsComputer}


if __name__ == "__main__":
    game = games.TicTacToe()    # create a new game object
    play_ttt(game)              # play the game
