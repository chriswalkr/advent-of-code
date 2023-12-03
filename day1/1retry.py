import re
from functools import reduce




mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "9": "9",
    "8": "8",
    "7": "7",
    "6": "6",
    "5": "5",
    "4": "4",
    "3": "3",
    "2": "2",
    "1": "1",
}

def getFirstMatch(string):
    lowest = 1000
    value = None
    for item in mapping.keys():
        index = string.find(item)
        
        if index > -1 and index < lowest:
            # print("IF TRUE", index, value)
            lowest = index
            # print("LOWEST", lowest)
            value = mapping[item]

    if lowest == 1000:
        raise Exception('this cant happen firstmatch')
    return value

def getLastMatch(string):
    lowest = 1000
    value = None
    for item in mapping.keys():
        index = string[::-1].find(item[::-1])
        print 
        if index > -1 and index < lowest:
            lowest = index
            value = mapping[item]
    if lowest == 1000:
        raise Exception('this cant happen')
    return value

def getCalibrationValue(previousValue, string):
    cleanString = "".join(string)
    

    firstMatch = getFirstMatch(cleanString)
    

    lastMatch = getLastMatch(cleanString)
    
    print(int(firstMatch + lastMatch))

    return int(firstMatch + lastMatch) + previousValue
    



def main():
    input = open('1.txt').read()

    blah = reduce(getCalibrationValue, input.splitlines(), 0)

    print(blah)
    

if __name__ == "__main__":
    main()