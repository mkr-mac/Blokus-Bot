from player import Player
from random import choice
from copy import copy

class AI(Player):
    def __init__(self, p_id):
        super().__init__(p_id)

    def decide_action(self, board):

        valid_moves = []
        # Check for valid moves if there are still pieces in hand
        if len(self.hand):
            valid_moves = self.find_valid_moves(board)

        # Pick a random move if there is at least one valid move
        if len(valid_moves):
            rand_blok, rand_y, rand_x, blok_iter = choice(valid_moves)
            if board.set_blok(rand_blok, rand_y, rand_x, self.id):  
                # Remove the piece from the hand
                self.remove_from_hand(blok_iter)
                
        # No pieces left? Show score, set as finished.
        else:
            self.final_score()
            return
        
        # Refresh score after turn
        self.tally_score()

    def find_valid_moves(self, board) -> list:

        valid = []
        # Check each space with each tile with every orientation
        for y in range(board.size):
            for x in range(board.size):
                for blok_iter in range(len(self.hand)-1):
                    for flip in range(2):
                        for rot in range(4):
                            if (board.check_valid_move(copy(self.hand[blok_iter]), y, x, self.id)):
                                valid.append([copy(self.hand[blok_iter]), y, x, blok_iter])

                            self.hand[blok_iter].rotate_clockwise()
                        self.hand[blok_iter].flip()

        return valid




class BigFirstAI(AI):
    def __init__(self, p_id):
        super().__init__(p_id)

    def decide_action(self, board):

        valid_moves = []
        # Check for valid moves if there are still pieces in hand
        if len(self.hand):
            valid_moves = self.find_valid_moves(board)

        # Pick one of the biggest pieces
        if len(valid_moves):

            highest_score = 0
            best_moves = []

            for x in valid_moves:
                if x[0].get_value() > highest_score:
                    highest_score = x[0].get_value()
                    best_moves.clear()
                    best_moves.append(x)
                elif x[0].get_value() == highest_score:
                    best_moves.append(x)

            rand_blok, rand_y, rand_x, blok_iter = choice(best_moves)

            if board.set_blok(rand_blok, rand_y, rand_x, self.id):  
                # Remove the piece from the hand
                self.remove_from_hand(blok_iter)
                
        # No pieces left? Show score, set as finished.
        else:
            self.final_score()
            return
        
        # Refresh score after turn
        self.tally_score()
    
    def find_valid_moves(self, board) -> list:
        return super().find_valid_moves(board)