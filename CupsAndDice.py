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
        print(self.getSum())

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

    def __init__(self, balance):
        self.balance = balance
        self.bet = 0
        self.goal = None
        self.cup = Cup(0, 0, 0)

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
        self.printBalance()
        return True

    def __deduct(self):
        self.balance -= self.bet

    def __addWinnings(self, multiplier):
        self.balance += self.bet * multiplier

    def __payout(self, rollTotal):
        if rollTotal - self.goal < 0:
            print("You busted and lost")
            return
        if rollTotal - self.goal <= 3:
            print("Within 3")
            self.__addWinnings(5)
            return
        if rollTotal - self.goal <= 10:
            print("Within 10")
            self.__addWinnings(2)
            return
        if rollTotal - self.goal == 0:
            print("Winner Winner, Chicken Dinner")
            self.__addWinnings(10)
            return
        else:
            print("You lose")

    def gameRoll(self):
        self.cup.roll()
        self.__payout(self.cup.getSum())
        self.printBalance()

    def getBalance(self):
        return self.balance

    def printBalance(self):
        print("Balance is now {}".format(self.getBalance()))

    def setCup(self, six, ten, twenty):
        self.cup = Cup(six, ten, twenty)



def greet():
    name = input("Hi welcome, what is your name?")
    return name

def doYouWantToPlay:
    answer = input("I've provided you with a balance of 100 dollars, would you like to play a game? Y or N?")



def main():
    diceGame = DiceGame(100)
    diceGame.setCup(1, 1, 1)
    diceGame.setGoal()
    diceGame.setBet(20)
    diceGame.gameRoll()


if __name__ == '__main__':
    main()
