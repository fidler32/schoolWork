# William Fidler
# 02/26/20
# Plot Generator
# "I have not given or received any unauthorized assistance on the assignment
# Link here: https://youtu.be/cJGdJeF4h-Y

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



def main():

    a = SimplePlotGenerator()
    print(a.generate())

    b = RandomPlotGenerator()
    print(b.generate())

    c = InteractivePlotGenerator()
    c.setPlotAdjective("anyAdj")
    c.setPlotAdjectiveEvil("evil")
    c.setPlotName("name")
    c.setPlotProfesions("prof")
    c.setPlotVerb("verb")
    c.setPlotVillain("villain")
    c.setPlotVillainJob("villainJob")
    print(c.generate())
    #
    # print(c.getPlotNameList())
    # print(c.getPlotAdjectiveList())
    # print(c.getPlotEvilAdjectiveList())
    # print(c.getPlotProfessionList())
    # print(c.getPlotVerbList())
    # print(c.getPlotVillainList())
    # print(c.getVillainJobList())


if __name__ == '__main__':
    main()



