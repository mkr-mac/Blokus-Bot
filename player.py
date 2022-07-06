import standard_hand

class Player():
    def __init__(self, p_id):
        self.id = p_id
        self.hand = standard_hand.get_standard()
        self.has_valid_moves = True
        self.score = self.tally_score()
        

    def decide_action(self, board):
        pass
    
    def tally_score(self):
        self.score = 0

        for p in self.hand:
            self.score += sum(map(sum, p))

    def remove_from_hand(self, p_id):
        del self.hand[p_id]
