from player import Player
from random import choice
from copy import copy

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
        if override_id:
            p_id = override_id
        else:
            p_id = self.id

        if override_hand:
            ohand = override_hand
        else:
            ohand = self.hand

        valid = []
        # Check each space with each tile with every orientation
        for y in range(board.size):
            for x in range(board.size):
                for blok_iter in range(len(ohand)-1):
                    for flip in range(2):
                        for rot in range(4):

                            if (board.check_valid_move(copy(ohand[blok_iter]), y, x, p_id)):
                                valid.append([copy(ohand[blok_iter]), y, x, blok_iter])

                            ohand[blok_iter].rotate_clockwise()
                        ohand[blok_iter].flip()

        return valid




class BigFirstAI(AI):

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



class RecursiveAI(AI):

    def decide_action(self, board, depth=0, player=0, playerhands=False):
        if player:
            p_id = player
        else:
            p_id = self.id
        
        print(depth, p_id)

        valid_moves = []
        # Check for valid moves if there are still pieces in hand
        if len(self.hand):
            valid_moves = self.find_valid_moves(board, p_id)

        if len(valid_moves):

            lowest_score = 999
            best_moves = []

            for move in valid_moves:
                score = 0
                bd_copy=copy(board)
                ph_copy=copy(playerhands)
                rblok, rand_y, rand_x, blok_iter = move
                if bd_copy.set_blok(rblok, rand_y, rand_x, p_id):
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

            rand_blok, rand_y, rand_x, blok_iter = choice(best_moves)

            if board.set_blok(rand_blok, rand_y, rand_x, self.id):  
                # Remove the piece from the hand
                self.remove_from_hand(blok_iter)
                
        # No pieces left? Show score, set as finished.
        elif not p_id == self.id:
            return self.decide_action(board, depth+1, ((p_id)%4)+1)
        elif depth > 0:
            self.tally_score()
            return self.score

        else:
            self.final_score()
            return
            
        
        # Refresh score after turn
        self.tally_score()