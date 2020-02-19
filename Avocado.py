# William Fidler
# 02/15/20
# Avocado
# "I have not given or received any unauthorized assistance on the assignment
# Link here:

import statistics

def getLinesOfFile():
    filepath = "resources/avocado.csv"
    file = open(filepath, "r")
    lines = file.readlines()
    file.close()
    return lines

def readAndComputeMean_SM(column):
    """
    Takes a variable name in the form of a string, reads into memory the values for that variable,
    and computes the mean using statistics module
    :param column: string
    :return: float
    """

    values = readCsv(column)
    # print(sum(values) / len(values))
    x = statistics.mean(values)
    printMean(column, x)
    return x

def readAndComputeSD_SM(column):
    """
    Takes a variable in the form of a string, reads into memory the values for that variable
    and computes the standard deviation using statistics module
    :param column:
    :return: float
    """

    values = readCsv(column)
    #print(values)
    x = statistics.stdev(values)
    print("The standard deviation of {} is {}".format(column, x))
    return x

def readAndComputeMedian_SM(column):
    """
    Takes a variable in the form of a string, reads into memory the values for that variable,
    and computes the median using the statistics module


    :param column:
    :return: float
    """
    values = readCsv(column)
    x = statistics.median(values)
    print("The median of {} is {}".format(column, x))
    return x

def readAndComputeMean_HG(column):
    values = readCsv(column)
    x = calculateSum(values)
    # print("length of values {}".format(len(values)))
    mean = x/len(values)
    print("The mean of {} is {}".format(column, mean))
    return mean

def readAndComputeSD_HG(column):
    values = readCsv(column)
    # print(values)
    x = calculateSd(values)
    print("The standard deviation of {} is {}".format(column, x))
    return x

def readAndComputeMedian_HG(column):
    values = readCsv(column)
    # print(values)
    x = statistics.median(values)
    print("The median of {} is {}".format(column, x))

def calculateSum(list):

    sum = 0

    for item in list:
        sum += item

    return sum

def calculateSd(list):

    x = calculateSum(list)
    length = len(list)
    avg = x/length
    list2 = []

    for item in list:
        y = item - avg
        list2.append(y**2)

    sum = calculateSum(list2)
    n = length-1
    stdv = (sum/n)**(1/2)

    return stdv

