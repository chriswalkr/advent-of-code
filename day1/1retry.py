from functools import reduce

# Just a map of the values
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
    for item in mapping.keys(): # Iterate through mapping above
        index = string.find(item)
        if index > -1 and index < lowest: # If it's found (index > -1) and lower than the last found (stroed in lowest)
            lowest = index
            value = mapping[item]

    if lowest == 1000:
        raise Exception('this cant happen firstmatch')
    return value # return the stored value (stuck it there for easy keeping)

def getLastMatch(string):
    lowest = 1000
    value = None
    for item in mapping.keys():
        index = string[::-1].find(item[::-1]) # Same as above, but flip the strings using slicing
        if index > -1 and index < lowest:
            lowest = index
            value = mapping[item]
    if lowest == 1000:
        raise Exception('this cant happen')
    return value

def getCalibrationValue(previousValue, string):
    firstMatch = getFirstMatch(string)
    lastMatch = getLastMatch(string)
    return int(firstMatch + lastMatch) + previousValue

def main():
    input = open('1.txt').read()
    result = reduce(getCalibrationValue, input.splitlines(), 0) # feed each line into a reduce, with starting value 0

    print("YOUR RESULT IS:", result)
    

if __name__ == "__main__":
    main()