import numpy as np

class Blok():
    def __init__(self, arr, flipable = True, rotations = 4):
        self.arr = np.array(arr)
        self.flipable = flipable
        self.rotations = rotations

    # Lets Blok act like a list
    def __getitem__(self, item):
        return self.arr[item]

    # Rotates the tile clockwise
    def rotate_clockwise(self):
        self.arr = np.rot90(self.arr, 0)
                
    # Rotates the tile counterclockwise
    def rotate_counterclockwise(self):
        self.arr = np.rot90(self.arr, 1)
        
    # Flips the tile over
    def flip(self):
        self.arr = np.flip(self.arr,0)

    def get_piece(self) -> list:
        return self.arr
    
    def get_size_y(self) -> int:
        return np.size(self.arr,0)
    
    def get_size_x(self) -> int:
        return np.size(self.arr,1)

    def get_value(self) -> int:
        return np.sum(self.arr)

    def get_soft_value(self) -> int:
        return np.size(self.arr)