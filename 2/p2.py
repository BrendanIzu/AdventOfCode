import re
import math

f = open('input.txt')
lines = f.readlines()

def parseRound(round: str, minRed, minGreen, minBlue):
  for handful in round:
    numCubes = int(re.sub(r'[^\d]', "", handful))

    if 'red' in handful:
      minRed = max(minRed, numCubes)
    if 'green' in handful:
      minGreen = max(minGreen, numCubes)
    if 'blue' in handful:
      minBlue = max(minBlue, numCubes)
  return minRed, minGreen, minBlue

def parseGame(game: str):
  game = game.strip('\n')
  rounds = re.split(': |;', game)
  if '' in rounds:
    rounds.remove('')
    
  minRed, minGreen, minBlue = 0, 0, 0
  for round in rounds:
    minRed, minGreen, minBlue = parseRound(re.split(',', round), minRed, minGreen, minBlue)
  
  return minRed * minGreen * minBlue
    
res = 0
for i, line in enumerate(lines): 
  res += parseGame(line)

print(res)
  
  