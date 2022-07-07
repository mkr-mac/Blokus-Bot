class Blok():
    def __init__(self, arr, flipable = True, rotations = 4):
        self.arr = arr
        self.size_y = len(arr)
        self.size_x = len(arr[0])
        self.flipable = flipable
        self.rotations = rotations

    # Lets Blok act like a list
    def __getitem__(self, item):
        return self.arr[item]

    # Rotates the tile clockwise
    def rotate_clockwise(self):
        temp = [[0 for x in range(len(self.arr))] for y in range(len(self.arr[0]))]

        for y in range(len(self.arr)):
            for x in range(len(self.arr[0])):
                temp[x][len(self.arr) - y - 1] = self.arr[y][x]

        self.arr = temp
        self.size_y = len(self.arr)
        self.size_x = len(self.arr[0])
                
    # Rotates the tile counterclockwise
    def rotate_counterclockwise(self):
        temp = [[0 for x in range(len(self.arr))] for y in range(len(self.arr[0]))]

        for y in range(len(self.arr)):
            for x in range(len(self.arr[0])):
                temp[x][y] = self.arr[y][x]

        self.arr = temp
        self.size_y = len(self.arr)
        self.size_x = len(self.arr[0])

    # Flips the tile over
    def flip(self):
        temp = [[0 for x in range(len(self.arr[0]))] for y in range(len(self.arr))]

        for y in range(len(self.arr)):
            for x in range(len(self.arr[0])):
                temp[y][len(self.arr[0]) - x - 1] = self.arr[y][x]
                
        self.arr = temp


    def get_piece(self) -> list:
        return self.arr

    def get_value(self) -> int:
        return sum(map(sum, self.arr))

    def get_soft_value(self) -> int:
        return self.size_y*self.size_x