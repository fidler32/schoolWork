# William Fidler
# 02/09/20
# Dice and Cups
# "I have not given or received any unauthorized assistance on the assignment
# Link here: https://youtu.be/nYY9GrAjXgc

from random import randint

class SixSidedDie():
    """
    Class for a six sided die
    """

    def __init__(self): #Initializer sets
        self.n = 6
        self.faceValue = None

    def roll(self):
        """
        Rolls a dice i.e. selects a random integer from 1 to size n
        :return: None
        """
        self.faceValue = randint(1, self.n)

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
        return "{n:" + self.n+ ", faceValue:,"+ self.faceValue + "}"


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

class DiceGame():

    """
    Class that represents my dice game
    """

    def __init__(self, balance, name):
        """
        Initailizes a game with a balance and name
        :param balance: int
        :param name: String
        """
        self.balance = balance
        self.bet = 0
        self.goal = None
        self.cup = Cup(0, 0, 0)
        self.name = name

    def setGoal(self):
        """
        Returns a random number from 1 to 100
        :return: int
        """
        self.goal = randint(1, 100)
        print("Goal is: {}".format(self.goal))

    def setBet(self, bet):
        """
        Set bet, return boolean True if bet is valid
        Betting with a negative number comes with a 5 dollar penalty
        :param bet: int
        :return: boolean
        """
        if self.balance == 0:
            #if balance is 0 can't place a bet
            print("You have no money")
            return False
        if bet > self.balance:
            #Cannot bet more then you have
            print("Your bet is more then your balance")
            return False
        if bet < 0:
            #Cannot bet negatively
            #Betting negatively comes with a 5 dollar penalty
            self.balance += bet
            print("Because you entered a negative amount you have been penalized 5 dollars")
            return False
        self.bet = bet
        self.__deduct() #deduct bet from balance
        print("You have bet {}, balance is now {}".format(self.bet, self.balance))
        return True

    def __deduct(self):
        """
        Helper method to deduct from balance
        :return: None
        """
        self.balance -= self.bet

    def __addWinnings(self, multiplier):
        """
        Helper method to add to balance
        Multipler will multiply bet appropiately

        :param multiplier: int
        :return: int
        """
        self.balance += self.bet * multiplier

    def __payout(self, rollTotal):
        """
        Handles payout

        :param rollTotal:
        :return: None
        """
        d = self.goal - rollTotal #calculate difference from goal and roll total
        print("You rolled {}".format(rollTotal))
        if d < 0: #rolltotal is greater then goal
            print("You busted and lost, you win nothing")
            return
        if d <= 3: #rolltotal is within 3
            print("Within 3 ")
            self.__addWinnings(5)
            return
        if d <= 10: #rolltotal is within 10
            print("Within 10")
            self.__addWinnings(2)
            return
        if d == 0: #rolltotal and goal are equal
            print("Winner Winner, Chicken Dinner")
            self.__addWinnings(10)
            return
        else:
            print("You lose")

    def gameRoll(self):
        """
        Roll the dice and trigger payout
        :return: None
        """
        print("---SHAKE SHAKE AND ROLL---\n")
        self.cup.roll()
        print("Goal is: {}".format(self.balance)) #added after video
        self.__payout(self.cup.getSum())
        self.printBalance()

    def getBalance(self):
        """
        Get current balance value
        :return: int
        """
        return self.balance

    def printBalance(self):
        """
        print balance with name
        :return:
        """
        print("{}, Your balance is {}".format(self.name, self.getBalance()))

    def setCup(self, six, ten, twenty):
        """
        Set the cup
        :param six: int
        :param ten: int
        :param twenty: int
        :return: None
        """
        self.cup = Cup(six, ten, twenty)

    def getBet(self):
        """
        Get bet
        :return: None
        """
        return self.bet



def sixSidedDie():
    """
    Get the amount of six sided die the user wants
    :return: int
    """
    while (True):
        try:
            # Get a number
            d = int(input("How many six sided die would you like?\n"))
            break

        except ValueError:
            print("Enter two integer values")

    return d

def tenSidedDie():
    """
    Get the amount of ten sided die from the user
    :return: int
    """
    while (True):
        try:
            #int
            d = int(input("How many ten sided die would you like?\n"))
            break

        except ValueError:
            print("Enter two integer values")

    return d

def twentySidedDie():
    """
    Get the amount of the twenty sided die from the user
    :return: int
    """
    while (True):
        try:
            #int
            d = int(input("How many twenty sided die would you like?\n"))
            break

        except ValueError:
            print("Enter two integer values")

    return d

def doYouWantToPlay():
    """
    Ask user if they want to play, if y, play, if n exit
    :return: None
    """
    while(True):
        answer = input("Would you like to play a game? y or n?\n")

        if answer.lower() == "y":
            return
        if answer.lower() == "n":
            print("Goodbye!")
            exit()

        print("Invalid input, please y for yes and n for no")


def greetAndGetName():
    """
    Greet the user and ask for their name
    :return: string
    """

    name = input("Hi!! What is your name?\n")

    return name


def setUpDiceFromUser():
    """
    Call underlying methods to get the amount of dice they want from user
    :return: int, int, int
    """
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
