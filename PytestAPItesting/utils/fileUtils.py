import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
TEST_DATA_DIR = BASE_DIR.joinpath('TestData')


def getJsonFromFile(filename):
    filename = TEST_DATA_DIR.joinpath(filename)
    with open(filename, 'r') as file:
        return json.load(file)

# Function to read data from CSV file
def getCsvDataAsDict(filename):
    filepath = TEST_DATA_DIR.joinpath(filename)
    with open(filepath, 'r') as file:
        csvFile = csv.DictReader(file)
        dictList = list(csvFile)
    return dictList

# Get data from CSV as a list
def getDataAsList(filename):
    filepath = TEST_DATA_DIR.joinpath(filename)
    with open(filepath, 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        lines = list(reader)
    return lines


def getDataAsTuple(file):
    dataList = getDataAsList(file)
    newList = []
    for line in dataList:
        newList.append((line[:2], line[2]))
    return newList


print("------------------------------")
# print(getCsvDataAsDict('D:\\PytestAPItesting\\TestData\\resgisterAPIdata.csv'))

print(getDataAsList('D:\\PytestAPItesting\\TestData\\registerApiDataWithStatus.csv'))

# Creating a dict from two lists
# keys = ['a', 'b', 'c']
# values = ['alpha', 'beta', 'delta']
# d = dict(zip(keys, values))
# print(d)

