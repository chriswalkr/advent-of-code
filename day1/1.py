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


# def cleanLine(line, newLine = ""):
#     matchResult = {}
#     for x in mapping.keys():
#         val = line.find(x)
#         if val > -1:
#             matchResult[val] = x
#     myKeys = list(matchResult.keys())
#     myKeys.sort()
#     if len(myKeys) == 0:
#         # print("final", line)
#         return newLine
#     # print(matchResult[myKeys[0]])
#     newLine = newLine + str(mapping[matchResult[myKeys[0]]])
#     line = line.replace(matchResult[myKeys[0]], "")
#     # print(blah)
#     return cleanLine(line, newLine)

        
def cleanLine(line, newLine = []):
    matchResult = {}
    for x in mapping.keys():
        val = line.find(x)
        if val > -1:
            matchResult[val] = x
    # print("mr", matchResult, line)
    myKeys = list(matchResult.keys())
    myKeys.sort()
    print("mykeys", myKeys, len(myKeys))
    if len(myKeys) == 0:
        return newLine
    if (myKeys[0] == 0):
        return newLine
    newLine.append(mapping[matchResult[myKeys[0]]])
    # print("before replace", myKeys[0])
    line = list(line).pop(myKeys[0])
    # print("new line", line, newLine)
    return cleanLine(line, newLine)
    

def getCalibrationValue(previousValue, string):
    cleanString = "".join(cleanLine(string))
    print("cs", cleanString)
    result = re.findall(r'[0-9]', cleanString)
    if len(result) == 1:
        print(int(result[0] + result[0]) + previousValue)
        return int(result[0] + result[0]) + previousValue
    else:
        print(int(result[0] + result[len(result) - 1]) + previousValue)
        return int(result[0] + result[len(result) - 1]) + previousValue


def main():
    input = open('test.txt').read()

    blah = reduce(getCalibrationValue, input.splitlines(), 0)
    print(blah)
    

if __name__ == "__main__":
    main()