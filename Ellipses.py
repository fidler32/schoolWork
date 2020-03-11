# William Fidler
# 02/26/20
# Ellipses
# "I have not given or received any unauthorized assistance on the assignment
# Link here: https://youtu.be/smkG3GcuCH0

import math
from time import time_ns

class WarAndPeacePseudoRandomNumberGenerator():

    filepath = "resources/war-and-peace.txt"

    def __init__(self, seedValue=None):

        self.seedValue = seedValue
        self.file = self.openFile()

    def getSeedValue(self):
        """
        Returns the seed value of the class, if there is none returns last 5 digits of time
        :return:
        """
        if self.seedValue is None:
            x = time_ns()
            sax = str(x)
            x = int(sax[-5:]) #last 5 digits

            return self.doSomeLCGMath(x)

        return self.doSomeLCGMath(self.seedValue)

    def doSomeLCGMath(self, seed):
        """
        Uses a value to calculate a number
        Numbers range from 0 to 999999
        :param seed:
        :return: int
        """
        a = 1
        c = 3123
        m = 999999
        return (a*seed + c) % m

    def random(self):
        """
        Calculate a random number using the text file
        :return:
        """
        value = self.getSeedValue()
        binaryString = ""

        while len(binaryString) < 16:
            a = self.getCharacter(value)
            i = value + self.getSeedValue()
            b = self.getCharacter(i)
            bit = self.judge(a, b)
            if bit is None:
                value = value + self.getSeedValue()
                continue
            value = value + self.getSeedValue()
            binaryString += bit

        return self.calculateNumber(binaryString)

    def calculateNumber(self, bitString):
        """
        Take a String of 0s and 1s and convert that to a number where 0<=number<1
        :param bitString:
        :return:
        """

        sum = 0.0

        divisor = 2

        for i in range(len(bitString)): #expect bit string to be len of 16 and made up of 0 and 1 only
            sum += int(bitString[i]) * (1/(divisor))
            divisor = divisor * 2
        return sum


    def judge(self, a, b):
        """
        Return a 0 or 1
        :param a: char
        :param b: char
        :return: String
        """
        if a>b:
            return "1"
        if a<b:
            return "0"
        else:
            return None

    def getCharacter(self,  value):
        """
        Get a character from a file
        :param value: int
        :return: char
        """
        a = " "
        b = None

        while a.isspace(): #avoid returning whitespace
            self.file.seek(value)
            a = self.file.read(1)
            value += 1 #increment value by 1
            try:
                b = a.decode("ascii")
            except UnicodeError: #if not an ascii continue loop
                a = " "

        return b

    def openFile(self):
        """
        Open file
        :return: File
        """
        return open(self.filepath, "rb")

    def closeFile(self):
        """
        Close file
        :return: None
        """
        self.file.close()

class Point():
    """
    Class that holds x,y coordinates
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Ellipse():

    """
    Holds two points in a graph and a width
    """

    def __init__(self, p1, p2, w):
        self.p1 = p1
        self.p2 = p2
        self.w = w

    def inEllipse(self, point):
        """
        returns boolean value to tell you if point is in this ellipse
        :param point: Point
        :return: boolean
        """
        d1 = self.getDistanceOfTwoPoints(self.p1, point)
        d2 = self.getDistanceOfTwoPoints(self.p2, point)
        return (d1+d2) <= self.w

    def getDistanceOfTwoPoints(self, p1, p2):
        """
        Get the distance of two points
        :param p1: Point
        :param p2: Point
        :return: float
        """
        return math.sqrt(((p2.x - p1.x)**2 + (p2.y - p1.y)**2))

class Box():
    """
    Represents a Box with two ellipses in it
    """

    def __init__(self, ellipse1, ellipse2):
        self.ellipse1 = ellipse1
        self.ellipse2 = ellipse2
        self.calculateBox()
        self.rando = WarAndPeacePseudoRandomNumberGenerator() #random number generator for every Box

    def calculateBox(self):
        """
        Calculates boundaries for box and sets the width and height
        :return: None
        """
        listOfX = [self.ellipse1.p1.x, self.ellipse1.p2.x, self.ellipse2.p1.x, self.ellipse2.p2.x]
        listOfY = [self.ellipse1.p1.y, self.ellipse1.p2.y, self.ellipse2.p1.y, self.ellipse2.p2.y]
        listOfW = [self.ellipse1.w, self.ellipse2.w]

        minX = min(listOfX)
        maxX = max(listOfX)
        minY = min(listOfY)
        maxY = max(listOfY)
        maxW = max(listOfW)

        maxW = maxW/2


        x1 = minX - maxW
        x2 = maxX + maxW
        y1 = minY - maxW
        y2 = maxY + maxW

        self.bottomLeft = Point(x1, y1) #all four coordinates could be added if needed

        self.boxWidth = x2-x1
        self.boxHeight = y2-y1


    def throwDart(self):
        """
        Gets random coordinates simulating a dart being thrown in the box
        :return: Point
        """
        x = self.rando.random()
        # print(x)
        x = (x * self.boxWidth) + self.bottomLeft.x
        y = self.rando.random()
        # print(y)
        y = (y * self.boxHeight) + self.bottomLeft.y
        # print(x, y)
        return Point(x,y)

    def getArea(self):
        """
        Returns area of the box
        :return: float
        """
        return self.boxWidth *self.boxHeight

    def dotInBothEllipses(self, p):
        """
        Tells you if a point is in both ellipses
        :param p: Point
        :return: boolean
        """
        return self.ellipse1.inEllipse(p) and self.ellipse2.inEllipse(p)


def calculateAreaOfOverlap(area, c, n):
    # print(area, c, n)
    """
    Calculates the estimate of the area of overlap of two ellipses
    :param area: float - area of box
    :param c: int
    :param n: int
    :return: float
    """
    return area * (c/n)

def computeOverlapOfEllipse(el1, el2):
    """
    Takes two ellipses and computes the area over the overlap
    :param el1: Ellipse
    :param el2: Ellipse
    :return: float
    """

    box = Box(el1, el2)

    constant = 100000 #raise this for accuracy
    c = 0 #number of random points in the overlap
    for i in range(constant):
        p = box.throwDart()
        if box.dotInBothEllipses(p):
            c += 1

    box.rando.closeFile() #file in box must be closed explicitly

    return calculateAreaOfOverlap(box.getArea(), c, constant)


def main():

    p1 = Point(0,0)
    p2 = Point(0,0)
    p3 = Point(0,0)
    p4 = Point(0,0)
    el1 = Ellipse(p1, p2, 2)
    el2 = Ellipse(p3, p4, 4)

    overlap = computeOverlapOfEllipse(el1, el2)

    print(overlap)

    # #For demo purposes
    #
    # p1 = Point(2, 3)
    # p2 = Point(3, 4)
    # p3 = Point(2, 2)
    # p4 = Point(3, 5)
    # el1 = Ellipse(p1, p2, 4)
    # el2 = Ellipse(p3, p4, 6)
    # overlap = computeOverlapOfEllipse(el1, el2)
    #
    # print(overlap)



if __name__ == '__main__':
    main()
