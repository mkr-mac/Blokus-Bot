class Blok():
    def __init__(self, arr):
        self.arr = arr
        self.size_y = len(arr)
        self.size_x = len(arr[0])

    def __getitem__(self, item):
        return self.arr[item]

    def rotate_clockwise(self):
        temp = [[0 for x in range(len(self.arr))] for y in range(len(self.arr[0]))]

        for y in range(len(self.arr)):
            for x in range(len(self.arr[0])):
                temp[x][len(self.arr) - y - 1] = self.arr[y][x]

        self.arr = temp
        self.size_y = len(self.arr)
        self.size_x = len(self.arr[0])
                

    def rotate_counterclockwise(self):
        temp = [[0 for x in range(len(self.arr))] for y in range(len(self.arr[0]))]

        for y in range(len(self.arr)):
            for x in range(len(self.arr[0])):
                temp[x][y] = self.arr[y][x]

        self.arr = temp
        self.size_y = len(self.arr)
        self.size_x = len(self.arr[0])


    def flip(self):
        temp = [[0 for x in range(len(self.arr[0]))] for y in range(len(self.arr))]

        for y in range(len(self.arr)):
            for x in range(len(self.arr[0])):
                temp[y][len(self.arr[0]) - x - 1] = self.arr[y][x]
                
        self.arr = temp


    def get_piece(self):
        return self.arr