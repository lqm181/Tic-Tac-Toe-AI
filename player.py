#
# player.py - contains the definition for Player
# which is a class representing a player of a 
# Tic Tac Toe game
# 
from board import Board

class Player:
    """ a data type for a Tic Tac Toe Player"""
    def __init__(self, name, checker):
        """ constructs a new Player object by initialize its attributes: 
                name: the nickname that the player goes by
                checker: a one-character string representing the gamepiece of the player
                num_moves: the number of moves the player made
        """
        assert(checker == 'O' or checker == 'X')
        self.name = name
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """ returns a string representing the Player object
        """
        return self.name + f' ({self.checker})'  

    def opponent_checker(self):
        """ returns a one-character string representing 
            the checker of the Player object's opponent
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
    
    def next_move(self, board):
        """ input: a parameter board representing a Board object
            reads and return the row and column where the player wants to 
            make the next move
        """
        while True:
            input_row = input("Enter a row: ")
            if input_row.lower() == 'c':
                exit("Game is terminated by players!")
            else:
                try:
                    row = int(input_row)
                except:
                    print("Please try again and input numbers only!")
                    continue
            
            input_col = input("Enter a column: ")
            if input_col.lower() == 'c':
                exit("Game is terminated by players!")
            else:
                try:
                    col = int(input_col)
                except:
                    print("Please try again and input numbers only!")
                    continue

            if board.can_add_to(row, col):
                self.num_moves += 1
                return (row,col)
            else:
                print(f"Cannot add a checker a row {row} and colum {col}. Try again!")
    
                
if __name__ == '__main__':
    p = Player("Player1", 'X')
    print(p)