def getMedian(list):

    list.sort()

    return list[len(list)//2]

def readCsv(column):
    """
    Read CSV file
    :return: list
    """
    list = []
    index = getIndex(column)
    lines = getLinesOfFile()
    i = 1
    while i < len(lines):
        nums = lines[i].split(",")
        # print(nums)
        list.append(float(nums[index]))
        i += 1

    return list

def readAndComputeMean_MML(column):
    """
    Read CSV file
    :return: list
    """
    index = getIndex(column)
    lines = getLinesOfFile()
    i = 1
    sum = 0
    while i < len(lines):
        nums = lines[i].split(",")
        # print(nums)
        sum += float(nums[index])
        i += 1
    n = i-1
    # printMean(column, sum/n)
    return sum/n

def readAndComputeSD_MML(column):
    """
    Read CSV file
    :return: list
    """

    index = getIndex(column)
    lines = getLinesOfFile()
    avg = readAndComputeMean_MML(column)
    n =len(lines)

    i = 1

    sumOfdiff = 0

    while i < n:
        nums = lines[i].split(",")
        y = float(nums[index]) - avg
        sumOfdiff += y **2
        i+=1

    #n = i-1 n being the length of list
    n = n-2
    sdv = (sumOfdiff/n) ** (1 / 2)
    printSD(column, sdv)
    return sdv

def readAndComputeMedian_MML(column):
    """
    Read CSV file
    :return: list
    """
    index = getIndex(column)
    lines = getLinesOfFile()
    low, high, length = getInitialValues(lines, index)
    i = 1
    winner = None
    tooLow = 1
    tooHigh = 0
    while tooLow != tooHigh:
        j = 1
        print("Cycle {}".format(i))
        bin = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        spread = calculateSpread(low, high, 10)
        size = 0
        print("------------------low: {} high: {}--------------".format(low, high))
        while j < length:
            nums2 = lines[j].split(",")
            x = float(nums2[index])
            # if x < low:
            #     tooLow += 1
            # elif x > high:
            #     # print("Putting {} in bin".format(x))
            #     tooHigh += 1
            # else:
            size += 1
            putInBin(low, high, bin, x, spread)
            j+=1
        print(bin)
        bin2 = bin.copy()

        calculatePercentages(bin, length - 1)
        multiplier = getBinIndex(bin)
        tooLow = calculateTooLow(bin2, multiplier)
        tooHigh = calculateTooHigh(bin2, multiplier)

        print(bin)
        low = (spread*multiplier)+low
        high = (spread*(multiplier+1))+low

        print(size)
        print("index: {}".format(multiplier))
        print("tooLow: {} tooHigh: {}".format(tooLow, tooHigh))

        i += 1


    print("The median of {} is {}".format(column, winner))

def getIndex(column):

    index = None
    lines = getLinesOfFile()
    i = 0
    first = lines[0].split(",")
    # print(first)
    while i < len(first):
        # print(first[i])
        if first[i] == column:
            index = i
            # print("indx={}, name={}".format(i, first[i]))
            break
        i += 1

    return index

def putInBin(low, high, tuple, x, spread):

    if x < low+spread:
        tuple[0]+=1
        return tuple
    if x < low+(spread*2):
        tuple[1]+=1
        return tuple
    if x < low+(spread*3):
        tuple[2]+=1
        return tuple
    if x < low+(spread*4):
        tuple[3]+=1
        return tuple
    if x < low+(spread*5):
        tuple[4]+=1
        return tuple
    if x < low+(spread*6):
        tuple[5]+=1
        return tuple
    if x <low+(spread*7):
        tuple[6]+=1
        return tuple
    if x < low+(spread*8):
        tuple[7]+=1
        return tuple
    if x < low+(spread*9):
        tuple[8]+=1
        return tuple
    if x < high:
        tuple[9]+=1
        return tuple
    return tuple

def calculatePercentages(tuple, size):

    total = 0
    for i in range(len(tuple)):
        total += tuple[i]
        tuple[i] = total/size

def calculateTooHigh(tuple, index):

    tooHigh = 0
    while index < len(tuple):
        tooHigh += tuple[index]
        index += 1
    return tooHigh

def calculateTooLow(tuple, index):
    tooLow = 0
    i = 0

    while i < index:
        tooLow += tuple[index]
        i += 1
    return tooLow

def calculateSpread(low, high, size):

    spread = (high-low)/size
    print("low: {} high: {}".format(low, high))
    print("Spread is {}".format(spread))
    return spread

def getBinIndex(tuple):
    i = 0
    while tuple[i] < .50:
        i+=1
    return i

def getInitialValues(lines, index):

    low = 100000000000000
    high = 0
    i = 1

    while i < len(lines):
        nums = lines[i].split(",")
        y = float(nums[index])

        if y < low:
             low = y

        if y > high:
            high = y

        i += 1

    return low, high, i

def printMean(column, mean):
    print("The mean of {} is {}".format(column, mean))

def printSD(column, sd):
    print("The standard deviation of {} is {}".format(column, sd))

def printMedian(column, median):
    print("The median of {} is {}".format(column, median))

def main():
    col = "Total Volume"
    readAndComputeMean_SM(col)
    readAndComputeSD_SM(col)
    readAndComputeMedian_SM(col)
    print("---Home Grown----")
    readAndComputeMean_HG(col)
    readAndComputeSD_HG(col)
    readAndComputeMedian_HG(col)
    print("---Memoryless---")
    x = readAndComputeMean_MML(col)
    printMean(col, x)
    readAndComputeSD_MML(col)
    readAndComputeMedian_MML(col)

if __name__ == '__main__':
    main()

