# William Fidler
# 02/03/20
# Human Pyramid
# "I have not given or received any unauthorized assistance on the assignment
# Link here: https://youtu.be/MPfI5_ggcUA

def humanPyramid(row, column):
    """
    Recursively calculate the weight being put on a humans body by position in a pyramid
    :param row: int
    :param column: int
    :return: int
    """

    if row == 0: #top row doesn't have weight
        return 0
    if row == 1: #nodes in row 1 will always have half the weight of the top row
        return 128/2
    if column == 0 or column == row: #edges are always 128/2 plus the weight of the node "above" it
        return 128/2 + humanPyramid(row -1, 0)

    #weight is equal to the sum of the nodes above pointing to target node
    return humanPyramid(row-1, column//2) + humanPyramid(row-1, (column//2)+1)

def hollaAtUser():
    """
    Greet user. Ask for row and column from user
    :return: int, int
    """

    #Keep asking user for input until they give an integer
    while(True):
        try:
            row, column = input("Hi, enter the row followed by column. EX: R C . -1 -1 to exit\n").split()

            if row == "-1" or column == "-1":
                exit()

            row = int(row)
            column = int(column)

            if(row<column):
                raise ValueError
            break

        except ValueError:
            print("Enter a integer value, row must be less then column")

    return row, column

def main():
    while(True):
        r, c = hollaAtUser()
        print(humanPyramid(r,c))

if __name__ == '__main__':
    main()