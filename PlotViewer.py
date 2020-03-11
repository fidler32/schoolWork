# William Fidler
# 02/26/20
# Plot Generator
# "I have not given or received any unauthorized assistance on the assignment
# Link here: https://youtu.be/pNXczyVgVH8

import random

class SimplePlotGenerator:

    def __init__(self):
        """
        Initialize SimplePlotGenerator
        """
        self.message = "Something happens"

    def generate(self):
        return self.message

class RandomPlotGenerator(SimplePlotGenerator):

    def __init__(self):
        """
        Message intialized by createMessage function
        """
        self.message = self.createMessage()

    def createMessage(self):
        """
        Forms the message using helper methods
        :return:
        """
        message = "{}, a {} {}, must {} the {} {}, {}"\
            .format(self.getPlotName(), self.getPlotAdjective(),
                    self.getPlotProfession(), self.getPlotVerb(), self.getPlotEvilAdjective(),
                    self.getVillainJob(), self.getPlotVillain())
        return message

    def getPlotName(self):
        """
        get random plot name
        :return: string
        """
        filepath = "resources/plot_names.txt"
        return self.readFile(filepath)

    def getPlotAdjective(self):
        """
        get random plot adjective
        :return: string
        """
        filepath = "resources/plot_adjectives.txt"
        return self.readFile(filepath)

    def getPlotProfession(self):
        """
        get plot random profession
        :return: string
        """
        filepath = "resources/plot_profesions.txt"
        return self.readFile(filepath)

    def getPlotVerb(self):
        """
        get random plot verb
        :return: string
        """
        filepath = "resources/plot_verbs.txt"
        return self.readFile(filepath)

    def getPlotEvilAdjective(self):
        """
        get random plot evil adjective
        :return: String
        """
        filepath = "resources/plot_adjectives_evil.txt"
        return self.readFile(filepath)


    def getVillainJob(self):
        """
        get random villain job
        :return: String
        """
        filepath = "resources/plot_villian_job.txt"
        return self.readFile(filepath)

    def getPlotVillain(self):
        """
        get random plot villain
        :return: String
        """
        filepath = "resources/plot_villains.txt"
        return self.readFile(filepath)

    def readFile(self, filepath):
        """
        Take a file path and return one randomly selected line
        :return: list
        """
        with open(filepath) as f:
            lineList = f.readlines()

        return lineList[random.randint(0, len(lineList)-1)].rstrip().strip('\n')

class InteractivePlotGenerator(SimplePlotGenerator):
    """
    Class is meant to be used by a view
    """

    def __init__(self):
        """
        intialize variables
        """
        self.message = None
        self.plotDict = {}

    def generate(self):
        """
        Generate message
        :return:
        """
        try:
            self.message = "{}, a {} {}, must {} the {} {}, {}" \
                .format(self.plotDict["name"], self.plotDict["adj"],
                        self.plotDict["prof"], self.plotDict["verb"], self.plotDict["adjEvil"],
                        self.plotDict["vJob"], self.plotDict["villain"])
        except Exception:
            return "Exception occured when generating message"

        return self.message

    def setPlotName(self, messagePiece):
        """
        set plot name n dict
        :param messagePiece:
        :return: None
        """
        self.plotDict["name"] = messagePiece

    def setPlotAdjective(self, messagePiece):
        """
        set plot adjective in dictionary
        :param messagePiece:
        :return:
        """
        self.plotDict["adj"] = messagePiece

    def setPlotAdjectiveEvil(self, messagePiece):
        """
        set plot adjective in dict
        :param messagePiece:
        :return:
        """
        self.plotDict["adjEvil"] = messagePiece

    def setPlotProfesions(self, messagePiece):
        """
        set plot profesion in dict
        :param messagePiece:
        :return:
        """
        self.plotDict["prof"] = messagePiece

    def setPlotVerb(self, messagePiece):
        """
        set plot verb in dictionary
        :param messagePiece:
        :return:
        """
        self.plotDict["verb"] = messagePiece

    def setPlotVillain(self, messagePiece):
        """
        set plot villain in dict
        :param messagePiece:
        :return:
        """
        self.plotDict["villain"] = messagePiece

    def setPlotVillainJob(self, messagePiece):
        """
        set plot villain job in dict
        :param messagePiece:
        :return:
        """
        self.plotDict["vJob"] = messagePiece

    def getPlotNameList(self):
        """
        get a list of length 5 of plot names
        :return:
        """
        filepath = "resources/plot_names.txt"
        return self.getList(filepath)

    def getPlotAdjectiveList(self):
        """
        get a list of length 5 of plot adjectives
        :return:
        """
        filepath = "resources/plot_adjectives.txt"
        return self.getList(filepath)

    def getPlotProfessionList(self):
        """
        get a list of length 5 of plot professions
        :return:
        """
        filepath = "resources/plot_profesions.txt"
        return self.getList(filepath)

    def getPlotVerbList(self):
        """
        get a list of length 5 of plot verb lists
        :return:
        """
        filepath = "resources/plot_verbs.txt"
        return self.getList(filepath)

    def getPlotEvilAdjectiveList(self):
        """
        get a list of length 5 of plot evil adjectives list
        :return:
        """
        filepath = "resources/plot_adjectives_evil.txt"
        return self.getList(filepath)


    def getVillainJobList(self):
        """
        get a list of length 5 of plot villain jobs
        :return:
        """
        filepath = "resources/plot_villian_job.txt"
        return self.getList(filepath)

    def getPlotVillainList(self):
        """
        get a list of length 5 of plot villains
        :return:
        """
        filepath = "resources/plot_villains.txt"
        return self.getList(filepath)

    def getList(self, filepath):
        """
        Takes a filepath and returns a list of 5 random lines
        :param: String - filepath
        :return: list
        """
        rList = []
        daSet = set()
        with open(filepath) as f:
            lineList = f.readlines()

        while len(rList) < 5:
            index = random.randint(0, len(lineList)-1)
            if index not in daSet:
                daSet.add(index)
                rList.append(lineList[index].rstrip().strip('\n'))

        return rList


