# William Fidler
# 01/25/20
# Goldbach
# "I have not given or received any unauthorized assistance on the assignment
# Link here: https://youtu.be/C7lUftZYQRo

def isPrime(number):
    """
    Finds if a number is prime and returns True if so
    :return: boolean
    """
    #TODO: Create a better checker

    if number % 2 == 0:  # if number is even it is not prime
        return False

    for i in range(3, number):  # check if i for i < number divides number if so return false
        if number % i == 0:
            return False
    return True  # if you make it here number is prime


def setOfPrimes(maxNumber):
    """
    Create a set of prime numbers from 2 to maxnumber (maxNumber included)
    :param maxNumber:
    :return: list
    """

    primes = set()  # instantiate a set

    for i in range(3, maxNumber + 1, 2):  # iterate through odd numbers only
        if isPrime(i):
            primes.add(i)

    return primes


def findPrimeSum(primes, number):
    """
    Takes a list of primes and an even number to find it's prime sum
    :param primes: list
    :param number: int
    :return: int, int
    """
    if number == 4:  # since 4 is single special case return 2 and 2
        return 2, 2

    for prime in sorted(primes):  # iterate through every prime in ascending order
        prime2 = number - prime
        if prime2 in primes:  # if the value of prime2 is prime then we found the prime pair
            return prime, prime2


def printPrimeSum(primes, number):
    """
    Finds the prime numbers that add up to number and prints it out in number = a + b format
    :param primes: set
    :param number: int
    :return: nothing
    """

    a, b = findPrimeSum(primes, number)

    print(number, "=", a, " + ", b)


def main():
    maxRange = 100
    primes = setOfPrimes(maxRange)
    # print(primes)
    for number in range(4, maxRange, 2):
        # print(number)
        printPrimeSum(primes, number)


if __name__ == '__main__':
    main()
