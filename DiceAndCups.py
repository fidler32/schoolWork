# William Fidler
# 02/09/20
# Dice and Cups
# "I have not given or received any unauthorized assistance on the assignment
# Link here: https://youtu.be/4-csfWaLFWo

from random import randint

class SixSidedDie():

    def __init__(self):
        self.n = 6
        self.faceValue = None

    def roll(self):
        self.faceValue = randint(1, self.n)
        print(self.faceValue)

    def getFaceValue(self):
        return self.faceValue

    def __repr__(self):
        return "{n:" + self.n+ ", faceValue:,"+ self.faceValue + "}"


class TenSidedDie(SixSidedDie):

    def __init__(self):
        self.n = 10


class TwentySidedDie(SixSidedDie):

    def __init__(self):
        self.n = 20


class Cup():

    def __init__(self, sixDie, tenDie, twentyDie):
        self.diceDict = {}
        self.sixDieList = []
        self.tenDieList = []
        self.twentyDieList = []
        self.diceDict["six"] = self.sixDieList
        self.diceDict["ten"] = self.tenDieList
        self.diceDict["twenty"] = self.twentyDieList
        for i in range(0, sixDie):
            self.diceDict["six"].append(SixSidedDie())
        for i in range(0, tenDie):
            self.diceDict["ten"].append(TenSidedDie())
        for i in range(0, twentyDie):
            self.diceDict["twenty"].append(TwentySidedDie())

    def getSum(self):

        total = 0

        for diceList in self.diceDict.values():
            for dice in diceList:
                total = total + dice.getFaceValue()

        return total

    def roll(self):
        for diceList in self.diceDict.values():
            for dice in diceList:
                dice.roll()
        print(self.getSum())

    def getAllFaceValues(self):
        for key, diceList in self.diceDict.items():
            print(key + ": ", end="")
            for dice in diceList:
                print(dice.getFaceValue(), end=" ")

    def __repr__(self):
        return "Cup(SixSidedDie({}), TenSidedDie({}), TwentySidedDie({})".format(len(self.diceDict["six"]), len(self.diceDict["ten"]), len(self.diceDict["twenty"]))



def main():
    cup = Cup(4, 2, 3)
    print(cup)
    cup.roll()
    print(cup.getAllFaceValues())

if __name__ == '__main__':
    main()
