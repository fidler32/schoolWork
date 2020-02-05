# William Fidler
# 01/13/20
# Grading Logic Assignment
# "I have not given or received any unauthorized assistance on the assignment
# Link here: https://youtu.be/MoKi-1_AU9o

def evaluate(answer):
    """
    Evaluates if String is a Yes or No answer
    Yes is True
    No is False
    :param answer: String expected to be an obvious form of yes or no
    :return: boolean
    """
    if answer == "y" or answer == "yes" or answer == "Yes" or answer == "Y":
        return True
    if answer == "n" or answer == "no" or answer == "No" or answer == "N":
        return False


def autoFailCheck():
    """
    Asks a series of questions utilizing the evaluate function.
    Will return false if any question doesn't receive a Yes
    :return: boolean
    """
    a = input("Is the assignment a single uncompressed .py file?\n")

    if evaluate(a):
        a = input("Is the author's name on the assigment?\n")
    if evaluate(a):
        a = input("Date?\n")
    if evaluate(a):
        a = input("Does the assignment include the honor statement?\n")
    if evaluate(a):
        a = input(
            "Does the assignment include a link to an unlisted 3 minute YouTube "
            "video presenting the code and answering the questions?\n")
    if evaluate(a):
        return True

    return False


def evaluateAssignment():
    """
    Asks user series of questions regarding evaluation.
    Will add up total and return the output of doMath function
    :return: float
    """
    evaluation = 0

    evaluation += int(input("Out of 10 points how would you evaluate the correctness of the code?\n"))
    evaluation += int(input("Out of 10 points how would you evaluate the elegance of the code?\n"))
    evaluation += int(input("Out of 10 points how would you evaluate the students code hygiene?\n"))
    evaluation += int(
        input("Out of 10 points how would you evaluate the the discussion quality of the YouTube video\n")
    )

    return doMath(evaluation, latePoints())


def latePoints():
    """
    Asks user if assignment was late, if so, returns amount of hours
    :return: float
    """
    a = input("Was the assignment late?\n")

    if not evaluate(a):
        return 0

    hours = float(input("How many hours was it late?\n"))

    return hours


def doMath(evaluation, hoursLate):
    """
    Calculates score
    :param evaluation:
    :param hoursLate:
    :return:
    """
    return ((evaluation / 40) * 100) - hoursLate


def getAssignmentScore():
    """
    If autoFail check is False will return score of 0, otherwise continues with evaluation
    :return: float
    """
    if not autoFailCheck():
        return print("Assignment Score is: " + str(0))
    else:
        return print("Assignment Score is: " + str(evaluateAssignment()))


getAssignmentScore()


