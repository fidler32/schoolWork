# William Fidler
# 02/22/20
# Dice and Cups
# "I have not given or received any unauthorized assistance on the assignment
# Link here:

from time import time_ns
from statistics import mean

class WarAndPeacePseudoRandomNumberGenerator():

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

        self.closeFile(file)

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
        filepath = "resources/war-and-peace.txt"
        fileString = ""
        with open(filepath, "r") as file:
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
            file.seek(value)
            a = file.read(1)
            value += 1
            try:
                b = a.decode("ascii")
            except UnicodeError:
                a = " "

        return b

    def openFile(self):
        filepath = "resources/war-and-peace.txt"
        return open(filepath, "rb")

    def closeFile(self, fileObject):
        fileObject.close()




def main():

    prng = WarAndPeacePseudoRandomNumberGenerator()
    list1 = []

    prng2 = WarAndPeacePseudoRandomNumberGenerator(1234)
    a = prng2.random()
    b = prng2.random()

    # c = prng2.getCharacter(1234)
    # print(c)

    for i in range(10000):
        r = prng.random()
        list1.append(r)

    median = mean(list1)
    minimum = min(list1)
    maximum = max(list1)

    print(median)
    print(minimum)
    print(maximum)
    print(a, b)


if __name__ == '__main__':
    main()



