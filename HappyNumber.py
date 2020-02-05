# William Fidler
# 01/25/20
# Happy Numbers
# "I have not given or received any unauthorized assistance on the assignment
# Link here: https://youtu.be/jMdPwt5XN4Q


def isHappy(testNumber):
    """
    Function returns True if number is "Happy" False if "Sad"
    :param testNumber: int
    :return: boolean
    """
    setOfNumbers = set() #create a set

    numList = prepList(testNumber) #generate a list of digits from integer

    total = getTotal(numList) #calculate the addition of digits squared

    setOfNumbers.add(total)

    #print(total)
    while total != 1: #if total is 1 then number is Happy
        numList = prepList(total)
        total = getTotal(numList)
        #print(total)
        if total in setOfNumbers: #if total has already been added to set return False
            return False
        setOfNumbers.add(total) #add total to set

    return True

def prepList(testNumber):
    """
    Returns a list of digits from given integer Ex. 123 returns [1,2,3]
    :param testNumber: int
    :return: list
    """

    #create list of digits from given integer
    numList = [int(d) for d in str(testNumber)]
    #print(numList)

    return numList

def getTotal(numList):

    """
    Calculates the sum of the items of a list squared
    :param numList: list
    :return: int
    """
    #for every item in numlist (x) multiply it by itself, then map it to a list, then get the sum of that list
    #return result
    return sum(map(lambda x: x*x, numList))

def isPrime(number):
    """
    Finds if a number is prime and returns True if so
    :return: boolean
    """
    #TODO: Create a better checker

    if number % 2 == 0 or number == 1:  # if number is even or 1 it is not prime
        return False

    for i in range(3, number):  # check if i for i < number divides number if so return false
        if number % i == 0:
            return False
    return True  # if you make it here number is prime

def hollaAtUser():

    #Keep asking user for input until they give an integer
    while(True):
        try:
            number = int(input("Enter a number you would like to test for happiness\n"))
            break
        except ValueError:
            print("Enter a integer value")

    if isPrime(number):
        #print("{} is prime".format(number))
        return number, True
    else:
        #print("{} is not prime".format(number))
        return number, False

def main():

    #loops infinitely .
    while(1):
        a, prime = hollaAtUser()

        if prime:
            if isHappy(a):
                print("{} is a happy prime".format(a))
            else:
                print("{} is a sad prime".format(a))
        else:
            if isHappy(a):
                print("{} is a happy non-prime".format(a))
            else:
                print("{} is a sad non-prime".format(a))


if __name__ == '__main__':
    main()