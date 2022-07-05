from player import Player
from random import randint

class AI(Player):
    def __init__(self, id):
        super().__init__(id)

    def decide_action(self, board):

        valid_moves = self.find_valid_moves(board)

        if len(valid_moves):
            rand_bloc, rand_y, rand_x = valid_moves[randint(0, len(valid_moves))]
            board.set_block(rand_bloc, rand_y, rand_x)

        else:
            print(f"Player {self.id} is out of moves!")
            self.tally_score()
            print(f"Final Score: {self.score}")
            self.has_valid_moves = False
            return
        

        self.tally_score()

    def get_valid_moves(self, board) -> list:

        valid = []

        for y in range(board.size):
            for x in range(board.size):
                for blok in self.hand:
                    for flip in range(2):
                        for rot in range(4):
                            if (board.check_valid_move(blok, y, x)):
                                valid.append([blok, y, x])

                            blok.rotate_counterclockwise()
                        blok.flip()

        return valid
