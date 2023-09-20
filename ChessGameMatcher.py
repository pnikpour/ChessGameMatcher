import yaml
import re
import collections
from Game import Game

def main():
    config = yaml.safe_load(open('config.yaml'))
    filePath = config['values']['filePath']
    regex = config['values']['regex']
    regexCompiled = re.compile(regex)
    file = open(filePath, 'r')
    games = []
    foundGames = []
    
    # Construct the list of Games
    for line in file:
        #print(line)
        matches = re.match(regex, line)
        if matches:
            #print(line)
            games += [matches.group()]
#            print(matches.group())
        #print(matches.group(0))
    #print([game for game, count in collections.Counter(games).items() if count > 1])
    gamesWithCounts = []
    duplicates = [game for game, count in collections.Counter(games).items() if count > 1]
    for dupe in duplicates:
        gameObj = Game(dupe, 0)
        for game in games:
            gameMatch = re.match(regex, game)
            gameResult = gameMatch.group()
  #          print('Comparing games: ')
            dupArrString = dupe.split()
            dupArrString.pop()
            dupArrStr = ' '.join(dupArrString)

            gameResultArr = gameResult.split()
            gameResultArr.pop()
            gameResults = ' '.join(gameResultArr)
#            print(dupArrStr)
 #           print(gameResults)
            gameObj.moves = dupArrStr
            if (dupArrStr == gameResults):
                gameObj.count += 1
        gamesWithCounts.append(gameObj)
    
    for g in gamesWithCounts:
        print(g.tostring())

if __name__ == '__main__':
    main()
