from player import Player
from random import choice
from copy import copy, deepcopy
from blok import Blok
from multiprocessing import Pool

class AI(Player):

    def __init__(self, p_id):
        self.board = []
        super().__init__(p_id)

    def decide_action(self, board, depth=0, player=0, playerhands=False):

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

    def find_valid_moves(self, board, override_id=0, override_hand=False) -> list:
        
        p_id = override_id if override_id else self.id

        ohand = override_hand if override_hand else self.hand
        self.board = board

        with Pool(len(ohand)) as p:
            res = p.map(self.tile_checks, ohand)

        valid = []
        for bl_num in range(len(res)):
            for mv in res[bl_num]:
                mv.append(bl_num)
                valid.append(mv)

        return valid

    def tile_checks(self, b, override_id=0):

        p_id = override_id if override_id else self.id

        valid_moves = []

        # Check each space with each tile with every useful orientation
        for flip in range(2 if b.flipable else 1):
                if b.flipable:
                    b.flip()

                for rot in range(b.rotations):
                    if rot:
                        b.rotate_clockwise()

                    for y in range(self.board.size + -b.size_y + 1):
                        for x in range(self.board.size + -b.size_x + 1):

                            if (self.board.check_valid_move(copy(b), y, x, p_id)):
                                valid_moves.append([copy(b), y, x])

        return valid_moves


class BigFirstAI(AI):

    def decide_action(self, board, depth=0, player=0, playerhands=False):

        valid_moves = []
        # Check for valid moves if there are still pieces in hand
        if len(self.hand):
            valid_moves = self.find_valid_moves(board)

        # Pick one of the biggest pieces
        if len(valid_moves):

            highest_score = 0
            best_moves = []

            for x in valid_moves:
                score = self.get_blok_value(x[0])
                if score > highest_score:
                    highest_score = score
                    best_moves.clear()
                    best_moves.append(x)
                elif score == highest_score:
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
    
    def get_blok_value(self, blok) -> int:
        return blok.get_value()


class SoftBigFirstAI(BigFirstAI):

    def get_blok_value(self, blok) -> int:
        return blok.get_soft_value()


class RecursiveAI(AI):
    
    def __init__(self, p_id, turns_to_predict=1):
        self.turns_to_predict = turns_to_predict
        super().__init__(p_id)

    def decide_action(self, board, depth=0, player=0, playerhands=False):
        
        p_id = player if player else self.id
        
        ohand = playerhands if playerhands else self.hand

        valid_moves = []
        # Check for valid moves if there are still pieces in hand
        if len(ohand[p_id-1]) and depth < self.turns_to_predict:
            valid_moves = self.find_valid_moves(board, p_id, ohand[p_id-1])

        if len(valid_moves):

            lowest_score = 999
            best_moves = []

            for move in valid_moves:

                score = 0

                bd_copy=deepcopy(board)
                # whywhywhywhywhywhy
                ph_copy=deepcopy(ohand)

                r_blok, r_y, r_x, blok_iter = move

                if bd_copy.set_blok(r_blok, r_y, r_x, p_id):
                    del ph_copy[p_id-1][blok_iter]
                
                if depth > 0:
                    return self.decide_action(bd_copy, depth+1, self.next_target(p_id), ph_copy)
                else:
                    score = self.decide_action(bd_copy, depth+1, self.next_target(p_id), ph_copy)


                if score < lowest_score:
                    lowest_score = score
                    best_moves.clear()
                    best_moves.append(move)
                
                elif score == lowest_score:
                    best_moves.append(move)

            if not depth:
                rand_blok, rand_y, rand_x, blok_iter = choice(best_moves)
                if board.set_blok(rand_blok, rand_y, rand_x, self.id):  
                    # Remove the piece from the hand
                    self.remove_from_hand(blok_iter)
                
        # No pieces left? Show score, set as finished.
        elif depth > 0:
            return self.get_soft_score()

        else:
            self.final_score()
            return
            
        
        # Refresh score after turn
        self.tally_score()

    def next_target(self, p_id) -> int:
        return ((p_id)%4)+1


class SelfOnlyRecursiveAI(RecursiveAI):

    def next_target(self, p_id) -> int:
        return p_id
