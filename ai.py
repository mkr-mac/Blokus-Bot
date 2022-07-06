from player import Player
from random import choice
from copy import copy

class AI(Player):
    def __init__(self, p_id):
        super().__init__(p_id)

    def decide_action(self, board):

        valid_moves = []

        if len(self.hand):
            valid_moves = self.find_valid_moves(board)

        if len(valid_moves):
            rand_blok, rand_y, rand_x, blok_iter = choice(valid_moves)
            if board.set_blok(rand_blok, rand_y, rand_x, self.id):
                print (blok_iter)
                self.remove_from_hand(blok_iter)
                
        else:
            print(f"Player {self.id} is out of moves!")
            self.tally_score()
            print(f"Final Score: {self.score}")
            self.has_valid_moves = False
            return
        

        self.tally_score()

    def find_valid_moves(self, board) -> list:

        valid = []

        for y in range(board.size):
            for x in range(board.size):
                for blok_iter in range(len(self.hand)-1):
                    for flip in range(2):
                        for rot in range(4):
                            if (board.check_valid_move(copy(self.hand[blok_iter]), y, x, self.id)):
                                valid.append([copy(self.hand[blok_iter]), y, x, blok_iter])

                            self.hand[blok_iter].rotate_counterclockwise()
                        self.hand[blok_iter].flip()

        return valid