class PlotViewer():
    """
    Class replicating a view
    """
    def registerPlotGenerator(self, generator):
        """
        Sets the class generator
        :param generator:
        :return:
        """
        if not isinstance(generator, SimplePlotGenerator):
            raise Exception

        self.generator = generator

    def generate(self):
        """
        Will generate a message using the class generator generate method
        :return: String
        """
        #if generator is a InteractivePlotGenerator interact with user
        if self.getType() is InteractivePlotGenerator:
            self.interact()
            return self.generator.generate()
        else:
            return self.generator.generate()

    def getType(self):
        """
        Get the type of the class generator
        :return: Type
        """
        return type(self.generator)

    def interact(self):
        """
        Interact with user and set the generator dictionary
        :return: None
        """
        plotName = self.interactToGetPlotName()
        plotAdjective = self.interactToGetPlotAdjective()
        plotAdjectiveEvil = self.interactToGetPlotAdjective()
        plotProfesion = self.interactToGetPlotProfesion()
        plotVerb = self.interactToGetPlotVerb()
        plotVillain = self.interactToGetPlotVillain()
        plotVillainJob = self.interactToGetPlotVillainJob()


        self.generator.setPlotAdjective(plotAdjective)
        self.generator.setPlotAdjectiveEvil(plotAdjectiveEvil)
        self.generator.setPlotName(plotName)
        self.generator.setPlotProfesions(plotProfesion)
        self.generator.setPlotVerb(plotVerb)
        self.generator.setPlotVillain(plotVillain)
        self.generator.setPlotVillainJob(plotVillainJob)

    def interactToGetPlotName(self):
        """
        Ask user to select a plot name
        :return:
        """
        list = self.generator.getPlotNameList()
        print("Chose a hero's name from the following list:\n")
        return self.printListandGetInput(list)

    def interactToGetPlotAdjective(self):
        """
        Ask user to select plot adjective
        :return:
        """
        list = self.generator.getPlotAdjectiveList()
        print("Chose a adjective from the following list:\n")
        return self.printListandGetInput(list)

    def interactToGetPlotEvilAdjective(self):
        """
        Ask user to select an evil adjective
        :return:
        """
        list = self.generator.getPlotNameList()
        print("Chose a evil adjective from the following list:\n")
        return self.printListandGetInput(list)

    def interactToGetPlotProfesion(self):
        """
        Ask user to select an profesion
        :return:
        """
        list = self.generator.getPlotProfessionList()
        print("Chose a profesion from the following list:\n")
        return self.printListandGetInput(list)

    def interactToGetPlotVerb(self):
        """
        Ask user to select a plot verb
        :return:
        """
        list = self.generator.getPlotVerbList()
        print("Chose a verb name from the following list:\n")
        return self.printListandGetInput(list)

    def interactToGetPlotVillain(self):
        """
        Ask user to select a plot villain
        :return:
        """
        list = self.generator.getPlotVillainList()
        print("Chose a hero's name from the following list:\n")
        return self.printListandGetInput(list)

    def interactToGetPlotVillainJob(self):
        """
        Ask user to select a plot villain job
        :return:
        """
        list = self.generator.getVillainJobList()
        print("Chose a hero's name from the following list:\n")
        return self.printListandGetInput(list)

    def printListandGetInput(self, list):
        """
        Display a list to user and return the index of the selected list
        :param list: selections
        :return: int
        """
        index = None

        while index is None:

            for i in range(0, len(list)):
                print("{}) {}".format(i+1, list[i]))

            try:
                index = int(input("\n"))
            except Exception:
                print("Please select options from the list. Either 1, 2, 3, 4 or 5")
                index = None
                continue

            if index > len(list) or index <=0:
                print("Invalid input please try again")
                index = None

        return list[index-1]

def main():
    pv = PlotViewer()
    pv.registerPlotGenerator(SimplePlotGenerator())
    print(pv.generate())
    pv.registerPlotGenerator(RandomPlotGenerator())
    print(pv.generate())
    pv.registerPlotGenerator(InteractivePlotGenerator())
    print(pv.generate())

if __name__ == '__main__':
    main()