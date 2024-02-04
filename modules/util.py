import json


def getAllUniqueEntries(dataFrame):
    """
    Creates a list of unique entries possible
    for each column in the raw data. Useful
    for validating input when using model.
    """
    columnList = []
    uniqueDict = {}
    for colName in dataFrame.columns:
        columnList.append(colName)
        uniqueList = []
        for item in dataFrame[colName]:
            if item not in uniqueList:
                uniqueList.append(item)
        uniqueDict[colName] = uniqueList

    del uniqueDict['salary']
    del uniqueDict['salary_in_usd']

    return uniqueDict


def createMenuOptions(dataFrame):
    """ Storing menu options to json on disk to avoid reparse"""
    options = getAllUniqueEntries(dataFrame)
    with open('predOptions.json', 'w') as file:
        json.dump(options, file)


def readInMenuOption():
    """Reading in stored and parsed json"""
    with open('predOptions.json', 'r') as file:
        options = json.load(file)
    return options
