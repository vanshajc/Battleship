import sys
class Board:
    '''8x8, 2 ships each of lengths 1, 2, 3, 4
        1 = hit, 2 = sink, 0 = nothing, 9 = boat'''
    def __init__(self, ships):
        #self.f.write("test")
        self.board = [[0 for i in range(8)] for j in range(8)]
        self.ships = ships
    def update(self, pos):
        for ship in self.ships:
            for pos_i in ship:
                if pos[0] == pos_i[0] and pos[1] == pos_i[1]:
                    ship.pop(ship.index(pos_i))
                    ship.append((pos_i[0], pos_i[1], "hit"))
                    self.board[pos[0]][pos[1]] = "1"
            sunk = True
            for pos_i in ship:
                if pos_i[2] == "not hit": sunk = False
            if sunk == True:
                for pos_i in ship:
                    self.board[pos_i[0]][pos_i[1]] = "2"

    def printBoard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                sys.stdout.write(str(self.board[i][j]) + " ")
            print("\n")
    def getBoard(self):
        return board

    def toString(self):
        message = ""
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                message+= str(self.board[i][j])
            message+="\n"
        return message