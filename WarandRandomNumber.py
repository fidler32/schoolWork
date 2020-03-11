# William Fidler
# 02/26/20
# War and Random Number
# "I have not given or received any unauthorized assistance on the assignment
# Link here:https://youtu.be/TympaY-sb6E

from time import time_ns
from statistics import mean


class WarAndPeacePseudoRandomNumberGenerator():
    """
    Random number generator
    Every instance will open a new File, so it's important to close explicitly
    using closeFile function
    """
    filepath = "resources/war-and-peace.txt"

    def __init__(self, seedValue=None):

        self.seedValue = seedValue
        self.file = self.openFile()

    def getRandomValue(self):
        """
        Returns the seed value of the class, if there is none returns last 5 digits of time
        :return:
        """
        if self.seedValue is None:
            x = time_ns()
            sax = str(x)
            x = int(sax[-5:])  # last 5 digits

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
        return (a * seed + c) % m

    def random(self):
        """
        Calculate a random number using the text file
        :return:
        """
        value = self.getRandomValue()
        binaryString = ""

        while len(binaryString) < 16:
            a = self.getCharacter(value)
            i = value + self.getRandomValue()
            b = self.getCharacter(i)
            bit = self.judge(a, b)
            if bit is None:
                value = value + self.getRandomValue()
                continue
            value = value + self.getRandomValue()
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

        for i in range(len(bitString)):  # expect bit string to be len of 16 and made up of 0 and 1 only
            sum += int(bitString[i]) * (1 / (divisor))
            divisor = divisor * 2
        return sum

    def judge(self, a, b):
        """
        Return a 0 or 1
        :param a: char
        :param b: char
        :return: String
        """
        if a > b:
            return "1"
        if a < b:
            return "0"
        else:
            return None

    def getCharacter(self, value):
        """
        Get a character from a file
        :param value: int
        :return: char
        """
        a = " "
        b = None

        while a.isspace():  # avoid returning whitespace
            self.file.seek(value)
            a = self.file.read(1)
            value += 1  # increment value by 1
            try:
                b = a.decode("ascii")
            except UnicodeError:  # if not an ascii continue loop
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




def main():

    prng = WarAndPeacePseudoRandomNumberGenerator()
    list1 = []

    prng2 = WarAndPeacePseudoRandomNumberGenerator(1234)
    a = prng2.random()
    b = prng2.random()
    prng2.closeFile() #file must be closed explicitly here

    for i in range(10000):
        r = prng.random()
        list1.append(r)

    prng.closeFile() #file must be closed explicitly
    median = mean(list1)
    minimum = min(list1)
    maximum = max(list1)

    print("median: {} ".format(median))
    print("minimum: {} ".format(minimum))
    print("maximum: {} ".format(maximum))
    print("With seed 1234: {} {}".format(a, b))


if __name__ == '__main__':
    main()



