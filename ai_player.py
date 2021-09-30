#
# ai_player.py - define AI_Player, representing 
# a computer using AI to play Tic Tac Toe. It's
# an subclass of the Player class
#
from os import replace
from player import Player
from board import Board
import numpy as np
from numpy.random import randint, choice
from random import sample
LOG_FILE = open("log_file.txt", "w")

WIN_EVAL = 100
TIE_EVAL = 0
LOSE_EVAL = -100
class AI_Player(Player):

    def __init__(self, name, checker, tiebreak, difficulty):
        """ construct the attributes for the AI_Player class
            input: name is the name of the AI_Player object
            input: checker is either 'X' or 'O', representing the gamepiece of the player 
            input: tiebreak determine the tie-break strategy, either "LEFT", "RIGHT", or "RANDOM" 
            input: difficulty is how many moves the AI will look ahead
        """
        assert(tiebreak == "LEFT" or tiebreak == "RIGHT" or tiebreak == "RANDOM")
        assert(type(difficulty) == int and difficulty >= 0)

        super().__init__(name, checker)
        self.tiebreak = tiebreak
        self.difficulty = difficulty
    
    def print_AI_info(self):
        """ print out the information of the AI Player object"""
        print(f"AI Player {{name: {self.name}, checker: {self.checker}, tie-break strategy: {self.tiebreak}, difficulty: {self.difficulty}}}")

    def minimax(self, board, alpha, beta, is_max_player):
        """ using minimax algorithm to calculate the best move for the player
            return the move and the score for that move
            evaluations: 100 + depth if the move cause the win 
                         0 if it's a tie
                         -100 - depth if it is the win for my opponent
        """
        if board.is_win_for(self.checker):
            if is_max_player:
                return (None, WIN_EVAL + self.difficulty)
            else:
                return (None, LOSE_EVAL - self.difficulty)

        elif board.is_win_for(self.opponent_checker()):
            if is_max_player:
                return (None, LOSE_EVAL - self.difficulty)
            else:
                return (None, WIN_EVAL + self.difficulty)

        elif board.is_full():
            return (None, TIE_EVAL)

        elif self.difficulty == 0:
            chosen_move = self.tie_break(board)
            return (chosen_move, TIE_EVAL)

        else:
            if is_max_player:
                maxEval = float('-inf')
                best_max_move = None

                for row in range(board.height):
                    for col in range(board.width):
                        if board.can_add_to(row, col):
                            board.add_checker(self.checker, row, col)
                            
                            # Make a recursive call
                            opponent_AI = AI_Player("Opponent", self.opponent_checker(), self.tiebreak, self.difficulty-1)
                            opponent_move, move_eval = opponent_AI.minimax(board, alpha, beta, False)

                            if move_eval > maxEval:
                                maxEval = move_eval
                                best_max_move = (row, col)

                            # Backtracking
                            board.remove_checker(row, col)

                            alpha = max(alpha, move_eval)
                            if beta <= alpha:
                                break
        
                return (best_max_move, maxEval)

            else:
                minEval = float('inf')
                best_min_move = None

                for row in range(board.height):
                    for col in range(board.width):
                        if board.can_add_to(row, col):
                            board.add_checker(self.checker, row, col)

                            # Make a recursive call
                            opponent_AI = AI_Player("Computer", self.opponent_checker(), self.tiebreak, self.difficulty-1)
                            opponent_move, move_eval = opponent_AI.minimax(board, alpha, beta, True)
                            
                            if move_eval < minEval:
                                minEval = move_eval
                                best_min_move = (row, col)
                            
                            board.remove_checker(row, col)

                            # Backtracking
                            beta = min(beta, move_eval)
                            if beta <= alpha:
                                break

                return (best_min_move, minEval)

    def tie_break(self, board):
        """ return a move according to the tiebreak strategy """
        chosen_move = None

        if not board.is_full():
            if self.tiebreak == "LEFT":
                chosen_move = board.available_moves[0]
            elif self.tiebreak == "RIGHT":
                chosen_move = board.available.moves[-1]
            else:
                # Randomly choose the location for the move from those that are available    
                move_sample = sample(board.available_moves, len(board.available_moves))
            
                choice_index = choice(len(move_sample), replace= False)
                chosen_move = move_sample[choice_index]

        return chosen_move

    def next_move(self, board):
        """ return the move that the AI will play """
        best_move, score = self.minimax(board, float('-inf'), float('inf'), True)

        if best_move != None:
            print(str(self) + f" places an '{self.checker}' at {best_move}.")
            print(f"move_score= {score}")
            self.num_moves += 1
            # print(f"num_moves= {self.num_moves}")
            return best_move
        else:
            print(f"{str(self)} did not make any move! best_move= {best_move}, move_score= {score}")
            exit()
        

if __name__ == '__main__':
    player = AI_Player("Computer", 'O', 'LEFT', 5)

        


    



