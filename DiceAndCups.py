# William Fidler
# 02/09/20
# Dice and Cups
# "I have not given or received any unauthorized assistance on the assignment
# Link here: https://youtu.be/7rc21vwnZYw

from random import randint

class SixSidedDie():
    """
    Class for a six sided die
    """

    def __init__(self): #Initializer
        self.n = 6
        self.faceValue = None

    def roll(self):
        """
        Rolls a dice i.e. selects a random integer from 1 to size n
        :return: None
        """
        self.faceValue = randint(1, self.n)
        print(self.faceValue) #Print the value

    def getFaceValue(self):
        """
        Getter for face value
        :return:
        """
        return self.faceValue

    def __repr__(self):
        """
        Prints a six sided die object
        :return:
        """
        return "{n:" + self.n+ ", faceValue:"+ self.faceValue + "}"


class TenSidedDie(SixSidedDie):
    """
    Ten sided die extends six sided die
    """
    def __init__(self):
        self.n = 10


class TwentySidedDie(SixSidedDie):
    """
    Ten sided die extends six sided die
    """
    def __init__(self):
        self.n = 20


class Cup():
    """
    Class representing a cup holding dice
    """
    def __init__(self, sixDie, tenDie, twentyDie):
        """
        Initializes a cup containing a amount of six, ten, and twenty sided dice
        :param sixDie: int
        :param tenDie: int
        :param twentyDie: int
        """
        self.diceDict = {} #dictionary of list of dice dice
        self.sixDieList = []
        self.tenDieList = []
        self.twentyDieList = []
        self.diceDict["six"] = self.sixDieList
        self.diceDict["ten"] = self.tenDieList
        self.diceDict["twenty"] = self.twentyDieList
        for i in range(0, sixDie): #add six sided dice to six list in dice dictionary
            self.diceDict["six"].append(SixSidedDie())
        for i in range(0, tenDie): #add ten sided dice to ten list in dice dictionary
            self.diceDict["ten"].append(TenSidedDie())
        for i in range(0, twentyDie): #add twenty sided dice to twenty list in dice dictionary
            self.diceDict["twenty"].append(TwentySidedDie())

    def getSum(self):
        """
        Calculates the sum of the dices face value in the cup
        :return: int
        """
        total = 0

        for diceList in self.diceDict.values():
            for dice in diceList:
                total = total + dice.getFaceValue()

        return total

    def roll(self):
        """
        Rolls all the dice in the cup
        :return: None
        """
        for diceList in self.diceDict.values():
            for dice in diceList:
                dice.roll()
        print(self.getSum())

    def __repr__(self):
        """
        Prints a cup object elegantly in a string
        :return: String
        """
        return "Cup(SixSidedDie({}), TenSidedDie({}), TwentySidedDie({})"\
            .format(len(self.diceDict["six"]),
                    len(self.diceDict["ten"]),
                    len(self.diceDict["twenty"]))

def main():
    cup = Cup(4, 2, 3)
    print(cup)
    cup.roll()
    d= TwentySidedDie()
    print(d.roll)
    print(d.getFaceValue())

if __name__ == '__main__':
    main()
