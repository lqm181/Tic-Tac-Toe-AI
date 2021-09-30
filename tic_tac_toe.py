#
# tic_tac_toe.py - play the tic tac toe game!
#
from board import Board
from player import Player
from ai_player import AI_Player
import numpy as np
import random
from numpy.random import choice

def tic_tac_toe(board_dim, p1, p2):
    """ inputs: board_dim is an integer specifying the board's dimension
                p1, p2 represents two Player objects.
        Generates the board and starts the tic tac toe game between the 2 
        specified player (p1 will go first).
        Returns the board when the game is finished. 
    """
    # Check if the players are opponents of each other
    if p1.checker not in 'XO' or p2.checker not in 'XO' or \
        p1.checker == p2.checker:
        print("Need one X player and one O player.")
        return None

    print("********************************")
    print("* Welcome to Tic Tac Toe game! *")
    print("********************************\n")

    board = Board(board_dim)
    print(board)

    while True:
        if process_move(p1, board):
            return board
        if process_move(p2, board):
            return board

def process_move(player, board):
    """ inputs: player is a Player object 
                board is a Board object
        process the move of the player p1 and 
        return True if that move causes the player to win or tie.
        Otherwise, return False
    """
    print(str(player) + "'s turn!")

    row, col = player.next_move(board)
    board.add_checker(player.checker, row, col)

    print()
    print(board)
    print()

    if board.is_win_for(player.checker):
        print(f"{player} wins in {player.num_moves} moves.")
        print("Congratulation!")
        return True
    elif board.is_full():
        print("It's a tie!")
        return True
    else:
        return False


if __name__ == '__main__':
    p1 = Player("Player 1", 'X')
    p2 = AI_Player("Computer1", 'X', 'RANDOM', 3)
    p3 = AI_Player("Computer2", 'O', 'RANDOM', 5)
    tic_tac_toe(4, p1, p3)
