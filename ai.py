from player import Player
from random import choice
from copy import copy, deepcopy
from blok import Blok

class AI(Player):

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

        valid_moves = []
        # Check each space with each tile with every orientation
        blok_iter = -1
        for b in ohand:
            blok_iter+=1
            
            for flip in range(2 if b.flipable else 1):
                if b.flipable:
                    b.flip()

                for rot in range(b.rotations):
                    if rot:
                        b.rotate_clockwise()

                    for y in range(board.size + -b.size_y + 1):
                        for x in range(board.size + -b.size_x + 1):

                            if (board.check_valid_move(copy(b), y, x, p_id)):
                                valid_moves.append([copy(b), y, x, blok_iter])

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



class RecursiveAI(AI):

    def decide_action(self, board, depth=0, player=0, playerhands=False):
        
        p_id = player if player else self.id
        
        ohand = playerhands if playerhands else self.hand

        valid_moves = []
        # Check for valid moves if there are still pieces in hand
        if len(ohand) and depth < 5:
            valid_moves = self.find_valid_moves(board, p_id, ohand[p_id-1])

        if len(valid_moves):

            lowest_score = 999
            best_moves = []

            mov_iter = 1
            for move in valid_moves:
                if p_id == 1 and not depth:
                    print(f"Evaluating move {mov_iter} of {len(valid_moves)}")
                    mov_iter += 1

                score = 0

                bd_copy=deepcopy(board)
                # whywhywhywhywhywhy
                ph_copy=deepcopy(ohand)

                r_blok, r_y, r_x, blok_iter = move

                if bd_copy.set_blok(r_blok, r_y, r_x, p_id):
                    del ph_copy[p_id-1][blok_iter]
                
                if depth > 0:
                    return self.decide_action(bd_copy, depth+1, ((p_id)%4)+1, ph_copy)
                else:
                    score = self.decide_action(bd_copy, depth+1, ((p_id)%4)+1, ph_copy)


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
        elif not p_id == self.id:
            self.tally_score()
            return self.score
        elif depth > 0:
            self.tally_score()
            return self.score

        else:
            self.final_score()
            return
            
        
        # Refresh score after turn
        self.tally_score()


