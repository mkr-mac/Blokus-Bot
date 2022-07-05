class Board():
    def __init__(self, size=20):
        self.size = size
        self.state = [[0 for x in range(self.size)] for y in range(self.size)]

    def get_state(self):
        return self.state

    def check_valid_move(self, blok, x, y, id):
        # We have to touch a freindly piece diagonally at least once to be valid
        diagonal_check = False

        for b_y in range(blok.size_y):
            for b_x in range(blok.size_x):
                # Check if this is an actual bit of the blok
                if (not blok[b_y][b_x]):
                    pass
                # Check if spot is taken
                elif (self.state[y+b_y][x+b_x]):
                    return False
                # Check adjacent to see if a tile from same user exists
                elif (self.state[y+b_y-1][x+b_x] == id):
                    return False
                elif (self.state[y+b_y+1][x+b_x] == id):
                    return False
                elif (self.state[y+b_y][x+b_x-1] == id):
                    return False
                elif (self.state[y+b_y][x+b_x+1] == id):
                    return False
                # Do diagonal checks
                elif(diagonal_check):
                    # Already valid, skip checks
                    pass
                elif (self.state[y+b_y-1][x+b_x-1] == id):
                    diagonal_check = True
                elif (self.state[y+b_y+1][x+b_x-1] == id):
                    diagonal_check = True
                elif (self.state[y+b_y-1][x+b_x+1] == id):
                    diagonal_check = True
                elif (self.state[y+b_y+1][x+b_x+1] == id):
                    diagonal_check = True

        if (not diagonal_check):
            return False

        return True

    def set_blok(self, blok, x, y, id):
        if (self.check_valid_move(blok, x, y, id)):
            for b_y in range(blok.size_y):
                for b_x in range(blok.size_x):
                    self.state[y+b_y][x+b_x] = id

            return True

        else:
            return False
