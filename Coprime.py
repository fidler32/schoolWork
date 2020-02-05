# William Fidler
# 01/13/20
# CoPrime
# "I have not given or received any unauthorized assistance on the assignment
# Link here: https://youtu.be/4-csfWaLFWo

import math


def coprime_test_loop():
    """
    Infinite loop asking user for values

    :return: boolean
    """
    while (True):
        print("-----Start-----")
        a = int(input("Please insert a value for a\n"))
        b = int(input("Please insert a value for b\n"))
        print()

        if(coprime(a, b)):
            print("{} and {} are coprime".format(a, b))
        else:
            print("{} and {} are NOT coprime".format(a, b))

        exit = input("Input exit to exit\n")

        if exit == "exit":
            break

def coprime(a, b):
    """
    Evaluates if a and b are coprime using the math libray which uses the standard C math functions

    i.e. greatest common divisor must be 1 else false

    could be written using the Euclidean algorithm which would be written

    a = bq + r
    b = rq + r1
    r = r1q + r2

    gcd(a, b)
        while(b):
            a, b = b, a%b
        return a == 1

    where a > b and the return value b would be the gcd

    reference: https://codility.com/media/train/10-Gcd.pdf, https://www.youtube.com/watch?v=H_2_nqKAZ5w

    :param a:
    :param b:
    :return: boolean
    """
    return math.gcd(a, b) == 1

coprime_test_loop()