# William Fidler
# 02/22/20
# Ellipses
# "I have not given or received any unauthorized assistance on the assignment
# Link here:
import math
from time import time_ns

class WarAndPeacePseudoRandomNumberGenerator():
    filepath = "resources/war-and-peace.txt"
    def __init__(self, seedValue=None):

        self.seedValue = seedValue

    def getSeedValue(self):

        if self.seedValue is None:
            x = time_ns()
            sax = str(x)
            x = int(sax[-5:])

            return self.doSomeLCGMath(x)

        return self.doSomeLCGMath(self.seedValue)

    def doSomeLCGMath(self, seed):

        a = 1
        c = 3123
        m = 999999
        return (a*seed + c) % m

    def random(self):
        value = self.getSeedValue()
        binaryString = ""

        file = self.openFile()

        while len(binaryString) < 16:
            a = self.getCharacter(file, value)
            i = value + self.getSeedValue()
            b = self.getCharacter(file, i)
            bit = self.judge(a, b)
            if bit is None:
                value = value + self.getSeedValue()
                continue
            value = value + self.getSeedValue()
            binaryString += bit

        self.closeFile()

        return self.calculateNumber(binaryString)

    def calculateNumber(self, bitString):

        sum = 0.0

        divisor = 2

        for i in range(len(bitString)): #expect bit string to be len of 16 and made up of 0 and 1 only
            sum += int(bitString[i]) * (1/(divisor))
            divisor = divisor * 2
        return sum


    def judge(self, a, b):
        if a>b:
            return "1"
        if a<b:
            return "0"
        else:
            return None


    def getLines(self):

        fileString = ""
        with open(self.filepath, "r") as file:
            lines = file.readlines()
        for line in lines:
            fileString += line.rstrip()
        fileString = fileString.replace(" ", "")
        # print(fileString)
        return fileString

    def getCharacter(self, file, value):
        a = " "
        b = None

        while a.isspace():
            self.file.seek(value)
            a = self.file.read(1)
            value += 1
            try:
                b = a.decode("ascii")
            except UnicodeError:
                a = " "

        return b

    def openFile(self):
        filepath = "resources/war-and-peace.txt"
        self.file = open(self.filepath, "rb")

    def closeFile(self):
        self.file.close()

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Ellipse():

    #if in ellipse d1 +d2 < w

    def __init__(self, p1, p2, w):
        self.p1 = p1
        self.p2 = p2
        self.w = w

    def inEllipse(self, point):

        d1 = self.getDistanceOfTwoPoints(self.p1, point)
        d2 = self.getDistanceOfTwoPoints(self.p2, point)
        return (d1+d2) <= self.w

    def getDistanceOfTwoPoints(self, p1, p2):

        return math.sqrt(((p2.x - p1.x)**2 + (p2.y - p1.y)**2))

class Box():

    rando = WarAndPeacePseudoRandomNumberGenerator()

    def __init__(self, ellipse1, ellipse2):
        self.ellipse1 = ellipse1
        self.ellipse2 = ellipse2
        self.calculateBox()

    def calculateBox(self):
        listOfX = [self.ellipse1.p1.x, self.ellipse1.p2.x, self.ellipse2.p1.x, self.ellipse2.p2.x]
        listOfY = [self.ellipse1.p1.y, self.ellipse1.p2.y, self.ellipse2.p1.y, self.ellipse2.p2.y]
        listOfW = [self.ellipse1.w, self.ellipse2.w]

        minX = min(listOfX)
        maxX = max(listOfX)
        minY = min(listOfY)
        maxY = max(listOfY)
        maxW = max(listOfW)
        maxW = maxW/2
        self.minX = minX
        self.minY = minY


        x1 = minX - maxW
        x2 = maxX + maxW
        y1 = minY - maxW
        y2 = maxY + maxW

        print(x1, x2, y1, y2)

        self.bottomLeft = Point(x1, y1)
        self.topLeft = Point(x1, y2)
        self.bottomRight = Point(x2, y1)
        self.topRight = Point(x2, y2)

        self.boxWidth = x2-x1
        self.boxHeight = y2-y1


    def throwDart(self):
        x = self.rando.random()
        # print(x)
        x = (x * self.boxWidth) + self.bottomLeft.x
        y = self.rando.random()
        # print(y)
        y = (y * self.boxHeight) + self.bottomLeft.y
        print(x, y)
        return Point(x,y)

    def getArea(self):
        return self.boxWidth *self.boxHeight


def calculateAreaOfOverlap(area, c, n):
    print(area, c, n)
    return area * (c/n)

def computeOverlapOfEllipse(el1, el2):

    box = Box(el1, el2)
    box.rando.openFile()

    constant = 100000
    c = 0
    for i in range(constant):
        p = box.throwDart()
        if el1.inEllipse(p) and el2.inEllipse(p):
            c += 1

    box.rando.closeFile()
    return calculateAreaOfOverlap(box.getArea(), c, constant)


def main():

    p1 = Point(2,3)
    p2 = Point(3,4)
    p3 = Point(2,2)
    p4 = Point(3,5)

    el1 = Ellipse(p1, p2, 4)
    el2 = Ellipse(p3, p4, 6)

    overlap = computeOverlapOfEllipse(el1, el2)

    print(overlap)



if __name__ == '__main__':
    main()

#min(x) - max(w)
#max(x) + max(w)
#min(y) - max(w)
#max(y) + max(w)