from xmlrpc.client import Boolean


class Board():
    def __init__(self, size=20):
        self.size = size
        self.state = [[0 for x in range(self.size)] for y in range(self.size)]

    # Lets Board act like a list
    def __getitem__(self, item):
        return self.state[item]

    def get_state(self):
        return self.state

    def check_valid_move(self, blok, y, x, p_id) -> Boolean:
        # We have to touch a freindly piece diagonally at least once to be valid
        diagonal_check = False

        # First Corner Check
        # It is the only valid place for the first piece
        if (not diagonal_check) and ((
            x==0 and y==0 and p_id==1 and blok[0][0]) or (
                blok.size_x==self.size-x and y==0 and p_id==2 and blok[0][blok.size_x-1]) or (
                    x==0 and blok.size_y==self.size-y and p_id==3 and blok[blok.size_y-1][0]) or (
                        blok.size_x==self.size-x and blok.size_y==self.size-y and p_id==4 and blok[blok.size_y-1][blok.size_x-1])
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
                # Finding one invalidates the tile
                elif self.check_sides(y, x, p_id, b_y, b_x):
                    return False

                # Do diagonal checks
                # At least one needs to be found to be considered valid
                elif not diagonal_check:
                    diagonal_check = self.check_diagonals(y, x, p_id, b_y, b_x)

        # Check if a diagonal was found on that tile
        if not diagonal_check:
            return False

        # If no checks fail, placement is valid
        return True

    # Checks diagonally from each tile
    def check_diagonals(self, y, x, p_id, b_y, b_x) -> Boolean:
        if x+b_x > 0 and y+b_y > 0:
            if self.state[y+b_y-1][x+b_x-1] == p_id:
                return True
        if y+b_y+1 < self.size and x+b_x > 0:
            if self.state[y+b_y+1][x+b_x-1] == p_id:
                return True
        if x+b_x+1 < self.size and y+b_y > 0:
            if self.state[y+b_y-1][x+b_x+1] == p_id:
                return True
        if y+b_y+1 < self.size and x+b_x+1 < self.size:
            if self.state[y+b_y+1][x+b_x+1] == p_id:
                return True

        return False

    # Checks to see if there is an adjecent tile
    def check_sides(self, y, x, p_id, b_y, b_x) -> Boolean:
        if y+b_y > 0:
            if self.state[y+b_y-1][x+b_x] == p_id:
                return True
        if x+b_x > 0:
            if self.state[y+b_y][x+b_x-1] == p_id:
                return True
        if y+b_y+1 < self.size:
            if self.state[y+b_y+1][x+b_x] == p_id:
                return True
        if x+b_x+1 < self.size:
            if self.state[y+b_y][x+b_x+1] == p_id:
                return True
        
        return False

    # Set a tile on the board
    def set_blok(self, blok, y, x, p_id) -> Boolean:
        # Check if move is valid
        if self.check_valid_move(blok, y, x, p_id):
            # Set each tile with the player id
            for b_y in range(blok.size_y):
                for b_x in range(blok.size_x):
                    if blok[b_y][b_x]:
                        self.state[y+b_y][x+b_x] = p_id
            
            return True

        else:
            print(f"ERROR: Failed Placement! {y, x, p_id}")
            return False
