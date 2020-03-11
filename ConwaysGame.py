# William Fidler
# 02/26/20
# Conways Game
# "I have not given or received any unauthorized assistance on the assignment
# Link here:

import numpy as np

class Board():

    def __init__(self, s, p):
        self.gameBoard = self.createBoard(s)
        self.populateBoard(p, s)
        self.size = s

    def createBoard(self, s):
        return np.random.random((s, s))

    def populateBoard(self, p, s):

        for i in range(s):
            for j in range(s):
                if self.gameBoard[i, j] < p:
                    self.gameBoard[i, j] = 1
                else:
                    self.gameBoard[i, j] = 0

    def setBoard(self, b):
        self.gameBoard = b

    def getBoard(self):
        return self.gameBoard

    def getItem(self, i, j):
        return self.gameBoard[i, j]

    def getSize(self):
        return self.size

    def advanceBoard(self):
        b = Board(self.size, 0)
        # print(b.gameBoard)
        for i in range(self.size):
            for j in range(self.size):
                n = self.getNeighborsAlive(i, j)
                if self.gameBoard[i, j]:
                    b.gameBoard[i, j] = self.doLiveLogic(n)
                else:
                    b.gameBoard[i, j] = self.doDeadLogic(n)

        self.gameBoard = b.gameBoard


    def getNeighborsAlive(self, i, j):
        neighborsAlive = 0
        up = i+1
        right = j+1
        down = i-1
        left = j-1

        if(up == self.size):
            up = 0
        if(right == self.size):
            right = 0
        if(down < 0):
            down = self.size -1
        if(left < 0):
            left = self.size-1

        if(self.gameBoard[down, j] ==1.):
            neighborsAlive += 1
        if(self.gameBoard[up, j] == 1.):
            neighborsAlive += 1
        if(self.gameBoard[i, left] == 1.):
            neighborsAlive += 1
        if(self.gameBoard[i, right] == 1.):
            neighborsAlive += 1

        return neighborsAlive

    def doLiveLogic(self, n):
        if n<2 or n>3:
            return 0
        else:
            return 1

    def doDeadLogic(self, n):
        if n == 3:
            return 1
        else:
            return 0


def advance(b, t):
    while(t>0):
        print("{}\n{}".format(t,b.gameBoard))
        b.advanceBoard()
        t = t-1
        # print(t)
    return b

def conways(s, p):
    return Board(s, p)


def main():
    a = conways(5, .5)
    # print(a.gameBoard)
    b = advance(a, 3)

    # print(b.gameBoard)


if __name__ == '__main__':
    main()
