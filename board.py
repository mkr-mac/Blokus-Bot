from xmlrpc.client import Boolean


class Board():
    def __init__(self, size=20):
        self.size = size
        self.state = [[0 for x in range(self.size)] for y in range(self.size)]

        
    def __getitem__(self, item):
        return self.state[item]

    def get_state(self):
        return self.state

    def check_valid_move(self, blok, y, x, id) -> Boolean:
        # We have to touch a freindly piece diagonally at least once to be valid
        diagonal_check = False

        # First Corner Check
        if (not diagonal_check) and (
            (x==0 and y==0 and id==1) or (x==self.size-1 and y==0 and id==2) or (x==0 and y==self.size-1 and id==3) or (x==self.size-1 and y==self.size-1 and id==4)
            ):
            
            diagonal_check = True


        # Check if it fits
        if (x + blok.size_x > self.size) or (y + blok.size_y > self.size):
            return False

        for b_y in range(blok.size_y):
            for b_x in range(blok.size_x):
                # Check if this is an actual bit of the blok
                if not blok[b_y][b_x]:
                    pass
                # Check if spot is taken
                elif self.state[y+b_y][x+b_x]:
                    return False
                # Check adjacent to see if a tile from same user exists
                elif self.state[y+b_y-1][x+b_x] == id:
                    return False
                elif self.state[y+b_y+1][x+b_x] == id:
                    return False
                elif self.state[y+b_y][x+b_x-1] == id:
                    return False
                elif self.state[y+b_y][x+b_x+1] == id:
                    return False
                # Do diagonal checks
                elif diagonal_check:
                    # Already valid, skip checks
                    pass
                elif self.state[y+b_y-1][x+b_x-1] == id:
                    diagonal_check = True
                elif self.state[y+b_y+1][x+b_x-1] == id:
                    diagonal_check = True
                elif self.state[y+b_y-1][x+b_x+1] == id:
                    diagonal_check = True
                elif self.state[y+b_y+1][x+b_x+1] == id:
                    diagonal_check = True

        if not diagonal_check:
            return False

        # If no checks fail, placement is valid
        return True

    def set_blok(self, blok, y, x, id) -> Boolean:

        if self.check_valid_move(blok, y, x, id):

            for b_y in range(blok.size_y):
                for b_x in range(blok.size_x):
                    if blok[b_y][b_x]:
                        self.state[y+b_y][x+b_x] = id

            return True

        else:
            return False
