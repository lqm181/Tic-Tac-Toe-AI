#
#    board.py- contain the class definition for Board
#    which will be used to represent a tic tac toe board
#
import numpy as np

class Board:
    """ a data type for a Tic Tac Toe Board"""

    # By default, our grid has the shape of 3 x 3 
    DEFAULT_DIM = 3

    def __init__(self, board_dim= DEFAULT_DIM):
        """ takes into an integer representing the width and height
            of the Board object. Initilize the grid to have the dimension
            according to the input. By default, the grid is 3 x 3.  
        """
        self.width = board_dim
        self.height = board_dim

        self.grid = np.array([[' '] * self.width for i in range(self.height)])
        self.num_checkers = 0 # keeps track of how many checkers have been added

        self.available_moves = [(row, col) for row in range(self.height) for col in range(self.width)]

        # Specify the winning condition based on the board's dimension
        if (self.width < 5):
            self.win_condition = self.width
        else:
            self.win_condition = 5

    def __repr__(self):
        """ return the string representation of the board"""
        # Initialize the return string
        s =  ''

        for row in range(self.height):
            # Print the index of the row
            s = s + str(row % 10) + ' |'

            for col in range(self.width):
                s += self.grid[row][col]
                s += '|'

            s += '\n'
            s += '--' * (self.width + 1)
            s += '-'
            s += '\n'
        
        s += '  '
        for i in range(self.width):
            s += ' ' +  str(i % 10)  
            
        return s

    def reset(self):
        """ reset the Board object that it contains only space character"""
        self.grid = np.array([[' '] * self.width for row in range(self.height)])
        self.num_checkers = 0

    def add_checker (self, checker, row, col):
        """ takes in a character (only 'X' or 'O') representing 
            the player's checker and 2 integers representing the 
            indexed row and column. Then, it adds the checker to 
            the board at the spcified row and column. 
        """
        assert(checker == 'X' or checker == 'O')
        assert(row >= 0 and row < self.width)
        assert(col >= 0 and col < self.width)
        assert(self.grid[row][col] == ' ')

        self.grid[row][col] = checker
        self.num_checkers += 1
        self.available_moves.remove((row, col))

    def remove_checker(self, row, col):
        """ inputs: row and col are integers representing
            the indeces for row and column.
            removes the checker at the specified row and column
        """
        assert(row >= 0 and row < self.width)
        assert(col >= 0 and col < self.width)
        self.grid[row][col] = ' '
        self.num_checkers -= 1
        self.available_moves.append((row, col))

    def is_full(self):
        """ return True if the board is full; otherwise False"""
        return self.num_checkers == self.width * self.height

    def can_add_to(self, row, col):
        """ return True if a checker can be added to the 
            specified row and col location. Otherwise, false
        """
        return (0<= row and row < self.height) and \
                (0<= col and col < self.width) and \
                (self.grid[row][col] == ' ')

    def is_horizontal_win(self, checker):
        """ return True if there is a horizontal win for the specified checker"""
        for row in range(self.height):
            for col in range(self.width - self.win_condition + 1):
                # Analyze every horizontal group of win_condition checkers 
                # (eg. every horizontal group of 3 checkers if the winning 
                # condition is 3 checkers in a row).
                # and calculate how many checkers that are in a row
                checker_group = self.grid[row, col : col + self.win_condition]
                num_checkers = sum(checker_group == checker)

                if num_checkers == self.win_condition:
                    return True

        # if we get here, there's no horizontal win
        return False

    def is_vertical_win(self, checker):
        """ return True if there is a vertical win for the specified checker"""
        for col in range(self.width):
            for row in range(self.height - self.win_condition + 1):
                # Analyze every vertical group of win_condition checkers 
                # (eg. every vertical group of 3 checkers if the winning 
                # condition is 3 checkers in a row).
                # and calculate how many checkers that are in a row
                checker_group = self.grid[row : row+self.win_condition, col]
                num_checkers = sum(checker_group == checker)

                if num_checkers == self.win_condition:
                    return True

        # if we get here, there's no horizontal win
        return False

    def is_down_diagonal_win(self, checker):
        """ retrun True if there is a down diagonal (go down from left to right) 
            win for the specified checker
        """
        for row in range(self.height - self.win_condition + 1):
            for col in range(self.width - self.win_condition + 1):
                num_checkers = 0
                for i in range(self.win_condition):
                    if self.grid[row + i][col + i] == checker:
                        num_checkers += 1

                if num_checkers == self.win_condition:
                    return True

        # if we get here, there's no horizontal win
        return False

    def is_up_diagonal_win(self, checker):
        """ retrun True if there is an up diagonal (go up from left to right) win for 
            the specified checker
        """
        for row in range(self.height - self.win_condition + 1):
            for col in range(self.width - self.win_condition + 1):
                num_checkers = 0
                for i in range(self.win_condition):
                    if self.grid[self.height - row - 1 - i][col+i] == checker:
                        num_checkers += 1

                if num_checkers == self.win_condition:
                    return True

        # if we get here, there's no horizontal win
        return False

    def is_win_for(self, checker):
        """ return True if there is a win for the specified checker
        """
        assert(checker == 'X' or checker == 'O')

        return self.is_horizontal_win(checker) or \
                self.is_vertical_win(checker) or \
                self.is_down_diagonal_win(checker) or \
                self.is_up_diagonal_win(checker)


if __name__ == '__main__':
    board = Board(3)
    print(board)

    board.add_checker("X", 0,2)
    board.add_checker("X", 1,1)
    board.add_checker("X", 2,0)
    print(board)
    print(board.is_win_for('X'))
    print(board.is_full())
    print(board.can_add_to(1, 0))