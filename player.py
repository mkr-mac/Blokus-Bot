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
            self.score += p.get_value()

    def remove_from_hand(self, bl_iter):
        del self.hand[bl_iter]

    def final_score(self):
        print(f"Player {self.id} is out of moves!")
        self.tally_score()
        print(f"Final Score: {self.score}")
        self.has_valid_moves = False
        for p in self.hand:
            for row in p.arr:
                print(row)
            print("--------------")
        return
