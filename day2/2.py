from collections import defaultdict 

def default_value():
    return 0

def parseGames(string):
    rawGameNumber, rawGameData = string.split(':')
    gameNumber = rawGameNumber.replace('Game ', '')
    games = []
    for rawGame in rawGameData.split(';'):
        d = defaultdict(default_value)
        for rawPlay in rawGame.split(','):
            print(rawPlay)
            _, num, colour = rawPlay.split(' ')
            d[colour] = d[colour] + int(num)
        print(d)
        print('----')


    print(gameNumber)
    print(rawGameData)
    

def main():
    print("Hello World!")

    games = open('2.txt').readlines()
    parseGames(games[0])

if __name__ == "__main__":
    main()
