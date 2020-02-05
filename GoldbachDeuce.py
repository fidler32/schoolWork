# William Fidler
# 02/03/20
# GoldbachDeuce
# "I have not given or received any unauthorized assistance on the assignment
# Link here: https://youtu.be/ttMm0i98u1I

from random import randint


def createList(i):
    """
    Will return a sorted list of random integers from 1 to 100 of size i
    :param i: int
    :return: sorted list
    """
    randos = [] #start a list of randos

    while i != 0:   #when i is 0 bail
        randos.append(randint(0, 100)) #use randint to add a random number to list
        i = i-1 #decrement i by 1

    randos.sort() #sort list
    return randos

def doBinarySearch(nums, x):
    """
    Will conduct a binary search on a list nums for int x
    :param nums: list
    :param x: int
    :return: boolean
    """
    low = 0
    high = len(nums) -1

    while low < high:
        mid = (low+high)//2 #middle of list
        item = nums[mid] #item is the digit in mid
        if x == item:
            return True
        elif x < item: #if the item we're searching for is less then the middle set new high to middle -1
            high = mid -1
        else: #if item we're searching for is greater then the middle bring low to mid + 1
            low = mid + 1
    return False



def sumInList(nums, n, size):
    """
    Prints pair of digits in list that add up to equal n
    :param nums: list
    :param n: int
    :param size: int
    :return: None
    """
    i = 0
    while i < size: #iterate through the whole list
        target = n-nums[i] #we find the target integer we need by subtracting n by the int of the index of list
        if target < 0: #because sorted list if we get a negative number we've gone too far
            print("No pair of numbers added up to {}".format(n))
            return
        if(doBinarySearch(nums, target)): #if we find our target we have found the pair that sums to n
            print(nums[i], target)
            return
        i = i+1 #increment i by 1
    print("No pair of numbers added up to {}".format(n)) #if you make it here the pair of integers doesn't exist

def hollaAtUser():
    """
    Greet user. Ask for i and n from user
    :return: int, int
    """

    #Keep asking user for input until they give an integer
    while(True):
        try:
            #split the input
            i, n = input("Hi, enter the i followed by n. Example -> i n \n -1 -1 to exit \n").split()

            #exit strategy
            if i == "-1" or n == "-1":
                exit()
            #cast to int
            i = int(i)
            n = int(n)
            break

        except ValueError:
            print("Enter two integer values")

    return i, n


def main():
    while(True):
        i, n = hollaAtUser()
        nums = createList(i)
        # print(nums)
        sumInList(nums, n, i)




if __name__ == '__main__':
    main()