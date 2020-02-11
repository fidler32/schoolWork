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

    def getFaceValue(self):
        return self.faceValue

    def __repr__(self):
        return "{n:" + self.n + ", faceValue:," + self.faceValue + "}"


class TenSidedDie(SixSidedDie):

    def __init__(self):
        self.n = 10


class TwentySidedDie(SixSidedDie):

    def __init__(self):
        self.n = 20

class Cup():

    def __init__(self, sixDie, tenDie, twentyDie):
        self.sum = 0
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

    def setSum(self):

        self.sum = 0

        for diceList in self.diceDict.values():
            for dice in diceList:
                self.sum = self.sum + dice.getFaceValue()

    def getSum(self):
        return self.sum

    def roll(self):
        for diceList in self.diceDict.values():
            for dice in diceList:
                dice.roll()
        self.setSum()

    def getAllFaceValues(self):
        for key, diceList in self.diceDict.items():
            print(key + ": ", end="")
            for dice in diceList:
                print(dice.getFaceValue(), end=" ")

    def __repr__(self):
        return "Cup(SixSidedDie({}), TenSidedDie({}), TwentySidedDie({})".format(len(self.diceDict["six"]),
                                                                                 len(self.diceDict["ten"]),
                                                                                 len(self.diceDict["twenty"]))


class DiceGame():

    def __init__(self, balance, name):
        self.balance = balance
        self.bet = 0
        self.goal = None
        self.cup = Cup(0, 0, 0)
        self.name = name

    def setGoal(self):
        self.goal = randint(1, 100)
        print("Goal is: {}".format(self.goal))

    def setBet(self, bet):
        if self.balance == 0:
            print("You have no money")
            return False
        if bet > self.balance:
            print("Your bet is more then your balance")
            return False
        if bet < 0:
            self.balance += bet
            print("Because you entered a negative amount you have been penalized 5 dollars")
            return False
        self.bet = bet
        self.__deduct()
        print("You have bet {}, balance is now {}".format(self.bet, self.balance))
        return True

    def __deduct(self):
        self.balance -= self.bet

    def __addWinnings(self, multiplier):
        self.balance += self.bet * multiplier

    def __payout(self, rollTotal):
        d = self.goal - rollTotal
        print("You rolled {}".format(rollTotal))
        if d < 0:
            print("You busted and lost, you win nothing")
            return
        if d <= 3:
            print("Within 3 ")
            self.__addWinnings(5)
            return
        if d <= 10:
            print("Within 10")
            self.__addWinnings(2)
            return
        if d == 0:
            print("Winner Winner, Chicken Dinner")
            self.__addWinnings(10)
            return
        else:
            print("You lose")

    def gameRoll(self):
        print("---SHAKE SHAKE AND ROLL---\n")
        self.cup.roll()
        self.__payout(self.cup.getSum())
        self.printBalance()

    def getBalance(self):
        return self.balance

    def printBalance(self):
        print("{}, Your balance is {}".format(self.name, self.getBalance()))

    def setCup(self, six, ten, twenty):
        self.cup = Cup(six, ten, twenty)

    def getBet(self):
        return self.bet



def sixSidedDie():
    while (True):
        try:
            # split the input
            d = int(input("How many six sided die would you like?\n"))
            break

        except ValueError:
            print("Enter two integer values")

    return d

def tenSidedDie():
    while (True):
        try:
            # split the input
            d = int(input("How many ten sided die would you like?\n"))
            break

        except ValueError:
            print("Enter two integer values")

    return d

def twentySidedDie():
    while (True):
        try:
            # split the input
            d = int(input("How many twenty sided die would you like?\n"))
            break

        except ValueError:
            print("Enter two integer values")

    return d

def doYouWantToPlay():
    while(True):
        answer = input("Would you like to play a game? y or n?\n")

        if answer.lower() == "y":
            return answer
        if answer.lower() == "n":
            print("Goodbye!")
            exit()

        print("Invalid input, please y for yes and n for no")


def greetAndGetName():

    name = input("Hi!! What is your name?\n")

    return name


def setUpDiceFromUser():

    sixDie = sixSidedDie()
    tenDie = tenSidedDie()
    twentyDie = twentySidedDie()

    return sixDie, tenDie, twentyDie

def setBet(diceGame):
    while (True):
        try:
            # split the input
            bet = int(input("How much would you like to bet?\n"))
            if diceGame.setBet(bet):
                break
            else:
                raise ValueError
        except ValueError:
            print("Enter a valid integer value")

def main():
    name = greetAndGetName()
    diceGame = DiceGame(100, name)
    diceGame.printBalance()

    while 1:
        doYouWantToPlay()
        s, t, tw = setUpDiceFromUser()
        diceGame.setCup(s, t, tw)
        diceGame.setGoal()
        setBet(diceGame)
        print()
        diceGame.gameRoll()




if __name__ == '__main__':
    main()
