import standard_hand

class Player():
    def __init__(self, id):
        self.id = id
        self.hand = standard_hand.get_standard()

    def decide_action(self, board):
        pass
    