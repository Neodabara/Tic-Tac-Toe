import games

'''
    CS316 TicTacToe Minimax demo program
'''

# play a game of TicTacToe
def play_ttt(game):

    # The initial state is a blank board
    state = game.initial

    # We'll cycle between the 2 players, X and O
    players = ['X', 'O']

    # Keep making moves until we reach a terminal state
    while True:
        for player in players:

            # Select a move based on minimax recursion
            move = games.minimax_decision(state, game)
            print("Player {} made a move:".format(player))

            # Update the state/board of the game with the move
            state = game.result(state, move)
            game.display(state)
            print()

            # We're done once the game is over
            if game.terminal_test(state):
                return

if __name__ == "__main__":
    game = games.TicTacToe()    # create a new game object
    play_ttt(game)              # play the game