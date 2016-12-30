class Board:
    '''8x8, '''
    def __init__(self):
        self.f = open("board.txt", "w")
        #self.f.write("test")
        row = "0 0 0 0 0 0 0 0"
        self.cols = [[] for i in range(8)]
        for i in range(8):
            self.cols[i].append(row)
        for i in range(len(self.cols)):
            for j in range(len(self.cols[i])):
                self.f.write(self.cols[i][j])
            self.f.write("\n")
    def setup(self):
        print()
    def update(self):
        print()
board = Board()