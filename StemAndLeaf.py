# William Fidler
# 01/21/20
# Stem and Leaf
# "I have not given or received any unauthorized assistance on the assignment
# Link here: https://youtu.be/u8gC-Mc2f00

file1 = "/home/fidler32/Documents/School/assignments/resources/StemAndLeaf1.txt"
file2 = "/home/fidler32/Documents/School/assignments/resources/StemAndLeaf2.txt"
file3 = "/home/fidler32/Documents/School/assignments/resources/StemAndLeaf3.txt"

def createDictionary(lineList):
    """
    Returns a dictionary where the key (stem) and list of values ( leafs)
    :param lineList: list
    :return dict:  dictionary
    """
    dict = {}

    lineList = list(map(str.strip, lineList)) #strip every item in the list of newLine

    split = getSplit(lineList) #calculate the split

    lineList = list(map(int, lineList)) #cast every item of the list to an integer

    for i in range(0, len(lineList)): #loop through and add item to dictionary appropiately
        createStruct(dict, lineList[i], split)

    return dict

def createStruct(dict, number, split):
    """
    Formats dictionary to have split values to have appropiate key value pairs
    :param dict: dictionary
    :param number: int
    :param split: int
    :return dict: dictionary
    """
    stem = getStem(number, split) #stem is all digits except last

    if stem in dict.keys(): #if key already exists add to list
        dict[stem].append(getLeaf(number, split))
    else: #create new key list pairing
        dict[stem] = [getLeaf(number, split)]

    return dict

def getSplit(numList):
    """
    Calculates the appropiate split value by finding the most common length and conducting an integer divsion of 2
    :param numList: list
    :return: int
    """
    dict = {}

    for num in numList: #check every number in list
        if len(num) in dict.keys():  # if key already exists increment by 1
            dict[len(num)] += 1
        else:  # add length to dictionary as key set value to 1
            dict[len(num)] = 1

    mostCommon = 0

    for key in dict: #find the most common length
        if dict[key] > mostCommon:
            mostCommon = key

    return mostCommon//2

def getLeaf(number, split):
    """
    use split value to get leaf
    :param number: int
    :param split: int
    :return: string
    """
    return str(number)[split:]

def getStem(number, split):
    """
    use split value to get stem
    :param number: int
    :param split: int
    :return: int
    """

    return int(str(number)[:split])

def printStemLeafFormat(dict):
    """
    Prints a dictionary in a stem and leaf format
    :param dict: dictionary
    :return: nothing
    """

    for key in sorted(dict.keys()): #sort keys before looping
        print(str(key) + ": ", end=" ") #print and add space instead of creating new line
        list = sorted(dict[key]) #create sorted list
        print(*list)  #print list seperated by space then create new line



def readFile(filePath):
    """
    Reads a file from filepath and returns a list
    :param filePath: string
    :return: list
    """
    infile = open(filePath, "r") #open for read
    lineList = infile.readlines() #create list
    infile.close()

    return lineList

def greet():
    """
    greet the user
    :return: nothing
    """
    print("Hello, welcome to the Stem Leaf Plot program")

def getFile():
    """
    Ask user to enter a number 1, 2, or 3. Exit if anything else is entered
    :return: string
    """
    num = input("Please enter a number, 1, 2, 3. Anything else will exit program\n")
    if num == "1":
        return file1
    if num == "2":
        return file2
    if num == "3":
        return file3
    else:
        exit()

def main():
    greet()
    while(1):
        file = getFile()
        list = readFile(file)
        dict = createDictionary(list)
        printStemLeafFormat(dict)

if __name__ == '__main__':
    main()