class Blok():
    def __init__(self, arr, flipable = True, rotations = 4):
        self.arr = arr
        self.flipable = flipable
        self.rotations = rotations

    # Lets Blok act like a list
    def __getitem__(self, item):
        return self.arr[item]

    # Rotates the tile clockwise
    def rotate_clockwise(self):
        self.arr = [[self.arr[j][i] for j in range(len(self.arr))] for i in range(len(self.arr[0]))][::-1]
                
    # Rotates the tile counterclockwise
    def rotate_counterclockwise(self):
        self.arr = self.arr
        
    # Flips the tile over
    def flip(self):
        self.arr = self.arr[::-1]

    def get_piece(self) -> list:
        return self.arr
    
    def get_size_y(self) -> int:
        return len(self.arr)
    
    def get_size_x(self) -> int:
        return len(self.arr[0])

    def get_value(self) -> int:
        return sum(map(sum, self.arr))

    def get_soft_value(self) -> int:
        return self.get_size_x() * self.get_size_y()